import urllib.request, json
url = "https://o136z8hk40.execute-api.us-east-1.amazonaws.com/dev/get-list-of-conferences"

response = urllib.request.urlopen(url)
data = json.loads(response.read())

def getdata():
    res = (data['free'])
    for i in res:
        ke=i.values()
        print(ke)
        if i not in res:
            print("duplicate",res[values])


getdata()
