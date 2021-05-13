import unittest
import requests

BASE = "http://127.0.0.1:5000/"


class ServerUnitTest(unittest.TestCase):
    def test_post_user(self):
        response = requests.put(BASE + "user/Ash", {"password": "helloworld", "victories": 10})
        status_code = response.status_code
        self.assertEqual(status_code, 201)

    def test_get_user(self):
        response = requests.get(BASE + "user/Monty")
        status_code = response.status_code
        user_data = response.json()
        user_password = user_data['password']
        user_victories = user_data['victories']

        self.assertEqual(status_code, 200)
        self.assertEqual(user_password, "helloworld")
        self.assertEqual(user_victories, 100)

    def test_get_questions(self):
        response = requests.get(BASE + "question/1")
        status_code = response.status_code
        question_data = response.json()
        question = question_data['question']
        answer = question_data['answer']

        self.assertEqual(status_code, 200)
        self.assertEqual(question, "Friends star Lisa Kudrow was originally cast in the sitcom Frasier.")
        self.assertTrue(answer)


if __name__ == '__main__':
    unittest.main()
