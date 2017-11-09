import sys
import os

from IPython import embed

from intercom_client import IntercomClient

# prevent generation of .pyc files
sys.dont_write_bytecode = True

intercom_api_base = 'https://api.intercom.io/'
token = os.environ['INTERCOM_TOKEN']
client = IntercomClient(intercom_api_base, token)

embed()
