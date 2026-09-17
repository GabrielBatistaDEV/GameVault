from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


def test_criar_game():
    response = client.post(
        "/games/",
        json={
            "titulo": "God of War",
            "descricao": "Jogo de ação e aventura",
            "nota": 9.5,
            "plataforma": "PC",
            "data_conclusao": "2026-09-15",
        },
    )

    assert response.status_code == 200

    data = response.json()

    assert data["titulo"] == "God of War"
    assert data["nota"] == 9.5


def test_listar_games():
    response = client.get("/games/")

    assert response.status_code == 200
    assert isinstance(response.json(), list)


def test_buscar_game():
    response = client.post(
        "/games/",
        json={
            "titulo": "Minecraft",
            "nota": 8,
            "plataforma": "PC",
        },
    )

    game_id = response.json()["id"]

    response = client.get(f"/games/{game_id}")

    assert response.status_code == 200
    assert response.json()["titulo"] == "Minecraft"


def test_atualizar_game():
    response = client.post(
        "/games/",
        json={
            "titulo": "Resident Evil 4",
            "nota": 9,
            "plataforma": "PC",
        },
    )

    game_id = response.json()["id"]

    response = client.put(
        f"/games/{game_id}",
        json={
            "titulo": "Resident Evil 4 Remake",
            "nota": 10,
            "plataforma": "PC",
        },
    )

    assert response.status_code == 200
    assert response.json()["titulo"] == "Resident Evil 4 Remake"
    assert response.json()["nota"] == 10


def test_deletar_game():
    response = client.post(
        "/games/",
        json={
            "titulo": "Jogo para excluir",
            "nota": 5,
            "plataforma": "PC",
        },
    )

    game_id = response.json()["id"]

    response = client.delete(f"/games/{game_id}")

    assert response.status_code == 200

    response = client.get(f"/games/{game_id}")

    assert response.status_code == 404