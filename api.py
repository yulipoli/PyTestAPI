import json
import requests
import uuid
from settings import VALID_EMAIL, VALID_PASSWORD


class Pets:
    """ API library for the website http://34.141.58.52:8080/#/"""
    def __init__(self):
        self.base_url = 'http://34.141.58.52:8000/'

    def get_registered(self) -> json:
        e = uuid.uuid4().hex
        data = {"email": f'{e}@gmail.com', "password": '1234', "confirm_password": '1234'}
        res = requests.post(self.base_url + 'register', data=json.dumps(data))
        users_token = res.json()['token']
        users_id = res.json()
        users_id = users_id.get('id')
        status = res.status_code
        return status, users_id, users_token

    def register_and_delete_user(self) -> json:
        e = uuid.uuid4().hex
        data = {"email": f'{e}@gmail.com', "password": '1234', "confirm_password": '1234'}
        res = requests.post(self.base_url + 'register', data=json.dumps(data))
        my_id = res.json().get('id')
        my_token = res.json()['token']
        headers = {'Authorization': f'Bearer {my_token}'}
        params = {'id': my_id}
        res = requests.delete(self.base_url + f'users/{my_id}', headers=headers, params=params)
        status = res.status_code
        return status, my_id

    def get_token(self) -> json:
        """Request to retrieve a unique user token for the specified email and password via Swagger"""
        data = {"email": VALID_EMAIL, "password": VALID_PASSWORD}
        res = requests.post(self.base_url + 'login', data=json.dumps(data))
        my_token = res.json()['token']
        my_id = res.json()['id']
        status = res.status_code
        return my_token, status, my_id

    def get_list_users(self):
        my_token = Pets().get_token()[0]
        headers = {'Authorization': f'Bearer {my_token}'}
        res = requests.get(self.base_url + 'users', headers=headers)
        status = res.status_code
        amount = res.json
        return status, amount

    def post_pet(self):
        my_token = Pets().get_token()[0]
        my_id = Pets().get_token()[2]
        headers = {'Authorization': f'Bearer {my_token}'}
        data = {"id": my_id,
                "name": 'AS', "type": 'reptile', "age": 99, "owner_id": my_id}
        res = requests.post(self.base_url + 'pet', data=json.dumps(data), headers=headers)
        pet_id = res.json()['id']
        status = res.status_code
        return pet_id, status

    def get_pet_photo(self):
        my_token = Pets().get_token()[0]
        pet_id = Pets().post_pet()[0]
        headers = {'Authorization': f'Bearer {my_token}'}
        files = {'pic': ('pet.jpg', open('/Users/yuliiapolishchuk/PycharmProjects/PyTestAPI/tests/photo/pet.jpg', 'rb'), 'image/jpg')}
        res = requests.post(self.base_url + f'pet/{pet_id}/image', headers=headers, files=files)
        status = res.status_code
        link = res.json()['link']
        return status, link

    def get_pet_id(self):
        my_token = Pets().get_token()[0]
        pet_id = Pets().post_pet()[0]
        headers = {'Authorization': f'Bearer {my_token}'}
        res = requests.get(self.base_url + f'pet/{pet_id}', headers=headers)
        status = res.status_code
        return status

    def patch_pet(self) -> json:
        my_token = Pets().get_token()[0]
        my_id = Pets().get_token()[2]
        headers = {'Authorization': f'Bearer {my_token}'}
        data = {"id": my_id,
                "name": 'PatchP', "type": 'cat', "age": 11, "gender": "string", "owner_id": my_id,
                 "pic": "string",
                "owner_name": "string", "likes_count": 0, "liked_by_user": True}
        res = requests.patch(self.base_url + 'pet', data=json.dumps(data), headers=headers)
        pet_id = res.json()['id']
        status = res.status_code
        return pet_id, status

    def get_pet_like(self):
        my_token = Pets().get_token()[0]
        pet_id = Pets().post_pet()[0]
        headers = {'Authorization': f'Bearer {my_token}'}
        data = {"id": pet_id}
        res = requests.put(self.base_url + f'pet/{pet_id}/like', data=json.dumps(data), headers=headers)
        status = res.status_code
        return status

    def put_pet_comment(self):
        my_token = Pets().get_token()[0]
        pet_id = Pets().post_pet()[0]
        headers = {'Authorization': f'Bearer {my_token}'}
        data = {"id": 0, "pet_id": 0, "date": "2023-02-04T01:07:25.048Z", "message": "new comment", "user_id": 0,
                "user_name": "string"}
        res = requests.put(self.base_url + f'pet/{pet_id}/comment', data=json.dumps(data), headers=headers)
        status = res.status_code
        return status

    def post_pets_list(self):
        my_token = Pets().get_token()[0]
        my_id = Pets().get_token()[2]
        headers = {'Authorization': f'Bearer {my_token}'}
        data = {"skip": 0, "num": 10, "type": "string", "petName": "string", "user_id": my_id}
        res = requests.post(self.base_url + 'pets', data=json.dumps(data), headers=headers)
        status = res.status_code
        return status

    def delete_pet_id(self):
        my_token = Pets().get_token()[0]
        pet_id = Pets().post_pet()[0]
        headers = {'Authorization': f'Bearer {my_token}'}
        res = requests.delete(self.base_url + f'pet/{pet_id}', headers=headers)
        status = res.status_code
        return status


Pets().get_registered()
Pets().register_and_delete_user()
Pets().get_token()
Pets().get_list_users()
Pets().post_pet()
Pets().get_pet_photo()
Pets().get_pet_id()
Pets().patch_pet()
Pets().get_pet_like()
Pets().put_pet_comment()
Pets().post_pets_list()
Pets().delete_pet_id()
