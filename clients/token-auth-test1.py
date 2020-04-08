import requests


def client():
    token_h = 'Token 507c9e60e13d417655f01ceb5b2d09ef21f36796'
    # credentials = {"username": "admin", "password": "D15067373"}
    # response = requests.post("http://127.0.0.1:8000/api/rest-auth/login/",
    #                           data=credentials)
    # credentials = {'username': 'admin', 'password': 'D15067373'}
    # response = requests.post('http://127.0.0.1:8000/api/rest-auth/login/', data=credentials)
    #
    # print('Status code:', response.status_code)
    # response_data = response.json()
    # print(response_data)
    headers = {'Authorization': token_h}
    response = requests.get("http://127.0.0.1:8000/api/profiles", headers=headers)
    print("Status Code: ", response.status_code)

    response_data = response.json()
    print(response_data)


if __name__ == '__main__':
    client()
