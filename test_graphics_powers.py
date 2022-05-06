from datasets import CHBMP,BIOMARCADORES,SRM,BIOMARCADORES_test,SRM_test # LEMON
from Graphics.GetDataframes import get_dataframe_powers
from Graphics.functions_postprocessing import compare_1S_nB_0C_power, compare_1S_1V_nB,compare_1S_1G_nB_0C_power,compare_1S_nV_nB,compare_1S_1B_nC_power, compare_nS_nB_power,compare_nS_nG_nB

Studies=[BIOMARCADORES_test,SRM_test]
datosPowers=get_dataframe_powers(Studies)
#datosPowers.to_csv('dataframe.csv',index=False)

# TOTAL
#compare_nD(datosPowers,plot=True)

# 1 estudio
#St=['CHBMP','BIOMARCADORES','SRM']
St=['BIOMARCADORES','SRM']
bands_1 = ['delta','theta','alpha-1','alpha-2','beta-1','beta-3','gamma']
GB = ['G1','G2','CTR','DCL','DTA']
Vs = ['V0','V1','V2','V3','V4']

for Study in St:
    compare_1S_nB_0C_power(datosPowers,Study,plot=True)
    compare_1S_nV_nB(datosPowers,Study)
    for gr in GB:
        compare_1S_1G_nB_0C_power(datosPowers,Study,gr,plot=True)
    for V in Vs:
        compare_1S_1V_nB(datosPowers,Study,V,True)        
    for band in bands_1:
        compare_1S_1B_nC_power(datosPowers,Study,band,plot=True)
St=['BIOMARCADORES','SRM']
bands_1 = ['delta','theta','alpha-1','alpha-2','alpha','beta','gamma']
GB = ['G1','G2','CTR','DCL','DTA']

for Study in St:
    compare_1S_nB_0C_power(datosPowers,Study,plot=True)
    # NOTA: Este gráfico por el momento no es representativo           
    # for band in bands_1:
    #     compare_1S_1B_nC_power(datosPowers,Study,band,plot=True)

#n estudios 
'''
# NOTA: Esta función por el momento no es representativa
channels = ['FP1', 'FPZ', 'FP2', 'AF3']
#, 'AF4', 'F7', 'F5', 'F3', 'F1', 'FZ', 'F2', 'F4', 'F6', 'F8', 'FC5', 'FC3', 'FC1', 'FCZ', 'FC2', 'FC4', 'FC6', 'T7', 'C5', 'C3', 'C1', 'CZ', 'C2', 'C4', 'C6', 'T8', 'TP7', 'CP5', 'CP3', 'CP1', 'CPZ', 'CP2', 'CP4', 'CP6', 'TP8', 'P7', 'P5', 'P3', 'P1', 'PZ', 'P2', 'P4', 'P6', 'P8', 'PO7', 'PO5', 'PO3', 'POZ', 'PO4', 'PO6', 'PO8', 'O1', 'OZ', 'O2']
for channel in channels:
    compare_nS_nB_power(datosPowers,name_channel=channel)
'''
compare_nS_nB_power(datosPowers,name_channel="None")

'''
Nota: Solo es útil para cuando el usuario quiera un grupo en especifico, de lo contrario
esta la función para n grupos

GB= ['G1','G2','CTR','DCL','DTA']
# 1  grupo
for G in GB:
    compare_1S_1G_nB_0C_power(datosPowers,'BIOMARCADORES',G,plot=True)
'''

# n grupos 
info={
   'SRM':['SRM'],
   'BIOMARCADORES':['G1','G2','CTR','DCL','DTA']
   #'CHBMP':['CHBMP']
}
compare_nS_nG_nB(datosPowers,info)

'''
# 1 sessions
# Solo es útil si se quiere una gráfica en especifico , para ver todas es mejor usar para nV
Vs = ['V0','V1','V2','V3','V4']
Vs_SRM=['t1','t2']
for V in Vs:
    compare_1S_1V_nB(datosPowers,'BIOMARCADORES',V,True)
for V in Vs_SRM:
    compare_1S_1V_nB(datosPowers,'SRM',V,True)
'''

# n sessions
compare_1S_nV_nB(datosPowers,'BIOMARCADORES')
compare_1S_nV_nB(datosPowers,'SRM')
