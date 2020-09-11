import json
import sys
import BMat
import gvar as gv
import numpy as np
import lsqfit
import matplotlib.pyplot as plt

import warnings
warnings.filterwarnings('ignore')

BMat_path = '/Users/wayne.lee/repos/pythib'
sys.path.append(BMat_path)


def run_from_ipython():
    try:
        __IPYTHON__
        return True
    except NameError:
        return False


# read a data file with correlated normal distributed energy levels
# (the x-variables)
fit_results = gv.load('result/posterior_singlet_t05_td10'
                      '_N_n2_t_5_20_R_n2_t_5_15_ratio_True.pickle')
mpi = gv.gvar('0.310811(85)')
vs_mpi = True  # this controls a "scaling" of the x-variable
L = 48
n_bs = 1000
svd_cut = 1.e-10

momRay = {0: 'ar', 1: 'oa', 2: 'pd', 3: 'cd', 4: 'oa'}

irreps_clrs = {
    'T1g': 'k', 'A2': 'b', 'E': 'r', 'B1': 'g', 'B2': 'magenta',
    'A1g': 'k', 'A1': 'b',
}

level_mrkr = {0: 's', 1: 'o',
              2: 'd', 3: 'p',
              4: 'h', 5: '8',
              6: 'v'}

mN = fit_results[((('0', 'T1g', 0), 'N', '0'), 'e0')]
nn_str = 'deuteron'

''' Functions needed for BMat to work '''
def isZero(JtimesTwo, Lp, SptimesTwo, chanp, L, StimesTwo, chan):
    return not (JtimesTwo==2
            and Lp==0 and L==0
            and chanp==0 and chan==0
            and SptimesTwo==2 and StimesTwo==2)

def calcFunc(self, JtimesTwo, Lp, SptimesTwo, chanp, L, StimesTwo, chan, Ecm_over_mref, pSqFuncList):
        return 0.
Kinv = BMat.KMatrix(calcFunc, isZero)
chanList = [BMat.DecayChannelInfo('n','n',1,1,True,True),]
''' ================================  '''

def make_bs(m_N,e_NN,n=100):
    ''' re-sample the normal distributed energies (m_N and e_NN)
        to create bootstrap samples
    '''
    d_dict = dict()
    d_dict['m_n']   = m_N
    d_dict['e_nn'] = e_NN
    bs_list = list(gv.bootstrap_iter(d_dict, n=n))
    return bs_list

def qcotd_gv(boxQ, x):
    ''' Create a gvar instance of the transformed x-variable if x is a gvar
        else, create a real if x is a float/real/complex
    '''
    if isinstance(x, gv.GVar):
        stepsize = 1e-14
        f    = boxQ.getBoxMatrixFromElab(x.mean)
        dfdx = 0.5*(boxQ.getBoxMatrixFromElab(x.mean + stepsize) - boxQ.getBoxMatrixFromElab(x.mean - stepsize)) / stepsize
        return gv.gvar_function(x, f.real, dfdx.real)
    else:
        return boxQ.getBoxMatrixFromElab(x).real

plt.ion()
plt.figure('qcotd',figsize=(7,4))
ax = plt.axes([0.12,0.12,0.87,0.87])

# prepare a master dictionary that will store correlate x-variables
all_data = dict()
all_data['m_n'] = mN
all_qcotd = dict()
all_qsq   = dict()

excluded = []
cut_data = []
#cut_data = [(('1', 'A2', 1), 'R', ('1', '2'))]

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

