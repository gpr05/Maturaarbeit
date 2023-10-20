import gym
from RPL01 import DeepQNetwork, Agent
import numpy as np


def preprocess(observation):
    return np.mean(observation[30:, :], axis=2).reshape(180,160,1)
def stack_frames(stacked_frames, frame, )
