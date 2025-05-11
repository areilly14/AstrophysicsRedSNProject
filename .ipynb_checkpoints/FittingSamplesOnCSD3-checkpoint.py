import numpy as np
import matplotlib.pyplot as plt
import sncosmo
from bayesn import SEDmodel

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

filter_yaml = "bayesn-filters/filters.yaml"
model = SEDmodel(load_model= model_name, filter_yaml = filter_yaml)

for dust_law in ["F99","F19","G23"]:
    for supernova_name in supernovae_names:
        supernova_file = "Archive/"+supernova_name+".dat"
        prior_distribution = "uniform"
        drop_bands=['u_CSP', 'U']
        samples, sn_props = model.fit_from_file(supernova_file, RV='uniform', drop_bands=drop_bands, redlaw=dust_law, file_prefix = "FittedSupernova/DustLawsFitOfAllSamples"+model_name+"/"+supernova_name + dust_law)