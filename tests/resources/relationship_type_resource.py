def test_relationship_type_resource(client):
    # Test List All
    response = client.get("/api/v1/relationship_type")
    assert response.status_code == 200

    TOTAL = response.json["data"]["total"]

    # Test Create New
    FIRST_NAME = "Test"
    response = client.post(
        "/api/v1/relationship_type",
        json={
            "name": FIRST_NAME,
        },
    )
    assert response.status_code == 200
    ID = response.json["data"]["id"]

    response = client.get("/api/v1/relationship_type")
    assert response.status_code == 200

    new_total = response.json["data"]["total"]
    assert TOTAL + 1 == new_total

    # Test Get 1
    response = client.get(f"/api/v1/relationship_type?id={ID}")
    assert response.status_code == 200

    # Test Update
    SECOND_NAME = "Test 2"
    response = client.put(
        "/api/v1/relationship_type",
        json={
            "id": ID,
            "name": SECOND_NAME,
        },
    )
    assert response.status_code == 200

    name = response.json["data"]["name"]
    assert name == SECOND_NAME

    # Test Delete
    response = client.delete(f"/api/v1/relationship_type?id={ID}")
    assert response.status_code == 200

    response = client.get("/api/v1/relationship_type")
    assert response.status_code == 200

    new_total = response.json["data"]["total"]
    assert TOTAL == new_total
