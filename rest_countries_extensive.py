import requests 

base_url = 'https://restcountries.eu/rest/v2/'

print('what info do you want? Choose one.')
print('1. Population')
print('2. Languages')
print('3. Time zone')
option = input('').strip()

# print('I chose {}'.format(option))

country = input('What country would you like this information for? ').strip()

# In a real app you wouldn't send user data directly to an API call—dangerous
# You'd sanitize the data in some way beforehand
params = {'fields': 'population;languages;timezones', 'fullText': 'true'}
r = requests.get(base_url + 'name/{}'.format(country), params=params)

if r.status_code == 404:
    print('Country not found')
else:
    json_response = r.json()
    country = json_response[0]

    if option == '1':
        population = country['population']
        print('Population is: {}'.format(population))
    elif option == '2':
        langs = []
        for language in country['languages']:
            langs.append(language['name'])
        print('The spoken languages are: {}'.format(', '.join(langs)))
    else: 
        # Timezones is already a list—no need for a loop
        print('The timezones are: {}'.format(', '.join(country['timezones'])))