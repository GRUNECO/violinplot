import re
import pandas as pd 
from bids import BIDSLayout
from bids.layout import parse_file_entities
from pydantic import NoneBytes
from Graphics.createDataframes import PowersChannels,rejectGraphic,indicesWica,indicesPrep,PowersComponents
import pandas as pd

def get_information_data(THE_DATASET):
  '''
  Function to extract information about data
  
  Parameters:
  --------------
    THE_DATASET: dictionary with the following keys:
    {
    'name': str, Name of the dataset
    'input_path': str, Path of the bids input dataset,
    'layout': dict, Arguments of the filter to apply for querying eegs to be processed. See pybids BIDSLayout arguments.
    'args': dict, Arguments of the sovaflow.preflow function in dictionary form.
    'group_regex': str, regex string to obtain the group from the subject id (if applicable) else None
    'events_to_keep': list, list of events to keep for the analysis
    'run-label': str, label associated with the run of the algorithm so that the derivatives are not overwritten.
    'channels': list, channel labels to keep for analysis in the order wanted. Use standard 1005 names in UPPER CASE
    'spatial_filter': str, spatial filter to be used for component analysis. Should correspond to those in sovaflow. One of '53x53', '58x25', '62x19'
    }
     
  Returns:
  -------------- 
    layout:
    task: string
      Type of any cognitive task 
    runlabel: string
      Name of  any cognitive task in format BIDS
    name: string
      Name of dataset 
    group_regex: string
      Properties can be inferred from the path of the source files for format BIDS. Refers to groups from the data.
    session_set: string 
      Properties can be inferred from the path of the source files for format BIDS. Refers to sessions from the data.

  '''
  input_path = THE_DATASET.get('input_path',None)
  task = THE_DATASET.get('layout',None).get('task',None)
  group_regex = THE_DATASET.get('group_regex',None)
  name = THE_DATASET.get('name',None)
  runlabel = THE_DATASET.get('run-label','')
  session_set = THE_DATASET.get('session',None)
  data_path = input_path
  layout = BIDSLayout(data_path,derivatives=True)
  return layout,task,runlabel,name,group_regex,session_set
   
def get_dataframe_powers(Studies,mode="channels",stage=None,save=False):
  """
  Function to read and store the data in the form of a dataframe for powers 

  Parameters:
  ---------------
    Studies: dict
    mode: string
      Type relative powers in channels o components
    stage: string
      Type of processing stage, with or without normalization data
    save: Boolean
      Optional for save the dataframe in format 'xlsx'

  Returns:
  -------------- 
    dataPowers: dataframe


  """
  dataframesPowers=[]
  for THE_DATASET in Studies:
    layout,task,runlabel,name,group_regex,session_set=get_information_data(THE_DATASET)
    Stage=stage
    if Stage == 'norm' and mode== "channels":
        # Data with stage of normalized for channels
        eegs_powers= layout.get(extension='.txt', task=task,suffix='norm', return_type='filename')
        eegs_powers = [x for x in eegs_powers if f'desc-channel[{runlabel}]' in x]

    elif Stage== None and mode== "channels":
      # Data without stage of normalized for channels
      eegs_powers= layout.get(extension='.txt', task=task,suffix='powers', return_type='filename')
      eegs_powers = [x for x in eegs_powers if f'desc-channel[{runlabel}]' in x]

    elif Stage == 'norm' and mode == "components":
        # Data with stage of normalized for components 
        eegs_powers= layout.get(extension='.txt', task=task,suffix='norm', return_type='filename')
        eegs_powers = [x for x in eegs_powers if f'desc-component[{runlabel}]' in x]

    else: 
      #Stage== None and mode == "components ":
      # Data without stage of normalized for components 
      eegs_powers= layout.get(extension='.txt', task=task,suffix='powers', return_type='filename')
      eegs_powers = [x for x in eegs_powers if f'desc-component[{runlabel}]' in x]
    
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

    list_stage=["Normalized data"]*len(list_info)
    if  Stage == 'norm':
        if mode=='channels':
          dataframesPowers.append(PowersChannels(eegs_powers,list_studies=list_studies,list_subjects=list_subjects,list_groups=list_groups,list_sessions=list_sessions,list_stage=list_stage))
        else: 
          dataframesPowers.append(PowersComponents(eegs_powers,list_studies=list_studies,list_subjects=list_subjects,list_groups=list_groups,list_sessions=list_sessions,list_stage=list_stage))
    else:
      if mode=='channels':
        dataframesPowers.append(PowersChannels(eegs_powers,list_studies=list_studies,list_subjects=list_subjects,list_groups=list_groups,list_sessions=list_sessions,list_stage=None))
      else:
        dataframesPowers.append(PowersComponents(eegs_powers,list_studies=list_studies,list_subjects=list_subjects,list_groups=list_groups,list_sessions=list_sessions,list_stage=None))       
  dataPowers=pd.concat((dataframesPowers))
  if save== True:
    if  mode== 'channels' and stage ==None:
      dataPowers.to_excel(r'Dataframes\longitudinal_data_powers_long_{mode}.xlsx'.format(mode=mode))
    if mode == 'components' and stage== None:
      dataPowers.to_excel(r'Dataframes\longitudinal_data_powers_long_{mode}.xlsx'.format(mode=mode))
    if mode == 'channels' and stage== 'norm':
      dataPowers.to_excel(r'Dataframes\longitudinal_data_powers_long_{mode}_{stage}.xlsx'.format(mode=mode,stage=stage))
    if mode == 'components' and stage== 'norm':
      dataPowers.to_excel(r'Dataframes\longitudinal_data_powers_long_{mode}_{stage}.xlsx'.format(mode=mode,stage=stage))  
  return dataPowers

