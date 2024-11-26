import pickle

import pandas as pd


data_files = ['/home/kls/data/tabletennisdata/xigua_set(labelXscrw25).pkl',
              '/home/kls/data/tabletennisdata/kls_set(labelXscrw25).pkl']

# print(data_files[0:1])
# print(data_files[1:2])


data = pd.read_pickle('/home/kls/data/tabletennisdata/kls_set(labelXscrw25).pkl')
print(data)
