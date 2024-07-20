import numpy as np
import pandas as pd
import janitor
import matplotlib.pyplot as plt
import seaborn as sns

def pie_chart(data, x, y, agg=np.sum):    
    data = data.groupby(x)[y].agg(agg).reset_index()    
    plt.figure(figsize=(5,5))
    plt.pie(data[y], labels=data[x], autopct='{:.2f}%'.format)
    plt.show()

def line_chart(data, x, y, c=None, agg=np.sum, width=15, height=5):
    plt.figure(figsize=(width, height))
    sns.lineplot(data=data, x=x, y=y, hue=c, estimator=agg, linewidth=1.5)
    plt.show()

def bar_chart(data, x, y, c, agg=np.sum, mode='group', orient='vertical', width=9, height=6):
    if mode == 'group':
        if orient.startswith('v'):
            plt.figure(figsize=(width, height))
            sns.barplot(data=data, x=x, y=y, hue=c, estimator=agg, ci=False)
            plt.show()
        if orient.startswith('h'):
            plt.figure(figsize=(width, height))
            sns.barplot(data=data, x=y, y=x, hue=c, estimator=agg, ci=False, orient='h')
            plt.show()
        
    if mode == 'stack':
        data = data.pivot_table(index=x, columns=c, values=y, aggfunc=agg)
        if orient.startswith('v'):
            data.plot.bar(stacked=True, figsize=(width, height))
            plt.legend(bbox_to_anchor=(1.04,1), loc='upper left')
            plt.show()
        if orient.startswith('h'):
            data.plot.barh(stacked=True, figsize=(width, height))
            plt.legend(bbox_to_anchor=(1.04,1), loc='upper left')
            plt.show()
            
    if mode == 'percent':
        data = data.pivot_table(index=x, columns=c, values=y, aggfunc=agg)
        data = data.div(data.sum(1), axis=0)
        if orient.startswith('v'):
            data.plot.bar(stacked=True, figsize=(width, height))
            plt.legend(bbox_to_anchor=(1.04,1), loc='upper left')
            plt.show()
        if orient.startswith('h'):
            data.plot.barh(stacked=True, figsize=(width, height))
            plt.legend(bbox_to_anchor=(1.04,1), loc='upper left')
            plt.show()

def area_chart(data, x, y, c, agg=np.sum, mode='stack', width=9, height=6):
    data = data.pivot_table(index=x, columns=c, values=y, aggfunc=agg)
    if mode == 'stack':
        data.plot.area(stacked=True, figsize=(width, height))
        plt.legend(bbox_to_anchor=(1.04,1), loc='upper left', title=c)
        plt.ylabel(y)
        plt.show()
        
    if mode == 'percent':
        data = data.div(data.sum(1), axis=0)
        data.plot.area(stacked=True, figsize=(width, height))
        plt.legend(bbox_to_anchor=(1.04,1), loc='upper left', title=c)
        plt.ylabel(y)
        plt.show()

def scatter_plot(data, x, y, c=None, s=None, agg=np.sum, opacity=0.8, width=10, height=5):
    plt.figure(figsize=(width, height))
    sns.scatterplot(data=data, x=x, y=y, hue=c, size=s, s=100, alpha=opacity, sizes=(100,1000))