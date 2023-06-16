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

# 4. libstdc error
ln -s /usr/lib/x86_64-linux-gnu/libstdc++.so.6.0.30 {conda_dir}/envs/marl/lib/libstdc++.so.6

# 5. build libgame.so
cd {conda_dir}/envs/marl/lib/python3.8/site-packages/gfootball_engine
cmake . && make
ln -s libgame.so _gameplayfootball.so
```

## marllib

```sh
git clone https://github.com/Replicable-MARL/MARLlib.git
cd MARLlib
pip install -r requirements.txt
python setup.py install
```