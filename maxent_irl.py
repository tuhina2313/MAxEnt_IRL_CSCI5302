import numpy as np
import mdp.value_iteration as value_iteration
from utils import *


def compute_state_visition_freq(P_a, gamma, trajs, policy, deterministic=True):

  n_states, _, n_actions = np.shape(P_a)

  T = len(trajs[0])
  # mu[s, t] is the prob of visiting state s at time t
  mu = np.zeros([n_states, T]) 

  for traj in trajs:
    mu[traj[0].cur_state, 0] += 1
  mu[:,0] = mu[:,0]/len(trajs)

  for s in range(n_states):
    for t in range(T-1):
      if deterministic:
        mu[s, t+1] = sum([mu[pre_s, t]*P_a[pre_s, s, int(policy[pre_s])] for pre_s in range(n_states)])
      else:
        mu[s, t+1] = sum([sum([mu[pre_s, t]*P_a[pre_s, s, a1]*policy[pre_s, a1] for a1 in range(n_actions)]) for pre_s in range(n_states)])
  p = np.sum(mu, 1)
  return p



def maxent_irl(feat_map, P_a, state_space, gamma, trajs, lr, iterations):

  n_states, _, n_actions = np.shape(P_a)

  # init parameters
  theta = np.random.uniform(size=(feat_map.shape[1],))

  # calc feature expectations
  feat_exp = np.zeros([feat_map.shape[1]])
  for episode in trajs:
    for step in episode:
      curr_state = step.cur_state
      if curr_state in state_space:
        feat_exp += 1
  feat_exp = feat_exp/len(trajs)

  for itr in range(iterations):
    rewards = np.dot(feat_map, theta)
    _, policy = value_iteration.value_iteration(P_a[:100][:100][:100], rewards, gamma, error=0.01, deterministic=False)
    svf = compute_state_visition_freq(P_a, gamma, trajs, policy, deterministic=False)
    grad = feat_exp - feat_map.T.dot(svf)

    theta += lr * grad

  rewards = np.dot(feat_map, theta)
  return normalize(rewards)


