from unittest.mock import MagicMock
import pytest
from app.crud import guild
from app import models, schemas

class TestGuildCRUDUnit:
    def setup_method(self):
        self.mock_db = MagicMock()
        self.fake_guild = models.Guild(guild_id=1, name="Guild1")

    def test_get_guild(self):
        query_mock = self.mock_db.query.return_value
        query_mock.filter.return_value.first.return_value = self.fake_guild
        g = guild.get_guild(self.mock_db, 1)
        assert g.name == "Guild1"

    def test_create_guild(self):
        self.mock_db.add.return_value = None
        self.mock_db.commit.return_value = None
        self.mock_db.refresh.return_value = None

        g_data = schemas.GuildCreate(name="Guild1")
        g = guild.create_guild(self.mock_db, g_data)
        self.mock_db.add.assert_called_once()
        self.mock_db.commit.assert_called_once()
        self.mock_db.refresh.assert_called_once()
        assert g.name == "Guild1"

    def test_update_guild(self):
        guild.get_guild = MagicMock(return_value=self.fake_guild)
        g_data = schemas.GuildCreate(name="GuildUpdated")
        g = guild.update_guild(self.mock_db, 1, g_data)
        assert g.name == "GuildUpdated"

    def test_delete_guild(self):
        guild.get_guild = MagicMock(return_value=self.fake_guild)
        guild.delete_guild(self.mock_db, 1)
        self.mock_db.delete.assert_called_once_with(self.fake_guild)
        self.mock_db.commit.assert_called_once()
