import pandas as pd

poke = pd.read_csv('pokemon_data.csv')
new_poke=poke.loc[(poke['Type 1']=='Grass') & (poke['Type 2']=='Poison') & (poke['HP']>70)]
print(new_poke)
poke = pd.read_csv('pokemon_data.txt',delimiter='\t' )
print(poke.tail(5))
print(poke.head(5))
print(poke.columns)
print(poke['Name'][0:9])
print(poke[['Name','Type 1']][0:9])
print(poke.iloc[1:4])
print(poke.iloc[3,1])
print(poke.sort_values('Name'))

#Filter
print(poke.loc[poke['Type 1']=='Fire'])
print(poke.loc[poke['Name'].str.contains('Mega')])

import re
print(poke.loc[poke['Type 1'].str.contains('Fire|Grass', flags=re.I, regex=True)])
print(poke.loc[poke['Type 1'].str.contains('pi[a-z]*', flags=re.I, regex=True)])
print(poke.loc[(poke['Type 1']=='Grass') & (poke['Type 2']=='Poison') & (poke['HP']>70)])
print(new_poke.reset_index())

print(poke.describe())

#file coverter
#poke.to_excel('modified.xlsx', index=False)
#print(new_poke.to_csv('new.csv'))

#statistics

poke['count']=0
print(poke.groupby(['Type 1']).count()['count'])
print(poke.groupby(['Type 1' , 'Type 2']).count()['count'])
