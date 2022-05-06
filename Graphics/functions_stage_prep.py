import matplotlib.pyplot as plt 
import seaborn as sns
import pandas as pd
from functionsImages import createCollage
from graphicsViolin import filter_nS_nG_1M
import numpy as np

# TOTAL

def compare_nD(data,title):
    filter_study=data.drop(["Study","Group","Session","Subject"],axis=1,inplace=False)
    metrics=filter_study.keys()
    figures=[]
    for i,metric in enumerate(metrics):
        fig,ax=plt.subplots()
        ax=sns.violinplot(y=metric,data= data,fontsize=70,ax=ax)
        plt.title(metric+' '+title,fontsize=15)
        plt.xticks(fontsize=15)
        plt.yticks(fontsize=15)
        fig.set_size_inches(15, 15)
        figures.append(fig)
    createCollage(figures,3000,3) 

# ESTUDIO 
def compare_1S_nM_prep(data,name_study,title):
    s=data["Study"]==name_study
    filter=data[s]
    filter_study=data.drop(["Study","Group","Session","Subject"],axis=1,inplace=False)
    metrics=filter_study.keys()
    figures=[]
    for i,metric in enumerate(metrics):
        fig,ax=plt.subplots()
        ax=sns.violinplot(y=metric,x="Study",data= filter,fontsize=70,ax=ax)
        plt.title(metric +' '+ title,fontsize=30)
        plt.xticks(fontsize=30)
        plt.yticks(fontsize=30)
        fig.set_size_inches(15, 15)
        figures.append(fig)
    createCollage(figures,3000,3) 

def compare_nS_nM_prep(data,title):
    filter_study=data.drop(["Study","Group","Session","Subject"],axis=1,inplace=False)
    metrics=filter_study.keys()
    figures=[]
    for i,metric in enumerate(metrics):
        fig,ax=plt.subplots()
        ax=sns.violinplot(y=metric,x="Study",data= data,fontsize=70,ax=ax)
        plt.title(metric+' '+title,fontsize=15)
        plt.xticks(fontsize=15)
        plt.yticks(fontsize=15)
        fig.set_size_inches(15, 15)
        figures.append(fig)
    createCollage(figures,3000,3) 
    return

# GRUPO

def compare_nS_nG_nB_prep(data,dict_info,title):
    figures_i=[]
    figures_f=[]
    filter_study=data.drop(["Study","Group","Session","Subject"],axis=1,inplace=False)
    metrics=filter_study.keys()
    for i,metric in enumerate(metrics):
        fig, ax = plt.subplots()
        filter_group=filter_nS_nG_1M(data,dict_info)
        ax=sns.violinplot(x='Group',y=metric,data=filter_group,ax=ax,hue='Study')
        plt.title(metric +' '+title,fontsize=35)
        plt.xticks(fontsize=35)
        plt.yticks(fontsize=35) 
        fig.set_size_inches(15, 15)  
        figures_i.append(fig)
    createCollage(figures_i,3000,3)       
    return 

# VISITA
def compare_1S_nV_nM_prep(data,name_study,title):
    filter_metrics=data.drop(["Study","Group","Session","Subject"],axis=1,inplace=False)
    metrics=filter_metrics.keys() 
    figures=[]
    for i,metric in enumerate(metrics):
        fig, ax = plt.subplots()
        filt_study=data["Study"]==name_study
        filter=data[filt_study]
        ax=sns.violinplot(x='Session',y=metric,data=filter,ax=ax,hue='Study')
        plt.title(metric +' '+ title,fontsize=40)
        plt.xticks(fontsize=40)
        plt.yticks(fontsize=40) 
        fig.set_size_inches(15, 15)
        figures.append(fig)

    createCollage(figures,3000,3)    
    return


