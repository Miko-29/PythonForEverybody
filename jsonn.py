import json, http, ssl
import urllib.request, urllib.parse

# data = '''
# [
#   { "id" : "001",
#     "x" : "2",
#     "name" : "Chuck"
#   } ,
#   { "id" : "009",
#     "x" : "7",
#     "name" : "Brent"
#   }
# ]'''

url = 'http://py4e-data.dr-chuck.net/comments_2028318.json'

print('Retrieving', url)
uh = urllib.request.urlopen(url, context=ctx)
data = uh.read().decode()
print('Retrieved', len(data), 'characters', data[:20].replace('\n', ' '))
js = json.loads(data)

summ = 0

for info in js["comments"]:
  summ = summ + info["count"]

print(summ)
