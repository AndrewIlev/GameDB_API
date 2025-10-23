import pytest
from fastapi.testclient import TestClient
from app.main import app
from app.database import Base, engine, SessionLocal
from app import database, models

# Створюємо тестову БД
Base.metadata.create_all(bind=engine)
client = TestClient(app)

def override_get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

app.dependency_overrides[database.get_db] = override_get_db

# Тести CRUD для Player

def test_create_player():
    response = client.post(
        "/players/",
        json={
            "login": "integration_login",
            "nickname": "integration_nick",
            "email": "integration@example.com",
            "level": 1,
            "xp": 0,
            "guild_id": None
        }
    )
    assert response.status_code == 200
    data = response.json()
    assert data["login"] == "integration_login"
    assert data["nickname"] == "integration_nick"

def test_read_players():
    response = client.get("/players/")
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, list)

def test_read_player_by_id():
    # Спершу створюємо гравця
    response_create = client.post(
        "/players/",
        json={
            "login": "read_test",
            "nickname": "read_nick",
            "email": "read@example.com",
            "level": 1,
            "xp": 0,
            "guild_id": None
        }
    )
    player_id = response_create.json()["player_id"]
    response = client.get(f"/players/{player_id}")
    assert response.status_code == 200
    data = response.json()
    assert data["player_id"] == player_id
    assert data["login"] == "read_test"

def test_update_player():
    response_create = client.post(
        "/players/",
        json={
            "login": "update_test",
            "nickname": "update_nick",
            "email": "update@example.com",
            "level": 1,
            "xp": 0,
            "guild_id": None
        }
    )
    player_id = response_create.json()["player_id"]
    response = client.put(
        f"/players/{player_id}",
        json={
            "login": "updated_login",
            "nickname": "updated_nick",
            "email": "updated@example.com",
            "level": 2,
            "xp": 10,
            "guild_id": None
        }
    )
    assert response.status_code == 200
    data = response.json()
    assert data["login"] == "updated_login"
    assert data["level"] == 2

def test_delete_player():
    response_create = client.post(
        "/players/",
        json={
            "login": "delete_test",
            "nickname": "delete_nick",
            "email": "delete@example.com",
            "level": 1,
            "xp": 0,
            "guild_id": None
        }
    )
    player_id = response_create.json()["player_id"]
    response = client.delete(f"/players/{player_id}")
    assert response.status_code == 200
    # Після видалення перевіримо, що гравця немає
    response_get = client.get(f"/players/{player_id}")
    assert response_get.status_code == 404
