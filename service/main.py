# This file includes some examples showing how to instantiate the SERVICE class and get its state.
from Service import Service

# # Creating a service instance using a predefined sample:
# srv_obj = Service({"SAMPLE": "SRV1"})
# print(srv_obj.SERVICES)

# # Creating a service instance using the default configurations:
srv_obj = Service({"NUM_SERVICES": 10})
print(srv_obj.SERVICES)
