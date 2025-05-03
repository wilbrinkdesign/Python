"""
    Connect to your M365 tenant with an App registration.

    To get started:
    - Create an App registration
    - Edit API permissions to 'Directory.Read.All'
    - Create a Client secret
    - Add the value of this secret to a system environment under the name 'M365_Secret'
    - Fill in the vars 'tenant_id' and 'app_id' in the script below
"""

import os
import requests
import json

# Tenant info and M365 URLs
tenant_id = ""
app_id = ""
secret_value = os.environ["M365_Secret"]
api_url = f"https://login.microsoftonline.com/{tenant_id}/oauth2/v2.0/token"
graph_url = "https://graph.microsoft.com/v1.0/users"

body = {
    "client_id"     : app_id,
    "client_secret" : secret_value,
    "scope"         : "https://graph.microsoft.com/.default",
    "grant_type"    : "client_credentials" 
}

response = requests.post(api_url, data=body)
token = json.loads(response.content)["access_token"]

site = requests.get(
    graph_url,
    headers={'Authorization': 'Bearer {0}'.format(token)}
)

# Print all M365 users
for user in json.loads(site.content)["value"]:
    print(user["displayName"])
