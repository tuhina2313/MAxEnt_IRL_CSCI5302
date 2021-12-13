import numpy as np
import pandas as pd

def get_traj_data():
    traj_data = pd.read_csv('combined_trajectories.csv', sep=',',header=None)
    print("loaded")

#def get_transition_matrix():
