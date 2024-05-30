import requests
import test_config
import pytest

endpoint = "secure/user"
url = test_config.base_url + endpoint


# def test_get_secure_user():
#     """
#     Test Scenario 1: Getting all user
#     """
#
#     header = {
#
#         "Authorization": test_config.authorization}
#     # Make the GET request
#     response = requests.get(url, headers=header)
#     print(f'{response.json()=}')
#     assert response.status_code == test_config.status_code_ok
#     # Assert that the response body is not empty
#     assert response.text != ""
#     # Check for the presence of security headers
#     assert "Content-Security-Policy" in response.headers
#     assert "X-Content-Type-Options" in response.headers
#     print(f'{response.headers=}')

#HTTPS/TLS Testing
# def test_create_user():
#     endpoint = "/secure/user"
#     # Given
#     payload = {
#         "given_name": "John",
#         "family_name": "Doe",
#         "blocked": False,
#         "email": "john.doe@example.com",
#         "email_name": "john.doe",
#         "email_domain": "example.com",
#         "title": "Software Engineer",
#         "phone": "123-456-7890",
#         "role_ids": [1, 2],
#         "provision_salesforce_user": False,
#         "send_reset_password": True
#     }
#
#     # When
#     response = requests.post(test_config.base_url + endpoint, json=payload)
#     # Then
#     assert response.status_code == 200
#     assert response.json()["id"] is not None
#     assert response.json()["given_name"] == "John"
#     assert response.json()["family_name"] == "Doe"
#     assert response.json()["blocked"] == False
#     assert response.json()["email"] == "john.doe@example.com"
#     assert response.json()["email_name"] == "john.doe"
#     assert response.json()["email_domain"] == "example.com"
#     assert response.json()["title"] == "Software Engineer"
#     assert response.json()["phone"] == "123-456-7890"
#     assert response.json()["role_ids"] == [1, 2]
#     assert response.json()["provision_salesforce_user"] == False
#     assert response.json()["send_reset_password"] == True
#
#
# def test_token_security():
#     # Attempt to access the same endpoint with an expired token
#     headers = {'Authorization': 'Bearer expired_token'}
#     token_response = requests.get(url, headers=headers)
#     # Expect the request to fail
#     assert token_response.status_code == test_config.unauthorized_code
#
#
# def test_get_users_invalid_email():
#     invalid_response = requests.get(url, params={"email": "invalid"})
#     assert invalid_response.status_code == test_config.bad_request_code
#     print(f'{invalid_response.json()=}')
#
#
# def test_get_users_missing_parameter():
#     missing_response = requests.get(url)
#     assert missing_response.status_code == test_config.bad_request_code

#Session Management:
def test_secure_user_post():
    header = {

                 "Authorization": test_config.authorization}
    # Define the request body
    request_body = {
        "given_name": "John",
        "family_name": "Doe",
        "blocked": False,
        "email": "john.doe@example.com",
        "email_name": "john.doe",
        "email_domain": "example.com",
        "title": "Software Engineer",
        "phone": "555-123-4567",
        "role_ids": [1, 2],
        "provision_salesforce_user": True,
        "send_reset_password": True
    }

    # Make the POST request
    response = requests.post(url, json=request_body,headers=header)

    # Assert that the response status code is 200 OK
    assert response.status_code == test_config.status_code_ok

    # Assert that the response body is as expected
    assert response.json() == {
        "id": 1,
        "given_name": "John",
        "family_name": "Doe",
        "blocked": False,
        "email": "john.doe@example.com",
        "email_name": "john.doe",
        "email_domain": "example.com",
        "title": "Software Engineer",
        "phone": "555-123-4567",
        "role_ids": [1, 2],
        "provision_salesforce_user": True
    }

    # Assert that the session cookie is set
    assert "session_id" in response.cookies

    # Assert that the session cookie is secure and HttpOnly
    assert response.cookies["session_id"]["secure"]
    assert response.cookies["session_id"]["httponly"]
