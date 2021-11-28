import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


# we will use this as a blueprint for the csv file
tesla = pd.read_csv('TSLA.csv')


#print(tesla.columns)
dates = tesla['Date']
Open = tesla['Open']
High = tesla['High']
Low = tesla['Low']
Close = tesla['Close']
Volume = tesla['Volume']



#
# print(Open)
g = Open.mean()
#print(g)
#print(len(Open))

'''
list = []
for i in range(len(Open)):
    list.append(Open[i])
    #print(list)

#plt.plot(dates, list)
#plt.show()

plt.plot(dates, list, 'r', label='Open')
plt.plot(dates, High, 'g', label='High')
plt.plot(dates, Low, 'b', label='Low')
plt.plot(dates, Close, 'y', label='Close')
plt.legend()
plt.show()
'''

'''
plt.plot(dates, Open, 'r', label='Open')
plt.show()
'''

tsladates = []
opendates = []
for i in range(len(dates)-10,len(dates)):
    tsladates.append(dates[i])
    opendates.append(Open[i])

#plt.plot(tsladates, opendates, 'r', label='Open')
#plt.show()


import plotly.graph_objects as go

'''
fig = go.Figure(data=[go.Scatter(x=tsladates, y=opendates, mode='lines')]) ## for plotting
fig.show() ## for plotting
'''

def show_plot():
    #fig = go.Figure(data=[go.Scatter(x=tsladates, y=opendates, mode='lines')]) ## for plotting
    #fig.show() ## for plotting
    fig = go.Figure(data=[go.Scatter(x=dates, y=Close, mode='lines')]) ## for plotting
    fig.show() ## for plotting
    
    return None



