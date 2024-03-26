percent = np.zeros(len(sources))
for source in data['source']:
  for index in range(len(sources)):
    if source == sources[index]:
      percent[index] +=1
      pass
percent /= 100

pie_chart.pd.Series(percent, index=sources, name='Sources')
pie_chart.plot.pie(fontsize=11, autopct='%.2f', figsize=(6,6))