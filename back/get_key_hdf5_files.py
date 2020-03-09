import pandas as pd
import sys

hdf5_file = "eeg_data.h5"
with pd.HDFStore(hdf5_file, 'r') as store: 
    print(store.keys())
