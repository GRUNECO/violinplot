from tokenize import group
import matplotlib.pyplot as plt 
import seaborn as sns
import pandas as pd
from .functionsImages import create_collage,createCollage
import numpy as np
import pandas as pd 

# **************************** WHITOUT NORMALIZING *********************************************
# TOTAL
def compare_nD_power(data,plot=False):
    """
    data: all dataset in format dataframe
    plot: False 

    Return
    Fig 

    """ 
    data=data.drop(["Channels"],axis=1,inplace=False)
    bandas=data["Bands"].unique()
    fig, ax = plt.subplots(1,1)
    fig.set_size_inches(len(bandas)*2,10)
    sns.violinplot(x='Bands',y="Powers",data=data, palette="winter_r")
    ax.set_title('Relative bands powers all data')
    ax.set_ylim(-0.1,1.0)
    if plot:
        plt.show()
    return fig 

# ESTUDIOS 

def compare_1D_nB_0C_power(data,name_study,plot=False): 
    """
    1 Dataset, n bandas, sin distinguir canal
    """ 
    data=data.drop(["Channels"],axis=1,inplace=False)
    s=data["Study"]==name_study
    filter_study=data[s]
    bandas=filter_study["Bands"].unique()
    fig, ax = plt.subplots(1,1)
    fig.set_size_inches(len(bandas)*2,10)
    sns.violinplot(x='Bands',y="Powers",data=filter_study,palette="winter_r")
    ax.set_title('Relative bands powers for the '+name_study)
    ax.set_ylim(-0.1,1.0)
    if plot:
        plt.show()
    return fig 

def compare_1D_1B_nC_power(data,name_study,name_band,plot=False):
    """
    1 dataset - 1 band - n channels
    
    """
    b=np.logical_and(data["Bands"]==name_band, data["Study"]==name_study)
    filter_band=data[b]
    channels=data["Channels"].unique()
    fig, ax = plt.subplots(1,1)
    fig.set_size_inches(len(channels)*2,10)
    sns.violinplot(x='Channels',y="Powers",data=filter_band,palette="winter_r")
    ax.set_title('Relative bands powers  '+name_study+'-'+name_band)
    ax.set_ylim(-0.1,1.0)
    fig.tight_layout()
    if plot:
        plt.show()
    return fig 

def filter_nD_1B_1C_power(data,channel):
    '''
    n datasets- 1 band- 1 channel 
    '''
    fil_B_C=data["Channels"]==channel
    filter=data[fil_B_C]
    return filter

def compare_nD_nB_power(data,name_channel="None"):
    '''
    n datasets - n bands
    '''
    bandas=data["Bands"].unique()
    rows=1
    cols=7
    #en un canal especifico
    if name_channel != "None":
        sns.violinplot(x='Bands',y="Powers",data=data,hue='Study',palette="winter_r")
        plt.ylim(-0.1,1.0)
        plt.title('Relative band powers for study'+ ' '+ name_channel,fontsize=15) 
        plt.xticks(fontsize=15)
        plt.yticks(fontsize=15)
        plt.show()
 
    else: 
        #sin distinguir el canal
        sns.violinplot(x='Bands',y="Powers",data=data,hue='Study',palette="winter_r")
        plt.title('Relative band powers for study',fontsize=15) 
        plt.ylim(-0.1,1.0)
        plt.xticks(fontsize=15)
        plt.yticks(fontsize=15) 
        plt.show() 
    return 
    

#RELATIVE BANDS POWER FOR GROUP 

def compare_1D_1G_nB_0C_power(data,name_study,name_group,plot=False):
    """
    1 dataset- 1 group - n bands - without distinguishing channels
    """ 
    data=data.drop(["Channels"],axis=1,inplace=False)
    s=np.logical_and(data["Study"]==name_study,data["Group"]==name_group)
    filter=data[s]
    #filter_group=filter_study[filter_study.Subject.str.contains(name_group)]
    bandas=filter["Bands"].unique()
    fig, ax = plt.subplots(1,1)
    fig.set_size_inches(len(bandas)*2,10)
    sns.violinplot(x='Bands',y="Powers",data=filter,palette='winter_r')
    plt.title(name_study +' '+name_group)
    if plot:
        plt.show()
    return fig 

def filter_nD_nG_1B_power(superdata,group_dict,name_band):
    """
    n datasets- n groups - 1 band
    group_dict={
        'BIOMARCADORES':[CTR,DCL],
        'SRM':['SRM'] # assume datasets with no groups have Group=Study
    }
    
    """
    fil=superdata[superdata["Bands"]==name_band]
    list_df=[]

    for dataset,group_list in group_dict.items():
        for group in group_list:
            auxfil = fil[fil['Group']==group]
            list_df.append(auxfil)
    df=pd.concat((list_df))
    return df

def compare_nD_nG_nB_power(data,dict_info):
    '''
    n dataset- n groups - n bands
    '''
    sns.catplot(x='Group',y="Powers",data=data,hue='Study', dodge=True, kind="violin",col='Bands',col_wrap=4,legend=False,palette="winter_r")
    plt.legend(bbox_to_anchor=(1.6, 0.2), loc=4, borderaxespad=0.)
    plt.show()
    return 

#RELATIVE BANDS POWER FOR VISIT

def compare_1D_1V_nB_power(data,name_study,name_session,plot=False):
    '''
    1 dataset- 1 visit - n bands
    '''
    data=data.drop(["Channels"],axis=1,inplace=False)
    b=np.logical_and(data["Study"]==name_study,data["Session"]==name_session)
    filter=data[b]
    bandas=filter["Bands"].unique()

    fig, ax = plt.subplots(1,1)
    fig.set_size_inches(len(bandas)*2,10)
    sns.violinplot(x='Bands',y="Powers",data=filter,palette='winter_r')
    ax.set_title("Bandas de frecuencia en: "+name_study+'-'+name_session)
    if plot:
        plt.show()
    return fig 

def compare_1D_nV_nB_power(data,name_study): #Solo sirve para biomarcadores y SRM 
    '''
    1 dataset- n visits - n bands
    '''
    filter=data["Study"]==name_study
    filter_study=data[filter]
    sns.catplot(x='Session',y="Powers",data=filter_study,dodge=True, kind="violin",col='Bands',col_wrap=4,legend=False,palette="winter_r")
    plt.ylim(-0.1,1.0)
    plt.show()
    return   



#bands=data['Bands'].unique()
#figures=[]
# for num,band in enumerate(bands):
#     fig, ax = plt.subplots()
#     filter_group=filter_1D_1V_1B(data,name_study,band)
#     ax=sns.violinplot(x='Session',y="Powers",data=filter_group,ax=ax)
#     plt.title(band,fontsize=40)
#     plt.xticks(fontsize=40)
#     plt.yticks(fontsize=40)
#     fig.set_size_inches(15, 15) 
#     figures.append(fig)
# createCollage(figures,800,3)    

# **************************** COMPARISON WITHOUT NORMALIZING- NORMALIZING *******************************

def compare_norm_1D_1G_nB_power(data,name_dataset,name_group):
    filter=np.logical_and(data["Study"]==name_dataset, data["Group"]==name_group)
    filter_group_dataset=data[filter]
    sns.catplot(x='Bands',y="Powers",data=filter_group_dataset,dodge=True, kind="box",hue="Normalize",palette='winter_r')
    sns.set(rc={'figure.figsize':(11.7,8.27)})
    plt.ylim(-0.1,1.0)
    plt.show()