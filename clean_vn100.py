import pandas as pd
import os

dir = os.getcwd()

df = pd.read_csv(dir + '\\DataScience\\stock_sentiment\\VN100.csv')
for i in range(len(df)):
    df['Lần cuối'].iloc[i] = df['Lần cuối'].iloc[i].replace(',','')
    df['Mở'].iloc[i] = df['Mở'].iloc[i].replace(',','')
    df['Thấp'].iloc[i] = df['Thấp'].iloc[i].replace(',','')
    df['Cao'].iloc[i] = df['Cao'].iloc[i].replace(',','')
    df['% Thay đổi'].iloc[i] = df['% Thay đổi'].iloc[i].replace('%','')
    if 'K' in df['KL'].iloc[i]:
        df['KL'].iloc[i] = pd.to_numeric(df['KL'].iloc[i].replace('K','')) * 1000
    elif 'M' in df['KL'].iloc[i]:
        df['KL'].iloc[i] = pd.to_numeric(df['KL'].iloc[i].replace('M','')) * 1000000
df['Ngày'] = pd.to_datetime(df['Ngày'], dayfirst=True)
df[['Lần cuối','Mở','Cao','Thấp','KL','% Thay đổi']] = df[['Lần cuối','Mở','Cao','Thấp','KL','% Thay đổi']].apply(pd.to_numeric)

df.to_csv(dir + '\\DataScience\\stock_sentiment\\VN100_cleaned.csv', sep='\t', encoding='utf16', index = False)