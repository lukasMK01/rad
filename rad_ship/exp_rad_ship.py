# -*- coding: utf-8 -*-
"""
Read SW down radiation data from PS122/4

Lukas Monrad-Krohn, 11.05.2023
"""

import numpy as np
import matplotlib.pyplot as plt
import datetime as dt
import pandas as pd

fp = './data/'
fn = 'PS122-4_cont_surf_meteorology.tab'
data = pd.read_table(fp+fn, skiprows=34)
old_clmns = data.columns # save the old column names for later/units
data.columns = ['date', 'lat', 'lon', 'head', 'crs', 'spd', 'bath', 'temp', 'TTT', 
                'rhum', 'Tdew', 'pres', 'wdir', 'wspd', 'dd', 'ff', 'wgus', 'swd', 
                'visi', 'ceil']


