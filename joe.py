# Nuit du c0de 2023 - Pasteur_2023_19 - Theme choisi : 

import pyxel, random

class Cube:
    def __init__(self, x: int, y: int, couleur: tuple, cote: str):
        self.x = x
        self.y = y
        self.u = couleur[0]
        self.v = couleur[1]
        self.cote = cote
        
    def deplacement(self):
        if self.cote == "gauche":
            if pyxel.btnp(pyxel.KEY_A):
               if self.x - 8 >= 0:
                   self.x -= 8
            elif pyxel.btnp(pyxel.KEY_D):
               if self.x + 8 < 64:
                   self.x += 8
        
        elif self.cote == "droite":
            if pyxel.btnp(pyxel.KEY_LEFT):
               if self.x - 8 >= 64:
                   self.x -= 8
            elif pyxel.btnp(pyxel.KEY_RIGHT):
               if self.x + 8 < 128:
                   self.x += 8
                   
    def collision(self, other):
        return self.x < other.x + 8 and\
               self.y < other.y + 8 and\
               self.x + 8 > other.x and\
               self.y + 8 > other.y
    
class Piece:
    def __init__(self, piece: int, cote: str):
        cote_x = 0
        if cote == "droite":
            cote_x = 64
        self.cote = cote
        
        if piece == 0:
            depart = random.randint(0, 5) * 8 + cote_x
            self.cubes = [Cube(0 + depart, -8, (1,1), cote), Cube(0 + depart, 0, (1,1),cote),\
                          Cube(8 + depart, 0, (1,1), cote), Cube(16 + depart, 0, (1,1),cote)]
        
    def tourner(self):
        pass
    
    def deplacement(self):
        valide = True
        for i in range(len(self.cubes) - 1):
            for j in range(i+1, len(self.cubes) - 1):
                if self.cubes[i].collision(self.cubes[j]):
                    valide = False
        if valide:
            for cube in self.cubes:
                cube.deplacement()
    
    def mouvement(self):
        for cube in self.cubes :
            if cube.y + 8 < 128:
                cube.y += 8
        
class App:
    def __init__(self):
        pyxel.init(128, 128, title="NDC 2023")
        
        self.pieces = []
        self.vitesse = 30
        self.piece_active = None
        
        pyxel.run(self.update, self.draw)
        
    def update(self):
        if pyxel.btnp(pyxel.KEY_SPACE):
            piece_nouvelle = Piece(0, "gauche")
            self.piece_active = piece_nouvelle
            self.pieces.append(piece_nouvelle)
        
        if pyxel.frame_count % self.vitesse == 0:
            for piece in self.pieces:
                piece.mouvement()
        if self.piece_active is not None:
            self.piece_active.deplacement() 
        
        
        
    def draw(self):
        pyxel.load("themes.pyxres", True, True, True, True)
        pyxel.cls(7)
        
        for piece in self.pieces:
            for cube in piece.cubes:
                pyxel.rect(cube.x, cube.y, 8, 8, 6)
            
App()
