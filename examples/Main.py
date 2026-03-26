
#Main.py 
# # Setup
from pathlib import Path
import codecamp 
import numpy as np
import os
import matplotlib.pyplot as plt

FILE_DIR = Path(__file__).parent  # directory where this file is located 
DATA_DIR = FILE_DIR / 'inputs'  # get the 'inputs' folder in the same directory as this file 



# We set easier paths for our 'wind_TI_0.1' folder and our 'wind_xx_ms_TI_0.1.txt' files
wind_folder = DATA_DIR / 'wind_TI_0.1'
wind_files = sorted(os.listdir(wind_folder))

