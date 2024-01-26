import pygame

class Player(pygame.sprite.Sprite):

    def __init__(self, x, y):
        super().__init__()
        self.sprite_sheet = pygame.image.load("ressource/player/luca_mother3.png")
        #position predefini
        self.image = self.get_image(0,0)
        # enlever les couleur du tiles
        self.image.set_colorkey([0,0,0])
        self.rect = self.image.get_rect()
        self.position = [x, y]
        #definire les image pour les deplacement
        self.images = {
            "up" : self.get_image( 0,0)
            , "down" : self.get_image(0,64)
            , "left" : self.get_image(0,96)
            , "right" : self.get_image(0,32)
        }
        # hitbox du joueur
        self.feet = pygame.Rect(0, 0, self.rect.width * 0.5, 12)
        self.old_position = self.position.copy()
        self.speed = 2

    def save_location(self):self.old_position = self.position.copy()

    #appele des diferente image voire game.py
    def change_animation(self,name):
        self.image = self.images[name]
        self.image.set_colorkey([0,0,0])



    #methode pour permetre de changer la position en x et de ne pas rester static a l'activation des touche.
    #self.position[0] +=3 pour definer la vitesse de deplacement
    def move_right(self): self.position[0] += 1.75
    def move_left(self): self.position[0] -= 1.75
    def move_down(self): self.position[1] += 1.75
    def move_up(self): self.position[1] -= 1.75


    def update(self):
        self.rect.topleft = self.position
        self.feet.midbottom = self.rect.midbottom

    def move_back(self):
        self.position = self.old_position
        self.rect.topleft = self.position
        self.feet.midbottom = self.rect.midbottom


    #methode permetant au jouer de ce placer avant la colision juste a ces pied
    def move_back(self):
        self.position = self.old_position
        self.rect.topleft = self.position
        self.feet.midbottom = self.rect.midbottom

    def get_image(self, x, y):
        image = pygame.Surface([24,32])
        image.blit(self.sprite_sheet, (0, 0), (x, y , 24,32))
        return image

    def get_position(self):
        return self.position