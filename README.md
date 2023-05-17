# authSecret-Graph
Python script to auth via secret. All requirements are in requierements.txt file.

How to use:

#Import auth module
from auth import get_token

#Provide necessary credentials to auth
info_auth = {
    "tenant_id'" = "Provide tenant ID"
    "client_id" = "Provide client ID",
    "secret_id" = "Provide secret ID"    
}
#Getting token, pass info_auth var into function arguments
token = get_token(info_auth)
#Display token on screen
print(token)