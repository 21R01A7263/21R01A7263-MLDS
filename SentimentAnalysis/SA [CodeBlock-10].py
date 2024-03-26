tlen = pd.Series(data=data['len'].values, index = data['Date'])
tfav = pd.Series(data=data['Likes'].values, index = data['Date'])
tret = pd.Series(data=data['RTs'].values, index = data['Date'])