# read data from pickle file
print('%78s        %s        %s' %('parent-x','x', 'y'))
print('==========================================================================================================')
for k in fit_results:
    if not (k[1] == 'e0' and k[0] in include_data and k[0] not in cut_data):
        continue
    # process to get the x-variable
    Psq, irrep, n = k[0][0]
    Psq = int(Psq)
    de_nn = fit_results[k]
    s1,s2 = k[0][2]
    st1 = ((k[0][0], 'N', s1), 'e0')
    st2 = ((k[0][0], 'N', s2), 'e0')
    en1 = fit_results[st1]
    en2 = fit_results[st2]
    e_nn = de_nn + en1 + en2
    E_cmSq = e_nn**2 - Psq*(2*np.pi/L)**2
    # our x-variable
    qsq = E_cmSq / 4 - mN**2

    # make the y-variable
    boxQ = BMat.BoxQuantization(momRay[Psq], Psq, irrep, chanList, [0,], Kinv, True)
    boxQ.setRefMassL(mN.mean*L)
    boxQ.setMassesOverRef(0, 1, 1)
    qcotd = boxQ.getBoxMatrixFromElab(e_nn.mean / mN.mean)

    # make a BS distribution of the mass and two-particle energy and y-variable
    # as well as the x-variable
    bs_vals = make_bs(mN, e_nn, n=n_bs)
    qsq_qcotd_bs = np.zeros([len(bs_vals),3])
    boxQ_bs = BMat.BoxQuantization(momRay[Psq], Psq, irrep, chanList, [0,], Kinv, True)
    boxQ_bs.setMassesOverRef(0,1,1)
    for bs in range(len(bs_vals)):
        mN_bs   = bs_vals[bs]['m_n']
        e_nn_bs = bs_vals[bs]['e_nn']
        boxQ_bs.setRefMassL(mN_bs.mean*L)
        E_cmSq_bs = e_nn_bs**2 - Psq*(2*np.pi/L)**2
        qsq_bs    = E_cmSq_bs/4 - mN_bs**2
        qsq_qcotd_bs[bs,0] = qsq_bs.mean / (mN_bs**2).mean
        qsq_qcotd_bs[bs,1] = boxQ_bs.getBoxMatrixFromElab(e_nn_bs.mean / mN_bs.mean).real
 
    qsq_qcotd_bs = qsq_qcotd_bs[qsq_qcotd_bs[:,1].argsort()]

    # x BS
    qsq_bs   = qsq_qcotd_bs[:,0]# - qsq_qcotd_bs[:,0].mean() + qsq.mean/mN.mean**2
    # y BS
    qcotd_bs = qsq_qcotd_bs[:,1]# - qsq_qcotd_bs[:,1].mean() + qcotd.real

    # plot the inner 68% interval
    i_16 = int(n_bs/100*16)
    i_84 = int(n_bs/100*84)
    clr = irreps_clrs[irrep]
    mkr = level_mrkr[Psq]
    if vs_mpi:
        ax.plot(qsq_bs[i_16:i_84]*(mN**2/mpi**2).mean, qcotd_bs[i_16:i_84]*(mN/mpi).mean,
            linestyle='None', color=clr, mfc='None', marker='.', alpha=0.1)
    else:
        ax.plot(qsq_bs[i_16:i_84], qcotd_bs[i_16:i_84],
            linestyle='None', color=clr, mfc='None', marker='.', alpha=0.1)

    # Plot the mean value of x,y pairs
    if n == 0:
        lbl = r'${\rm %s}(P_{\rm  tot}^2 = %d)$' %(irrep,Psq)
    else:
        lbl = ''
    if vs_mpi:
        ax.plot(qsq.mean/mpi.mean**2, qcotd*(mN/mpi).mean, linestyle='None',
            color=clr, marker=mkr, label=lbl)
    else:
        ax.plot(qsq.mean/mN.mean**2, qcotd, linestyle='None',
            color=clr, marker=mkr, label=lbl)

    all_qcotd[k] = qcotd_gv(boxQ, e_nn / mN)
    all_qsq[k]   = qsq/mN**2
    if vs_mpi:
        qsq_m   = qsq / mpi**2
        qcotd_m = all_qcotd[k] *mN / mpi
    else:
        qsq_m = qsq / mN**2
        qcotd_m = all_qcotd[k]
    print('%d& %3s& %s& %s& %s& %s& %s& %s& %s& %s& %s& %s\\\\' \
        %(Psq, irrep, n, s1, en1, s2, en2, de_nn, e_nn, np.sqrt(E_cmSq), qsq_m, qcotd_m))

    # put parent x-variable into dictionary
    all_data[k] = e_nn

#print(all_data)

# Using correlated parent-x variables, create BS distribution of them for different data sets
all_data_bs = list(gv.bootstrap_iter(all_data, n=n_bs))

# create container for x-variable for plotting
qsqmn_range = np.arange(-0.04, 0.501,.001)
qsqmn_plot = {k:k for k in qsqmn_range}

