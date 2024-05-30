import requests
import test_config

endpoint = "secure/account/users"
url = test_config.base_url + endpoint


def test_get_secure_account_users():
    """
    Test Scenario 1: Getting all secure account users
    """

    header = {

        "Authorization": test_config.authorization}
    # Make the GET request
    response = requests.get(url, headers=header)
    print(response.json())
    assert response.status_code == test_config.status_code_ok

    # Assert that the response body is not empty
    assert response.text != ""
    # Check for the presence of security headers
    assert "Content-Security-Policy" in response.headers
    assert "X-Content-Type-Options" in response.headers
    print(f'{response.headers=}')


def test_patch_secure_account_user():
    # Replace with your auth0_user_id
    endpoint = "secure/account/user/" + test_config.auth0_user_id
    print("url ", endpoint)
    header = {

        "Authorization": test_config.authorization}
    request_body = {
        "given_name": "Shilpa",
        "family_name": "Shahpurkar1",
        "blocked": False,
        "email": "sshahpurkar@npifinancial.com",
        "email_name": "shilpa",
        "email_domain": "string",
        "title": "string",
        "phone": "string",
        "role_ids": [1, 2, 3, 4, 5, 6, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21]
    }

    response = requests.patch(test_config.base_url + endpoint, json=request_body, headers=header)
    # Print the response
    patch_response_json = response.json()
    print(f'{patch_response_json=}')
    assert response.status_code == test_config.status_code_ok
    assert isinstance(response.json(), dict)

    # Assert that the response body contains the updated user information
    assert response.json()["given_name"] == request_body["given_name"]
    assert response.json()["family_name"] == request_body["family_name"]
    assert response.json()["blocked"] == request_body["blocked"]
    assert response.json()["email"] == request_body["email"]
    assert response.json()['user_metadata']["title"] == request_body["title"]
    assert response.json()['user_metadata']["phone"] == request_body["phone"]


# assert set(response.json()['user_metadata']["role_ids"]) == set(request_body["role_ids"])


def test_token_security():
    # Attempt to access the same endpoint with an expired token
    headers = {'Authorization': 'Bearer expired_token'}
    token_response = requests.get(url, headers=headers)
    # Expect the request to fail
    assert token_response.status_code == test_config.unauthorized_code


def test_get_users_invalid_email():
    invalid_response = requests.get(url, params={"email": "invalid"})
    assert invalid_response.status_code == test_config.bad_request_code
    print(f'{invalid_response.json()=}')


def test_get_users_missing_parameter():
    missing_response = requests.get(url)
    assert missing_response.status_code == test_config.bad_request_code


#Insecure Direct Object References (IDOR)
def test_check_unauthorized_access():
    # First, make a request to the API to get the list of users.
    header = {

        "Authorization": test_config.authorization}
    # Make the GET request
    response = requests.get(url, headers=header)

    # Check that the response is successful.
    assert response.status_code == test_config.status_code_ok

    # Get the list of users from the response.
    users = response.json()

    # Now, try to make a request to update one of the users using a
    # different user ID.
    response = requests.put(test_config.base_url + "secure/account/users/1", data={"given_name": "New Name"})

    # Check that the request is unauthorized.
    assert response.status_code == test_config.bad_request_code
