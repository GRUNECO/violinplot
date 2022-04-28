from tokenize import group
import matplotlib.pyplot as plt 
import seaborn as sns
import pandas as pd
#from datasets import CHBMP,BIOMARCADORES,SRM # LEMON
from Graphics.FunctionsGraphics import create_collage,createCollage
from Graphics.GetDataframes import get_dataframe_powers
import numpy as np
import pandas as pd 
import itertools
from pprint import pprint
from IPython.display import HTML, display_html, display
import dataframe_image as dfi

from matplotlib.gridspec import GridSpec

datos=pd.read_csv('datospotencias.csv',sep=",")
datos['Group']=datos['Group'].replace({'CHBMP':'CTR','SRM':'CTR'})
datos['Session']=datos['Session'].replace({'VO':'V0','V4P':'V4'})
datos.to_csv('Datos_potencias.csv', index=False)

#sns.boxplot(x='Bands',y="Powers",data=filter_study)
#sns.boxplot(x='Bands',y="Powers",data=filter_study,whis=np.inf)

# #Grafico de violin todas las bandas de potencia por cada base de datos
# plt.figure(figsize = (30, 10)) 
# sns.set_theme(style = "darkgrid")
# sns.violinplot(x='Bands',y="Powers",data=datos, hue='Study',palette="bright")
# plt.title("Band Powers DataBases")
# plt.show()

# #Grafico de dispersión todas las bandas de potencia por cada base de datos

# plt.figure(figsize = (30, 10)) 
# sns.set_theme(style = "darkgrid")
# sns.stripplot(x='Bands',y="Powers",data=datos,hue='Study',dodge=True,palette="bright",edgecolor='gray',linewidth=1)
# plt.title("Band Powers DataBases")
# plt.show()

# #Grafico de violin todas las bandas de potencia por cada base de datos y por grupo
# plt.figure(figsize = (28, 20)) 
# sns.set_theme(style = "darkgrid")
# sns.catplot(x='Group',y="Powers",data=datos,hue='Study', dodge=True, kind="violin",col='Bands',palette="bright",col_wrap=2,legend=False)
# plt.legend(bbox_to_anchor=(1.6, 0.2), loc=4, borderaxespad=0.)
# plt.show()

#Grafico de violin todas las bandas de potencia por grupo sin unir G1 y G2 con controles
# plt.figure(figsize = (28, 20)) 
# sns.set_theme(style = "darkgrid")
# sns.catplot(x='Group',y="Powers",data=datos, dodge=True, kind="violin",col='Bands',palette="bright",col_wrap=2,legend=False)
# plt.legend(bbox_to_anchor=(1.6, 0.2), loc=4, borderaxespad=0.)
# plt.show()

#Grafico de violin todas las bandas de potencia por grupo uniendo todos los controles
datosunion=datos.copy()
datosunion['Group']=datosunion['Group'].replace({'G1':'CTR','G2':'CTR'})
# print(datosunion['Group'].unique())
# plt.figure(figsize = (28, 20)) 
# sns.set_theme(style = "darkgrid")
# sns.catplot(x='Group',y="Powers",data=datosunion, dodge=True, kind="violin",col='Bands',palette="bright",col_wrap=2,legend=False)
# plt.legend(bbox_to_anchor=(1.6, 0.2), loc=4, borderaxespad=0.)
# plt.show()

#Grafico de violin todas las bandas de potencia por grupo uniendo todos los controles discriminando por base de datos
# plt.figure(figsize = (28, 20)) 
# sns.set_theme(style = "darkgrid")
# sns.catplot(x='Group',y="Powers",data=datosunion,hue='Study', dodge=True, kind="violin",col='Bands',palette="bright",col_wrap=2,legend=False)
# plt.legend(bbox_to_anchor=(1.6, 0.2), loc=4, borderaxespad=0.)
# plt.show()

# Graficos por banda y por visita de biomarcadores y por grupo
# plt.figure(figsize = (28, 20)) 
# sns.set_theme(style = "darkgrid")
# sns.catplot(x='Session',y="Powers",data=datos[datos['Study']=='BIOMARCADORES'],hue='Group', dodge=True, kind="violin",col='Bands',palette="bright",col_wrap=2,legend=False)
# plt.legend(bbox_to_anchor=(1.6, 0.2), loc=4, borderaxespad=0.)
# plt.show()

# Graficos por banda y por visita de biomarcadores sin separar por grupo 
# plt.figure(figsize = (28, 20)) 
# sns.set_theme(style = "darkgrid")
# sns.violinplot(x='Session',y="Powers",data=datos[datos['Study']=='BIOMARCADORES'],hue='Bands',palette="bright")
# plt.title("Biomarcadores: potencias por bandas y visitas")
# plt.show()

# plt.figure(figsize = (28, 20)) 
# sns.set_theme(style = "darkgrid")
# sns.violinplot(x='Bands',y="Powers",data=datos[datos['Study']=='BIOMARCADORES'],hue='Session',palette="bright")
# plt.title("Biomarcadores: potencias por bandas y visitas")
# plt.show()

# Graficos por banda y por visita de SRM sin separar por grupo 
# plt.figure(figsize = (28, 20)) 
# sns.set_theme(style = "darkgrid")
# sns.violinplot(x='Bands',y="Powers",data=datos[datos['Study']=='SRM'],hue='Session',palette="bright")
# plt.title("SRM: potencias por bandas y visitas")
# plt.show()


#Descripcion d elos datos

print("Todos los datos",datos.describe())


study=['CHBMP','BIOMARCADORES','SRM']

datosCHBMP=datos[datos['Study']=='CHBMP']
datosBM=datos[datos['Study']=='BIOMARCADORES']
datosSRM=datos[datos['Study']=='SRM']


desDBs=pd.concat([datosCHBMP.describe(),datosBM.describe(),datosSRM.describe()],axis=1)
desDBs.columns=study
display(HTML('<h2>Potencias de todas las bases de datos</h2>'))
display(desDBs)
desDBs.dfi.export('describetodaslas bases de datos todas las bandas.png')

DB=[datosCHBMP,datosBM,datosSRM]

bands = ['delta','theta','alpha-1','alpha-2','alpha','beta','gamma']
k=0
for i in DB:

    des=pd.DataFrame()
    for j in bands:
        des=pd.concat([des,i[i['Bands']==j].describe()],axis=1)
    des.columns=bands
    print(study[k])
    print(des) 
    des.dfi.export('describebandas'+study[k]+'.png')
    k=k+1
    
    
               