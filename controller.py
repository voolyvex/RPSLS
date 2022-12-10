
from PyQt5.QtWidgets import *
from view import *


QtWidgets.QApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling, True)
QtWidgets.QApplication.setAttribute(QtCore.Qt.AA_UseHighDpiPixmaps, True)

class Controller(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(Controller, self).__init__()
        self.setupUi(self)
        self.rock_button.clicked.connect(lambda: self.display_image("rock.jpg"))
        self.paper_button.clicked.connect(lambda: self.display_image("paper.jpg"))
        self.scissors_button.clicked.connect(lambda: self.display_image("scissors.jpg"))
        self.lizard_button.clicked.connect(lambda: self.display_image("lizard.jpg"))
        self.spock_button.clicked.connect(lambda: self.display_image("spock.jpg"))
        
   
    def display_image(self, image: str):
        if self.radio_button1.isChecked():
            self.p1_image.setPixmap(QtGui.QPixmap(image))
        else:
            self.p2_image.setPixmap(QtGui.QPixmap(image))
        
        
        


        # self.p1_image.setPixmap(QtGui.QPixmap("lizard.jpg"))
    # #radio buttons
    # def radio_button1_clicked(self, enabled):
    #     if enabled: # Human vs Human game
    #         self.game_mode = "1"
    # def radio_button2_clicked(self, enabled):
    #     if enabled: # Human vs AI game
    #         self.game_mode = "2"
            
    # def welcome(self):
    #     self.game_text1.setText("")
    #     self.game_text1.setText("Each match will be best of three games.\nUse the BUTTONS to select a gesture.\nRock crushes Scissors..........Scissors cuts Paper\nPaper covers Rock..............Rock crushes Lizard\nLizard poisons Spock...........Spock smashes Scissors\nScissors decapitates Lizard....Lizard eats Paper\nPaper disproves Spock..........Spock vaporizes Rock")
    #     self.get_players(self.game_mode)
    # def get_players(self, game_mode):
    #     human, ai = "Human", "AI"
    #     if game_mode == "1":
    #         p1 = Player(human)
    #         p2 = Player(human)
    #     if game_mode == "2":
    #         p1 = Player(human)
    #         p2 = Player(ai)
    #     return p1, p2

    # def start_new_round(self, p1, p2):
    #     print()
    #     slow_print2(f"Round {self.round}\nPlayer 1 {p1.type} vs Player 2 {p2.type}\nGet ready...on Three...\n")
    #     slow_print2("One..... Two..... ")
    #     slow_print2("Three!\n")

    # def run(self):
    #     self.welcome()
    #     p1, p2 = self.get_players(self.game_mode)
    #     while not self.winner:
    #         self.start_new_round(p1, p2)
    #         self.determine_round_winner(p1, p2)
    #         self.round += 1
        
    # def determine_round_winner(self, p1, p2):

    #     # instantiate gesture objects
    #     rock, paper, scissors, lizard, spock = Rock(), Paper(), Scissors(), Lizard(), Spock()

    #     # store and display players' chosen gestures
    #     p1_gesture, p2_gesture = p1.get_gesture(), p2.get_gesture()
    #     self.game_text2.setText(f"{p1.type} picks {p1_gesture}!\n{p2.type} has picked {p2_gesture}!")
        
    #     # adjudicate winner
    #     if p1_gesture == "Rock":
    #         round_winner = rock.will_defeat_or_lose(p2_gesture)
    #     elif p1_gesture == "Paper":
    #         round_winner = paper.will_defeat_or_lose(p2_gesture)
    #     elif p1_gesture == "Scissors":
    #         round_winner = scissors.will_defeat_or_lose(p2_gesture)
    #     elif p1_gesture == "Lizard":
    #         round_winner = lizard.will_defeat_or_lose(p2_gesture)
    #     elif p1_gesture == "Spock":
    #         round_winner = spock.will_defeat_or_lose(p2_gesture)
        
    #     # add to a player's win count if they won
    #     if round_winner == "1":
    #         p1.win_count += 1
    #         print(f"Player 1 {p1.type} wins the round")
    #     elif round_winner == "2":
    #         p2.win_count += 1
    #         print(f"Player 2 {p2.type} wins the round")
    #     elif round_winner == "tie":
    #         slow_print2("It was a tie\n")

    #     # check if best-of-three was won
    #     self.check_for_winner(p1, p2)

    # def check_for_winner(self, p1, p2):
    #     if p1.win_count == 2:
    #         slow_print2(f"\nPlayer 1 {p1.type} is the winner! ")
    #         self.winner = True
    #     elif p2.win_count == 2:
    #         slow_print2(f"\nPlayer 2 {p2.type} is the winner! ")
    #         self.winner = True
        