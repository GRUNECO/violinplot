import os
import glob
import pandas as pd 

def load_feather(path):
    '''
    Function to upload files with feather format

    Parameters
    ----------
        path:str
            Directory where the file with the extension .feather

    Returns 
    -------
        data: dataframe
            Data in dataframe format
    '''
    data=pd.read_feather(os.path.join(path).replace("\\","/"))
    return data

def concat_df(path):
    path_df=glob.glob(path)
    print(path_df)
    data=[]
    for df in path_df:
        data.append(load_feather(df))
    print(data)
    data_concat=pd.concat((data))
    return data_concat