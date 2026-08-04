from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_get_home_returns_200():
    response = client.get("/")
    assert response.status_code == 200

def test_post_generate_team_returns_200():
    response = client.post(
        "/teams/generate",
        json={
            "club_name": "FC Test",
            "country": "England",
            "league": "Premier League",
            "budget": 50000000,
            "formation": "4-3-3",
            "playing_style": "Possession",
        },
    )

    assert response.status_code == 200
    data = response.json()

    assert "name" in data
    assert "manager" in data
    assert "players" in data
    assert len(data["players"]) == 11


def test_post_generate_team_without_body_returns_200():
    response = client.post("/teams/generate")

    assert response.status_code == 200
    data = response.json()

    assert "name" in data
    assert "manager" in data
    assert "players" in data
    assert len(data["players"]) == 11

def test_invalid_formation_returns_error():
    response = client.post(
        "/teams/generate",
        json={
            "club_name": "FC Test",
            "country": "England",
            "league": "Premier League",
            "budget": 50000000,
            "formation": "9-9-9",
            "playing_style": "Possession",
        },
    )

    assert response.status_code in [400, 422]

def test_missing_country_returns_422():
    response = client.post(
        "/teams/generate",
        json={
            "club_name": "FC Test",
            "league": "Premier League",
            "budget": 50000000,
            "formation": "4-3-3",
            "playing_style": "Possession",
        },
    )

    assert response.status_code == 422

def test_negative_budget_returns_422():
    response = client.post(
        "/teams/generate",
        json={
            "club_name": "FC Test",
            "country": "England",
            "league": "Premier League",
            "budget": -1,
            "formation": "4-3-3",
            "playing_style": "Possession",
        },
    )

    assert response.status_code == 422