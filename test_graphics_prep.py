from Graphics.graphicsViolin import get_dataframe_prep

import matplotlib.pyplot as plt 
import seaborn as sns
import pandas as pd
from datasets import BIOMARCADORES
from datasets import SRM
from Graphics.graphicsViolin import get_dataframe_wica
import numpy as np
import itertools
from pprint import pprint


Studies=[BIOMARCADORES,SRM]
dataPrepOriginal,dataPrepBefore,dataPrepAfter=get_dataframe_prep()
#PREP ESTUDIO 