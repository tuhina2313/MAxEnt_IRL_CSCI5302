Implementation of Maximum Entropy IRL (Advanced Robotics - CSCI 5302)

Algorithm implemented: Maximum entropy IRL. From Ziebart et al., 2008.

To run the code, type the following command in terminal:
: `python3 irl_learning.py`

Dataset: TRAJECTORIES.xlsx (Complete set of trajectories. Sheet 'T1' includes the original recorded GPS data points without rounding)
         combined_trajectories.csv: the combined list of datapoints used for training. 

irl_learning: contains initialization of parameters and caller function for the implementation

irl_utils: implements the functions for loading data, defining trajectories, creating state space and generating transition matrix. 

maxent_irl: implements the functions for computing state frequencies, generating reward matrix and performing value and policy iteration

mdp(folder): contains implemntation of value and policy iteration. (adapted from Yiren Lu's implementation of the Maximum entropy inverse reinforcement learning (Ziebart et al. 2008) on 1-D and 2-D grid-worlds (https://github.com/yrlu/irl-imitation).)

