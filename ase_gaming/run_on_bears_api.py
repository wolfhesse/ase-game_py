'''

TODO
status: deserialization problem

'''

from __future__ import print_function

from pprint import pprint

import bears_api
from bears_api.rest import ApiException

# import ase_back_api_product
# from ase_back_api_product.rest import ApiException
# Configure OAuth2 access token for authorization: OAuth2
# ase_back_api_product.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_client = bears_api.ApiClient(host="http://bearsapi.wolfspool.chickenkiller.com/api")
api_instance = bears_api.DefaultApi(api_client)

size = 1  # float | Size of array (optional) (default to 1)

try:
    api_response = api_instance.find_bears()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->..._get: %s\n" % e)
