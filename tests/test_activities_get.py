def test_get_activities_returns_200(client):
    # Arrange – client fixture provides a ready TestClient

    # Act
    response = client.get("/activities")

    # Assert
    assert response.status_code == 200


def test_get_activities_returns_dict_keyed_by_name(client):
    # Arrange
    expected_key = "Chess Club"

    # Act
    response = client.get("/activities")
    data = response.json()

    # Assert
    assert expected_key in data


def test_get_activities_each_entry_has_required_fields(client):
    # Arrange
    required_fields = {"description", "schedule", "max_participants", "participants"}

    # Act
    response = client.get("/activities")
    data = response.json()

    # Assert
    for activity in data.values():
        assert required_fields.issubset(activity.keys())
