import pandas as pd

ds = pd.read_csv('data/fake_data.csv', encoding='utf-8', delimiter=';')
ds_brazil = ds[ds.Nationality == 'Brazil']
print(ds_brazil)
