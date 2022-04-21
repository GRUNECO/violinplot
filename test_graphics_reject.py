import matplotlib.pyplot as plt 
import seaborn as sns
import pandas as pd
from datasets import BIOMARCADORES
from datasets import SRM
from Graphics.graphicsViolin import get_dataframe_wica
import numpy as np
import itertools
from pprint import pprint


Studies=[BIOMARCADORES,SRM]

datosReject=get_dataframe_reject(Studies)

# REJECT ESTUDIO 

# Preguntar: si es importante hacerlo por canal 
def compare_1S_0C_reject(data,name_study,plot=False):
    """
    todos sujetos, 1 estudio todas las bandas sin distinguir el canal
    """ 
    s=data["Study"]==name_study
    filter=data[s]
    filter_study=data.drop(["Study"],axis=1,inplace=False)
    metrics=filter_study.keys()
    initial_metrics=metrics[0:5]
    final_metrics=metrics[5:]
    figure1=plt.figure(figsize=(30,60), dpi=30) 
    #plt.subplots_adjust(hspace=0.5,wspace=7) 
        
    for i,metric in enumerate(metrics[0:5]):
        plt.subplot(len(metrics[0:5]),1,i+1)
        f=sns.violinplot(y=metric,x="Study",data= filter,fontsize=70)
        f.set_ylabel(metric,fontsize=70)
        plt.xticks(fontsize=70)
        plt.yticks(fontsize=70)

    figure1.tight_layout()
    plt.savefig('Images/Reject/'+'initialMetrics_'+name_study+'.png')
    plt.show()

    figure2=plt.figure(figsize=(30,60), dpi=30) 
    for i,metric in enumerate(metrics[5:]):
        plt.subplot(len(metrics[5:]),1,i+1)
        f=sns.violinplot(y=metric,x="Study",data= filter,fontsize=70)
        f.set_ylabel(metric,fontsize=70)
        plt.xticks(fontsize=70)
        plt.yticks(fontsize=70)
    figure2.tight_layout()
    plt.savefig('Images/Reject/'+'finalMetrics_'+name_study+'.png')
    plt.show()
    listofimages_i='Images/Reject/'+'initialMetrics_'+name_study+'.png'
    listofimages_f='Images/Reject/'+'finalMetrics_'+name_study+'.png'
    return listofimages_i,listofimages_f

def compare_nS_0C_reject(data):   
    studies=data["Study"].unique()
    listImages_i=[]
    listImages_f=[]
    for study in studies:
        listofimages_i,listofimages_f =compare_1S_0C_reject(data,study,plot=False)
        listImages_i.append(listofimages_i)
        listImages_f.append(listofimages_f)
    listImages_i.extend(listImages_f)
    return listImages_i
        
'''
# Reject
create_collage(4,1,1800, 1000,compare_nS_0C_reject(datosReject))
'''
