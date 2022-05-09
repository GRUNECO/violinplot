import re
import pandas as pd 
from bids import BIDSLayout
from bids.layout import parse_file_entities
from pydantic import NoneBytes
from Graphics.graphicsViolin import PowersGraphic,rejectGraphic,indicesWica,indicesPrep
import pandas as pd 

def get_information_data(THE_DATASET):
  input_path = THE_DATASET.get('input_path',None)
  task = THE_DATASET.get('layout',None).get('task',None)
  group_regex = THE_DATASET.get('group_regex',None)
  name = THE_DATASET.get('name',None)
  runlabel = THE_DATASET.get('run-label','')
  session_set = THE_DATASET.get('session',None)
  data_path = input_path
  layout = BIDSLayout(data_path,derivatives=True)
  layout.get(scope='derivatives', return_type='file')
  return layout,task,runlabel,name,group_regex,session_set
   
def get_dataframe_powers(Studies,mode=None):
  dataframesPowers=[]
  for THE_DATASET in Studies:
    layout,task,runlabel,name,group_regex,session_set=get_information_data(THE_DATASET)
    Mode=mode
    if Mode == 'norm':
        eegs_powers= layout.get(extension='.txt', task=task,suffix='norm', return_type='filename')
        eegs_powers = [x for x in eegs_powers if f'desc-channel[{runlabel}]' in x]
    else:
      eegs_powers= layout.get(extension='.txt', task=task,suffix='powers', return_type='filename')
      eegs_powers = [x for x in eegs_powers if f'desc-channel[{runlabel}]' in x]
    
    list_studies=[name]*len(eegs_powers)
    list_info=[parse_file_entities(eegs_powers[i]) for i in range(len(eegs_powers))]
    list_subjects=[info['subject'] for info in list_info]
    # Grupos
    if group_regex:
      list_groups=[re.search('(.+).{3}',group).string[re.search('(.+).{3}',group).regs[-1][0]:re.search('(.+).{3}',group).regs[-1][1]] for group in list_subjects]
    else:
      list_groups=list_studies
    # Visita 
    if session_set == None:
      list_sessions=list_studies
    else:
      list_sessions=[info['session'] for info in list_info]
      
    list_norm=[1]*len(list_info)
    if  Mode == 'norm':
      dataframesPowers.append(PowersGraphic(eegs_powers,list_studies=list_studies,list_subjects=list_subjects,list_groups=list_groups,list_sessions=list_sessions,list_norm=list_norm))
    else:
      dataframesPowers.append(PowersGraphic(eegs_powers,list_studies=list_studies,list_subjects=list_subjects,list_groups=list_groups,list_sessions=list_sessions,list_norm=None))
            
  dataPowers=pd.concat((dataframesPowers)) 
  return dataPowers


def get_dataframe_reject(Studies):
  dataframesReject=[]
  for THE_DATASET in Studies:
    layout,task,runlabel,name,group_regex,session_set=get_information_data(THE_DATASET)
    stats_reject = layout.get(extension='.txt', task=task,suffix='stats', return_type='filename')
    stats_reject = [x for x in stats_reject if f'desc-reject[{runlabel}]' in x]        #rej_stats_studies+=stats_reject
    list_studies=[name]*len(stats_reject)
    list_info=[parse_file_entities(stats_reject[i]) for i in range(len(stats_reject))]
    list_subjects=[info['subject'] for info in list_info]
    if group_regex:
      list_groups=[re.search('(.+).{3}',group).string[re.search('(.+).{3}',group).regs[-1][0]:re.search('(.+).{3}',group).regs[-1][1]] for group in list_subjects]
    else:
      list_groups=list_studies
    if session_set == None:
      list_sessions=list_studies
    else:
      list_sessions=[info['session'] for info in list_info]
      
    dataframesReject.append(rejectGraphic(stats_reject,list_studies=list_studies,list_subjects=list_subjects,list_groups=list_groups,list_sessions=list_sessions))
        
  dataReject=pd.concat((dataframesReject))
  return dataReject       

def get_dataframe_wica(Studies):
  dataframesWica=[]
  for THE_DATASET in Studies:
    layout,task,runlabel,name,group_regex,session_set=get_information_data(THE_DATASET)
    stats_wica = layout.get(extension='.txt', task=task,suffix='stats', return_type='filename')
    stats_wica = [x for x in stats_wica if f'desc-wica' in x]
    #wica_stats_studies+=stats_wica
    list_studies=[name]*len(stats_wica)
    list_info=[parse_file_entities(stats_wica[i]) for i in range(len(stats_wica))]
    list_subjects=[info['subject'] for info in list_info]
    if group_regex:
      list_groups=[re.search('(.+).{3}',group).string[re.search('(.+).{3}',group).regs[-1][0]:re.search('(.+).{3}',group).regs[-1][1]] for group in list_subjects]
    else:
      list_groups=list_studies
    if session_set == None:
      list_sessions=list_studies
    else:
      list_sessions=[info['session'] for info in list_info]
      
    dataframesWica.append(indicesWica(stats_wica,list_studies=list_studies,list_subjects=list_subjects,list_groups=list_groups,list_sessions=list_sessions))
        
  dataWica=pd.concat((dataframesWica))
  return dataWica 

def get_dataframe_prep(Studies):
  dataframesPrepOriginal=[]
  dataframesPrepBefore=[]
  dataframesPrepAfter=[]
  for THE_DATASET in Studies:
    layout,task,runlabel,name,group_regex,session_set=get_information_data(THE_DATASET)
    stats_prep = layout.get(extension='.txt', task=task,suffix='stats', return_type='filename')
    stats_prep = [x for x in stats_prep if f'desc-prep' in x]
    #prep_stats_studies+=stats_prep
    list_studies=[name]*len(stats_prep)
    list_info=[parse_file_entities(stats_prep[i]) for i in range(len(stats_prep))]
    list_subjects=[info['subject'] for info in list_info]
    if group_regex:
      list_groups=[re.search('(.+).{3}',group).string[re.search('(.+).{3}',group).regs[-1][0]:re.search('(.+).{3}',group).regs[-1][1]] for group in list_subjects]
    else:
      list_groups=list_studies
    if session_set == None:
      list_sessions=list_studies
    else:
      list_sessions=[info['session'] for info in list_info]
    list_Prep=indicesPrep(stats_prep,list_studies=list_studies,list_subjects=list_subjects,list_groups=list_groups,list_sessions=list_sessions)
    dataframesPrepOriginal.append(list_Prep[0])
    dataframesPrepBefore.append(list_Prep[1])
    dataframesPrepAfter.append(list_Prep[2])
  dataPrepOriginal=pd.concat((dataframesPrepOriginal))
  dataPrepBefore=pd.concat((dataframesPrepBefore))
  dataPrepAfter=pd.concat((dataframesPrepAfter))
  return dataPrepOriginal,dataPrepBefore,dataPrepAfter

