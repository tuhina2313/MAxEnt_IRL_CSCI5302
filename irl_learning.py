import numpy as np
import matplotlib.pyplot as plt
import argparse
from collections import namedtuple 
from irl_utils import *
from mdp import value_iteration
from maxent_irl import *


gamma = 0.8     #discount factor
act_random = 0.3    #probability of acting randomly
r_max = 1
n_x = 78    #no of possible x-values
n_y = 108   #no of possible y-values
n_theta = 7 #no of possible angles
n_trajs = 20#total trajectories
l_traj = 22 #len of each trajectory
rand_start = False  
learning_rate = 0.01
iterations = 20
actions = [-1, 314, 315, 316]

curr_state = namedtuple("S",["x","y","theta"])
next_state = namedtuple("S_next",["x","y","theta"])



def main():
  N_STATES = n_x * n_y * n_theta
  N_ACTIONS = len(actions)

  reward_ground = np.zeros([n_x , n_y , n_theta])

  rewards_gt = np.reshape(reward_ground, n_x * n_y * n_theta, order='F')
  P_a, state_space = get_transition_mat(n_x, n_y, n_theta, actions)
  # print(P_a)

  # values_gt, policy_gt = value_iteration.value_iteration(P_a, rewards_gt, gamma, error=0.01, deterministic=True)
  
  feat_map = np.eye(N_STATES)

  np.random.seed(1)
  traj_data = get_traj_data()
  trajs = define_trajectories(traj_data)
  rewards = maxent_irl(feat_map, P_a, state_space, gamma, trajs, learning_rate, iterations)
  
  values, _ = value_iteration.value_iteration(P_a, rewards, gamma, error=0.01, deterministic=True)

if __name__ == "__main__":
  main()