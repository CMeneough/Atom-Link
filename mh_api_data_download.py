# Manufactured Home Data API
import requests
import pandas as pd
import json

# Login Token - Need to change after every login
myToken = 'eyJraWQiOiJyRzhja1lKNXFnS2FwNitpVG52UWpmM1pSK1lpRG9GOFY5c1pjR1B3MGUwPSIsImFsZyI6IlJTMjU2In0.eyJjdXN0b206b3JnYW5pemF0aW9uIjoiR2VvcmdlIFdhc2hpbmd0b24gVW5pdmVyc2l0eSIsInN1YiI6IjhlNTE3ZjI4LWY4NGQtNDc3NC05ZTk3LWJkMjc0YzA2ZmFkYSIsImVtYWlsX3ZlcmlmaWVkIjp0cnVlLCJpc3MiOiJodHRwczpcL1wvY29nbml0by1pZHAudXMtZWFzdC0xLmFtYXpvbmF3cy5jb21cL3VzLWVhc3QtMV9HNWpZSUxFcVgiLCJjb2duaXRvOnVzZXJuYW1lIjoiY21lbmVvdWdoQGd3dS5lZHUiLCJjdXN0b206am9iX3RpdGxlIjoiT3RoZXIiLCJnaXZlbl9uYW1lIjoiQ29ubm9yIiwiYXVkIjoiMzgwZGlpdG1zYmE3ZDYyMjBoOGxzcTFicW8iLCJldmVudF9pZCI6IjUzYzY4ZDJjLWQ2MDEtNGZjNi1hMGVmLWViNTk1ODY2ZTIxMiIsInRva2VuX3VzZSI6ImlkIiwiYXV0aF90aW1lIjoxNTYyNjk5MzExLCJjdXN0b206am9iX3RpdGxlX290aGVyIjoiR3JhZHVhdGUgU3R1ZGVudCIsImV4cCI6MTU2MjcwMzA2MSwiaWF0IjoxNTYyNjk5NDYxLCJmYW1pbHlfbmFtZSI6Ik1lbmVvdWdoIiwiZW1haWwiOiJjbWVuZW91Z2hAZ3d1LmVkdSJ9.UPRyO60XQmqFjDvv5XCvfn6B3My6JuUQGVr7EIPR96IxUDYYNlLxIhcpLHJlSINaX_3awf9O58W-0lwx3JRT1LYxjDWoBhGl2lMIQ2zcfZHWss9iudtIv1PlDaCU7i2ibzuN1WqcTyiDJmbnl5BYDimGjXbtJo7qqfqMCGHXTbUI691_iq7j-BKzW-12L-Qjafa2NQB8LGe7AA6SJoRLb6men0LJWmGvuar0PkuDMZ8pnqWmepjWqwMR-enqmib6bqJYV2Ph2wTzjXgDKZ2tMUcDweieSJ_hweD5ylVTqGPgp2UKNEz3DQlNbW-_ry8D_rdLNh9PQdmdaouw2YOjYw'

# Import Acquistion Data
myURL = 'https://api.theexchange.fanniemae.com/v1/manufactured-housing-loans/acquisitions'
head = {'Authorization': '{}'.format(myToken)}
response = requests.get(myURL, headers=head)

x=response.json()
x=x['_embedded']
x=x['acquisitions']
df = pd.DataFrame(x)
df.set_index('loanIdentifier',inplace=True)
df.to_csv('data_acq',index=False)

# Import Performance Data
myURL = 'https://api.theexchange.fanniemae.com/v1/manufactured-housing-loans/performance'
head = {'Authorization': '{}'.format(myToken)}
response = requests.get(myURL, headers=head)

x=response.json()
x=x['_embedded']
x=x['performance']
df = pd.DataFrame(x)
df.set_index('loanIdentifier',inplace=True)
df.to_csv('data_perform',index=False)
