from base_resource_client import BaseResourceClient

class UsersClient(BaseResourceClient):

    def create_with_email(self,email):
        data = {
        "email": email
        }
        return self.http_client.post('users', data)

    def create_with_user_id(self, user_id):
        data = {
        "user_id": user_id
        }
        return self.http_client.post('users', data)
        