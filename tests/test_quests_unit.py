from unittest.mock import MagicMock
from app.crud import quest
from app import models, schemas

class TestQuestCRUDUnit:
    def setup_method(self):
        self.mock_db = MagicMock()
        self.fake_quest = models.Quest(quest_id=1, title="Quest1")

    def test_get_quest(self):
        self.mock_db.query.return_value.filter.return_value.first.return_value = self.fake_quest
        q = quest.get_quest(self.mock_db, 1)
        assert q.title == "Quest1"

    def test_create_quest(self):
        self.mock_db.add.return_value = None
        self.mock_db.commit.return_value = None
        self.mock_db.refresh.return_value = None
        q_data = schemas.QuestCreate(title="Quest1")
        q = quest.create_quest(self.mock_db, q_data)
        assert q.title == "Quest1"

    def test_update_quest(self):
        quest.get_quest = MagicMock(return_value=self.fake_quest)
        q_data = schemas.QuestCreate(title="QuestUpdated")
        q = quest.update_quest(self.mock_db, 1, q_data)
        assert q.title == "QuestUpdated"

    def test_delete_quest(self):
        quest.get_quest = MagicMock(return_value=self.fake_quest)
        quest.delete_quest(self.mock_db, 1)
        self.mock_db.delete.assert_called_once_with(self.fake_quest)
        self.mock_db.commit.assert_called_once()
