import requests as r
'''
resp = r.get('https://reqres.in/api/users/2')

if resp.status_code == 200:
    # not parseable
    print(resp.text) 
    
    # parseable; python dictionary
    json_data = resp.json()
    print(json_data['data']['first_name'])


# Using https://requestbin.com/ to view requests - passing a payload
request = r.get('https://enqlv2x2eg6qc.x.pipedream.net?key1=value1&key2=value2')

payload = {'first': 'one', 'second': 'two'}
request = r.get('https://enqlv2x2eg6qc.x.pipedream.net', params=payload)


# Passing custom headers
headers = {'my-token':'kdjngur934429308lksarj', 'User-Agent': 'test agent'}
request = r.get('https://enqlv2x2eg6qc.x.pipedream.net', headers=headers)

# Sending a JSON object
payload = {'name': 'aimee', 'status': 'fluctuating'}
request = r.get('https://enqlv2x2eg6qc.x.pipedream.net', json=payload)
print(request)
print(request.text)

# Passing form data
payload = {'name': 'aimee', 'age': '24'}
request = r.post('https://reqres.in/api/users', data=payload)
request = r.post('https://httpbin.org/post', data=payload)
print(request.text)

# Sending a file - STRIPE INTERVIEW QUESTION
opening in read mode and in binary mode - will send as raw data without MIME type
files = {'file': open('mel.jpeg', 'rb')}
reqeust = r.post('https://enqlv2x2eg6qc.x.pipedream.net/', files=files)

# Passing a dictionary w tuple
files = {'file': ('mel.jpg', open('mel.jpeg', 'rb'), 'image/jpeg')}
reqeust = r.post('https://enqlv2x2eg6qc.x.pipedream.net/', files=files)

# Saving an image
res = r.get('https://ichef.bbci.co.uk/news/800/cpsprodpb/12A9B/production/_111434467_gettyimages-1143489763.jpg')
print(res.headers)

with open('cat.jpeg', 'wb') as f:
    for chunk in res.iter_content(chunk_size=10000):
        f.write(chunk)

# Raise an exception if not a 200 response
resp = r.get('https://httpbin.org/status/500')

try:
    resp.raise_for_status()
# Catch and HANDLE the error to allow the app to continue running
except r.exceptions.HTTPError:
    print('error error error')
print(resp)

# Timeout error handling. Important to consider when writing an app
try:
    resp = r.get('http://fgdgsdfgsdfg.com')
except r.exceptions.ConnectionError:
    print('Connection error!')


# Error handling timeouts (in seconds)
try: 
    resp = r.get('http://www.google.com', timeout=0.01)
except r.exceptions.ConnectTimeout:
    print('Timed out!')
except r.exceptions.ReadTimeout:
    print('Timed out!')


from requests.auth import HTTPBasicAuth
resp = r.get('https://httpbin.org/basic-auth/user/passwd', auth=HTTPBasicAuth('user', 'passwd'))
print(resp)

'''

