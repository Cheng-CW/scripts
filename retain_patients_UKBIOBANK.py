#python filter_specific.py id_20002.csv datacoding(1074) output.csv

import pandas as pd
import numpy as np
import os
import sys

input=sys.argv[1]
field=sys.argv[2]
output_name=sys.argv[3]

PID = pd.read_csv(input, index_col=0)
print("dataset:", PID.shape)
selected=PID[(PID.iloc[0:, 0:] == int(field)).any(axis=1)]
selected.to_csv(output_name)
print("final dataset:", selected.shape)
