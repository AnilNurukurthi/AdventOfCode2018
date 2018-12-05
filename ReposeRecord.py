import pandas as pd
repose_records = open('data\input3.txt', 'r')


df = pd.DataFrame([str.split(r, ']') for r in repose_records.readlines()], columns=['time', 'action'])

df['time'] = df['time'].str.replace('[', '').str.replace('1518-','1678-').str.strip()# + ':00'
df['action'] = df['action'].str.strip()

print(df['time'].head())
#print(df['time'].sort_values())

df['time'] = pd.to_datetime(df['time'], infer_datetime_format=True)#format='%Y-%d-%m %H:%M')
#pd.factorize(df['action'])

df = df.set_index('time')

df['GuardId'] = df['action'].str.split(' ', n =2, expand=True)[1]#(' ')[1]
#df['action'] = df['action'].str.replace(df['GuardId'], '').str.strip()

print(df.sort_index().head())

