#

conda create -n physics python=3.7 numpy pandas pyyaml matplotlib ipykernel scipy statsmodels
conda activate physics
pip install gvar
pip install lsqfit

cd ~/repos
git clone https://github.com/ebatz/TwoHadronsInBox.git
git fetch origin mac.clang.accelerate
git checkout mac.clang.accelerate
cd TwoHadronsInBox/build
./build_mac.sh

cd ~/repos
git clone https://github.com/ebatz/pythib.git
conda install pybind11
# EDIT paths in the build.mac.clang.accelerate.sh
# You do not need to uncomment the PYBIND path

#Edit get_x_to_y.py for the `BMat_path` so it points to the pythib code
python get_x_to_y.py


# I've edited the code and created `qcotd_m.py` that produces the x, y, dy/dx for each irrep
