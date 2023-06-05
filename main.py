from trivia_game import TriviaGame
import os

object = TriviaGame()
restart = 'y'
while True:
    if restart == "n":
        break
    else:
        os.system('cls')
        object.question()
        restart = input("\nDo you wanna restart your TriviaGame ('y'/'n')?: ")
        os.system('cls')