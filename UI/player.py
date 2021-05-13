import time

class Player:
    def __init__(self, username, password, victories):
        self.username = username
        self.password = password
        self.victories = victories
        self.score = 0

    def answer_question(self,answer_to_question, player_answer):
        if player_answer in ["true", "True", "t", "T"]:
            player_answer = True
        elif player_answer in ["false, False", "f", "F"]:
            player_answer = False
        if player_answer == answer_to_question:
            print("Correct")
            time.sleep(1)
            self.score += 1
        else:
            print("Wrong")
            time.sleep(1)

    def get_player_score(self):
        return self.score


