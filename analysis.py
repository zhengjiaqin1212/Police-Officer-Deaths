#-*- coding:utf-8 -*-

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns;
from matplotlib.ticker import MultipleLocator,FuncFormatter;

data = pd.read_csv("clean_data.csv");
data = data[data.canine==False];
data.drop(['person','dept','eow','cause','canine'],1,inplace=True)

cause = [];
for name,group in data.groupby('cause_short'):
    if group['cause_short'].count()>500:
        cause.append(name);
data = data[data['cause_short'].isin(cause)];
data.index = range(len(data))
state = [];
# print data;
# print data.groupby('state').size();
for name,group in data.groupby('state'):
    if group['dept_name'].count()>500:
        state.append(name);
# print state
data = data[data['state'].isin(state)];
data.index = range(len(data))
# print data.groupby('dept_name').size();
depart = [];
for name,group in data.groupby('dept_name'):
    if group['cause_short'].count()>20:
        depart.append(name);
data = data[data['dept_name'].isin(depart)];
data.index = range(len(data))
# print data;

death_num = [];
year = [];
for name,group in data.groupby('year'):
    year.append(name-1794);
    death_num.append(group['date'].count());
# print death_num;
# print year;

figure1 = plt.figure(figsize=(10,8));
axe1 = figure1.add_subplot(1,1,1);
plt.xlim([0,2016-1794]);
plt.ylim([0,max(death_num)+10])
axe1.xaxis.set_major_locator( MultipleLocator(20));
axe1.xaxis.set_minor_locator(MultipleLocator(5));
def setMajorLabel(x,pos):
    time = int(x/20);
    xlabel = str(1794+time*20);
    return xlabel;
axe1.xaxis.set_major_formatter(FuncFormatter(setMajorLabel))
axe1.plot(year,death_num,color="#7AC5CD",linewidth=3);
plt.xlabel('Year');
plt.ylabel('deathNum');
plt.title('Police Officer Deaths by Year (1791-2016)')
plt.show()

data.groupby('cause_short').size().plot(kind="barh",color="#7AC5CD")
plt.title('Police Officer Deaths by Cause(1791-2016)')
plt.show()