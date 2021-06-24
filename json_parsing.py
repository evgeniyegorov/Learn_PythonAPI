import requests
#
# response = requests.post("https://playground.learnqa.ru/api/get_301", allow_redirects=True)
# firs_response = response.history[0]
# second_response = response
#
# print(firs_response.url)
# print(second_response.url)
#
#
# headers = {"some_header": "123"}
# response = requests.get("https://playground.learnqa.ru/api/show_all_headers", headers = headers)
# print(response.text)
# print(response.headers)


payload = {"login": "secret_login", "password": "secret_pass1"}
response1 = requests.post("https://playground.learnqa.ru/api/get_auth_cookie", data=payload)

cookie_value = response1.cookies.get('auth_cookie')

cookies = {}
if cookie_value is not None:
    cookies.update({'auth_cookie': cookie_value})


response2 = requests.post("https://playground.learnqa.ru/api/check_auth_cookie", cookies=cookies)

print(response2.text)


