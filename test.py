class Grid():
    def __init__(self):
        self.grid = []
        for i in range(2):
            self.grid.append([])
            for j in range(3):
                self.grid[i].append((i+1) * j)
    
    def get_grid(self):
        return self.grid

def f(grid):
    grid[0][2] = 10
    return
g = Grid()
print(g.grid)
thegrid = g.get_grid()
f(thegrid)
print(g.grid)



# import pygame as py
# import sys

# WHITE = (250, 250, 250)
# BLUE = (100, 100, 240)
# BLUE1 = (200, 200, 250)
# GREY = (50, 50, 50)
# button_size = (50, 50)
# button_location = (50, 50)
# button_location2 = (50, 150)
# button_location3 = (200, 200)

# py.init()
# screen = py.display.set_mode((400, 400))

# class Box(py.sprite.Sprite):
#     def __init__(self, dimension, color, location):
#         py.sprite.Sprite.__init__(self)
#         self.image = py.Surface(dimension)
#         self.color = color
#         self.image.fill(color)
#         self.location = location
#         self.rect = self.image.get_rect(center=(dimension[0]/2, dimension[1]/2))
#         self.clicked = True
#         self.number = 1
#         return
    
#     def show(self):
#         screen.blit(self.image, self.location)

#     def clear(self):
#         self.image.fill(self.color)
    
#     # def change_number(self):
#     #     self.image.fill(BLUE if self.clicked else BLUE1)
#     #     self.number += 1
#         # font = py.font.SysFont('arial', 24)
#         # text = font.render(str(self.number), 1, GREY)
#         # textpos = text.get_rect(center=self.rect.center)
#         # self.image.blit(text, textpos)


# mytimerevent = py.USEREVENT + 1

# box = Box(button_size, BLUE1, button_location)
# box2 = Box(button_size, BLUE1, button_location2)
# solve = Box(button_size, BLUE, button_location3)
# mousex, mousey = 0, 0
# box_clicked = False

# i, j = 1, 1

# def detect_box_click(x, y):
#     print(box.rect.collidepoint(x, y))

# while 1:
#     # Goal: 
#     #   1. When "Solve" button is clicked, do a nested "for loop" for the other 2 boxes (1 ~ 9, 1 ~ 9)

#     for event in py.event.get():
#         if event.type == py.QUIT:
#             py.quit()
#             sys.exit()
#         elif event.type == py.MOUSEBUTTONUP:
#             mousex, mousey = event.pos
#             print("mousex: {}, mousey: {}".format(mousex, mousey))
#             # detect_box_click(mousex, mousey)
#             # pos = py.mouse.get_pos()
#             # clicked_sprites = [s for s in sprites if s.rect.collidepoint(pos)]
#             # print(clicked_sprites)
#             if solve.rect.collidepoint(mousex - button_location3[0], mousey - button_location3[0]):                
#                 py.time.set_timer(mytimerevent, 300)
#                 print("solve button clicked")
#         if event.type == mytimerevent:
#             print("custom event going on...")
#             box.clear()
#             box2.clear()
            
#             font = py.font.SysFont('arial', 24)
#             text1 = font.render(str(i), 1, GREY)
#             textpos1 = text1.get_rect(center=box.rect.center)
#             box.image.blit(text1, textpos1)

#             text2 = font.render(str(j), 1, GREY)
#             textpos2 = text2.get_rect(center=box2.rect.center)
#             box2.image.blit(text2, textpos2)

#             if j < 9 or i < 9:
#                 j += 1
#             if j > 9:
#                 if i == 9:
#                     j = 9
#                 else:
#                     j = 1
#                     i += 1
#             if i > 9: 
#                 i = 9
            
    
#     screen.fill(WHITE)
#     box.show()
#     box2.show()
#     solve.show()
    
#     py.display.update()

# From: https://stackoverflow.com/questions/10990137/pygame-mouse-clicking-detection
# import pygame

# class SpriteObject(pygame.sprite.Sprite):
#     def __init__(self, x, y, color):
#         super().__init__() 
#         pygame.Surface((50, 50))
#         self.original_image = pygame.Surface((50, 50), pygame.SRCALPHA)
#         pygame.draw.circle(self.original_image, color, (25, 25), 25)
#         self.click_image = pygame.Surface((50, 50), pygame.SRCALPHA)
#         pygame.draw.circle(self.click_image, color, (25, 25), 25)
#         pygame.draw.circle(self.click_image, (255, 255, 255), (25, 25), 25, 4)
#         self.image = self.original_image 
#         self.rect = self.image.get_rect(center = (x, y))
#         self.clicked = False

#     def update(self, event_list):
#         for event in event_list:
#             if event.type == pygame.MOUSEBUTTONDOWN:
#                 if self.rect.collidepoint(event.pos):
#                     self.clicked = not self.clicked

#         self.image = self.click_image if self.clicked else self.original_image

# pygame.init()
# window = pygame.display.set_mode((300, 300))
# clock = pygame.time.Clock()

# sprite_object = SpriteObject(*window.get_rect().center, (128, 128, 0))
# group = pygame.sprite.Group([
#     SpriteObject(window.get_width() // 3, window.get_height() // 3, (128, 0, 0)),
#     SpriteObject(window.get_width() * 2 // 3, window.get_height() // 3, (0, 128, 0)),
#     SpriteObject(window.get_width() // 3, window.get_height() * 2 // 3, (0, 0, 128)),
#     SpriteObject(window.get_width() * 2// 3, window.get_height() * 2 // 3, (128, 128, 0)),
# ])

# run = True
# while run:
#     clock.tick(60)
#     event_list = pygame.event.get()
#     for event in event_list:
#         if event.type == pygame.QUIT:
#             run = False 

#     group.update(event_list)

#     window.fill(0)
#     group.draw(window)
#     pygame.display.flip()

# pygame.quit()
# exit()