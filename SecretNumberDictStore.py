import datetime
import random


class SecretNumber():
    def __init__(self):
        self.number = random.randint(1, 30)

    def getSecretNumber(self):
        return self.number


class Results():
    def __init__(self, score, name, date):
        self.attempts = score
        self.name = name #Player's name
        self.date = date

    def get_date(self):
        return self.date

    def get_player_name(self):
        return self.name

    def set_player_name(self, name):
        self.name = name


NumberToGuess = SecretNumber()
player_name = input("Enter your name : ")
attempts = 0
while True:
    guess = int(input("Enter your guess (1-30) : "))
    if guess == NumberToGuess.getSecretNumber():
        print("Congratulations!!! You guessed the secret number in " + str(attempts) + " attempt(s)")
        break
    elif guess < NumberToGuess.getSecretNumber():
        print("The secret number is larger !!!")
        attempts = attempts + 1
    elif guess > NumberToGuess.getSecretNumber():
        print("The secret number is smaller !!!")
        attempts = attempts + 1

todayDate = datetime.datetime.now().strftime("%d %m %Y")  # Datum abspreichern in todayDate
new_store = Results(score=attempts, name=player_name, date=todayDate)
with open("results.txt", "w") as file_writer:
    file_writer.write(str(new_store.__dict__))
print("Results : {0}".format(new_store.__dict__))