import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from unittest.mock import MagicMock, patch
import pytest
from app import models, schemas
from app.crud import item  # <-- виправлено

class TestItemCRUDUnit:
    def setup_method(self):
        self.mock_db = MagicMock()
        self.fake_item = models.Item(item_id=1, name="Item1")

    def test_get_item(self):
        self.mock_db.query.return_value.filter.return_value.first.return_value = self.fake_item
        result = item.get_item(self.mock_db, 1)
        assert result.name == "Item1"
        assert result.item_id == 1

    def test_create_item(self):
        self.mock_db.add.return_value = None
        self.mock_db.commit.return_value = None
        self.mock_db.refresh.return_value = None

        i_data = schemas.ItemCreate(name="Item1")

        with patch("app.models.Item", return_value=self.fake_item):
            result = item.create_item(self.mock_db, i_data)

        assert result.name == "Item1"
        self.mock_db.add.assert_called_once_with(self.fake_item)
        self.mock_db.commit.assert_called_once()
        self.mock_db.refresh.assert_called_once_with(self.fake_item)

    def test_update_item(self):
        with patch("app.crud.item.get_item", return_value=self.fake_item):
            i_data = schemas.ItemCreate(name="ItemUpdated")
            result = item.update_item(self.mock_db, 1, i_data)

        assert result.name == "ItemUpdated"
        self.mock_db.commit.assert_called_once()

    def test_delete_item(self):
        with patch("app.crud.item.get_item", return_value=self.fake_item):
            deleted_item = item.delete_item(self.mock_db, 1)

        self.mock_db.delete.assert_called_once_with(self.fake_item)
        self.mock_db.commit.assert_called_once()
        assert deleted_item == self.fake_item
