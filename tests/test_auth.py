import unittest
from auth.auth import register_user, authenticate_user, hash_password


class TestAuth(unittest.TestCase):
    
    def setUp(self):
        self.user_db_test = {"user": hash_password("123")}
        
    def tearDown(self):
        self.user_db_test.clear()    
    
    
    def test_register_user(self):        
        register_user(self.user_db_test, username="admin", password="pass_admin")       
        self.assertIn("admin", self.user_db_test.keys())
        self.assertIn(hash_password("pass_admin"), self.user_db_test.values())     
        
    def test_authenticate_user(self):
        result = authenticate_user(self.user_db_test, "user", "123")
        self.assertTrue(result)        
    
    def test_authenticate_user_wrong(self):
        result_fail = authenticate_user(self.user_db_test, "user", "1234")
        self.assertFalse(result_fail)  
        
        result_fail_2 = authenticate_user(self.user_db_test, "user_1", "123")
        self.assertFalse(result_fail_2)  
        