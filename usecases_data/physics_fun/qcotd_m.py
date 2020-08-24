import json
import sys

import gvar as gv
import numpy as np


BMat_path = '/Users/wayne.lee/repos/pythib'
sys.path.append(BMat_path)

import BMat


L = 48
momRay = {0: 'ar', 1: 'oa', 2: 'pd', 3: 'cd', 4: 'oa'}
include_data = [
    (('0', 'T1g', 0), 'R', ('0', '0')), (('0', 'T1g', 1), 'R', ('1', '1')),
    (('1', 'A2', 0), 'R', ('0', '1')),  (('1', 'A2', 1), 'R', ('1', '2')),
    (('1', 'E', 0), 'R', ('0', '1')),   (('1', 'E', 1), 'R', ('1', '2')),
    (('4', 'E', 0), 'R', ('1', '1')),   (('4', 'E', 1), 'R', ('0', '4')),
    (('2', 'A2', 0), 'R', ('1', '1')),  (('4', 'A2', 0), 'R', ('1', '1')),
    (('4', 'A2', 1), 'R', ('0', '4')),  (('2', 'B1', 0), 'R', ('1', '1')),
    (('2', 'B2', 0), 'R', ('1', '1')),  (('2', 'B2', 3), 'R', ('1', '3')),
    (('3', 'A2', 0), 'R', ('0', '3')),  (('3', 'E', 0), 'R', ('0', '3')),
]


# Functions needed for BMat to work
def isZero(JtimesTwo, Lp, SptimesTwo, chanp, L, StimesTwo, chan):
    return not (JtimesTwo == 2
                and Lp == 0 and L == 0
                and chanp == 0 and chan == 0
                and SptimesTwo == 2 and StimesTwo == 2)


def calcFunc(self, JtimesTwo, Lp, SptimesTwo, chanp, L, StimesTwo, chan,
             Ecm_over_mref, pSqFuncList):
        return 0.


Kinv = BMat.KMatrix(calcFunc, isZero)
chanList = [BMat.DecayChannelInfo('n', 'n', 1, 1, True, True), ]

# To define the y = f(x) function
# read a data file with correlated normal distributed energy levels
# (the x-variables)
fit_results = gv.load('result/posterior_singlet_t05_td10'
                      '_N_n2_t_5_20_R_n2_t_5_15_ratio_True.pickle')
mN = fit_results[((('0', 'T1g', 0), 'N', '0'), 'e0')]


def make_bs(m_N, e_NN, n=100):
    ''' re-sample the normal distributed energies (m_N and e_NN)
        to create bootstrap samples
    '''
    d_dict = dict()
    d_dict['m_n'] = m_N
    d_dict['e_nn'] = e_NN
    bs_list = list(gv.bootstrap_iter(d_dict, n=n))
    return bs_list


def qcotd_gv(boxQ, x):
    ''' Create a gvar instance of the transformed x-variable if x is a gvar
        else, create a real if x is a float/real/complex
    '''
    if isinstance(x, gv.GVar):
        stepsize = 1e-14
        f = boxQ.getBoxMatrixFromElab(x.mean)
        dfdx = (0.5*(boxQ.getBoxMatrixFromElab(x.mean + stepsize)
                     - boxQ.getBoxMatrixFromElab(x.mean - stepsize))
                / stepsize)
        return gv.gvar_function(x, x.mean, x.sdev, f.real, dfdx.real)
    else:
        return boxQ.getBoxMatrixFromElab(x).real


e0_results = {result: fit_results[result] for result in fit_results
              if result[1] == 'e0' and result[0] in include_data}
step = 1e-14
n_bs = 1000
boot_bag = {}
for k in e0_results:
    # process to get the x-variable
    Psq, irrep, n = k[0][0]
    Psq = int(Psq)
    de_nn = e0_results[k]
    s1, s2 = k[0][2]
    st1 = ((k[0][0], 'N', s1), 'e0')
    st2 = ((k[0][0], 'N', s2), 'e0')
    en1 = fit_results[st1]
    en2 = fit_results[st2]
    e_nn = de_nn + en1 + en2
    E_cmSq = e_nn**2 - Psq*(2*np.pi/L)**2
    # our x-variable
    qsq = E_cmSq / 4 - mN**2

    # make the y-variable
    boxQ = BMat.BoxQuantization(momRay[Psq], Psq, irrep, chanList, [0, ],
                                Kinv, True)
    boxQ.setRefMassL(mN.mean*L)
    boxQ.setMassesOverRef(0, 1, 1)
    qcotd = boxQ.getBoxMatrixFromElab(e_nn.mean / mN.mean)

    bs_vals = make_bs(mN, e_nn, n=n_bs)
    qsq_qcotd_bs = {}
    boxQ_bs = BMat.BoxQuantization(momRay[Psq], Psq, irrep, chanList,
                                   [0, ], Kinv, True)
    boxQ_bs.setMassesOverRef(0, 1, 1)
    for bs in range(len(bs_vals)):
        mN_bs = bs_vals[bs]['m_n']
        e_nn_bs = bs_vals[bs]['e_nn']
        boxQ_bs.setRefMassL(mN_bs.mean*L)
        E_cmSq_bs = e_nn_bs**2 - Psq*(2*np.pi/L)**2
        qsq_bs = E_cmSq_bs/4 - mN_bs**2
        qsq_qcotd_bs.update({'x_mean': qsq_bs.mean / (mN_bs**2).mean})
        x_mean = e_nn_bs.mean / mN_bs.mean
        qsq_qcotd_bs.update({
            'y_at_x_mean': boxQ_bs.getBoxMatrixFromElab(x_mean).real})
        qsq_qcotd_bs.update({
            'dydx': (0.5
                     * (boxQ_bs.getBoxMatrixFromElab(x_mean + step).real
                        - boxQ_bs.getBoxMatrixFromElab(x_mean - step).real)
                     / step)
            })

    boot_bag.update({'{}_{}_{}'.format(Psq, irrep, n): qsq_qcotd_bs})

json.dump(boot_bag, open('waynbe_boot.json', 'w'))
