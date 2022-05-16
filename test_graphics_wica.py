from sovaViolin.functions_stage_wica import compare_all_nD_wica,compare_nD_wica,compare_1D_wica,compare_1D_nV_wica,compare_nD_nG_wica,compare_nD_nG_wica
import pandas as pd 

datosWica=pd.read_excel(r'D:\WEB\backend\filesSaved\SRMPrueba\derivatives\data_wICA.xlsx')

# 1 estudio
compare_1D_wica(datosWica,'SRM',plot=True)
# n estudios 
compare_nD_wica(datosWica,plot=True)
# n grupos

# n visitas
compare_1D_nV_wica(datosWica,'SRM',plot=True)


#N GRUPOS
group_dict1={
    #'BIOMARCADORES':['CTR','DCL','G1','G2'],
    'SRM':['SRM'] # assume datasets with no groups have Group=Study
}
compare_nD_nG_wica(datosWica,group_dict1,plot=True)

# group_dict2={
#     #'BIOMARCADORES':['CTR','DCL','G1','G2'],
# }
# compare_nD_nG_wica(datosWica,group_dict2)
