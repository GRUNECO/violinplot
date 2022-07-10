import mne 
import matplotlib.pyplot as plt 
import numpy as np 

norm=mne.read_epochs(r'F:\BIOMARCADORES\derivatives\sovaharmony\sub-CTR001\ses-V0\eeg\sub-CTR001_ses-V0_task-CE_desc-norm_eeg.fif',verbose='error')
reject=mne.read_epochs(r'F:\BIOMARCADORES\derivatives\sovaharmony\sub-CTR001\ses-V0\eeg\sub-CTR001_ses-V0_task-CE_desc-reject[restCE]_eeg.fif',verbose='error')



fig, ax = plt.subplots(2)

norm.plot_psd(ax=ax[0], show=False)
reject.plot_psd(ax=ax[1], show=False)

ax[0].set_title('PSD norm')
ax[1].set_title('PSD reject')
ax[1].set_xlabel('Frequency (Hz)')
fig.set_tight_layout(True)
plt.show()
