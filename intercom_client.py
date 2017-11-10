from base_http_client import BaseHttpClient 
from users_client import UsersClient
from conversations_client import ConversationsClient

class IntercomClient:

    def __init__(self, intercom_api_base, intercom_token):
        self.http_client = BaseHttpClient(intercom_api_base, intercom_token)
        self.users = UsersClient(self.http_client)
        self.conversations = ConversationsClient(self.http_client)