import matplotlib.pyplot as plt 
import seaborn as sns
import pandas as pd
from .functionsImages import fig2img_encode  
import numpy as np

#TOTAL
def compare_all_nD_wica(data,plot=False,encode=False):
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
    axs=sns.catplot(y='Components',data=data,palette='winter_r',kind='violin')
    plt.legend(data['Study'].unique())
    plt.title("The Wavelet Transform and the Independent Component Analysis (wICA) technique for all datasets")
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

def compare_nD_wica(data,plot=False,encode=False):
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
    axs=sns.catplot(x='Study',y='Components',data=data,kind='violin',palette='winter_r',legend=True)
    print(data)
    if plot:
        plt.show()
    if encode:
        img_encode=fig2img_encode(axs)
        plt.close()
        return img_encode
    return 

# WICA  VISITAS
def compare_1D_nV_nM_wica(data,name_study,plot=False,encode=False):
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
    axs=sns.catplot(x='Session',y='Components',data=filter_study,palette='winter_r',kind='violin')
    plt.title("Comparison of different session in the Wavelet Transform stage and the Independent Component Analysis (wICA) technique for "+name_study)
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

def compare_1D_nG_wica(data,name_study,plot=False,encode=False):
    s=data["Study"]==name_study
    filter_study=data[s]
    axs=sns.catplot(x='Group',y='Components',data=filter_study,palette='winter_r',kind='violin')
    plt.title("Comparison of different session in the Wavelet Transform stage and the Independent Component Analysis (wICA) technique for "+name_study)
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

