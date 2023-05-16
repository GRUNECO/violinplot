'''
@autor: Luisa María Zapata Saldarriaga, Universidad de Antioquia, luisazapatasaldarriaga@gmail.com  
'''

import matplotlib.pyplot as plt 
import seaborn as sns
import pandas as pd
from .functionsImages import create_collage,createCollage,fig2img_encode
import numpy as np

# TOTAL
def compare_all_nD_reject(data,color='winter_r',plot=False,encode=False):
    sns.set_theme(style="darkgrid")
    axs=sns.catplot(y="Metric_Value",data=data,dodge=True, kind="violin",col='Metric',col_wrap=3,palette=color,legend=False)
    axs.fig.suptitle('Análisis global para las métricas de calidad de la etapa de rechazo de épocas')
    axs.set(xlabel=None)
    axs.set(ylabel=None)
    axs.fig.subplots_adjust(top=0.855,bottom=0.095, right=0.976,left=0.052, hspace=0.193, wspace=0.036) # adjust the Figure in rp
    axs.add_legend(loc='upper center',bbox_to_anchor=(.5,.95),ncol=len(data['Group'].unique()))
    axs.fig.text(0.5, 0.04, 'Métrica', ha='center', va='center')
    axs.fig.text(0.01, 0.5,  'Valor de la métrica', ha='center', va='center',rotation='vertical')
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

def compare_nD_reject(data,color='winter_r',plot=False,encode=False):
    """
    todos sujetos, n estudio 
    """ 
    sns.set_theme(style="darkgrid")
    data["Study"].replace({'BIOMARCADORES':'UdeA 1','DUQUE':'UdeA 2'}, inplace=True)
    axs=sns.catplot(x='Study',y="Metric_Value",data=data,dodge=True, kind="violin",col="Metric",col_wrap=3,palette=color,legend=False)
    axs.fig.suptitle('Comparative Analysis of Quality Metrics in the Period Rejection Stage Across Cohorts')
    axs.set(xlabel=None)
    axs.set(ylabel=None)
    axs.fig.subplots_adjust(top=0.855,bottom=0.095, right=0.976,left=0.052, hspace=0.193, wspace=0.036) # adjust the Figure in rp
    axs.add_legend(loc='upper center',bbox_to_anchor=(.5,.95),ncol=len(data['Group'].unique()))
    axs.fig.text(0.5, 0.04, 'Cohorts', ha='center', va='center')
    axs.fig.text(0.01, 0.5,  'Metric value', ha='center', va='center',rotation='vertical')
    if plot:
        plt.show()
    if encode:
        img_encode=fig2img_encode(axs)
        plt.close()
        return img_encode
    return 

# GRUPO

def compare_1D_nG_nM_reject(data,name_study,color='winter_r',plot=False,encode=False):
    sns.set_theme(style="darkgrid")
    filter=data[data["Study"]==name_study]
    axs=sns.catplot(x='Group',y="Metric_Value",data=filter,dodge=True, kind="violin",col="Metric",hue='Group',col_wrap=3,bw=1,palette=color,legend=False)
    axs.fig.suptitle('Análisis entre grupos para las métricas de calidad de la etapa de rechazo de épocas en el conjunto de datos de '+ name_study)
    axs.set(xlabel=None)
    axs.set(ylabel=None)
    axs.fig.subplots_adjust(top=0.855,bottom=0.095, right=0.976,left=0.052, hspace=0.193, wspace=0.036) # adjust the Figure in rp
    axs.add_legend(loc='upper center',bbox_to_anchor=(.5,.95),ncol=len(data['Group'].unique()))
    axs.fig.text(0.5, 0.04, 'Grupos', ha='center', va='center')
    axs.fig.text(0.01, 0.5,  'Valor de la métrica', ha='center', va='center',rotation='vertical')
    
    if plot:
        plt.show()
    if encode:
        img_encode=fig2img_encode(axs)
        plt.close()
        return img_encode
    return 

# VISITAS
    
def compare_1D_nV_nM_reject(data,name_study,color='winter_r',plot=False,encode=False):
    sns.set_theme(style="darkgrid")
    filter=data[data["Study"]==name_study]
    axs=sns.catplot(x='Session',y="Metric_Value",data=filter,dodge=True, kind="violin",col="Metric",hue='Session',bw=1,col_wrap=3,palette=color,legend=False)
    axs.fig.suptitle('Análisis entre sesiones para las métricas de calidad de la etapa del PREP en el conjunto de datos de '+ name_study)
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
        plt.close()
        return img_encode
    return   
