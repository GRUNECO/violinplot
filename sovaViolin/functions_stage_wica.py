import matplotlib.pyplot as plt 
import seaborn as sns
import pandas as pd
from .functionsImages import fig2img_encode  
import numpy as np

#TOTAL
def compare_all_nD_wica(data,plot=False,encode=False):
    axs=sns.violinplot(y='Components',data=data,palette='winter_r')
    plt.title("")
    if plot:
        plt.show()
    if encode:
        img_encode=fig2img_encode(axs)
        return img_encode
    return 

# ESTUDIO

def compare_1D_wica(data,name_study,plot=False,encode=False):
    s=data["Study"]==name_study
    filter_study=data[s]
    axs=sns.violinplot(x='Study',y='Components',data=filter_study,palette='winter_r')
    if plot:
        plt.show()
    if encode:
        img_encode=fig2img_encode(axs)
        return img_encode
    return 

def compare_nD_wica(data,plot=False,encode=False):
    axs=sns.violinplot(x='Study',y='Components',data=data,palette='winter_r')
    if plot:
        plt.show()
    if encode:
        img_encode=fig2img_encode(axs)
        return img_encode
    return 

# WICA  VISITAS
def compare_1D_nV_wica(data,name_study,plot=False,encode=False):
    s=data["Study"]==name_study
    filter_study=data[s]
    axs=sns.violinplot(x='Session',y='Components',data=filter_study,palette='winter_r')
    if plot:
        plt.show()
    if encode:
        img_encode=fig2img_encode(axs)
        return img_encode
    return 

# GRUPOS
def filter_nD_nG_1B(superdata,group_dict):
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

def compare_nD_nG_wica(data,dict_info,plot=False,encode=False):
    fig, ax = plt.subplots(figsize=(15,10))
    filter_group=filter_nD_nG_1B(data,dict_info)
    axs=sns.violinplot(x='Group',y="Components",data=filter_group,ax=ax,hue='Study',palette='winter_r')
    if plot:
        plt.show()
    if encode:
        img_encode=fig2img_encode(axs)
        return img_encode      
    return 

