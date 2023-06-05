from trivia_data import data
import random

class TriviaGame:
    def __init__(self):
        self.score = 0
        self.total = 0

    def question(self):
        question_data = []
        for i in range(0, 10):
            question_data.append(random.choice(data["results"]))
        for i, question in enumerate(question_data):
            if i == 15:
                self.score = 0
                self.total = 0
                break
            answer = input(f"Q.{i+1}: {question['question']}. (True/False): ").lower()
            self.total += 1
            correct_answer = question['correct_answer']
            is_correct = (answer == correct_answer.lower())
            self.update_score(is_correct, correct_answer)

    def update_score(self, is_correct, correct_answer):
        if is_correct:
            self.score += 1
            print(f"You got it right!\nThe correct answer was: {correct_answer}")
        else:
            print(f"That's wrong!\nThe correct answer was: {correct_answer}")
        print(f"Your current score is: {self.score}/{self.total}\n")


        