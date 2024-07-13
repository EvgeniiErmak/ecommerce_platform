# ecommerce_platform/tests/test_products.py

import unittest
import requests

BASE_URL = "http://localhost:8000"


class TestProducts(unittest.TestCase):

    def test_get_products(self):
        response = requests.get(f"{BASE_URL}/products")
        self.assertEqual(response.status_code, 200)

    def test_create_product(self):
        product = {
            "name": "Test Product",
            "description": "Test Description",
            "price": 10.0
        }
        response = requests.post(f"{BASE_URL}/products", json=product)
        self.assertEqual(response.status_code, 201)


if __name__ == '__main__':
    unittest.main()
