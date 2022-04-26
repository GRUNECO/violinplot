from requests import session
import seaborn as sns
import json
import numpy as np
from pandas.core.frame import DataFrame
import glob
import pandas as pd 
import itertools
import os

def load_txt(file):
  '''
  Function that reads txt files

  Parameters
  ----------
  file:

  Returns
  -------

  '''
  with open(file, 'r') as f:
    data=json.load(f)
  return data

def indicesPrep(files,list_studies=None,list_subjects=None,list_groups=None,list_sessions=None):
  
  if list_studies is None:
    list_studies=["None"]*len(files)
  if list_subjects is None:
    list_subjects=["None"]*len(files) 
  if list_groups is None:
    list_groups=["None"]*len(files)
  if list_sessions is None:
    list_sessions=["None"]*len(files)
  
  list_noisy_channels_original=[]
  list_noisy_channels_before_interpolation=[]
  list_noisy_channels_after_interpolation=[]
  for file in files:
    dataFile=load_txt(file)
    noisy_channels_original=dataFile['noisy_channels_original']
    list_noisy_channels_original.append(pd.DataFrame({key:[len(val)] for key,val in noisy_channels_original.items()}))
    noisy_channels_before_interpolation=dataFile['noisy_channels_before_interpolation']
    list_noisy_channels_before_interpolation.append(pd.DataFrame({key:[len(val)] for key,val in noisy_channels_before_interpolation.items()}))
    noisy_channels_after_interpolation= dataFile['noisy_channels_after_interpolation']
    list_noisy_channels_after_interpolation.append(pd.DataFrame({key:[len(val)] for key,val in noisy_channels_after_interpolation.items()}))
  
  df_noisy_channels_original=pd.concat((list_noisy_channels_original))
  df_noisy_channels_before_interpolation=pd.concat((list_noisy_channels_before_interpolation))
  df_noisy_channels_after_interpolation=pd.concat((list_noisy_channels_after_interpolation))

  df_noisy_channels_original=df_noisy_channels_original.assign(Study=list_studies,Subject=list_subjects,Group=list_groups,Session=list_sessions)
  df_noisy_channels_before_interpolation=df_noisy_channels_before_interpolation.assign(Study=list_studies,Subject=list_subjects,Group=list_groups,Session=list_sessions)
  df_noisy_channels_after_interpolation=df_noisy_channels_after_interpolation.assign(Study=list_studies,Subject=list_subjects,Group=list_groups,Session=list_sessions)

  return df_noisy_channels_original,df_noisy_channels_before_interpolation,df_noisy_channels_after_interpolation

def indicesWica(files,list_studies=None,list_subjects=None,list_groups=None,list_sessions=None):
  '''
  canales,epocas
  Parameters
  ----------

  Returns
  -------
  '''
  if list_studies is None:
    list_studies=["None"]*len(files)
  if list_subjects is None:
    list_subjects=["None"]*len(files) 
  if list_groups is None:
    list_groups=["None"]*len(files)
  if list_sessions is None:
    list_sessions=["None"]*len(files)   

  sums=[]
  for file in files:
    print(file)
    dataFile=load_txt(file)
    mat=np.array(dataFile)
    sum=np.sum(mat.flatten())
    sums.append(sum/mat.size)

  dfstats_wica=pd.DataFrame({'Study':list_studies,'Subject':list_subjects,'Group':list_groups,'Session':list_sessions,'Components':sums})
  return dfstats_wica

def channelsPowers(data,name_study="None",subject="None",group="None",session="None"):
  '''
  Function to return the power bands

  Parameters
  ----------
  data:

  Returns
  -------
  '''

  df_powers={}
  df_powers['Powers']=[]
  df_powers['Bands']=[]
  df_powers['Channels']=[]
  df_powers['Study']=[]
  df_powers['Session']=[]
  df_powers['Subject']=[]
  df_powers['Group']=[]

  for i,key in enumerate(data['bands']):
    df_powers['Study']+=[name_study]*len(data['channels'])
    df_powers['Subject']+=[subject]*len(data['channels'])
    df_powers['Group']+=[group]*len(data['channels'])
    df_powers['Session']+=[session]*len(data['channels'])
    df_powers['Powers']+=data['channel_power'][i]
    df_powers['Bands']+=[key]*len(data['channels'])
    df_powers['Channels']+=data['channels']
  powers=pd.DataFrame(df_powers)
  return powers 

