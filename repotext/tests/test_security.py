import unittest
from repotext.security import check_for_sensitive_info

class TestSecurity(unittest.TestCase):

    def test_api_key_redaction(self):
        content = "My API key is AbCdEfGhIjKlMnOpQrStUvWxYz123456789"
        result = check_for_sensitive_info(content)
        self.assertIn('[API_KEY_REDACTED]', result)
        self.assertNotIn('AbCdEfGhIjKlMnOpQrStUvWxYz123456789', result)

    def test_password_redaction(self):
        content = 'password = "mysecretpassword"\npassword: hardertoguess'
        result = check_for_sensitive_info(content)
        self.assertIn('[PASSWORD_REDACTED]', result)
        self.assertNotIn('mysecretpassword', result)
        self.assertNotIn('hardertoguess', result)

if __name__ == '__main__':
    unittest.main()