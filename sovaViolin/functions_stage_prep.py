import matplotlib.pyplot as plt 
import seaborn as sns
import pandas as pd
from functionsImages import createCollage
from createDataframes import filter_nS_nG_1M
import numpy as np

# TOTAL

def compare_nD(data):
    sns.catplot(x='State',y='Metric_value',data=data, col='Metric',col_wrap=3,dodge=True, kind="violin",palette="winter_r")   
    plt.legend(bbox_to_anchor=(1.6, 0.2), loc=4, borderaxespad=0.)
    plt.show()
    return 


# ESTUDIO 
def compare_1D_nM_prep(data,name_study):
    s=data["Study"]==name_study
    filter=data[s]
    sns.catplot(x='State',y='Metric_value',data=filter, hue='Study',col='Metric',col_wrap=3,dodge=True, kind="violin",palette="winter_r")   
    plt.legend(bbox_to_anchor=(1.6, 0.2), loc=4, borderaxespad=0.)
    plt.show()
    return 
    
def compare_nD_nM_prep(data):
    filter_study=data.drop(["Study","Group","Session","Subject"],axis=1,inplace=False)
    metrics=filter_study['Metric'].unique()
    figures=[]
    for i,metric in enumerate(metrics):
        fig,axs=plt.subplots()
        data_filter=data["Metric"]==metric
        filter=data[data_filter]
        parameters = {'axes.labelsize': 45,
          'axes.titlesize': 45}
        plt.rcParams.update(parameters)
        ax=sns.violinplot(y='Metric_value',x="State",data= filter,hue='Study',fontsize=70,ax=axs,palette="winter_r",height=5, aspect=.8,legend=False)
        ax.get_legend().remove()
        plt.title(metric+' ',fontsize=45)
        plt.xticks(fontsize=45)
        plt.yticks(fontsize=45)
        fig.set_size_inches(30, 15)
        figures.append(fig)
    createCollage(figures,3000,3) 
    return

# GRUPO

def compare_nD_nG_nB_prep(data,dict_info):
    figures_i=[]
    figures_f=[]
    filter_study=data.drop(["Study","Group","Session","Subject"],axis=1,inplace=False)
    metrics=filter_study.keys()
    for i,metric in enumerate(metrics):
        fig, ax = plt.subplots()
        filter_group=filter_nS_nG_1M(data,dict_info)
        ax=sns.violinplot(x='Group',y=metric,data=filter_group,ax=ax,hue='Study')
        plt.title(metric +' ',fontsize=35)
        plt.xticks(fontsize=35)
        plt.yticks(fontsize=35) 
        fig.set_size_inches(15, 15)  
        figures_i.append(fig)
    createCollage(figures_i,3000,3)       
    return 

# VISITA
def compare_1D_nV_nM_prep(data,name_study):
    filter_metrics=data.drop(["Study","Group","Session","Subject"],axis=1,inplace=False)
    metrics=filter_metrics.keys() 
    figures=[]
    for i,metric in enumerate(metrics):
        fig, ax = plt.subplots()
        filt_study=data["Study"]==name_study
        filter=data[filt_study]
        ax=sns.violinplot(x='Session',y=metric,data=filter,ax=ax,hue='Study')
        plt.title(metric +' ',fontsize=40)
        plt.xticks(fontsize=40)
        plt.yticks(fontsize=40) 
        fig.set_size_inches(15, 15)
        figures.append(fig)

    createCollage(figures,3000,3)    
    return


