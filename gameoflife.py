class GameOfLife:
    def __init__(self, w=10, h=10):
        self.w = w
        self.h = h
        self.map = self.setup_map()
        self.next_map = self.setup_map()
        
    def setup_map(self):
        return [[0 for j in range(self.w)] for i in range (self.h)]
    
    def count(self, x, y, target=1):
        if x < 0 or y < 0 or x > self.w - 1 or y > self.h - 1:
            print("error")
            return -1

        l_cell = self.map[y][x-1]
        r_cell = self.map[y][0 if (x+1) >= self.w else x+1]
        u_cell = self.map[y-1][x]
        d_cell = self.map[0 if (y+1) >= self.h else y+1][x]
        
        lu_cell = self.map[y-1][x-1]
        ru_cell = self.map[y-1][0 if (x+1) >= self.w else x+1]
        ld_cell = self.map[0 if (y+1) >= self.h else y+1][x-1]
        rd_cell = self.map[0 if (y+1) >= self.h else y+1][0 if (x+1) >= self.w else x+1]
        
        around = [l_cell, r_cell, u_cell, d_cell, lu_cell, ru_cell, ld_cell, rd_cell]

        return around.count(target)
    
    def update(self):
        self.next_map = [[0 for j in range(self.h)] for i in range(self.h)]
        
        for i, line in enumerate(self.map):
            for j, cell in enumerate(line):
                c = self.count(j, i)

                # dead cell
                if cell == 0:    
                    if c == 3:
                        self.next_map[i][j] = 1
                
                # alive cell
                if cell == 1:
                    if c < 2:
                        self.next_map[i][j] = 0
                    if c >= 2 and c <= 3:
                        self.next_map[i][j] = 1
                    if c > 3:
                        self.next_map[i][j] = 0
        
        self.map = self.next_map.copy()
    
    def draw(self, x, y):
        self.map[y][x] = 1 if self.map[y][x] == 0 else 0
        
    def display(self):
        for i, line in enumerate(self.map):
            for j, cell in enumerate(line):
                print("." if cell == 0 else "#", end="")
            print()
            
    def display_array(self):
        for line in self.map:
            print(line)
            

if __name__ == "__main__":
    from os import system
    
    main = GameOfLife(20, 20)

    running = True

    while running:
        system("cls")
        
        main.display()
        
        ip = input("-->").split(" ")
        
        cmd = ip[0]
        
        if cmd == "q" or cmd == "quit":
            running = False
        elif cmd == "" or cmd == "next" or cmd == "n":
            main.update()
        elif cmd == "draw" or cmd == "d":
            x = int(ip[1])
            y = int(ip[2])
            main.draw(x, y)
        elif cmd == "r" or cmd == "reset":
            main.map = main.setup_map()
        elif cmd == "h" or cmd == "help":
            print("""command list
    \tq, quit - quit the game
    \tn, next, <press-enter> - update the game state
    \td, draw <x> <y> - swipe cell state from 0, 1 or 1, 0
    \tr, reset - reset map
            """)
            input("press enter to quit:")
        else:
            print("not found command. type 'help' or 'h' for view command list.")
            
    print("\nclosed.")