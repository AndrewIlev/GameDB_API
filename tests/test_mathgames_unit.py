import pytest
from unittest.mock import MagicMock
from app import crud, models, schemas

class TestMathGameCRUDUnit:
    def setup_method(self):
        self.mock_db = MagicMock()
        self.fake_mathgame = models.MathGame(
            match_id=1,
            match_date="2025-10-24",
            match_type="Easy",
            result="Win"
        )

    def test_get_mathgame(self):
        self.mock_db.query().filter().first.return_value = self.fake_mathgame
        mathgame = crud.mathgame.get_mathgame(self.mock_db, 1)
        assert mathgame.match_id == 1

    def test_create_mathgame(self):
        self.mock_db.add.return_value = None
        self.mock_db.commit.return_value = None
        self.mock_db.refresh.return_value = None
        mathgame_data = schemas.MathGameCreate(
            match_date="2025-10-24",
            match_type="Easy",
            result="Win"
        )
        mathgame = crud.mathgame.create_mathgame(self.mock_db, mathgame_data)
        assert mathgame is not None

    def test_update_mathgame(self):
        self.mock_db.query().filter().first.return_value = self.fake_mathgame
        mathgame_data = schemas.MathGameCreate(
            match_date="2025-10-25",
            match_type="Hard",
            result="Lose"
        )
        updated = crud.mathgame.update_mathgame(self.mock_db, 1, mathgame_data)
        assert updated.match_date == "2025-10-25"

    def test_delete_mathgame(self):
        self.mock_db.query().filter().first.return_value = self.fake_mathgame
        deleted = crud.mathgame.delete_mathgame(self.mock_db, 1)
        assert deleted.match_id == 1
