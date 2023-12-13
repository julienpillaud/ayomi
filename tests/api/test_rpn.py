from fastapi import status
from fastapi.testclient import TestClient


def test_evaluate_rpn_invalid_input(client: TestClient) -> None:
    json_data = {"elements": "1"}
    response = client.post("/rpn", json=json_data)
    assert response.status_code == status.HTTP_422_UNPROCESSABLE_ENTITY


def test_evaluate_rpn_wrong_input(client: TestClient) -> None:
    json_data = {"elements": ["1", "2"]}
    response = client.post("/rpn", json=json_data)
    assert response.status_code == status.HTTP_400_BAD_REQUEST


def test_evaluate_rpn(client: TestClient) -> None:
    json_data = {"elements": ["1", "2", "+"]}
    response = client.post("/rpn", json=json_data)
    data = response.json()

    assert response.status_code == status.HTTP_200_OK
    assert data["elements"] == json_data["elements"]
    assert data["result"] == 3
