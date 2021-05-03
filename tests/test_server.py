from starlette.testclient import TestClient

from server import app

client = TestClient(app=app, base_url="http://127.0.0.1:8000")

user = {
    "id": "12345678",
    "password": "1234",
    "p_ars": "5678",
}

option = {
    "headless": True,
    "commit": True
}

purchases = (
    {"racecourse": "tokyo", "type": "複勝", "horse_numbers": [1], "price": 100},
    {"racecourse": "nakayama", "type": "単勝", "horse_numbers": [2], "price": 200},
)


def test_deposit():
    response = client.post(
        "/deposit",
        json={
            "user": user,
            "amount": 1000,
            "option": option
        }
    )
    print(response.json())
    assert response.status_code == 201


def test_buy():
    response = client.post(
        "/buy",
        json={
            "user": user,
            "purchases": purchases,
            "option": option
        }
    )
    print(response.json())
    assert response.status_code == 201
