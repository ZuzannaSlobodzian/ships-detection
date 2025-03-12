import json
from google.oauth2 import credentials as credentials_lib
from google.auth.transport.requests import Request

def authorize():
    token_file = "config.json"
    with open(token_file, "r") as f:
        credentials = json.load(f)

    creds = credentials_lib.Credentials(
        token=credentials['token'],
        refresh_token=credentials['refresh_token'],
        token_uri=credentials['token_uri'],
        client_id=credentials['client_id'],
        client_secret=credentials['client_secret'],
        scopes=credentials['scopes']
    )

    # refreshing token and generate new (if this is necessary)
    if creds and creds.expired and creds.refresh_token:
        creds.refresh(Request())

        with open(token_file, "w") as f:
            json.dump({
                'token': creds.token,
                'refresh_token': creds.refresh_token,
                'token_uri': creds.token_uri,
                'client_id': creds.client_id,
                'client_secret': creds.client_secret,
                'scopes': creds.scopes
            }, f)

    return creds