def get_dataframe_reject(Studies,save=False):
  '''
  Function to read and store the data in the form of a dataframe for stage the rejects of processing 

  Parameters:
  ---------------
    Studies: dict
    save: Boolean
      Optional for save the dataframe in format 'xlsx'

  Returns:
  -------------- 
    dataReject: dataframe

  '''
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
  if save== True:
        dataReject.to_excel(r'Dataframes\data_reject.xlsx')
  return dataReject       

def get_dataframe_wica(Studies,save=False):
  '''
  Function to read and store the data in the form of a dataframe for stage the wICA of processing
  
  Parameters:
  ---------------
    Studies: dict
    save: Boolean
      Optional for save the dataframe in format 'xlsx'

  Returns:
  -------------- 
    dataWica: dataframe
  '''
  dataframesWica=[]
  for THE_DATASET in Studies:
    layout,task,runlabel,name,group_regex,session_set=get_information_data(THE_DATASET)
    stats_wica = layout.get(extension='.txt', task=task,suffix='stats', return_type='filename')
    stats_wica = [x for x in stats_wica if f'desc-wica' in x]
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
  if save== True:
    dataWica.to_excel(r'Dataframes\data_wICA.xlsx')
  return dataWica 

def get_dataframe_prep(Studies,save=False):
  '''
  Function to read and store the data in the form of a dataframe for stage the PREP of processing
  
  Parameters:
  ---------------
    Studies: dict
    save: Boolean
      Optional for save the dataframe in format 'xlsx'

  Returns:
  -------------- 
    data_Prep: dataframe
  '''
  dataframes=[]
  for THE_DATASET in Studies:
    layout,task,runlabel,name,group_regex,session_set=get_information_data(THE_DATASET)
    stats_prep = layout.get(extension='.txt', task=task,suffix='stats', return_type='filename')
    stats_prep = [x for x in stats_prep if f'desc-prep' in x]
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
    data_Prep=indicesPrep(stats_prep,list_studies=list_studies,list_subjects=list_subjects,list_groups=list_groups,list_sessions=list_sessions)
    dataframes.append(data_Prep)

  data_Prep=pd.concat(dataframes)
  if save== True:
    data_Prep.to_excel(r'Dataframes\data_PREP.xlsx')
  return data_Prep 

