## gfootball

```sh
# 1. create conda env
conda create -n marl python=3.8 -y
conda activate marl

# 2. install py-boost
conda install -c anaconda py-boost

# 3. install gym==0.21.0  gfootball and some base packages
pip install setuptools==63.2.0
pip install gym==0.21.0
pip install gfootball
pip install six
pip install torch==1.9.1+cu111 torchvision==0.10.1+cu111 torchaudio==0.9.1 -f https://download.pytorch.org/whl/torch_stable.html

# 4. libstdc error
ln -s /usr/lib/x86_64-linux-gnu/libstdc++.so.6.0.30 {conda_dir}/envs/marl/lib/libstdc++.so.6

# 5. build libgame.so
cd {conda_dir}/envs/marl/lib/python3.8/site-packages/gfootball_engine
# when error with: "CMake Error at CMakeLists.txt:117 (message):Boost Python not found"
# edit CMakeLists.txt: add set(Python_VERSION_MINOR 8) after line 67
cmake . && make
rm _gameplayfootball.so
ln -s libgame.so _gameplayfootball.so
```

## marllib

```sh
git clone https://github.com/Replicable-MARL/MARLlib.git
cd MARLlib
pip install -r requirements.txt
python setup.py install
```