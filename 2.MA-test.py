import pandas as pd
data = pd.read_csv("test_pandas.csv") #читаю данные в dataframe
data['sum'] = data['price_per_job'] * data['jobs_made'] #добавляю поле sum, в котором получаю сумму выполненных работ
ved_df = data.groupby(['uid'])['sum'].sum().reset_index() #групперую по uid и суммирую по полю sun.
sort_df = ved_df.sort_values(by=['sum'], ascending=False) #сортирую по убыванию
sort_df['cumsum'] = sort_df['sum'].cumsum() #добавляю поле cumsum и высчитываю кумулятивное значение
sum60perc = sort_df['sum'].sum() * 0.6 #нахожу значение 60% от всех сумм
#print("uids 60%:", sort_df.loc[sort_df['cumsum'] <= sum60perc])
sort_df.loc[sort_df['cumsum'] <= sum60perc].to_csv(r'df-test2.csv', index=False, header=True) #сохраняю результат выборки в файл df-test2.csv
