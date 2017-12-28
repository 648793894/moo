import urllib2
import csv
line = '1 2 3 4 5'
fields = line.split()
print(fields)

url = 'http://google.com'
get_csv = urllib2.urlopen(url)
data = []
for line in get_csv:
    data.append(line.split(","))
print(data[:4])