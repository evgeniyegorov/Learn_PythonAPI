import requests
import pytest
from lib.bas_case import BaseCase


class TestUserAuth(BaseCase):

    exclude_params = [
        ("no_cookie"),
        ("no_token")
    ]

    def setup(self):
        data = {
            'email': 'vinkotov@example.com',
            'password': '1234'
        }

        user_login_url = "https://playground.learnqa.ru/api/user/login"

        response1 = requests.post(user_login_url, data=data)

        assert "auth_sid" in response1.cookies, "There is not auth cookie in the response"
        assert "x-csrf-token" in response1.headers, "There is no CRSF token header in the response"
        assert "user_id" in response1.json(), "There is no user id in the response"

        self.auth_sid = response1.cookies.get("auth_sid")
        self.token = response1.headers.get("x-csrf-token")
        self.user_id_from_auth_method = response1.json()["user_id"]

    def test_auth_user(self):

        user_auth_url = "https://playground.learnqa.ru/api/user/auth"

        response2 = requests.get(user_auth_url,
                                 headers={"x-csrf-token": self.token},
                                 cookies={"auth_sid": self.auth_sid}
                                 )
        
        assert "user_id" in response2.json(), "There is no user id in the second response"

        user_id_from_check_method = response2.json()["user_id"]

        assert self.user_id_from_auth_method == user_id_from_check_method, "User id from auth method is not equal to user id from chek method"

    @pytest.mark.parametrize('condition', exclude_params)
    def test_negative_auth_check(self, condition):

        user_auth_url = "https://playground.learnqa.ru/api/user/auth"

        if condition == "no_cookie":
            response2 = requests.get(
                user_auth_url,
                headers={"x-csrf-token": self.token}
            )
        else:
            response2 = requests.get(
                user_auth_url,
                cookies={"auth_sid": self.auth_sid}
            )

        # assert "user_id" in self.response2.json(), "There is no user id in the second response"

        user_id_from_chek_method = response2.json()["user_id"]

        assert user_id_from_chek_method == 0, f"User is authorized with condition {condition}"



