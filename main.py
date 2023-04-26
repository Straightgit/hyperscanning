import numpy as np
import mne
from hypyp import viz
def epochs():
    #epoch_1 = mne.io.read_raw_fieldtrip('d:/user/Desktop/Hyperscanning_py/Hyper39Dual3.mat',info=None)
    epoch_1 = mne.read_epochs(r'd:\user\Desktop\Hyperscanning_py\Hyper39Dual3.mat')
    #epoch_2 = mne.read_epochs_fieldtrip(r'd:\user\Desktop\Hyperscanning_py\Hyper40Dual3')
    return epoch_1,epoch_2
epoch_1,epoch_2 = epochs()
def high_pass_filtering(raw1,raw2):
    filt_raws = prep.filt(raws=[raw1,raw2])
    return filt_raws
def computing_ICA(epochs_1,epochs_2):
    icas = prep.ICA_fit(epochs=[epochs1,epochs2],n_components = 15,method = 'infomax'
                        fit_params = dict,rando_state = 42)
    cleaned_epochs_ICA = prep.ICA_choice_comp(icas,epochs=[epochs1,epochs2])
    cleaned_epochs_AR = prep.AR_cocal(cleaned_epochs_ICA,verbose=True)
    return cleaned_epochs_ICA,cleaned_epochs_AR
computing_ICA(epoch_1,epoch_2)
def merge(epochs1,epochs2):
    hyper_epo = merge(epochs_S1=epochs1,epochs_S2 = epochs2)
    epochs1,epochs2 = split(hyper_epo)
