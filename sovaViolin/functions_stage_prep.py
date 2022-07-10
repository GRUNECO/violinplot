'''
@autor: Luisa María Zapata Saldarriaga, Universidad de Antioquia, luisazapatasaldarriaga@gmail.com  
'''

import matplotlib.pyplot as plt 
import seaborn as sns
import pandas as pd
from .functionsImages import createCollage,fig2img_encode
from sovaharmony.createDataframes import filter_nS_nG_1M
import numpy as np
import time 

# TOTAL
def compare_all_nD_prep(data,color="winter_r",plot=False,encode=False):
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

    axs=sns.catplot(x='State',y='Metric_value',data=data, col='Metric',col_wrap=3,dodge=True,hue='Study', kind="violin",palette=color, bw=1,legend=False) 
    axs.fig.suptitle('Análisis global para las métricas de calidad de la etapa del PREP')
    axs.set(xlabel=None)
    axs.set(ylabel=None)
    axs.fig.subplots_adjust(top=0.855,bottom=0.095, right=1,left=0.052, hspace=0.193, wspace=0.036) # adjust the Figure in rp
    axs.add_legend(loc='upper center',bbox_to_anchor=(.5,.95),ncol=len(data['Study'].unique()))
    axs.fig.text(0.5, 0.04, 'Estado', ha='center', va='center')
    axs.fig.text(0.02, 0.5,  'Valor de la métrica', ha='center', va='center',rotation='vertical')
    
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
    axs=sns.catplot(x='State',y='Metric_value',data=filter, hue='Study',col='Metric',col_wrap=3,dodge=True, kind="violin")   
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
    axs=sns.catplot(x='Study',y="Metric_value",data= data,col='Metric',hue='State',col_wrap=3,palette="winter_r",height=5, aspect=.8,legend=False,kind="violin")
    axs.add_legend(loc='upper center',bbox_to_anchor=(.4,1.02),ncol=3)
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
    filter=data[data["Study"]==name_study]
    axs=sns.catplot(x='Group',y='Metric_value',data=filter,row='Metric',col='State',dodge=True, kind="violin",palette="winter_r",legend=False) 
    
    if plot:
        plt.show()
    if encode:
        img_encode=fig2img_encode(axs)
        plt.close()
        return img_encode     
    return 

# VISITA
def compare_1D_nV_nM_prep(data,name_study,color='winter_r',plot=False,encode=False):
    filter=data[data["Study"]==name_study]
    axs=sns.catplot(x='State',y='Metric_value',data=filter,col='Metric',col_wrap=3,hue='Session',kind="violin",dodge=True,palette=color,bw=1,legend=False) 
    axs.fig.suptitle('Análisis entre sesiones para las métricas de calidad de la etapa del PREP')
    axs.set(xlabel=None)
    axs.set(ylabel=None)
    sns.set_theme(style="darkgrid")
    axs.fig.subplots_adjust(top=0.855,bottom=0.095, right=0.976,left=0.052, hspace=0.193, wspace=0.036) # adjust the Figure in rp
    axs.add_legend(loc='upper center',bbox_to_anchor=(.5,.95),ncol=len(data['Session'].unique()))
    axs.fig.text(0.5, 0.04, 'Estado', ha='center', va='center')
    axs.fig.text(0.01, 0.5,  'Valor de la métrica', ha='center', va='center',rotation='vertical')
    
    if plot:
        plt.show()
    if encode:
        img_encode=fig2img_encode(axs)
        plt.close()
        return img_encode     
    return


