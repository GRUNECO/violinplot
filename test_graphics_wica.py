from sovaViolin.functions_stage_wica import compare_all_nD_wica
from sovaViolin.functions_stage_wica import compare_nD_wica
from sovaViolin.functions_stage_wica import compare_1D_nV_nM_wica
from sovaViolin.functions_stage_wica import compare_1D_nG_wica
from sovaViolin.functions_dataframes import concat_df
import pandas as pd 

save_path='D:/TDG/filesSaved/'
datosWica=concat_df(save_path+'*/*/*wICA.feather')


# Overall

compare_all_nD_wica(datosWica,color="hsv_r",plot=True,encode=False)

# n estudios 
compare_nD_wica(datosWica,color='hsv_r',plot=True,encode=False)

#n sessions
compare_1D_nV_nM_wica(datosWica,'SRM',color='hsv_r',plot=True,encode=False)

# n grupos
compare_1D_nG_wica(datosWica,'SRM',color='hsv_r',plot=True,encode=False)
compare_1D_nG_wica(datosWica,'Biomarcadores',color='hsv_r',plot=True,encode=False)
compare_1D_nG_wica(datosWica,'CHBMP',color='hsv_r',plot=True,encode=False)

'''



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
'''