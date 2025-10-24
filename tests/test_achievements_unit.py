from unittest.mock import MagicMock
from app.crud import achievement
from app import models, schemas

class TestAchievementCRUDUnit:
    def setup_method(self):
        self.mock_db = MagicMock()
        self.fake_achievement = models.Achievement(achievement_id=1, name="Achieve1")

    def test_get_achievement(self):
        self.mock_db.query.return_value.filter.return_value.first.return_value = self.fake_achievement
        a = achievement.get_achievement(self.mock_db, 1)
        assert a.name == "Achieve1"

    def test_create_achievement(self):
        self.mock_db.add.return_value = None
        self.mock_db.commit.return_value = None
        self.mock_db.refresh.return_value = None
        a_data = schemas.AchievementCreate(name="Achieve1")
        a = achievement.create_achievement(self.mock_db, a_data)
        assert a.name == "Achieve1"

    def test_update_achievement(self):
        achievement.get_achievement = MagicMock(return_value=self.fake_achievement)
        a_data = schemas.AchievementCreate(name="AchieveUpdated")
        a = achievement.update_achievement(self.mock_db, 1, a_data)
        assert a.name == "AchieveUpdated"

    def test_delete_achievement(self):
        achievement.get_achievement = MagicMock(return_value=self.fake_achievement)
        achievement.delete_achievement(self.mock_db, 1)
        self.mock_db.delete.assert_called_once_with(self.fake_achievement)
        self.mock_db.commit.assert_called_once()
