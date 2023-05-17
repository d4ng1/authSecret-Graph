def get_token(credentials):
    # Importing msla lib
    from msal import ConfidentialClientApplication
    # Define Scopes
    scopes= ['https://graph.microsoft.com/.default']
    # Login in tenant
    msal_authority = f"https://login.microsoftonline.com/{credentials['tenant_id']}"

    # Preparing Auth process 
    auth_app = ConfidentialClientApplication(client_id=credentials['client_id'],client_credential=credentials['secret_id'],authority=msal_authority) 

    # Getting token
    token = auth_app.acquire_token_silent(
        scopes=scopes,
        account=None,
        
    ) 

    # Checking token
    if not token:
        token = auth_app.acquire_token_for_client(scopes=scopes)

    # Setting token and returning it
    if "access_token" in token:
        access_token = token['access_token']
    else:
        raise Exception("No access Token Found")

    
    return access_token
