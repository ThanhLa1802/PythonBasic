class Participant:
    def __init__(self, name) -> None:
        self.player_name = name
        self.points = 0
        self.choice = ""
    def choose(self):
        self.choice = input(f"Hello {self.player_name}, please choose Paper, Rock or Scissor: ")
        print(f"{self.player_name} has selected {self.choice}")
class GameRound:
    def __init__(self, p1, p2) -> None:
        p1.choose()
        p2.choose()
        
class Game:
    def __init__(self) -> None:
        self.end_game = False
        self.participate_first = Participant("Thanh") 
        self.participate_second = Participant("Nam") 
    def start(self):
        game_round = GameRound (self.participate_first, self.participate_second)

game = Game()
game.start()