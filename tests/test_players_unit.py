from unittest.mock import MagicMock
from app import crud, models

class TestPlayerCRUDUnit:
    def setup_method(self):
        self.mock_db = MagicMock()

    def test_get_player(self):
        fake_player = models.Player(
            player_id=1,
            login="login",
            nickname="nick",
            email="email@example.com"
        )

        query_mock = self.mock_db.query.return_value
        filter_mock = query_mock.filter.return_value
        filter_mock.first.return_value = fake_player

        player = crud.player.get_player(self.mock_db, 1)

        assert player.nickname == "nick"
        assert player.login == "login"
