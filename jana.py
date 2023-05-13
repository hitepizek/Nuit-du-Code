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
                          Cube(16 + depart, 0, (1,1), cote), Cube(32 + depart, 0, (1,1),cote)]
            
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
