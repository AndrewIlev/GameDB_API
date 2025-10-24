import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from unittest.mock import MagicMock
import pytest
from app.crud.player import get_player, create_player, update_player, delete_player
from app import models, schemas


class TestPlayerCRUDUnit:
    def setup_method(self):
        self.mock_db = MagicMock()
        self.fake_player = models.Player(
            player_id=1,
            login="login",
            nickname="nick",
            email="email@example.com"
        )
        self.player_data = schemas.PlayerCreate(
            login="login",
            nickname="nick",
            email="email@example.com"
        )

    def test_get_player(self):
        query_mock = self.mock_db.query.return_value
        filter_mock = query_mock.filter.return_value
        filter_mock.first.return_value = self.fake_player

        player = get_player(self.mock_db, 1)

        assert player.nickname == "nick"
        assert player.login == "login"

    def test_create_player(self):
        self.mock_db.add.return_value = None
        self.mock_db.commit.return_value = None
        self.mock_db.refresh.return_value = None

        created_player = create_player(self.mock_db, self.player_data)

        self.mock_db.add.assert_called_once()
        self.mock_db.commit.assert_called_once()
        self.mock_db.refresh.assert_called_once()
        assert created_player.login == "login"

    def test_update_player(self):
        from app.crud import player as player_crud
        player_crud.get_player = MagicMock(return_value=self.fake_player)

        update_data = schemas.PlayerCreate(
            login="login",
            nickname="updated_nick",
            email="email@example.com"
        )

        updated_player = update_player(self.mock_db, 1, update_data)

        assert updated_player.nickname == "updated_nick"
        player_crud.get_player.assert_called_once_with(self.mock_db, 1)

    def test_delete_player(self):
        from app.crud import player as player_crud
        player_crud.get_player = MagicMock(return_value=self.fake_player)

        delete_player(self.mock_db, 1)

        self.mock_db.delete.assert_called_once_with(self.fake_player)
        self.mock_db.commit.assert_called_once()

