import requests

# Splitting URL into base and endpoint
base_url = 'https://restcountries.eu/rest/v2/'
'''
r = requests.get(base_url + 'all')

json_result = r.json()

print(json_result)


# Searching for 'can' using the name endpoint
r = requests.get(base_url + 'name/can')
print(r.json())

fields = {'fields': 'altSpellings;name'}
r = requests.get(base_url + 'name/can', params=fields)
print(r.json())

'''

fields = {'fields': 'name;currencies'}
r = requests.get(base_url + 'capital/tokyo', params=fields)
print(r.json())