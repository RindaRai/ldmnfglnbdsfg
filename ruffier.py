from pygame import *

mixer.init()
mixer.music.load('space.ogg')
mixer.music.play()
fire_sound = mixer.Sound('fire.ogg')

img_back = 'galaxy.jpg'
img_hero = 'rocket.png'

class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, size_x, size_y, player_speed):
        sprite.Sprite.__init__(self)
        
        self.image = transform.scale(image.load(player_image), (size_x, size_y))
        self.speed = player_speed
        
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
        
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):
    def update(self):
        keys = key.get_pressed()
        if keys[K_LEFT] and self.rect.x > 5:
            self.rect.x -= self.speed
        if keys[K_RIGHT] and self.rect.x < win_width - 80:
            self.rect.x += self.speed

win_width = 700
win_height = 500
display.set_caption('Cyberpunk 3033')
window = display.set_mode((win_width, win_height))
back = transform.scale(image.load(img_back), (win_width, win_height))

ship = Player(img_hero, 300, win_height - 100, 80, 100, 10)

finish = False
run = True

while run:
    for e in event.get():
        if e.type == QUIT:
            run = False
    
    if not finish:
        window.blit(back, (0, 0))
        
        ship.update()
        ship.reset()
        
        display.update()
    time.delay(50)