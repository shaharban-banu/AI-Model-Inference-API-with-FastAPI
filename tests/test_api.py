import sys
import os

# add project root to Python path
sys.path.append(os.path.dirname(os.path.dirname(__file__)))


from fastapi.testclient import TestClient
from main import app

client = TestClient(app)


def test_register():

    response = client.post(
        "/register",
        json={
            "username": "testuser",
            "password": "1234"
        }
    )

    assert response.status_code == 200


def test_login():

    # make sure user exists
    client.post(
        "/register",
        json={
            "username": "loginuser",
            "password": "1234"
        }
    )

    response = client.post(
        "/login",
        json={
            "username": "loginuser",
            "password": "1234"
        }
    )

    assert response.status_code == 200
    assert "access_token" in response.json()


def test_predict():

    # register user
    client.post(
        "/register",
        json={
            "username": "predictuser",
            "password": "1234"
        }
    )

    # login user
    login_response = client.post(
        "/login",
        json={
            "username": "predictuser",
            "password": "1234"
        }
    )

    token = login_response.json()["access_token"]

    # call predict endpoint with token
    response = client.post(
        f"/predict?token={token}",
        json={
            "text": "good product"
        }
    )

    assert response.status_code == 200
    assert "prediction" in response.json()