# create dictionaries to hold mean and BS results
qcotd_vals_0  = dict()
qsq_result_0  = dict()
qcotd_vals_bs = dict()
qsq_result_bs = dict()
for k in all_data_bs[0]:
    if k != 'm_n':
        x = []
        y = []
        for bs in range(n_bs):
            # create x-variable from parent x-variable
            m_n = all_data_bs[bs]['m_n']
            Psq, irrep, n = k[0][0]
            Psq = int(Psq)
            e_nn   = all_data_bs[bs][k]
            E_cmSq = e_nn**2 - Psq*(2*np.pi/L)**2
            # x_bs
            qsq    = E_cmSq / 4 - m_n**2

            # make y bs data
            boxQ = BMat.BoxQuantization(momRay[Psq], Psq, irrep, chanList, [0,], Kinv, True)
            boxQ.setRefMassL(m_n.mean*L)
            boxQ.setMassesOverRef(0, 1, 1)
            if vs_mpi:
                x.append((qsq / mpi**2).mean)
                y.append(((qcotd_gv(boxQ, e_nn / m_n)* m_n/mpi).mean).real)
            else:
                x.append((qsq / m_n**2).mean)
                y.append(((qcotd_gv(boxQ, e_nn / m_n)).mean).real)

        qsq_result_bs[k[0]] = x
        qcotd_vals_bs[k[0]]  = y

xy = {'x': {str(k): v for k, v in qsq_result_bs.items()},
      'y': {str(k): v for k, v in qcotd_vals_bs.items()}}

