# LoL analysis code
# import libraries
import pandas as pd
import numpy as np 
import matplotlib.pyplot as plt 
import seaborn as sns
import json
sns.set_style('darkgrid')
%matplotlib inline

# import original data
data = pd.read_csv('games.csv')

# rename column, add new column to show minutes
data.rename(columns={'gameDuration': 'gameLength (seconds)'}, inplace=True)
data['gameLength (minutes)'] = data['gameLength (seconds)'].apply(lambda x: x//60)

# import champion info json and grab the data
jDict = pd.read_json('champion_info.json')
champData = jDict['data']


def idToName(ID, dic):
	'''
	ID: champion ID as listed in original dataframe
	dic: champData from json, defined above

	used to convert ID's to champion names
	'''
    champ = dic[ID]
    return champ['name']


# create an ordered list of champion names for later use
champList = []
for info in champData:
    champList.append(info['name'])
champList = sorted(champList)

# create list of columns of user picks and another list for bans
champCols = ['t1_champ1id','t1_champ2id','t1_champ3id','t1_champ4id','t1_champ5id',
             't2_champ1id','t2_champ2id','t2_champ3id','t2_champ4id','t2_champ5id']
banCols = ['t1_ban1','t1_ban2','t1_ban3','t1_ban4','t1_ban5',
             't2_ban1','t2_ban2','t2_ban3','t2_ban4','t2_ban5',]

# apply the idToName function for these columns so we have 
# champion names rather than ID's
for c in champCols:
    data[c] = data[c].apply(lambda x: idToName(x, champData))

for c in banCols:
    data[c] = data[c].apply(lambda x: idToName(x, champData))       
