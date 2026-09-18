from fastapi.testclient import TestClient

from src.app import app

client = TestClient(app)


def test_unregister_participant_from_activity():
    # Arrange
    activity_name = "Chess Club"
    email = "newstudent@mergington.edu"
    if email not in client.get("/activities").json()[activity_name]["participants"]:
        response = client.post(f"/activities/{activity_name}/signup?email={email}")
        assert response.status_code == 200

    # Act
    response = client.delete(f"/activities/{activity_name}/participants?email={email}")

    # Assert
    assert response.status_code == 200
    assert email not in client.get("/activities").json()[activity_name]["participants"]


def test_unregister_missing_participant_returns_404():
    # Arrange
    activity_name = "Chess Club"
    email = "does-not-exist@mergington.edu"

    # Act
    response = client.delete(f"/activities/{activity_name}/participants?email={email}")

    # Assert
    assert response.status_code == 404
