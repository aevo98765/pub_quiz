import unittest
from .main import create_account, login


class MainTest(unittest.TestCase):
    def test_create_account(self):
        print("completed 1")
        username = "joe_bloggs123"
        password = "Helloworld"
        create_account_success = create_account(username, password)

        self.assertEqual(create_account_success, 201)


    def test_duplicate_user(self):
        username = "james_bond007"
        password = "Helloworld"
        password2 = "Hellopython"

        create_account_success = create_account(username, password)
        create_account_failed = create_account(username, password2)

        self.assertEqual(create_account_success, 201)
        self.assertNotEqual(create_account_failed, 201)
        self.assertEqual(create_account_failed, 409)

    def test_successful_login(self):
        username = "Monty"
        password = "helloworld"
        user_data = login(username, password)
        returned_username = user_data[0]
        returned_password = user_data[1]
        returned_victories = user_data[2]

        self.assertEqual(returned_username, "Monty")
        self.assertEqual(returned_password, "helloworld")
        self.assertEqual(returned_victories, 100)


if __name__ == '__main__':
    unittest.main()
