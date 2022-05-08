from tokenize import group
import matplotlib.pyplot as plt 
import seaborn as sns
import pandas as pd
from Graphics.functionsImages import create_collage,createCollage
import numpy as np
import pandas as pd 

# TOTAL
def compare_nD(data,plot=False):
    """
    todos sujetos -1 estudio- 1 grupo -todas las bandas sin distinguir el canal
    """ 
    data=data.drop(["Channels"],axis=1,inplace=False)
    bandas=data["Bands"].unique()

    fig, ax = plt.subplots(1,1)
    fig.set_size_inches(len(bandas)*2,10)
    sns.violinplot(x='Bands',y="Powers",data=data,palette="bright")
    ax.set_title('Relative band power all data')
    if plot:
        plt.show()
    return fig 

# ESTUDIOS 

def compare_1S_nB_0C_power(data,name_study,plot=False): 
    """
    todos sujetos -1 estudio-todas las bandas sin distinguir el canal
    """ 
    data=data.drop(["Channels"],axis=1,inplace=False)
    s=data["Study"]==name_study
    filter_study=data[s]
    bandas=filter_study["Bands"].unique()
    fig, ax = plt.subplots(1,1)
    fig.set_size_inches(len(bandas)*2,10)
    sns.violinplot(x='Bands',y="Powers",data=filter_study)
    ax.set_title('Bands powers for the '+name_study)
    if plot:
        plt.show()
    return fig 

def compare_1S_1B_nC_power(data,name_study,name_band,plot=False):
    """
    todos sujetos, 1 estudio 1 grupo 1 banda por canal
    
    """
    b=np.logical_and(data["Bands"]==name_band, data["Study"]==name_study)
    filter_band=data[b]
    channels=data["Channels"].unique()
    # f=8
    # c=8
    # fig,axs= plt.subplots(f,c,figsize=(c*3,f*3)) 
    # axs=list(itertools.chain(*axs))
    # print(axs)
    # for i,nombreColumna in enumerate(channels):
    #   sns.violinplot(data=filter_band[filter_band['Channels']==nombreColumna],ax=axs[i]) 
    #   axs[i].set_title(nombreColumna)
    
    fig, ax = plt.subplots(1,1)
    fig.set_size_inches(len(channels)*2,10)
    sns.violinplot(x='Channels',y="Powers",data=filter_band)
    ax.set_title('Bands powers for the '+name_study+'-'+name_band)
    fig.tight_layout()
    if plot:
        plt.show()
    return fig 

def filter_nS_1B_1C_power(data,channel):
    "todos sujetos, n estudios 1 bandas por 1 canal"
    fil_B_C=data["Channels"]==channel
    filter=data[fil_B_C]
    return filter

def compare_nS_nB_power(data,name_channel="None"):
    bandas=data["Bands"].unique()
    rows=1
    cols=7
    #en un canal especifico
    if name_channel != "None":
        fig, ax = plt.subplots()
        filter= filter_nS_1B_1C_power(data,name_channel) 
        ax=sns.violinplot(x='Bands',y="Powers",data=data,hue='Study',palette="bright")
        plt.title('Relative band powers for study'+ ' '+ name_channel,fontsize=15) 
        plt.xticks(fontsize=15)
        plt.yticks(fontsize=15)
        plt.show()
 
    else: 
        #sin distinguir el canal
        
        sns.set_theme(style = "darkgrid")
        sns.violinplot(x='Bands',y="Powers",data=data,hue='Study',palette="bright")
        plt.title('Relative band powers for study',fontsize=15) 
        plt.xticks(fontsize=15)
        plt.yticks(fontsize=15) 
        plt.show() 
    return 
    

#POTENCIAS POR GRUPO 

def compare_1S_1G_nB_0C_power(data,name_study,name_group,plot=False):
    """
    todos sujetos -1 estudio- 1 grupo -todas las bandas sin distinguir el canal
    """ 
    data=data.drop(["Channels"],axis=1,inplace=False)
    s=np.logical_and(data["Study"]==name_study,data["Group"]==name_group)
    filter=data[s]
    #filter_group=filter_study[filter_study.Subject.str.contains(name_group)]
    bandas=filter["Bands"].unique()
    fig, ax = plt.subplots(1,1)
    fig.set_size_inches(len(bandas)*2,10)
    sns.violinplot(x='Bands',y="Powers",data=filter)
    plt.title(name_study +' '+name_group)
    if plot:
        plt.show()
    return fig 

def filter_nS_nG_1B(superdata,group_dict,name_band):
    """
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

def compare_nS_nG_nB(data,dict_info):
    figures=[]
    bands=data['Bands'].unique()
    for j,band in enumerate(bands):
        fig, ax = plt.subplots()
        filter_group=filter_nS_nG_1B(data,dict_info,band)
        ax=sns.catplot(x='Group',y="Powers",data=data,hue='Study', dodge=True, kind="violin",col='Bands'c,col_wrap=2,legend=False,sharex=False,sharey=False,height=5, aspect=0.8)
        ax.get_legend().remove()
        plt.title(band,fontsize=40) 
        plt.xticks(fontsize=40)
        plt.yticks(fontsize=40)   
        fig.set_size_inches(15, 15) 
        figures.append(fig)
    plt.legend(bbox_to_anchor=(1.6, 0.2), loc=4, borderaxespad=0.)
    createCollage(figures,800,3)      
    return 

#POTENCIAS POR VISITA 

def compare_1S_1V_nB(data,name_study,name_session,plot=False):
    data=data.drop(["Channels"],axis=1,inplace=False)
    b=np.logical_and(data["Study"]==name_study,data["Session"]==name_session)
    filter=data[b]
    bandas=filter["Bands"].unique()

    fig, ax = plt.subplots(1,1)
    fig.set_size_inches(len(bandas)*2,10)
    sns.violinplot(x='Bands',y="Powers",data=filter)
    ax.set_title("Bandas de frecuencia en: "+name_study+'-'+name_session)
    if plot:
        plt.show()
    return fig 

def filter_1S_1V_1B(data,name_study,name_band):
    b=np.logical_and(data["Bands"]==name_band, data["Study"]==name_study)
    filter=data[b]
    return filter

def compare_1S_nV_nB(data,name_study): #Solo sirve para biomarcadores y SRM 
    bands=data['Bands'].unique()
    figures=[]
    for num,band in enumerate(bands):
        fig, ax = plt.subplots()
        filter_group=filter_1S_1V_1B(data,name_study,band)
        ax=sns.violinplot(x='Session',y="Powers",data=filter_group,ax=ax)
        plt.title(band,fontsize=40)
        plt.xticks(fontsize=40)
        plt.yticks(fontsize=40)
        fig.set_size_inches(15, 15) 
        figures.append(fig)
    createCollage(figures,800,3)    
    return   

