# Nuit du c0de 2023 - Pasteur_2023_19 - Theme choisi : 

import pyxel

class App:
    def __init__(self):
        pyxel.init(128, 128, title="NDC 2023")
        self.x = 0
        pyxel.run(self.update, self.draw)
        
    def update(self):
        self.x = (self.x + 1) % pyxel.width
    
    def draw(self):
        pyxel.cls(0)
        pyxel.rect(self.x, 0, 8, 8, 9)
        
        
class Piece:
    def __init__(self, piece: int):
        
App()
