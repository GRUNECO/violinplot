import matplotlib.pyplot as plt 
import seaborn as sns
import pandas as pd
from .functionsImages import createCollage,fig2img_encode
from sovaharmony.createDataframes import filter_nS_nG_1M
import numpy as np

# TOTAL
def compare_all_nD_prep(data,plot=False,encode=False):
    '''
    Parameters
    ----------
    data:
    plot:
    encode:

    Returns
    ----------

    '''
    axs=sns.catplot(x='State',y='Metric_value',data=data, col='Metric',col_wrap=3,dodge=True, kind="violin",palette="winter_r")   
    plt.title("")
    axs.fig.subplots_adjust(top=0.905,bottom=0.112, right=0.97,left=0.052, hspace=0.202, wspace=0.014) # adjust the Figure in rp
    plt.legend(data['Study'].unique(),bbox_to_anchor=(1.6, 0.2), loc=4, borderaxespad=0.)
    if plot:
        plt.show()
    if encode:
        img_encode=fig2img_encode(axs)
        return img_encode 
    return 

# ESTUDIO 
def compare_1D_nM_prep(data,name_study,plot=False,encode=False):
    s=data["Study"]==name_study
    filter=data[s]
    axs=sns.catplot(x='State',y='Metric_value',data=filter, hue='Study',col='Metric',col_wrap=3,dodge=True, kind="violin",palette="winter_r")   
    plt.legend(bbox_to_anchor=(1.6, 0.2), loc=4, borderaxespad=0.)
    if plot:
        plt.show()
    if encode:
        img_encode=fig2img_encode(axs)
        return img_encode 
    return 

def compare_nD_nM_prep(data,plot=False,encode=False):
    filter_study=data.drop(["Study","Group","Session","Subject"],axis=1,inplace=False)
    axs=sns.catplot(y='Metric',x="State",data= filter,hue='Study',fontsize=70,palette="winter_r",height=5, aspect=.8,legend=False)
    if plot:
        plt.show()
    if encode:
        img_encode=fig2img_encode(axs)
        return img_encode 
    return

# GRUPO

def compare_nD_nG_nB_prep(data,dict_info,plot=False,encode=False):
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
def compare_1D_nV_nM_prep(data,name_study,plot=False,encode=False):
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


