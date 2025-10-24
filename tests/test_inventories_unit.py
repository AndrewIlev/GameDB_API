from unittest.mock import MagicMock
from app.crud import inventory
from app import models, schemas

class TestInventoryCRUDUnit:
    def setup_method(self):
        self.mock_db = MagicMock()
        self.fake_inventory = models.Inventory(player_id=1, item_id=1, quantity=5)

    def test_get_inventory(self):
        self.mock_db.query.return_value.filter.return_value.first.return_value = self.fake_inventory
        inv = inventory.get_inventory(self.mock_db, 1, 1)
        assert inv.quantity == 5

    def test_create_inventory(self):
        self.mock_db.add.return_value = None
        self.mock_db.commit.return_value = None
        self.mock_db.refresh.return_value = None
        inv_data = schemas.InventoryCreate(player_id=1, item_id=1, quantity=5)
        inv = inventory.create_inventory(self.mock_db, inv_data)
        assert inv.quantity == 5

    def test_update_inventory(self):
        inventory.get_inventory = MagicMock(return_value=self.fake_inventory)
        inv_data = schemas.InventoryCreate(player_id=1, item_id=1, quantity=10)
        inv = inventory.update_inventory(self.mock_db, 1, 1, inv_data)
        assert inv.quantity == 10

    def test_delete_inventory(self):
        inventory.get_inventory = MagicMock(return_value=self.fake_inventory)
        inventory.delete_inventory(self.mock_db, 1, 1)
        self.mock_db.delete.assert_called_once_with(self.fake_inventory)
        self.mock_db.commit.assert_called_once()
