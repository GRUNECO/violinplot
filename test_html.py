# escribe-html-2-windows.py

import webbrowser
import pandas as pd
from sovaViolin.functions_stage_prep import compare_1D_nV_nM_prep
from sovaViolin.functions_stage_wica import compare_1D_nV_nM_wica
from sovaViolin.functions_stage_reject import compare_1D_nV_nM_reject
from sovaViolin.functions_postprocessing_components import compare_norm_1D_1G_1B_nV_ncomp_power
from sovaViolin.data_feather import Estudiantes2021 as DATA    
from sovaViolin.functions_connectivity import graphics
import io, base64
from PIL import Image

DIR_INPUT=r'D:\XIMENA\BIDS\Estudiantes2021'
input_pdf = DIR_INPUT + r"\reporte_preprocesamiento.html"
f = open(input_pdf,'w')

prep=compare_1D_nV_nM_prep(DATA['prep'],'Estudiantes2021',color='hsv_r',plot=False,encode=True)
# wica=compare_1D_nV_nM_wica(DATA['Wica'],'Estudiantes2021',color='hsv_r',plot=False,encode=True)
# reject=compare_1D_nV_nM_reject(DATA['Reject'],'Estudiantes2021',color='hsv_r',plot=False,encode=True)

# encodes=[]
# img_names=['prep','wica','reject']
# encodes+=[prep]
# encodes+=[wica]
# encodes+=[reject]


bands= DATA['component']['Power']['Band'].unique()
# for band in bands:
#     str_power='power_'+band
#     img_names.append(str_power)
#     obj_encode=compare_norm_1D_1G_1B_nV_ncomp_power(DATA['component']['Power'],'Estudiantes2021','Control',band,num_columns=4, save=False,plot=False,encode=True)
#     encodes.append(obj_encode)

# for i,img in enumerate(img_names):
#     img_object=Image.open(io.BytesIO(base64.decodebytes(bytes(encodes[i]))))
#     img_object.save(r'D:\XIMENA\violinplot\sovaViolin\imgs\report_{name}.jpeg'.format(name=img))


table_prep = DATA['prep'].describe()
table_wica = DATA['Wica'].describe()
table_reject = DATA['Reject'].describe()
table_html_prep = table_prep.to_html(table_id="table")
table_html_wica = table_wica.to_html(table_id="table")
table_html_reject = table_reject.to_html(table_id="table")


path='D:\XIMENA\BIDS\Estudiantes2021\derivatives\Long_format'
# for metric in DATA['component'].keys():
#     for band in bands:
#         d_com=DATA['component'][metric]
#         d_banda_com=d_com[d_com['Band']==band]
#         path_com=graphics(d_banda_com,metric,path,band,'IC',num_columns=4,save=True,plot=False,encode=True)


mensaje = f"""<html>
<head></head>
<body><h1 style="text-align: center;">REPORTE ANÁLISIS DE CALIDAD PREPROCESAMIENTO</h1></body>
</html>
<h2 style="text-align: center;"> Etapa PREP</h2>
<p style="text-align:center">{table_html_prep} </p>
<img src="data:image/jpeg;base64,{prep}/>
<img  src="D:/XIMENA/violinplot/sovaViolin/imgs/report_prep.jpeg"  width="85%" alt="Red dot" />
<h2 style="text-align: center;"> Etapa wICA</h2>
<p style="text-align:center">{table_html_wica}</p>
<img src="D:/XIMENA/violinplot/sovaViolin/imgs/report_wica.jpeg" width="85%" class="center"/>
<h2 style="text-align: center;"> Etapa rechazo de épocas</h2>
<p style="text-align:center">{table_html_reject}</p>
<img src="D:/XIMENA/violinplot/sovaViolin/imgs/report_reject.jpeg" width="85%" class="center"/>
<h1 style="text-align: center;">REPORTE ANÁLISIS DE CALIDAD PROCESAMIENTO</h1>
<h2 style="text-align: center;">Análisis de potencia espectral</h2>
<h2 style="text-align: center;">Potencia en Delta</h2>
<img src="D:/XIMENA/violinplot/sovaViolin/imgs/report_power_Delta.jpeg" width="85%" class="center"/>
<h2 style="text-align: center;">Potencia en Theta</h2>
<img src="D:/XIMENA/violinplot/sovaViolin/imgs/report_power_Theta.jpeg" width="85%" class="center"/>
<h2 style="text-align: center;">Potencia en Alpha-1</h2>
<img src="D:/XIMENA/violinplot/sovaViolin/imgs/report_power_Alpha-1.jpeg" width="85%" class="center"/>
<h2 style="text-align: center;">Potencia en Alpha-2</h2>
<img src="D:/XIMENA/violinplot/sovaViolin/imgs/report_power_Alpha-2.jpeg" width="85%" class="center"/>
<h2 style="text-align: center;">Potencia en Beta-1</h2>
<img src="D:/XIMENA/violinplot/sovaViolin/imgs/report_power_Beta1.jpeg" width="85%" class="center"/>
<h2 style="text-align: center;">Potencia en Beta-2</h2>
<img src="D:/XIMENA/violinplot/sovaViolin/imgs/report_power_Beta2.jpeg" width="85%" class="center"/>
<h2 style="text-align: center;">Potencia en Gamma</h2>
<img src="D:/XIMENA/violinplot/sovaViolin/imgs/report_power_Gamma.jpeg" width="85%" class="center"/>


"""

f.write(mensaje)
f.close()


webbrowser.open_new_tab(input_pdf)
output_pdf = DIR_INPUT + r"\reporte_preprocesamiento.pdf"


