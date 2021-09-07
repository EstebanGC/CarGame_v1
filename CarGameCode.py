from random import randint

class Car:
    def __init__(self, driver, lane):
            self.driver = driver
            self.lane = lane
            self.position = 0

    def advance(self): 
        dice = randint(1, 6)
        self.position = self.position + dice
        return dice

    def print_player(self):
        return (self.driver + " of lane: " +  str(self.lane) + ". Take care, he comes fast!")

goal = -1
won = False
play = True
Message1 = "That was too short, type a longer name (at least 3 letters): "
Message2 = "Ok, "
Message3 = " get ready!"
Message4 = ", of lane "
Message5 = "Would you like to run again? (y/n): "

#----- select Players:
while play == True:
    players = []
    input("Welcome to PyCar Game! \nWhen you are ready to run, press the accelerator [Enter].")
    add_player = str(input("Please type the name of the PLAYER1: "))
    player1 = Car(add_player, 1)
    while len(player1.driver) < 3:
        player1.driver = str(input(Message1))
    players.append(player1)
    print(Message2 + player1.driver + Message3)

    add_player = str(input("Please type the name of the PLAYER2: "))
    player2 = Car(add_player, 2)
    while len(player2.driver) < 3:
        player2.driver = str(input(Message1))
    players.append(player2)
    print(Message2 + player2.driver + Message3)

    more_players = input("Are there others pilots who want to run? (y/n):  ")
    while more_players != "y" and more_players != "n":
        more_players = input("I did not understand that, please answer <y> or <n>. Would you like to add more players? (y/n): ")
    counter = 2
    while more_players == "y":
        add_player = str(input("Please type the name of the PLAYER" + str(counter + 1) + ": "))
        additional_player = Car(add_player, counter + 1)
        while len(additional_player.driver) < 3:
            additional_player.driver = str(input(Message1))
        players.append(additional_player)
        print(Message2 + additional_player.driver + Message3)
        counter = counter + 1
        more_players = input("Are there others pilots who want to run? (y/n): ")

    print("Right. All pilots are in the start lane. \nThe players in this race are: ")
    for player in players:
        print(player.print_player())

    goal = int(input("Type the meters of the race: "))
    while goal < 10:
        goal = input("That was too short. Please, type at least 10 characters!: ")

    #----- play Game:
    input("OK, the race starts, get ready!!")
    print("READY")
    print("SET")
    print("GO!")
    won = False
    while won == False:
        for i in range(0, len(players)):
            go = str(input("Ok, ¡" + players[i].driver + "It's your turn! Type <go> y press [ENTER] for throwing the dice and see how far you can get: "))
            while go != "go":
                    go = str(input("Please type <go>!"))
            dice = players[i].advance()

            if players[i].position >= goal:
                input(players[i].driver + " cross the line! how fast !!!")
                winners = sorted(players, key=lambda x: x.position, reverse=True)
                won = True
                if len(winners) < 3:
                    input("And the  absolute champion and gold medal's winner is: " + winners[0].driver + Message4 + str(winners[0].lane) + ". \nCongratulations!!")
                else:
                    input("And the winners are: \nIn third place and bronze medal's winner is: " + winners[2].driver + Message4 + str(winners[2].lane) + "." 
                    + "\nIn second place and silver medal's winner io: " + winners[1].driver + Message4 + str(winners[1].lane) + "."
                    + "\nAnd the  absolute champion and gold medal's winner is: " + winners[0].driver + Message4 + str(winners[0].lane) + ". \nCongratulations!!")
                again = input(Message5)
                while again != "y" and again != "n":
                    again = input(Message5)
                if again == "n":
                    play = False
                break
            else:
                input(players[i].driver + " you've got a " + str(dice) + "!! Now, you're in the position " + str(players[i].position) + ". Let's go!")
