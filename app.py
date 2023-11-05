#-----------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See LICENSE in the project root for license information.
#-----------------------------------------------------------------------------------------

from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return app.send_static_file("index.html")

# escribe una consola para para interactura con el usuario, debe tener las opciones de rock, paper y scissors
# y debe mostrar el resultado de la partida
def play():
    import random
    score = 0
    again = "yes"
    while again == "yes":
        option = input("Choose rock, paper or scissors: ")
        options = ["rock", "paper", "scissors"]
        computer = random.choice(options)
        print("Computer chose: " + computer)

        if option == computer:
            print("It's a tie!")
            score = score + 50
        elif option == "rock" and computer == "scissors":
            score = score + 100
            print("You win!")
        elif option == "paper" and computer == "rock":
            score = score + 100
            print("You win!")
        elif option == "scissors" and computer == "paper":
            score = score + 100
            print("You win!")
        else:
            print("You lose!")
            score = score - 50
        
        again = input("Do you want to play again? (yes/no) ")
        if again == "no":
            print("Your score is: " + str(score))
            break
        else:
            print("Your score is: " + str(score))
            continue

    return option + " vs " + computer

play()
    