from base_http_client import BaseHttpClient 
from users_client import UsersClient

class IntercomClient:

    def __init__(self, intercom_api_base, intercom_token):
        self.base_client = BaseHttpClient(intercom_api_base, intercom_token)
        self.users = UsersClient(self.base_client)
