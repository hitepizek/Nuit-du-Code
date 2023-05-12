# Nuit du c0de 2023 - Pasteur_2023_19 - Theme choisi : 

import pyxel, random

class App:
    def __init__(self):
        pyxel.init(128, 128, title="NDC 2023")
        
        self.pieces = []
        
        pyxel.run(self.update, self.draw)
        
    def update(self):
        if pyxel.frame_count % 30 == 0:
            piece = Piece(0)
            self.pieces.append(piece)
            
            for piece in self.pieces:
                piece.mouvement()
        
        
    def draw(self):
        pyxel.load("themes.pyxres", True, True, True, True)
        pyxel.cls(0)
        
        for piece in self.pieces:
            pyxel.rect(piece.x, piece.y, 0, 16, 16, 6)
        
        
class Piece:
    def __init__(self, piece: int):
        self.x = 0
        self.y = 0
        
        if piece == 0:
            self.forme = [[1]]

    def tourner(self):
        pass
    
    def mouvement(self):
        if self.y + 16 <= 128:
            self.y += 16
            
App()
