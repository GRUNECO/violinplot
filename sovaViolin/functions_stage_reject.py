'''
@autor: Luisa María Zapata Saldarriaga, Universidad de Antioquia, luisazapatasaldarriaga@gmail.com  
'''

import matplotlib.pyplot as plt 
import seaborn as sns
import pandas as pd
from .functionsImages import create_collage,createCollage,fig2img_encode
from sovaharmony.createDataframes import filter_nS_nG_1M
import numpy as np

# TOTAL
def compare_all_nD_reject(data,plot=False,encode=False):
    axs=sns.catplot(x='Metric',y="Metric_Value",data=data,dodge=True, kind="violin",col_wrap=3,palette='winter_r',legend=False)
    
    if plot:
        plt.show()
    if encode:
        img_encode=fig2img_encode(axs)
        plt.close()
        return img_encode
    return 

# ESTUDIO 

def compare_1S_0C_nM_reject(data,name_study):
    """
    todos sujetos, 1 estudio todas las bandas sin distinguir el canal
    """ 
    s=data["Study"]==name_study
    filter=data[s]
    filter_study=data.drop(["Study","Group","Session","Subject"],axis=1,inplace=False)
    metrics=filter_study.keys()
    figures_i=[]
    for i,metric in enumerate(metrics[0:5]):
        fig,ax=plt.subplots()
        ax=sns.violinplot(y=metric,x="Study",data= filter,fontsize=70,ax=ax,palette='winter_r')
        plt.title(metric,fontsize=15)
        plt.xticks(fontsize=15)
        plt.yticks(fontsize=15)
        fig.set_size_inches(15, 15)
        figures_i.append(fig)
    figures_f=[]
    for i,metric in enumerate(metrics[5:]):
        fig,ax=plt.subplots()
        ax=sns.violinplot(y=metric,x="Study",data= filter,fontsize=70,ax=ax,palette='winter_r')
        plt.title(metric,fontsize=35)
        plt.xticks(fontsize=35)
        plt.yticks(fontsize=35)
        fig.set_size_inches(15, 15)
        figures_f.append(fig)
    createCollage(figures_i,3000,3) 
    createCollage(figures_f,3000,4) 
    return 

def compare_nD_reject(data,plot=False,encode=False):
    """
    todos sujetos, n estudio 
    """ 
    axs=sns.catplot(x='Study',y="Metric_Value",data=data,dodge=True, kind="violin",col="Metric",col_wrap=3,palette='winter_r',legend=False)
    
    if plot:
        plt.show()
    if encode:
        img_encode=fig2img_encode(axs)
        plt.close()
        return img_encode
    return 

# GRUPO

def compare_1D_nG_nM_reject(data,name_study,plot=False,encode=False):
    filt_study=data["Study"]==name_study
    filter=data[filt_study]
    axs=sns.catplot(x='Group',y="Metric_Value",data=filter,dodge=True, kind="violin",col="Metric",col_wrap=3,palette='winter_r',legend=False)
    
    if plot:
        plt.show()
    if encode:
        img_encode=fig2img_encode(axs)
        plt.close()
        return img_encode
    return 

# VISITAS
    
def compare_1D_nV_nM_reject(data,name_study,plot=False,encode=False):
    filt_study=data["Study"]==name_study
    filter=data[filt_study]
    axs=sns.catplot(x='Session',y="Metric_Value",data=filter,dodge=True, kind="violin",col="Metric",col_wrap=3,palette='winter_r',legend=False)
    
    if plot:
        plt.show()
    if encode:
        img_encode=fig2img_encode(axs)
        plt.close()
        return img_encode
    return   
