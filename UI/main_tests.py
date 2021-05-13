import unittest
from .main import create_account, login



class MyTestCase(unittest.TestCase):
    def test_create_account(self):
        print("completed 1")
        username = "joe_bloggs123"
        password = "Helloworld"
        create_account_success = create_account(username, password)

        self.assertEqual(create_account_success, 201)


if __name__ == '__main__':
    unittest.main()
