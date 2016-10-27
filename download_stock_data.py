import numpy as np
import matplotlib.pyplot as plt
%matplotlib inline
import seaborn as sns
import pandas as pd
from scipy.spatial.distance import euclidean

from fastdtw import fastdtw
import time


df_code=pd.read_csv("data/company_code.csv", sep='\t')
# http://www.jpx.co.jp/markets/indices/topix/ 浮動株比率の変更情報より
df_code=df_code[["SC","名称","市場","業種"]]

for i, row in df_code.query('市場 == ["東証一部"]').iterrows():
    df_company_tmp=pd.DataFrame()
    for year in ["2014","2015","2016"]:
        url="http://k-db.com/stocks/"+str(int(row["SC"]))+"-T/1d/"+year+"?download=csv"
        df_tmp=pd.read_csv(url)
        df_tmp.to_csv("download/"+str(row["SC"])+row["名称"]+year+".csv")
        df_company_tmp=pd.concat([df_tmp,df_company_tmp])
        print(url)
        time.sleep(10)

    # まとめて保存
    df_company_tmp.reset_index().to_csv("download/"+str(row["SC"])+row["名称"]+".csv")
