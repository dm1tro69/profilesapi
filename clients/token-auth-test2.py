import requests


def client():
    token_h = 'Token 09e245c7346edb6b052f7a53417c7af1729b75b2'
    headers = {'Authorization': token_h}
    credentials = {"username": "username", "password": "D15067373"}
    response = requests.get("http://127.0.0.1:8000/api/profiles/",
                             headers=headers)
    # data = {'username': 'username', 'email': 'test@mail.com', 'password1': 'D15067373', 'password2': 'D15067373'}
    # response = requests.post('http://127.0.0.1:8000/api/rest-auth/registration/', data=data)
    # # #
    # # print('Status code:', response.status_code)
    # # response_data = response.json()
    # # print(response_data)
    # headers = {'Authorization': token_h}
    # response = requests.get("http://127.0.0.1:8000/api/profiles", headers=headers)
    print("Status Code: ", response.status_code)

    response_data = response.json()
    print(response_data)


if __name__ == '__main__':
    client()
