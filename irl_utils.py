import numpy as np
import pandas as pd
from collections import namedtuple 

def get_traj_data():
    traj_data = pd.read_csv('combined_trajectories.csv', sep=',',header=None)
    return traj_data.to_numpy()

def define_trajectories(traj_data):
    state = namedtuple('S',['x','y','theta'])
    Step = namedtuple('Step','cur_state action next_state reward done')

    episodes = []
    traj = []

    for t in range(len(traj_data)):
        episode = []
        for i in range(19):
            curr_tuple = traj_data[t]
            s = state(x=traj_data[t][0], y=traj_data[t][1], theta=traj_data[t][2])
            a = traj_data[t][3]
            s_next = state(x=traj_data[t][4], y=traj_data[t][5], theta=traj_data[t][6])
            episode.append(Step(cur_state = s, action = a, next_state = s_next, reward = 0, done = 0))
            if t < 399:
                t = t+1
        episode.append(Step(cur_state = s, action = a, next_state = s_next, reward = 10, done = 1))
        traj.append(episode)

    return traj

def get_transition_mat(n_x, n_y, n_theta, actions):
    """
    get transition dynamics of the gridworld

    return:
        P_a         NxNxN_ACTIONS transition probabilities matrix - 
                    P_a[s0, s1, a] is the transition prob of 
                    landing at state s1 when taking action 
                    a at state s0
    """
    traj_data = get_traj_data()

    theta = [-0.3 , -0.2, -0.1, 0 , 0.1, 0.2, 0.3]

    state_space = dict()
    count = 0
    for i in range(0, 79):
        for j in range(-70, 38):
            for t in theta:
                x = [(i,j,t)]
                state_space[tuple(x)] = 1
    
    N_STATES = len(state_space)
    N_ACTIONS = len(actions)
    P_a = np.zeros((N_STATES, N_STATES, N_ACTIONS))

    for t in range(len(traj_data)):
        s = traj_data[t]
        curr_state = [(s[0],s[1],s[2])]
        next_state = [(s[4],s[5],s[6])]
        action = s[3]

        curr_state = tuple(curr_state)
        next_state = tuple(next_state)

        curr_index = list(state_space.keys()).index(curr_state)
        next_index = list(state_space.keys()).index(next_state)
        action_index = actions.index(action)

        P_a[curr_index , next_index , action_index] = 1

    print ("Test")
    return P_a, state_space

if __name__ == "__main__":
    get_traj_data()

#def get_transition_matrix():