def PowersGraphic(powersFiles,list_studies=None,list_subjects=None,list_groups=None,list_sessions=None):
  dataframesPowers=[]
  if list_studies is None:
    list_studies=["None"]*len(powersFiles)
  if list_subjects is None:
    list_subjects=["None"]*len(powersFiles) 
  if list_groups is None:
    list_groups=["None"]*len(powersFiles)
  if list_sessions is None:
    list_sessions=["None"]*len(powersFiles)  
  for power,name_study,subject,group,session in zip(powersFiles,list_studies,list_subjects,list_groups,list_sessions):
    dataFile=load_txt(power)
    statsPowers=channelsPowers(dataFile,name_study,subject,group,session)
    dataframesPowers.append(statsPowers)
  datosPowers=pd.concat((dataframesPowers))
  return datosPowers 

def reject_thresholds(data,name_study="None",subject="None",group="None",session="None"):
  '''
  Function to extract the initial and the final thresholds from the reject metric

  Parameters
  ----------
  data:

  Returns
  -------

  '''
  df= pd.DataFrame({
  'Study':[name_study]*len(data['final_thresholds']['spectrum'][1]),
  'Subject':[subject]*len(data['final_thresholds']['spectrum'][1]),
  'Group':[group]*len(data['final_thresholds']['spectrum'][1]),
  'Session':[session]*len(data['final_thresholds']['spectrum'][1]),
  'i_kurtosis_min':data['initial_thresholds']['kurtosis'][0],
  'i_kurtosis_max':data['initial_thresholds']['kurtosis'][1],
  'i_amplitude_min': data['initial_thresholds']['amplitude'][0],
  'i_amplitude_max':data['initial_thresholds']['amplitude'][1],
  'i_trend':data['initial_thresholds']['trend'][0],
  'f_kurtosis_min':data['final_thresholds']['kurtosis'][0],
  'f_kurtosis_max':data['final_thresholds']['kurtosis'][1],
  'f_amplitude_min': data['final_thresholds']['amplitude'][0],
  'f_amplitude_max':data['final_thresholds']['amplitude'][1],
  'f_trend':data['final_thresholds']['trend'][0],
  'f_spectrum_min':data['final_thresholds']['spectrum'][0],
  'f_spectrum_max':data['final_thresholds']['spectrum'][1]
  
  })
  return df

def rejectGraphic(files,list_studies=None,list_subjects=None,list_groups=None,list_sessions=None):
  if list_studies is None:
    list_studies=["None"]*len(files)
  if list_subjects is None:
    list_subjects=["None"]*len(files) 
  if list_groups is None:
    list_groups=["None"]*len(files)
  if list_sessions is None:
    list_sessions=["None"]*len(files)  
  dataframesReject=[]
  for file,name_study,subject,group,session in zip(files,list_studies,list_subjects,list_groups,list_sessions):
    dataFile=load_txt(file)
    statsReject=reject_thresholds(dataFile,name_study,subject,group,session)
    dataframesReject.append(statsReject)
  dataReject=pd.concat((dataframesReject))
  return dataReject

def final_rejection_percentages(listIn,data,keyInput):
  '''
  Function to extract percentages
  Parameters
  ----------
  listIn:
  data:
  keyInput:

  Returns
  -------
  '''
  dataframes={}
  print("-------------------------")
 
  for i,key in enumerate(data['rejection']['criteria']):
    dataframes[key]=data['rejection'][keyInput][i]
  listIn.append(dataframes)
  return listIn 

# FILTROS
def filter_nS_nG_1M(superdata,group_dict):
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
