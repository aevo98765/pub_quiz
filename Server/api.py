from flask import Flask, request
from flask_restful import Api, Resource, reqparse, abort
from data import users, questions
app = Flask(__name__)
api = Api(app)


user_put_args = reqparse.RequestParser()
user_put_args.add_argument("password", type=str, help="String of password", required=True)
user_put_args.add_argument("victories", type=int, help="Number of victories", required=True)

user_update_args = reqparse.RequestParser()
user_update_args.add_argument("password", type=str, help="String of password")
user_update_args.add_argument("victories", type=int, help="Number of victories")



def abort_if_user_id_doesnt_exist(username):
    if username not in users:
        abort(404, message="User id is not valid.")

def abort_if_user_exits(username):
    if username in users:
        abort(409, message="User already exists")

def abort_if_question_id_doesnt_exist(question_id):
    if question_id not in questions:
        abort(404, message="Question id is not valid.")

class User(Resource):
    def get(self, username):
        abort_if_user_id_doesnt_exist(username)
        return users[username]

    def put(self, username):
        abort_if_user_exits(username)
        args = user_put_args.parse_args()
        users[username] = args
        return {username: args}, 201

    def patch(self, username):
        abort_if_user_id_doesnt_exist(username)
        args = user_update_args.parse_args()
        users[username]['victories'] = args['victories']





class Question(Resource):
    def get(self, question_id):
        abort_if_question_id_doesnt_exist(question_id)
        return questions[question_id]

class Questions(Resource):
    def get(self):
        return questions

class NumberOfQuestions(Resource):
    def get(self):
        number_of_questions = len(questions)
        return number_of_questions


api.add_resource(User, "/user/<string:username>")
api.add_resource(Question, "/question/<int:question_id>")
api.add_resource(Questions, "/questions")
api.add_resource(NumberOfQuestions, "/number_of_questions")


if __name__ == "__main__":
    app.run(debug=True)