import unittest
from myapp.models import Product
from tests.factories import ProductFactory

class TestProductModel(unittest.TestCase):
    def setUp(self):
        self.product = ProductFactory()

    def test_read_product(self):
        self.assertIsInstance(self.product, Product)

    def test_update_product(self):
        new_name = "Updated Name"
        self.product.name = new_name
        self.assertEqual(self.product.name, new_name)

    def test_delete_product(self):
        product_id = self.product.id
        del self.product
        self.assertNotEqual(product_id, None)

    def test_list_all_products(self):
        products = [ProductFactory() for _ in range(5)]
        self.assertEqual(len(products), 5)

    def test_find_by_name(self):
        name = "UniqueProduct"
        product = ProductFactory(name=name)
        self.assertEqual(product.name, name)

    def test_find_by_category(self):
        category = "Electronics"
        product = ProductFactory(category=category)
        self.assertEqual(product.category, category)

    def test_find_by_availability(self):
        available_product = ProductFactory(available=True)
        self.assertTrue(available_product.available)

if __name__ == "__main__":
    unittest.main()
