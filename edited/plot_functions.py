import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
plt.style.use('ggplot')

def plot_kmeans_centers(model, n_clust, pos=plt):
    
    for k in range(n_clust):
        n_entries = np.sum(model.labels_ == k)
        pos.plot(model.cluster_centers_[k,:], label='c'+str(k)+' ('+str(n_entries)+')')
    
    pos.legend(loc='best')

def plot_clust(model, df1, df2, l, pos = plt):
    pos.plot(np.arange(10), df1.iloc[np.where(model.labels_==l)].values.T, color=(1.0,0.0,0.0,0.1))
    pos.plot(np.arange(10), df2.iloc[np.where(model.labels_==l)].values.T, color=(0.0,0.0,1.0,0.1))
    
    red = mpatches.Patch(color='red', label='prot')
    blue = mpatches.Patch(color='blue', label='mRNA')
    pos.legend(handles=[red,blue], loc='best')

def plot_clust_avg(model, df1, df2, l, pos = plt):
    pos.plot(pd.DataFrame(df1.iloc[np.where(model.labels_==l)].values).mean(), label = "protein")
    pos.plot(pd.DataFrame(df2.iloc[np.where(model.labels_==l)].values).mean(), label = "mRNA")
    
    pos.legend(loc='best')