from tokenize import group
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt 
import seaborn as sns
import pandas as pd
from .functionsImages import create_collage,createCollage,fig2img_encode
import numpy as np
import pandas as pd 

# **************************** COMPARISON BETWEEN NORMALIZE DATA AND PROCESSING DATA *******************************
# GLOBAL
def compare_all_nD_ch_power(data,plot=False,encode=False):
    '''
    '''
    axs=sns.catplot(x='Bands',y="Powers",data=data,hue="Stage",dodge=True, kind="box",palette='winter_r',legend=False)
    plt.title("")
    plt.yticks(np.arange(0,1,0.1))
    axs.set(xlabel=None)
    axs.set(ylabel=None)
    axs.fig.suptitle('Relative power bands of normalized and preprocessed data given in channels')
    axs.add_legend(loc='upper center',bbox_to_anchor=(.5,.95),ncol=2)
    axs.fig.subplots_adjust(top=0.857,bottom=0.155, right=0.986,left=0.05, hspace=0.138, wspace=0.062) # adjust the Figure in rp
    axs.fig.text(0.5, 0.04, 'Frequency bands', ha='center', va='center')
    axs.fig.text(0.003, 0.5,  'Relative powers', ha='center', va='center',rotation='vertical')
    if plot:
        plt.show()
    if encode:
        img_encode=fig2img_encode(axs)
        plt.cla()
        plt.close()
        return img_encode
    return 
#ESTUDIOS
def compare_nD_ch_power(data,plot=False,encode=False):
    axs=sns.catplot(x='Study',y="Powers",data=data,hue="Stage",dodge=True, kind="box",col='Bands',col_wrap=3,palette='winter_r',fliersize=1.5,linewidth=0.5,legend=False)
    
    if plot:
        plt.show()
    if encode:
        img_encode=fig2img_encode(axs)
        plt.cla()
        plt.close()
        return img_encode


#GROUPS
def compare_norm_1D_1G_nB_ch_power(data,name_dataset,save=False,plot=False,encode=False):
    data['Session']=data['Session'].replace({'VO':'V0'})
    data['Group']=data['Group'].replace({'G2':'CTR'})

    filter=data["Study"]==name_dataset
    filter_group_dataset=data[filter]
    sns.set(rc={'figure.figsize':(11.7,8.27)})
    sns.set_theme(style="white")
    axs=sns.catplot(x='Bands',y="Powers",data=filter_group_dataset,hue="Stage",palette='winter_r',kind="box",col='Group',col_wrap=2,legend=False)
    plt.yticks(np.arange(0,1,0.1))
    axs.fig.suptitle("Relative power bands of normalized and preprocessed data given")
    axs.set(xlabel=None)
    axs.set(ylabel=None)
    axs.add_legend(loc='upper center',bbox_to_anchor=(.5,.95),ncol=2)
    axs.fig.subplots_adjust(top=0.857,bottom=0.121, right=0.986,left=0.05, hspace=0.138, wspace=0.062)
    plt.yticks(np.arange(0,1,0.1))
    
    if save==True:
        plt.savefig('Resultados\Graphics_channels\Groups\{name_dataset}_channels.png'.format(name_dataset=name_dataset))
        plt.close()
    if plot: 
        plt.show()
    if encode:
        img_encode=fig2img_encode(axs)
        plt.cla()
        plt.close()
        return img_encode
    return 

#SESSIONS
def compare_norm_1D_1G_nB_nV_ch_power(data,name_dataset,name_group,num_columns=4,save=False,plot=False,encode=False):
    '''
    Compare normalized and preprocessed data for 1 dataset- 1 group- n bands- n visits
    
    Parameters
    ----------
        data:dataset 
        name_dataset: str
        name_group: str
        save: boolean

    Returns
    -------
    '''
    data['Session']=data['Session'].replace({'VO':'V0'})
    data['Group']=data['Group'].replace({'G2':'CTR'})
    filter=np.logical_and(data["Study"]==name_dataset, data["Group"]==name_group)
    filter_group_dataset=data[filter]
    sns.set(rc={'figure.figsize':(11.7,8.27)})
    sns.set_theme(style="white")
    axs=sns.catplot(x='Session',y="Powers",data=filter_group_dataset,hue="Stage",dodge=True, kind="box",col='Bands',col_wrap=num_columns,palette='winter_r',legend=False)
    plt.yticks(np.arange(0,1,0.1))
    axs.fig.suptitle('Relative power bands of normalized and preprocessed data given by '+name_group+" and all visits")
    axs.set(xlabel=None)
    axs.set(ylabel=None)
    axs.add_legend(loc='upper center',bbox_to_anchor=(.5,.95),ncol=2)
    axs.fig.subplots_adjust(top=0.857,bottom=0.121, right=0.986,left=0.05, hspace=0.138, wspace=0.062) # adjust the Figure in rp
    axs.fig.text(0.5, 0.04, 'Sessions', ha='center', va='center')
    axs.fig.text(0.01, 0.5,  'Relative powers', ha='center', va='center',rotation='vertical')
    
    if save:
         plt.savefig('Resultados\Graphics_channels\Visits\{name_dataset}_{name_group}_visits_channels.png'.format(name_dataset=name_dataset,name_group=name_group))
    if plot: 
        plt.show()
    if encode:
        img_encode=fig2img_encode(axs)
        plt.cla()
        plt.close()
        return img_encode
    return 




# **************************** PROCESSING DATA WHITOUT NORMALIZING *********************************************
# TOTAL
def compare_nD_power(data,plot=False):
    """
    data: all dataset in format dataframe
    plot: Boolean  

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



