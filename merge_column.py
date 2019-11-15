#Usage: python extract_info.py ReferenceCSV/TXTFile QueryCSV/TXTFile ColumnName OutputName.csvOR.txt

import pandas as pd
import os
import sys

reference=sys.argv[1]
query=sys.argv[2]
column_name=sys.argv[3]
output_name=sys.argv[4]

if reference.endswith(".csv"):
    Matrix=pd.read_csv(reference)
elif reference.endswith(".txt"):
    Matrix=pd.read_csv(reference, sep="\t")
else:
    print("Plese provide the reference file in CSV or TXT format")
    exit()

if query.endswith(".csv"):
    PID=pd.read_csv(query)
elif query.endswith(".txt"):
    PID=pd.read_csv(query, sep=".txt")
else:
    print("Plese provide the query file in CSV or TXT format")
    exit()

Data=pd.merge(Matrix,PID,on=column_name)

if output_name.endswith(".csv"):
    Data.to_csv(output_name, index=False)
elif output_name.endswith(".txt"):
    Data.to_csv(output_name, index=False, sep="\t")
