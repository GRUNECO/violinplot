import seaborn as sns
import json
from matplotlib import pyplot as plt
import numpy as np
from pandas.core.frame import DataFrame
import glob
import pandas as pd 
import itertools
import os
from PIL import Image
from bids import BIDSLayout
from bids.layout import parse_file_entities
import re

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

def create_collage(cols,rows,width, height, listofimages,channel="None"):
  thumbnail_width = width//cols
  thumbnail_height = height//rows
  size = thumbnail_width, thumbnail_height
  new_im = Image.new('RGB', (width, height), 'white')
  ims = []
  for p in listofimages:
      im = Image.open(p)
      im.thumbnail(size)
      ims.append(im)
  i = 0
  x = 0
  y = 0
  for col in range(cols):
      for row in range(rows):
          if i>= len(ims):
            pass
          else:
            new_im.paste(ims[i], (x, y))
            i += 1
            x += thumbnail_width
      y += thumbnail_height 
      x = 0
  if channel != "None":
    new_im.save("Images/Collage"+'_'+channel+'.jpg')
  else:
    new_im.save("Images/Collage.jpg")
  return 

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

def get_information_data(THE_DATASET):
  input_path = THE_DATASET.get('input_path',None)
  task = THE_DATASET.get('layout',None).get('task',None)
  group_regex = THE_DATASET.get('group_regex',None)
  name = THE_DATASET.get('name',None)
  runlabel = THE_DATASET.get('run-label','')
  data_path = input_path
  layout = BIDSLayout(data_path,derivatives=True)
  layout.get(scope='derivatives', return_type='file')
  return layout,task,runlabel,name,group_regex
   
def get_dataframe_powers(Studies):
  dataframesPowers=[]
  for THE_DATASET in Studies:
    layout,task,runlabel,name,group_regex=get_information_data(THE_DATASET)
    eegs_powers= layout.get(extension='.txt', task=task,suffix='powers', return_type='filename')
    eegs_powers = [x for x in eegs_powers if f'desc-channel[{runlabel}]' in x]
    #cpowers_studies+=eegs_powers
    list_studies=[name]*len(eegs_powers)
    list_info=[parse_file_entities(eegs_powers[i]) for i in range(len(eegs_powers))]
    list_subjects=[info['subject'] for info in list_info]
    if group_regex:
      list_groups=[re.search('(.+).{3}',group).string[re.search('(.+).{3}',group).regs[-1][0]:re.search('(.+).{3}',group).regs[-1][1]] for group in list_subjects]
    else:
      list_groups=list_subjects
    list_sessions=[info['session'] for info in list_info]
    dataframesPowers.append(PowersGraphic(eegs_powers,list_studies=list_studies,list_subjects=list_subjects,list_groups=list_groups,list_sessions=list_sessions))
            
  dataPowers=pd.concat((dataframesPowers)) 
  return dataPowers

def get_dataframe_reject(Studies):
  dataframesReject=[]
  for THE_DATASET in Studies:
    layout,task,runlabel,name,group_regex=get_information_data(THE_DATASET)
    stats_reject = layout.get(extension='.txt', task=task,suffix='stats', return_type='filename')
    stats_reject = [x for x in stats_reject if f'desc-reject[{runlabel}]' in x]        #rej_stats_studies+=stats_reject
    list_studies=[name]*len(stats_reject)
    list_info=[parse_file_entities(stats_reject[i]) for i in range(len(stats_reject))]
    list_subjects=[info['subject'] for info in list_info]
    if group_regex:
      list_groups=[re.search('(.+).{3}',group).string[re.search('(.+).{3}',group).regs[-1][0]:re.search('(.+).{3}',group).regs[-1][1]] for group in list_subjects]
    else:
      list_groups=list_subjects
    list_sessions=[info['session'] for info in list_info]
    dataframesReject.append(rejectGraphic(stats_reject,list_studies=list_studies,list_subjects=list_subjects,list_groups=list_groups,list_sessions=list_sessions))
        
  dataReject=pd.concat((dataframesReject))
  return dataReject       

def get_dataframe_wica(Studies):
  dataframesWica=[]
  for THE_DATASET in Studies:
    layout,task,runlabel,name,group_regex=get_information_data(THE_DATASET)
    stats_wica = layout.get(extension='.txt', task=task,suffix='stats', return_type='filename')
    stats_wica = [x for x in stats_wica if f'desc-wica' in x]
    #wica_stats_studies+=stats_wica
    list_studies=[name]*len(stats_wica)
    list_info=[parse_file_entities(stats_wica[i]) for i in range(len(stats_wica))]
    list_subjects=[info['subject'] for info in list_info]
    if group_regex:
      list_groups=[re.search('(.+).{3}',group).string[re.search('(.+).{3}',group).regs[-1][0]:re.search('(.+).{3}',group).regs[-1][1]] for group in list_subjects]
    else:
      list_groups=list_subjects
    list_sessions=[info['session'] for info in list_info]
    dataframesWica.append(indicesWica(stats_wica,list_studies=list_studies,list_subjects=list_subjects,list_groups=list_groups,list_sessions=list_sessions))
        
  dataWica=pd.concat((dataframesWica))
  return dataWica 

def get_dataframe_prep(Studies):
  dataframesPrepOriginal=[]
  dataframesPrepBefore=[]
  dataframesPrepAfter=[]
  for THE_DATASET in Studies:
    layout,task,runlabel,name,group_regex=get_information_data(THE_DATASET)
    stats_prep = layout.get(extension='.txt', task=task,suffix='stats', return_type='filename')
    stats_prep = [x for x in stats_prep if f'desc-prep' in x]
    #prep_stats_studies+=stats_prep
    list_studies=[name]*len(stats_prep)
    list_info=[parse_file_entities(stats_prep[i]) for i in range(len(stats_prep))]
    list_subjects=[info['subject'] for info in list_info]
    if group_regex:
      list_groups=[re.search('(.+).{3}',group).string[re.search('(.+).{3}',group).regs[-1][0]:re.search('(.+).{3}',group).regs[-1][1]] for group in list_subjects]
    else:
      list_groups=list_subjects
    list_sessions=[info['session'] for info in list_info]
    list_Prep=indicesPrep(stats_prep,list_studies=list_studies,list_subjects=list_subjects,list_groups=list_groups,list_sessions=list_sessions)
    dataframesPrepOriginal.append(list_Prep[0])
    dataframesPrepBefore.append(list_Prep[1])
    dataframesPrepAfter.append(list_Prep[2])
  dataPrepOriginal=pd.concat((dataframesPrepOriginal))
  dataPrepBefore=pd.concat((dataframesPrepBefore))
  dataPrepAfter=pd.concat((dataframesPrepAfter))
  return dataPrepOriginal,dataPrepBefore,dataPrepAfter