json.dump(xy, open('qcotd2xy.json', 'w'))
## use the BS results of y to create correlated y dataset
#qcotd_vals_gv = gv.dataset.avg_data(qcotd_vals_bs, bstrap=True)
#
## set x variable to mean and y to correlated y-dataset
#x = {k:qsq_result_bs[k].mean() for k in qsq_result_bs}
#y = qcotd_vals_gv
## get covariance of y-datasets
#cov = gv.evalcov(qcotd_vals_gv)
#
## set up fit
#def qcotd_ere_1(x,p):
#    ''' linear fit function
#        x = qSq
#        y = qcotd
#
#        qcotd = -1/(ma)  +  0.5 * (mr) * qSq
#    '''
#    result = dict()
#    for k in x:
#        result[k]  = p['mainv']
#        result[k] += 0.5 * p['r'] * x[k]
#    return result
#
#priors = dict()
#priors['mainv'] = gv.gvar(0.01,.3)
#priors['r'] = gv.gvar(10,1000)
## set starting values
#p_1 = {k:v.mean for k,v in priors.items()}
#
#if vs_mpi:
#    qsq_mN_plot = np.arange(-0.13,0.26,.0005)
#else:
#    qsq_mN_plot = np.arange(-0.03,0.0605,.0005)
#
#''' create correlated y-data using covariance determined above
#    and mean value of y-data from very first data collection loop
#'''
#if vs_mpi:
#    x_0 = {k:(all_qsq[(k, 'e0')]*mN**2/mpi**2).mean for k in qcotd_vals_gv}
#    y_0 = gv.gvar({k:(all_qcotd[(k, 'e0')]*mN/mpi).mean for k in qcotd_vals_gv}, cov)
#else:
#    x_0 = {k:all_qsq[(k, 'e0')].mean for k in qcotd_vals_gv}
#    y_0 = gv.gvar({k:all_qcotd[(k, 'e0')].mean for k in qcotd_vals_gv}, cov)
#
#''' perform fit using lsqfit '''
#fit_1_0 = lsqfit.nonlinear_fit(data=(x_0,y_0), p0=p_1, fcn=qcotd_ere_1,svdcut=svd_cut, fitter='scipy_least_squares')
#print(fit_1_0.format(maxline=True))
#
#''' plot data used in fit on plot to verify it matches our plotted BS values '''
#for k in x_0:
#    ax.errorbar(fit_1_0.x[k],fit_1_0.y[k].mean,yerr=fit_1_0.y[k].sdev,color='magenta')
#
#''' Now do a loop over BS samples and fit each BS draw with same frozen covariance
#'''
#bs_fit = []
#bs_p   = []
#bs_r1  = []
#r_1    = []
#''' set start values of BS fit from mean values in fit_1_0 '''
#p_bs_1 = {k:v.mean for k,v in fit_1_0.p.items()}
#for bs in range(n_bs):
#    x_bs = {k:qsq_result_bs[k][bs] for k in qsq_result_bs}
#    y_bs = {k:qcotd_vals_bs[k][bs] for k in qcotd_vals_bs}
#    y_bs_gv = gv.gvar(y_bs, cov)
#    bs_1 = lsqfit.nonlinear_fit(data=(x_bs,y_bs_gv), p0=p_bs_1, fcn=qcotd_ere_1,svdcut=svd_cut, fitter='scipy_least_squares')
#    bs_p.append({k:v.mean for k,v in bs_1.p.items()})
#    bs_r1.append(qcotd_ere_1({k:k for k in qsq_mN_plot}, {k:v.mean for k,v in bs_1.p.items()}))
#    r_1.append([v for k,v in bs_r1[-1].items()])
#r_1 = np.array(r_1)
#
## sort the bs fit results so we can cut the middle 68%
#r_1.sort(axis=0)
#
## get mean value of result, r_1_m
#r_1_m = np.array([vv for kk,vv in qcotd_ere_1({k:k for k in qsq_mN_plot}, {k:v.mean for k,v in fit_1_0.p.items()}).items()])
#
## minus is mean minus BS lower bound
#r_1_em = (r_1.mean(axis=0) - r_1[int(.16*n_bs)])
## plus is BS upper minus mean
#r_1_ep = (r_1[int(.84*n_bs)] - r_1.mean(axis=0))
## fill between
#ax.fill_between(qsq_mN_plot, r_1_m-r_1_em, r_1_m+r_1_ep, color='magenta',alpha=.3)
#
#''' print BS uncertainty of fit params '''
#print('resulting fit params')
#mainv_1 = np.array([bs_p[bs]['mainv'] for bs in range(n_bs)])
#ainv_plot = np.array(mainv_1)
#i_sort = mainv_1.argsort()
#m = fit_1_0.p['mainv'].mean
#dmm = mainv_1.mean() - mainv_1[i_sort][int(.16*n_bs)]
#dmp = mainv_1[i_sort][int(.84*n_bs)] - mainv_1.mean()
#print('-1/(a m) = %f -%f +%f' %(m, dmm, dmp))
#mr_1     = np.array([bs_p[bs]['r'] for bs in range(n_bs)])
#r_plot=np.array(mr_1)
#i_sort = mr_1.argsort()
#m = fit_1_0.p['r'].mean
#dmm = mr_1.mean() - mr_1[i_sort][int(.16*n_bs)]
#dmp = mr_1[i_sort][int(.84*n_bs)] - mr_1.mean()
#print('    r m  = %f -%f +%f' %(m, dmm, dmp))
#
## plot axes = 0 and phys point
#if vs_mpi:
#    x_phys = np.arange(-0.13,0.,.00001)
#else:
#    x_phys = np.arange(-0.04,0.,.00001)
#y_phys = -np.sqrt(-x_phys)
#ax.plot(x_phys,y_phys,color='cyan')
#ax.axhline(color='k')
#ax.axvline(color='k')
#
#if vs_mpi:
#    ax.set_xlabel(r'$q_{\rm cm}^2 / m_\pi^2$', fontsize=16)
#    ax.set_ylabel(r'$q {\rm cot} \delta / m_\pi$', fontsize=16)
#else:
#    ax.set_xlabel(r'$q_{\rm cm}^2 / m_N^2$', fontsize=16)
#    ax.set_ylabel(r'$q {\rm cot} \delta / m_N$', fontsize=16)
#ax.legend(loc=2, ncol=5, columnspacing=0, handletextpad=0.1)
#if vs_mpi:
#    t_cut = (1/2)**2
#else:
#    t_cut = ((mpi / mN / 2)**2).mean
#
#ax.axvline(t_cut,color='k',linestyle='--')
#if vs_mpi:
#    ax.axis([-.12, 0.25, -.4,1.2])
#else:
#    ax.axis([-.026, 0.05, -.15,0.6])
#
#
#plt.ioff()
#if run_from_ipython():
#    plt.show(block=False)
#else:
#    plt.show()
