class Player:
    def __init__(self):
        self.name = ""
        self.x = 0
        self.y = 0

    def set_name(self, name):
        self.name = name

    def move(self, xA, yA):
        self.x += xA
        self.y += yA

    def p_encode(self):
        return f"{self.name}:{self.x}:{self.y}"
    
    @staticmethod
    def p_decode(self, name, x, y):
        decoded_player = Player()
        decoded_player.set_name(name)
        decoded_player.move(x, y)
        return decoded_player