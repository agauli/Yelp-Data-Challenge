import sys
for line in sys.stdin:
  data = line.strip().split(",")
if len(data) == 3:
  id, city, attire = data
  attire = attire[11:14]
  print "{0}\t{1}".format(city, attire)
