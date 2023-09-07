import unittest
from flask import Flask
from app import app, convertCurrency

class appTestCase(unittest.TestCase):

    def setUp(self):
        # Create a test client
        self.app = app.test_client()

    def tearDown(self):
        pass

    def test_convertCurrency_success(self):
        # Test the convertCurrency function for successful conversion
        form_data = {"from": "USD", "to": "EUR", "amount": "100"}
        result = convertCurrency(form_data)
        self.assertIsNotNone(result)

    def test_convertCurrency_failure(self):
        # Test the convertCurrency function for failed conversion
        form_data = {"from": "XYZ", "to": "EUR", "amount": "100"}
        result = convertCurrency(form_data)
        self.assertIsNone(result)

    def test_convert_view(self):
        # Test the /submit route (convert view) for successful conversion
        response = self.app.post('/submit', data={"from": "USD", "to": "EUR", "amount": "100"})
        self.assertEqual(response.status_code, 302)  # Expecting a redirect

    def test_convert_view_invalid_form(self):
        # Test the /submit route (convert view) for invalid form data
        response = self.app.post('/submit', data={"from": "", "to": "EUR", "amount": "100"})
        self.assertEqual(response.status_code, 302)  # Expecting a redirect

    def test_showResult_view(self):
        # Test the /results route (showResult view)
        response = self.app.get('/results/100?curr=EUR')
        self.assertEqual(response.status_code, 200)
        self.assertIn('EUR', response.data)  # Expecting the Euro symbol in the response

if __name__ == '__main__':
    unittest.main()
