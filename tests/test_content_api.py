from fastapi.testclient import TestClient

from src.table_data.table_data_controller import router

test_client = TestClient(router)

def test_given_valid_id_return_valid_table_data_with_200():
    valid_id = 25
    response = test_client.get(f"/tabledata/get/{valid_id}")
    assert response.status_code == 200
    assert response.json()['id']==str(valid_id)

def test_given_non_existing_id_return_null_with_204():
    invalid_id=0
    response = test_client.get(f"/tabledata/get/{invalid_id}")
    assert response.status_code == 204
    assert response.json() == null


def test_all_endpoint_return_with_200():
    response = test_client.get(f"/tabledata/get/all")
    assert response.status_code == 200
    assert isinstance(response.json(),list)
