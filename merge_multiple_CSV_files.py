#Usage: python merge_multiple_CSV_files.py NameofOutput

import pandas as pd
import glob
import xlsxwriter
import os

dfs=glob.glob("*.csv")
writer=pd.ExcelWriter("WGCNA.xlsx", engine="xlsxwriter")
for f in dfs:
    df=pd.read_csv(f)
    df.to_excel(writer, sheet_name=os.path.splitext(os.path.basename(f))[0], index=False)

writer.save()
