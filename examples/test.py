import numpy as np
import pandas as pd

import gym
import gym_anytrading
import quantstats as qs

from stable_baselines3 import A2C, PPO, DQN
from stable_baselines3.common.vec_env import DummyVecEnv
import cloudpickle
import matplotlib.pyplot as plt

with open('../dataset/train.pkl', 'rb') as f:
    train_data = cloudpickle.load(f)
with open('../dataset/test.pkl', 'rb') as f:
    test_data = cloudpickle.load(f)
train_data = train_data.loc[:, ['close'] + list(range(10))]
test_data = test_data.loc[:, ['close'] + list(range(10))]
train_data.columns = ['Close'] + list(range(10))
test_data.columns = ['Close'] + list(range(10))

window_size = 10
start_index = window_size
end_index = len(train_data)
import sys
sys.path.append('../gym_anytrading/envs/')
from forex_env import ForexEnv
env_maker = ForexEnv(
    df = train_data,
    window_size = window_size,
    frame_bound = (start_index, end_index)
)
print(env_maker.signal_features.shape)