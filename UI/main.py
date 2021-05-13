import requests
from UI.player import Player
import random

SERVER_BASE = "http://127.0.0.1:5000/"


def create_account(username, password):
    response = requests.put(SERVER_BASE + f"user/{username}", {"password": {password}, "victories": 0})
    return response.status_code


def login(username, entered_password):
    response = requests.get(SERVER_BASE + f"user/{username}")
    if response.status_code == 200:
        user_data = response.json()
        stored_password = user_data['password']
        victories = user_data['victories']
        if stored_password == entered_password:
            return 200, [username, stored_password, victories]
        else:
            return True

def get_question():
    response = requests.get(SERVER_BASE + f"question/{next_question_id}")
    question_data = response.json()
    question = question_data['question']
    answer = question_data['answer']

    return question, answer


if __name__ == '__main__':

    while True:
        create_account_decision = input("Would you like to create a new account? (y/n): ")
        if create_account_decision in ["y", "Y", "yes", "Yes"]:
            username = input("Please enter your username: ")
            password = input("Please enter your password: ")
            if create_account(username, password) == 201:
                break
            elif create_account(username, password) == 409:
                print("This username already exists. Please try again.")
            else:
                pass
        else:
            break

    while True:
        print("Welcome to the quiz game!!")
        username = input("Please enter your username: ")
        password = input("Please enter your password: ")
        status_code = 0
        try:
            status_code, user_data = login(username, password)
        except:
            pass



        if status_code == 200:
            print(f"Welcome {username}")
            victories = user_data[2]
            player = Player(username, password, victories)
            break
        else:
            print("Please try again...")
            pass
    round_number = 0

    asked_questions = []

    response = requests.get("http://127.0.0.1:5000/number_of_questions")
    number_of_questions = response.json()
    winning_target = 3

    while True:
        next_question_id = random.randint(1, number_of_questions)
        if next_question_id not in asked_questions:
            asked_questions.append(next_question_id)
            question, answer = get_question()
            player_answer = input(f"{question} (True (t) or False (f): ")
            player.answer_question(answer, player_answer)
            player_score = player.get_player_score()
            round_number += 1
            if player.get_player_score() == winning_target:
                print("Congratulations!! You have won!!")
                response = requests.patch(SERVER_BASE + f"user/{username}", {"victories": player.victories+1})
                break

            print(f"After round number {round_number} you have {player_score} points")
        else:
            if len(asked_questions) == number_of_questions:
                print("Game Over! Sorry there are no questions remaining!")
                response = requests.patch(SERVER_BASE + f"user/{username}", {"victories": player.victories})
                break
            else:
                pass


