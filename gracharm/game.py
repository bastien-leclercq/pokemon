import pygame
import pytmx
import pyscroll

from player import Player
from pygame import mixer



class Game:
    def __init__(self):
        # 1: Fenêtre
        self.screen = pygame.display.set_mode((800, 600))
        pygame.display.set_caption("pokemon")

        # Charger la carte (tmx)
        tmx_data = pytmx.util_pygame.load_pygame("Ma_carte/carte.tmx")
        map_data = pyscroll.data.TiledMapData(tmx_data)
        map_layer = pyscroll.orthographic.BufferedRenderer(map_data, self.screen.get_size())
        map_layer.zoom = 3

        # Générer un joueur
        # Import de l'objet layer "position" pour définir le point de spawn (macFarlaine)
        player_position = tmx_data.get_object_by_name("player")
        self.player = Player(player_position.x, player_position.y)

        #definire les rect de colli
        self.walls = []

        for obj in tmx_data.objects:
            if obj.type == "collision":
                self.walls.append(pygame.Rect(obj.x, obj.y, obj.width, obj.height))

        # Dessiner le groupe de calques
        # Sélection du calque sur lequel commencer
        self.group = pyscroll.PyscrollGroup(map_layer=map_layer, default_layer=6)
        self.group.add(self.player)

        mixer.init()
        mixer.music.load("Persona 5 OST 17 - Last Surprise.mp3")
        mixer.music.play(-1)
    # Déplacement et input
    def handle_input(self):
        # Récupération des touches
        pressed = pygame.key.get_pressed()
        if pressed[pygame.K_UP]:
            # Déclencher les différentes touches du clavier
            self.player.move_up()
            self.player.change_animation("up")
        elif pressed[pygame.K_DOWN]:
            self.player.move_down()
            self.player.change_animation("down")
        elif pressed[pygame.K_LEFT]:
            self.player.move_left()
            self.player.change_animation("left")
        elif pressed[pygame.K_RIGHT]:
            self.player.move_right()
            self.player.change_animation("right")

    def update(self):
        self.group.update()

        #verification des colli
        for sprite in self.group.sprites():
            if sprite.feet.collidelist(self.walls)> -1:
                sprite.move_back()


    def run(self):
        # Fixer le nombre de FPS
        clock = pygame.time.Clock()
        # a) Boucle de jeu
        running = True
        while running:
            self.player.save_location()
            # Enregistrement des touches avant tout
            self.handle_input()
            # Actualisation de la position du joueur
            self.update()
            # Placer la caméra au centre de la carte
            self.group.center(self.player.rect)
            self.group.draw(self.screen)
            pygame.display.flip()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
            # On bride le nombre de FPS
            clock.tick(40)

        pygame.quit()

# Create an instance of the Game class and run the game
game = Game()
game.run()
