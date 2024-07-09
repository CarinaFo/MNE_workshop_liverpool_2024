# EEG analysis in MNE Python

# Aim: analyze resting state data
import mne
import numpy as np
import matplotlib.pyplot as plt
from pathlib import Path

# this command enables matplotlib to use the qt backend that allows you to view data interactively
#%matplotlib inline
#%matplotlib qt

# load bdf resting state raw data for a single participant
main_exp_dir = Path("C:/", "Users", "Carina", "Desktop", "data_liverpool",  "data_mainexp")
filename = "participant 2 - rest.bdf"
raw = mne.io.read_raw_bdf(Path(f'{main_exp_dir}/{filename}'))

# we only minimally preprocess the data (which you should never do in practice)
raw.load_data()
raw.filter(1, 40)
raw.set_eeg_reference("average")
raw.pick_types(eeg=True)
# drop EXG channels
raw.drop_channels(["EXG1", "EXG2", "EXG3", "EXG4", "EXG5", "EXG6", "EXG7", "EXG8"])

raw.set_montage("standard_1020")

raw.info.ch_names;

# plot the PSD
#raw.pick_channels(['P10']).plot_psd(fmax=50);

# https://mne.tools/mne-connectivity/stable/install.html

# Spectral connectivity is a method for inferring the relationship between channels 
# decomposed at different frequencies of interest. 
# The channels could be M/EEG sensors or brain regions estimated with source localization.

from mne_connectivity import spectral_connectivity_epochs
# 2D plot
from mne_connectivity.viz import plot_connectivity_circle

# Compute connectivity for band containing the evoked response.
# We exclude the baseline period:
fmin, fmax = 7, 13 # alpha frequency
#sfreq = raw.info["sfreq"]  # the sampling frequency
tmin = 0.0  # exclude the baseline period

# Provide the freq points
freqs = np.linspace(fmin, fmax, 2)

# Get the total duration of the raw data in seconds
duration = raw.times[-1]

# Create a single event that starts at the beginning (sample 0)
events = np.array([[0, 0, 1]])  # [start_sample, previous_event_id, event_id]

# Define the epoch parameters
tmin = 0  # Start of the epoch relative to the event, in seconds
tmax = duration  # End of the epoch relative to the event, in seconds

# Create the epoch using the single event
epochs = mne.Epochs(raw, events, event_id=1, tmin=tmin, tmax=tmax, baseline=None)

# Compute spectral connectivity
con = spectral_connectivity_epochs(
    epochs,
    method='coh',
    mode='multitaper',
    sfreq=epochs.info['sfreq'],
    fmin=fmin,
    fmax=fmax,
    faverage=True,
    n_jobs=1
)

# Extract the connectivity matrix (average over frequency band)
con_matrix = con.get_data(output='dense')
con_matrix = con_matrix[:, :, 0]  # select the first frequency band

# Ensure the connectivity matrix is square
assert con_matrix.shape[0] == con_matrix.shape[1], "Connectivity matrix should be square."

# Extract the connectivity matrix (for the selected frequency band)
#con_matrix = con[:, :, 0]  # We only have one frequency band here

# Define node names (channel names)
node_names = epochs.ch_names

# Plot the connectivity circle
plot_connectivity_circle(con_matrix, node_names, n_lines=100,
                         title=f'Connectivity (Coherence, {fmin}-{fmax} Hz)',
                         vmin=0.0, vmax=1.0, colormap='hot')