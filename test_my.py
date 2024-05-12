from fastapi import FastAPI
from fastapi.testclient import TestClient

from manage import app


client = TestClient(app)

def test_create_film():
    film_data = {
        "name": "Sample Film",
        "year": 2023,
        "tags": "Adventure",
        "rating": 8
    }
    response = client.post("/film/", json=film_data)
    assert response.status_code == 200
    assert response.json()["name"] == "Sample Film"

def test_get_films():
    response = client.get("/film/")
    assert response.status_code == 200
    # Add more assertions based on the expected response for get_films endpoint

def test_get_film():
    film_id = 2  # Replace with an actual film ID
    response = client.get(f"/film/{film_id}")
    assert response.status_code == 200
    # Add more assertions based on the expected response for get_film endpoint

def test_update_film():
    film_id = 3  # Replace with an actual film ID
    updated_film_data = {
        "name": "qwertyuiop",
        "year": 2020,
        "tags": "Adventure",
        "rating": 11
    }
    response = client.put(f"/film/{film_id}", json=updated_film_data)
    assert response.status_code == 200
    assert response.json()["name"] == "qwertyuiop"

def test_delete_film():
    film_id = 2  # Replace with an actual film ID
    response = client.delete(f"/film/{film_id}")
    assert response.status_code == 200
    # Add more assertions based on the expected response for delete_film endpoint


    # pytest [name_python_file_with_test]::[name_function_for_test] ->>>>>>> pytest test_my.py::test_get_film   
