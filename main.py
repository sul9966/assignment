import sys

#Variables that will be passed during script execution
apiKey = sys.argv[1]
macAddress = sys.argv[2]

#Api url 
url = "https://api.macaddress.io/v1?apiKey=" + apiKey + "&output=json&search=" + macAddress

import  requests
import json

def get_macaddr(url):
    api_result = requests.get(url)
    result = api_result.json()
    try:
      return result['vendorDetails']['companyName']
    except:
        return "Mac Address not found"

print(get_macaddr(url))
