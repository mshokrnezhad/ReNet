# This file includes some examples showing how to instantiate the REQUEST class and get its state.
from Request import Request

# # Creating a request instance using a predefined sample:
# req_obj = Request({"SAMPLE": "REQ1"})
# request_features = req_obj.get_state()

# Creating a request instance using the default configurations:
req_obj = Request({"NUM_REQUESTS": 10})
request_features = req_obj.get_state()
print(request_features)
