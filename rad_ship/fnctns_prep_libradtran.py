# -*- coding: utf-8 -*-
"""
functions for preparing the libradtran input

Lukas Monrad-Krohn: 16.05.2023
"""

import numpy as np
import pandas as pd
import datetime as dati
import matplotlib.pyplot as plt


# a function that read the surface meteorology data of PS, 
# and prepares it for use (timestepping currently hourly, choose day)
def read_PS_SWD(fp = './data/', fn = 'PS122-4_cont_surf_meteorology.tab', day = None):
    data = pd.read_table(fp+fn, skiprows=34)
    old_clmns = data.columns # save the old column names for later/units
    data.columns = ['date', 'lat', 'lon', 'head', 'crs', 'spd', 'bath', 'temp', 'TTT', 
                    'rhum', 'Tdew', 'pres', 'wdir', 'wspd', 'dd', 'ff', 'wgus', 'swd', 
                    'visi', 'ceil']
    
    data['dt'] = pd.to_datetime(data['date'], format='%Y-%m-%dT%H:%M')
    data['date'] = data['dt'].dt.date
    data['time'] = data['dt'].dt.time
    
    # only keep full hour values
    data['mm'] = [data['dt'][i].minute for i in range(len(data['dt']))]
    data['ss'] = [data['dt'][i].second for i in range(len(data['dt']))]
    data = data[(data['mm'] == 0) & (data['ss'] == 0)]
    data.reset_index(inplace=True, drop=True)
    data.drop(columns=['mm', 'ss', 'time'],  inplace=True)
    #to get hours: data['dt'][i].hour
    
    
    data['ceil'] = data['ceil'] * 0.3048 # transform to meters
    
    data_days = np.array([y for x,y in data.groupby(['date'],as_index=False)])
    days =  np.array([x for x,y in data.groupby(['date'],as_index=False)])
    
    # only return data of one day if specified
    if day == None:
        return data, data_days, days
    else:
        mask = np.array([i == day for i in days], dtype=np.bool)
        idx = np.where(mask)[0][0]
        day = days[mask][0]
        
        return data_days[idx], day
        
dat1, day1 = read_PS_SWD(day = dati.date(2020,7,8))
print(dat1, day1)

#%%
