import numpy as np
import matplotlib.pyplot as plt
import sncosmo
from bayesn import SEDmodel
import os

directory = os.fsencode("Archive")
supernovae_names = ["sn2006hb"]
for file in os.listdir(directory):
    filename = os.fsdecode(file)
    if filename.endswith(".dat"): 
        supernovae_names.append(filename[:-4])
        continue
    else:
        continue

model_name = "W22_F19_model"
dust_law = "F19"

directory = os.fsencode("/root/partiiiproject/DustLawsFitOfAllSamples"+model_name)

supernovae_done = ["sn2006hb"]
for file in os.listdir(directory):
    filename = os.fsdecode(file)
    if filename.endswith(dust_law+"_fit_summary.csv"):
        len_remove = len(dust_law+"_fit_summary.csv")
        supernovae_done.append(filename[:-len_remove])
        continue
    else:
        continue

supernovae_names = list(set(supernovae_names) - set(supernovae_done))
print(supernovae_names)


filter_yaml = "bayesn-filters/bayesn-filters/filters.yaml"
model = SEDmodel(load_model= model_name, filter_yaml = filter_yaml)

for dust_law in ["F99","F19","G23"]:
    for supernova_name in supernovae_names:
        supernova_file = "Archive/"+supernova_name+".dat"
        prior_distribution = "uniform"
        drop_bands=['u_CSP', 'U']
        samples, sn_props = model.fit_from_file(supernova_file, RV='uniform', drop_bands=drop_bands, redlaw=dust_law, file_prefix = "DustLawsFitOfAllSamples"+model_name+"/"+supernova_name + dust_law)
