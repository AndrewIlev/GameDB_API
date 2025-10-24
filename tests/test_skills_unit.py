from unittest.mock import MagicMock
from app.crud import skill
from app import models, schemas

class TestSkillCRUDUnit:
    def setup_method(self):
        self.mock_db = MagicMock()
        self.fake_skill = models.Skill(skill_id=1, name="Skill1")

    def test_get_skill(self):
        self.mock_db.query.return_value.filter.return_value.first.return_value = self.fake_skill
        s = skill.get_skill(self.mock_db, 1)
        assert s.name == "Skill1"

    def test_create_skill(self):
        self.mock_db.add.return_value = None
        self.mock_db.commit.return_value = None
        self.mock_db.refresh.return_value = None
        s_data = schemas.SkillCreate(name="Skill1")
        s = skill.create_skill(self.mock_db, s_data)
        assert s.name == "Skill1"

    def test_update_skill(self):
        skill.get_skill = MagicMock(return_value=self.fake_skill)
        s_data = schemas.SkillCreate(name="SkillUpdated")
        s = skill.update_skill(self.mock_db, 1, s_data)
        assert s.name == "SkillUpdated"

    def test_delete_skill(self):
        skill.get_skill = MagicMock(return_value=self.fake_skill)
        skill.delete_skill(self.mock_db, 1)
        self.mock_db.delete.assert_called_once_with(self.fake_skill)
        self.mock_db.commit.assert_called_once()
