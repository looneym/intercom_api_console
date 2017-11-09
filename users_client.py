class UsersClient:

    def __init__(self, base_client):
        self.base_client = base_client

    def create_with_email(self,email):
        data = {
        "email": email
        }
        return self.base_client.post('users', data)

    def create_with_user_id(self, user_id):
        data = {
        "user_id": user_id
        }
        return self.base_client.post('users', data)
        