import matplotlib.pyplot as plt 
import seaborn as sns
import pandas as pd
from .functionsImages import createCollage,fig2img_encode
from sovaharmony.createDataframes import filter_nS_nG_1M
import numpy as np
import time 

# TOTAL
def compare_all_nD_prep(data,plot=False,encode=False):
    '''
    Parameters
    ----------
        data:dataframe
        plot: Boolean 
        encode: Boolean 

    Returns
    ----------
        img_encode: str
        
    '''
    axs=sns.catplot(x='State',y='Metric_value',data=data, col='Metric',col_wrap=3,dodge=True, kind="violin",palette="winter_r") 
    plt.title("")
    axs.fig.subplots_adjust(top=0.905,bottom=0.112, right=0.97,left=0.052, hspace=0.202, wspace=0.014) # adjust the Figure in rp
    plt.legend(data['Study'].unique(),bbox_to_anchor=(1.6, 0.2), loc=4)
    
    if plot:
        plt.show()
    if encode:
        img_encode=fig2img_encode(axs)
        plt.close()
        return img_encode 
    return 

# ESTUDIO 
def compare_1D_nM_prep(data,name_study,plot=False,encode=False):
    '''
    Parameters
    ----------
        data:dataframe
        name_study: str
        plot: Boolean 
        encode: Boolean 

    Returns
    ----------
        img_encode: str
        
    '''
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

def compare_nD_prep(data,plot=False,encode=False):
    '''
    Compare n studies n metrics 

    Parameters
    ----------
        data:dataframe
        plot: Boolean 
        encode: Boolean 

    Returns
    ----------
        img_encode: str
    '''
    axs=sns.catplot(x='State',y="Metric_value",data= data,col='Metric',hue='Study',col_wrap=3,palette="winter_r",height=5, aspect=.8,legend=False,kind="violin")
    
    if plot:
        plt.show()
    if encode:
        img_encode=fig2img_encode(axs)
        plt.close()
        return img_encode 
    return

# GRUPO

def compare_1D_nG_prep(data,name_study,plot=False,encode=False):
    '''
    Compare n studies n  groups metrics

    Parameters
    ----------
        data:dataframe
        plot: Boolean 
        encode: Boolean 

    Returns
    ----------
        img_encode: str
    '''    
    filt_study=data["Study"]==name_study
    filter=data[filt_study]
    axs=sns.catplot(x='Group',y='Metric_value',data=filter,row='Metric',col='State',dodge=True, kind="violin",palette="winter_r",legend=False) 
    
    if plot:
        plt.show()
    if encode:
        img_encode=fig2img_encode(axs)
        plt.close()
        return img_encode     
    return 

# VISITA
def compare_1D_nV_nM_prep(data,name_study,plot=False,encode=False):
    filt_study=data["Study"]==name_study
    filter=data[filt_study]
    axs=sns.catplot(x='Session',y='Metric_value',data=filter,row='Metric',col='State',dodge=True, kind="violin",palette="winter_r",legend=False) 
    
    if plot:
        plt.show()
    if encode:
        img_encode=fig2img_encode(axs)
        plt.close()
        return img_encode     
    return


