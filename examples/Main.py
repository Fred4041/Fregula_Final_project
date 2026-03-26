
#Main.py 
# # Setup
from pathlib import Path
from matplotlib import pyplot as plt
import numpy as np
import pandas as pd
import matplotlib.dates as mdates
from datetime import datetime
import os 
import sys 

sys.path.append(str(Path(__file__).parent.parent / 'src'))  # add the 'src' folder to the Python path
from __init__ import plot_windspeeds



FILE_DIR = Path(__file__).parent  # directory where this file is located 
DATA_DIR = FILE_DIR.parent / 'inputs'  # get the 'inputs' folder in the same directory as this file 



# We set easier paths for our 'wind_TI_0.1' folder and our 'wind_xx_ms_TI_0.1.txt' files
wind_loc_1 = DATA_DIR / 'Location1.csv'  # get the 'Location1.csv' file in the 'inputs' folder
# wind_files = sorted(os.listdir(wind_folder)) #

location1_windspeeds_10m = np.loadtxt(wind_loc_1, delimiter=',', skiprows=1, usecols=(4))  # load the wind speeds from the 'Location1.csv' file, skipping the header row
location1_windspeeds_100m = np.loadtxt(wind_loc_1, delimiter=',', skiprows=1, usecols=(5))  # load the wind speeds from the 'Location1.csv' file, skipping the header row

df = pd.read_csv(wind_loc_1, parse_dates=[0])
location1_timestamps = df.iloc[:, 0]
print(location1_timestamps)  # print the wind speeds to check if they were loaded correctly


# Single wind speed
plot_windspeeds(location1_timestamps, location1_windspeeds_10m, show=True)

# Multiple wind speeds
plot_windspeeds(location1_timestamps, [location1_windspeeds_10m, location1_windspeeds_100m], show=True)


# TO DO LIST : 
# CREATE A PLOT FUNCTION  THAT has the correct variables. 
#Plot timeseries of a selected variable (like wind_speed_100m or Power) for a given site (site 1, 2, 3 or 4) within a specific perid, i.e., a function with variable_name, site_index, starting_time and ending_time as inputs.
