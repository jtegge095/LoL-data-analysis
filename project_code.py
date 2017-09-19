# LoL analysis code
# import libraries
import pandas as pd
import numpy as np 
import matplotlib.pyplot as plt 
import seaborn as sns
import json
sns.set_style('darkgrid')
%matplotlib inline

def idToName(ID, dic):
    '''
    ID: champion ID as listed in original dataframe
    dic: champInfo from json, defined above

    used to convert ID's to champion names
    '''
    champ = dic['name'][ID]
    return champ

def getTag(name, data):
    '''
    name: champion name as listed in dataframe
    data: champInfo

    used to get primary tag from champInfo
    '''
    tags = data['tags'][name][0]
    return tags

def numToColor(data):
    '''
    data: main dataframe

    used to get color of team from 0 or 1
    assuming that team 0 is red and 1 is blue
    '''
    if data == 0:
        color = 'red'
    else:
        color = 'blue'
    return color

# import original data
data = pd.read_csv('games.csv')

# rename column, add new column to show minutes
data.rename(columns={'gameDuration': 'gameLength (seconds)'}, inplace=True)
data['gameLength (minutes)'] = data['gameLength (seconds)'].apply(lambda x: x//60)

# import champion info json and grab the data
jDict = pd.read_json('champion_info.json')
champInfo = pd.read_json((jDict['data']).to_json(), orient='index')

# Temp. set index to id 
champInfo.set_index(['id'], inplace=True)

# create list of columns of user picks and another list for bans
champCols = ['t1_champ1id','t1_champ2id','t1_champ3id','t1_champ4id','t1_champ5id',
             't2_champ1id','t2_champ2id','t2_champ3id','t2_champ4id','t2_champ5id']
banCols = ['t1_ban1','t1_ban2','t1_ban3','t1_ban4','t1_ban5',
             't2_ban1','t2_ban2','t2_ban3','t2_ban4','t2_ban5',]

# apply the idToName function for these columns so we have 
# champion names rather than ID's
for c in champCols:
    data[c] = data[c].apply(lambda x: idToName(x, champInfo))

for c in banCols:
    data[c] = data[c].apply(lambda x: idToName(x, champInfo))    

# Set index to champion names
champInfo.set_index(['name'],inplace=True)   

# apply the getTag function for these columns so we have 
# new primary champion tags columns

for col in champCols:
    data[col + '_tags'] = data[col].apply(lambda x: getTag(x, champInfo))

# Variables to be used for data visualization
sortedPick = sorted(data['t1_champ1id'])
sortedBan = sorted(data['t1_ban1'])
tagsList = data['t1_champ1id_tags']

# Add winner color column to see which side the team was on
data['winner(color)'] = data['winner'].apply(lambda x: numToColor(x))
