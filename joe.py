# Nuit du c0de 2023 - Pasteur_2023_19 - Theme choisi : 

import pyxel, random

class Cube:
    def __init__(self, x: int, y: int, couleur: tuple, cote: str):
        self.x = x
        self.y = y
        self.u = couleur[0]
        self.v = couleur[1]
        self.cote = cote
        
    def deplacement_gauche(self):
        if self.cote == "gauche":
            if self.x - 8 >= 0:
                self.x -= 8
        elif self.cote == "droite":
            if self.x - 8 >= 64:
                self.x -= 8
            
    def deplacement_droite(self):
        if self.cote == "gauche":
            if self.x + 8 < 64:
                self.x += 8
        elif self.cote == "droite":
            if self.x + 8 <  128:
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
        self.limite = cote_x
        self.cote = cote
        
        if piece == 0:
            depart = random.randint(0, 5) * 8 + cote_x
            self.cubes = [Cube(0 + depart, -8, (1,1), cote), Cube(0 + depart, 0, (1,1),cote),\
                          Cube(8 + depart, 0, (1,1), cote), Cube(16 + depart, 0, (1,1),cote)]
        elif piece == 1:
            depart = random.randint(0, 5) * 8 + cote_x
            self.cubes = [Cube(0 + depart, 0, (1,1), cote), Cube(8 + depart, -8, (1,1),cote),\
                          Cube(8 + depart, 0, (1,1), cote), Cube(16 + depart, 0, (1,1),cote)]
            
        elif piece == 2:
            depart = random.randint(0, 4) * 8 + cote_x
            self.cubes = [Cube(0 + depart, 0, (1,1), cote), Cube(8 + depart, 0, (1,1),cote),\
                          Cube(16 + depart, 0, (1,1), cote), Cube(24 + depart, 0, (1,1),cote)]
            
        elif piece == 3:
            depart = random.randint(0, 5) * 8 + cote_x
            self.cubes = [Cube(0 + depart, 0, (1,1), cote), Cube(0 + depart, -8, (1,1),cote),\
                          Cube(8 + depart, -8, (1,1), cote), Cube(16 + depart, -8, (1,1),cote)]
        elif piece == 4:
            depart = random.randint(0, 6) * 8 + cote_x
            self.cubes = [Cube(0 + depart, 0, (1,1), cote), Cube(0 + depart, -8, (1,1),cote),\
                          Cube(8 + depart, -8, (1,1), cote), Cube(-8 + depart, -8, (1,1),cote)]
            
        elif piece == 5:
            depart = random.randint(0, 5) * 8 + cote_x
            self.cubes = [Cube(0 + depart, 0, (1,1), cote), Cube(8 + depart, 0, (1,1),cote),\
                          Cube(8 + depart, -8, (1,1), cote), Cube(16 + depart, -8, (1,1),cote)]
            
        elif piece == 6:
            depart = random.randint(0, 6) * 8 + cote_x
            self.cubes = [Cube(0 + depart, 0, (1,1), cote), Cube(0 + depart, -8, (1,1),cote),\
                          Cube(8 + depart, -8, (1,1), cote), Cube(8 + depart, -16, (1,1),cote)]
            
    def tourner(self):
        if pyxel.btnp(pyxel.KEY_UP) and self.cote == "droite":
            pass
    
    def deplacement_gauche(self):
        if pyxel.btnp(pyxel.KEY_A) or pyxel.btnp(pyxel.KEY_LEFT):
            valide = True
            for cube in self.cubes:
                if cube.x == 0 + self.limite:
                    valide = False
            if valide:
                for cube in self.cubes:
                    cube.deplacement_gauche()
                
    def deplacement_droite(self):
        if pyxel.btnp(pyxel.KEY_D) or pyxel.btnp(pyxel.KEY_RIGHT):
            valide = True
            for cube in self.cubes:
                if cube.x == 56 + self.limite:
                    valide = False
            if valide:
                for cube in self.cubes:
                    cube.deplacement_droite()
                    
    def deplacement_bas(self):
        if pyxel.btnp(pyxel.KEY_S) and self.cote == "gauche":
            for cube in self.cubes:
                if cube.y + 8 < 120:
                    self.mouvement()
                
        if pyxel.btnp(pyxel.KEY_DOWN) and self.cote == "droite":
            for cube in self.cubes:
                if cube.y + 8 < 120:
                    self.mouvement()
                
    def mouvement(self):
        valide = True
        for cube in self.cubes:
            if cube.y == 120:
                valide = False
        if valide:
            for cube in self.cubes:
                cube.y += 4
                
    def collision(self, other):
        elimination = False
        for cube_s in self.cubes:
            for cube_o in other.cubes:
                if cube_s.collision(cube_o):
                    elimination = True
        return elimination
        
class App:
    def __init__(self):
        pyxel.init(128, 128, title="NDC 2023")
        
        self.pieces = []
        self.vitesse = 30
        self.piece_active = None
        
        pyxel.run(self.update, self.draw)
        
    def update(self):
        if pyxel.btnp(pyxel.KEY_SPACE):
            piece_nouvelle = Piece(random.randint(0,6), "gauche")
            self.piece_active = piece_nouvelle
        
        if pyxel.frame_count % self.vitesse == 0:
            for piece in self.pieces:
                piece.mouvement()
                
        if self.piece_active is not None:
            self.piece_active.deplacement_gauche()
            self.piece_active.deplacement_droite()
            self.piece_active.deplacement_bas()
            for piece in self.pieces:
                if self.piece_active.collision(piece):
                    self.pieces.append(self.piece_active)
                    piece_nouvelle = Piece(random.randint(0,6), "gauche")
                    self.piece_active = piece_nouvelle
        
    def draw(self):
        pyxel.load("themes.pyxres", True, True, True, True)
        pyxel.cls(7)
        
        for piece in self.pieces:
            for cube in piece.cubes:
                pyxel.rect(cube.x, cube.y, 8, 8, 6)
        if self.piece_active is not None:
            for cube in self.piece_active.cubes:
                pyxel.rect(cube.x, cube.y, 8, 8, 6)
App()

