import pandas as pd
import ydata_profiling as yp
from ydata_profiling import ProfileReport
df=pd.read_excel('your_output_file2.xlsx')
profile= ProfileReport(df,title="prilereport")
profile.to_file('htmlreport.html')