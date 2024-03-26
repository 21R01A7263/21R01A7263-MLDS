sources = []
for source in data['Source']:
  if source not in sources:
    sources.append(source)
print("Creation of content sources:")
for source in sources:
  print("* {}".format(source))