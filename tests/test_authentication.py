import unittest
from authentication import register_user, authenticate_user, hash_password


class TestAuth(unittest.TestCase):
    
    def setUp(self):
        self.test_database_user = {"test_admin": hash_password("password123")}
        
    def tearDown(self):
        self.test_database_user.clear()
    
    def test_register_success(self):
        register_user("user_test", "passw_test", self.test_database_user)
        
        self.assertIn("user_test", self.test_database_user.keys()) 
        self.assertIn(hash_password("passw_test"), self.test_database_user.values()) 
        
    def test_auth_user_true(self):
        res = authenticate_user(username="test_admin", password="password123", users_db=self.test_database_user)
        self.assertTrue(res)
    
    def test_auth_user_wrong_username(self):
        res = authenticate_user(username="test_admin_123", password="password123", users_db=self.test_database_user)
        self.assertFalse(res)
    
    def test_auth_user_wrong_password(self):
        res = authenticate_user(username="test_admin", password="passw", users_db=self.test_database_user)
        self.assertFalse(res)
        