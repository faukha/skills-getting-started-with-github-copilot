def test_signup_adds_participant(client):
    # Arrange
    activity = "Chess Club"
    email = "new_student@mergington.edu"

    # Act
    response = client.post(f"/activities/{activity}/signup?email={email}")

    # Assert
    assert response.status_code == 200
    assert response.json()["message"] == f"Signed up {email} for {activity}"


def test_signup_participant_appears_in_activity(client):
    # Arrange
    activity = "Chess Club"
    email = "new_student@mergington.edu"
    client.post(f"/activities/{activity}/signup?email={email}")

    # Act
    response = client.get("/activities")
    participants = response.json()[activity]["participants"]

    # Assert
    assert email in participants


def test_signup_unknown_activity_returns_404(client):
    # Arrange
    activity = "Nonexistent Club"
    email = "student@mergington.edu"

    # Act
    response = client.post(f"/activities/{activity}/signup?email={email}")

    # Assert
    assert response.status_code == 404
    assert response.json()["detail"] == "Activity not found"


def test_signup_duplicate_returns_400(client):
    # Arrange
    activity = "Chess Club"
    email = "michael@mergington.edu"  # already a participant in seed data

    # Act
    response = client.post(f"/activities/{activity}/signup?email={email}")

    # Assert
    assert response.status_code == 400
    assert response.json()["detail"] == "Student is already signed up for this activity"
