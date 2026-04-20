def test_unregister_removes_participant(client):
    # Arrange
    activity = "Chess Club"
    email = "michael@mergington.edu"  # existing participant in seed data

    # Act
    response = client.delete(f"/activities/{activity}/participants?email={email}")

    # Assert
    assert response.status_code == 200
    assert response.json()["message"] == f"Removed {email} from {activity}"


def test_unregister_participant_no_longer_in_activity(client):
    # Arrange
    activity = "Chess Club"
    email = "michael@mergington.edu"
    client.delete(f"/activities/{activity}/participants?email={email}")

    # Act
    response = client.get("/activities")
    participants = response.json()[activity]["participants"]

    # Assert
    assert email not in participants


def test_unregister_unknown_activity_returns_404(client):
    # Arrange
    activity = "Nonexistent Club"
    email = "student@mergington.edu"

    # Act
    response = client.delete(f"/activities/{activity}/participants?email={email}")

    # Assert
    assert response.status_code == 404
    assert response.json()["detail"] == "Activity not found"


def test_unregister_nonmember_returns_404(client):
    # Arrange
    activity = "Chess Club"
    email = "not_a_member@mergington.edu"

    # Act
    response = client.delete(f"/activities/{activity}/participants?email={email}")

    # Assert
    assert response.status_code == 404
    assert response.json()["detail"] == "Student is not signed up for this activity"
