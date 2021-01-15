import pandas as pd
ma_df = pd.read_csv('test_pandas.csv') #загружаю данные в dataframe
ma_df['sum'] = ma_df['price_per_job'] * ma_df['jobs_made'] # высчитываю поле sum
ved_df = ma_df.groupby(['uid'])['sum'].sum().reset_index() #формирую группировку по uid и скалдываю по полю sum
#print(ved_df)
ved_df.to_csv(r'df-test1.csv', index=False, header=True) #сохраняю результат в файл df-test1.csv
