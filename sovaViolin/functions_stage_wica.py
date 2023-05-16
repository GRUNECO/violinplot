'''
@autor: Luisa María Zapata Saldarriaga, Universidad de Antioquia, luisazapatasaldarriaga@gmail.com  
'''

import matplotlib.pyplot as plt 
import seaborn as sns
import pandas as pd
from .functionsImages import fig2img_encode  
import numpy as np

#TOTAL
def compare_all_nD_wica(data,color='winter_r',plot=False,encode=False):
    '''
    Parameters
    ----------
        data: dataframes
        plot: Boolean
        encode: Boolean 

    Returns
    ----------
        img_encode:
    '''
    sns.set_theme(style="darkgrid")
    axs=sns.catplot(y='Components',data=data,palette=color,kind='violin',legend=False)
    plt.legend(data['Study'].unique())
    axs.fig.suptitle('Análisis global para las métricas de calidad de la etapa del wICA')
    axs.set(xlabel=None)
    axs.set(ylabel=None)
    sns.set_theme(style="darkgrid")
    axs.fig.subplots_adjust(top=0.855,bottom=0.095, right=1,left=0.052, hspace=0.193, wspace=0.036) # adjust the Figure in rp
    axs.fig.text(0.5, 0.04, 'Componentes', ha='center', va='center')
    axs.fig.text(0.02, 0.5,  'Porcentaje de componentes filtradas', ha='center', va='center',rotation='vertical')

    if plot:
        plt.show()
    if encode:
        img_encode=fig2img_encode(axs)
        
        plt.close()
        return img_encode
    return 

# ESTUDIO

def compare_1D_wica(data,name_study,plot=False,encode=False):
    '''
    Parameters
    ----------
        data: dataframes
        name_study: str 
        plot: Boolean
        encode: Boolean 

    Returns
    ----------
        img_encode:
    '''
    s=data["Study"]==name_study
    filter_study=data[s]
    axs=sns.violinplot(x='Study',y='Components',data=filter_study,palette='winter_r')
    plt.title("The Wavelet Transform and the Independent Component Analysis (wICA) technique for "+ name_study)
    if plot:
        plt.show()
    if encode:
        img_encode=fig2img_encode(axs)
        return img_encode
    return 

def compare_nD_wica(data,color='winter_r',plot=False,encode=False):
    '''
    Parameters
    ----------
        data: dataframes
        plot: Boolean
        encode: Boolean 

    Returns
    ----------
        img_encode:
    '''
    sns.set_theme(style="darkgrid")
    data["Study"].replace({'BIOMARCADORES':'UdeA 1','DUQUE':'UdeA 2'}, inplace=True)
    axs=sns.catplot(x='Study',y='Components',data=data,kind='violin',hue='Study',palette=color,legend=True)
    axs.fig.suptitle('Comparative Analysis of Quality Metrics in the wICA Stage Across Cohorts')
    axs.set(xlabel=None)
    axs.set(ylabel=None)
    sns.set_theme(style="darkgrid")
    axs.fig.subplots_adjust(top=0.88,bottom=0.14, right=0.921,left=0.079, hspace=0.193, wspace=0.036) # adjust the Figure in rp
    axs.add_legend(loc='upper center',bbox_to_anchor=(.5,.95),ncol=len(data['Study'].unique()))
    axs.fig.text(0.5, 0.04, 'Estado', ha='center', va='center')
    axs.fig.text(0.02, 0.5,  'Metric value', ha='center', va='center',rotation='vertical')
    if plot:
        plt.show()
    if encode:
        img_encode=fig2img_encode(axs)
        plt.close()
        return img_encode
    return 

# WICA  VISITAS
def compare_1D_nV_nM_wica(data,name_study,color='winter_r',plot=False,encode=False):
    '''
    Parameters
    ----------
        data: dataframes
        name_study: str 
        plot: Boolean
        encode: Boolean 

    Returns
    ----------
        img_encode:
    '''
    filter=data[data["Study"]==name_study]
    axs=sns.catplot(x='Session',y='Components',data=filter,palette=color,kind='violin',hue='Session')
    axs.fig.suptitle('Análisis entre sesiones para las métricas de calidad de la etapa de rechazo de épocas en el conjunto de datos de '+ name_study)
    axs.set(xlabel=None)
    axs.set(ylabel=None)
    sns.set_theme(style="darkgrid")
    axs.fig.subplots_adjust(top=0.855,bottom=0.095, right=0.976,left=0.052, hspace=0.193, wspace=0.036) # adjust the Figure in rp
    axs.add_legend(loc='upper center',bbox_to_anchor=(.5,.95),ncol=len(data['Session'].unique()))
    axs.fig.text(0.5, 0.04, 'Sesiones', ha='center', va='center')
    axs.fig.text(0.01, 0.5,  'Valor de la métrica', ha='center', va='center',rotation='vertical')
    
    if plot:
        plt.show()
    if encode:
        img_encode=fig2img_encode(axs)
        return img_encode
    return 

# GRUPOS
def filter_nD_nG_wica(superdata,group_dict):
    """
    group_dict={
        'BIOMARCADORES':[CTR,DCL],
        'SRM':['SRM'] # assume datasets with no groups have Group=Study
    }
    
    """
    fil=superdata
    list_df=[]

    for dataset,group_list in group_dict.items():
        for group in group_list:
            auxfil = fil[fil['Group']==group]
            list_df.append(auxfil)
    df=pd.concat((list_df))
    return df

def compare_1D_nG_wica(data,name_study,color='winter_r',plot=False,encode=False):
    sns.set_theme(style="darkgrid")
    filter=data[data["Study"]==name_study]
    axs=sns.catplot(x='Group',y='Components',data=filter,palette=color,kind='violin',bw=1)
    axs.fig.suptitle('Análisis entre grupos para las métricas de calidad de la etapa del wICA en el conjunto de datos de '+ name_study)
    axs.set(xlabel=None)
    axs.set(ylabel=None)
    sns.set_theme(style="darkgrid")
    axs.fig.subplots_adjust(top=0.855,bottom=0.095, right=0.976,left=0.052, hspace=0.193, wspace=0.036) # adjust the Figure in rp
    axs.add_legend(loc='upper center',bbox_to_anchor=(.5,.95),ncol=len(data['Group'].unique()))
    axs.fig.text(0.5, 0.04, 'Grupos', ha='center', va='center')
    axs.fig.text(0.01, 0.5,  'Valor de la métrica', ha='center', va='center',rotation='vertical')
    if plot:
        plt.show()
    if encode:
        img_encode=fig2img_encode(axs)
        return img_encode


# def compare_nD_nG_wica(data,dict_info,plot=False,encode=False):
#     '''
#     Parameters
#     ----------
#         data: dataframes
#         dict_info: dict 
#         plot: Boolean
#         encode: Boolean 

#     Returns
#     ----------
#         img_encode:
#     '''
#     fig, ax = plt.subplots(figsize=(15,10))
#     filter_group=filter_nD_nG_wica(data,dict_info)
#     axs=sns.violinplot(x='Group',y="Components",data=filter_group,ax=ax,hue='Study',palette='winter_r')
#     plt.title("Comparison of different groups in the Wavelet Transform stage and the Independent Component Analysis (wICA) technique for ")
#     if plot:
#         plt.show()
#     if encode:
#         img_encode=fig2img_encode(axs)
#         return img_encode      
#     return 

