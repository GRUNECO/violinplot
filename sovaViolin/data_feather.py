import pandas as pd
save_path='D:\XIMENA\BIDS\Estudiantes2021\derivatives\Long_format'
Estudiantes2021={
    'prep':pd.read_feather(save_path+ r'\data_CE_PREP.feather'),
    'Wica':pd.read_feather(save_path+r'\data_CE_wICA.feather'),
    'Reject':pd.read_feather(save_path+r'\data_CE_reject.feather'),
    'component':{'Power':pd.read_feather(save_path+r'\data_long_power_components.feather'),
                'SL':pd.read_feather(save_path+r'\data_long_sl_components.feather'),
                'Coherence':pd.read_feather(save_path+r'\data_long_coherence_components.feather'),
                'Entropy':pd.read_feather(save_path+r'\data_long_entropy_components.feather')
                }
    }