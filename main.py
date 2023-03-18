import sched
from pygame import *

font.init()
score_text = font.Font(None, 36)
score = 0
lost_text = font.Font(None, 36)
lost = 0


lose_text = font.Font(None, 36)
win_text = font.Font(None, 36)

class GameSprite(sprite.Sprite):
   def __init__(self, player_image, player_x, player_y, player_speed, wight, height):
       super().__init__()
       self.image = transform.scale(image.load(player_image), (wight, height)) #разом 55,55 - параметри
       self.speed = player_speed
       self.rect = self.image.get_rect()
       self.rect.x = player_x
       self.rect.y = player_y
 
   def reset(self):
       window.blit(self.image, (self.rect.x, self.rect.y))
 
class Player(GameSprite):
   def update_r(self):
       keys = key.get_pressed()
       if keys[K_UP] and self.rect.y > 5:
           self.rect.y -= self.speed
       if keys[K_DOWN] and self.rect.y < win_height - 80:
           self.rect.y += self.speed
   def update_l(self):
       keys = key.get_pressed()
       if keys[K_w] and self.rect.y > 5:
           self.rect.y -= self.speed
       if keys[K_s] and self.rect.y < win_height - 80:
           self.rect.y += self.speed
 
background = (200, 255, 255)
win_width = 600
win_height = 500
window = display.set_mode((win_width, win_height))
window.fill(background)
 
run = True
finish = False
clock = time.Clock()
FPS = 60
 
 
ball = GameSprite("tennis_ball.png", 300, 250, 10, 50, 50)
racket1 = Player("racket.png", 30, 200, 4, 50, 150)
racket2 = Player("racket.png", 520, 200, 4, 50, 150)

speed_x = 3
speed_y = 3

while run:

    window.fill(background)
   
    text1 = score_text.render("Рахунок: " + str(score), 1, (0, 0, 0))
    window.blit(text1, (10, 20))
    text2 = lost_text.render("Пропущено: " + str(lost), 1, (0, 0, 0))
    window.blit(text2, (10, 50))

    for e in event.get():
        if e.type == QUIT:
            run = False


    ball.reset()
    racket1.reset()
    racket2.reset()

    racket1.update_l()
    racket2.update_r()
    ball.rect.x += speed_x
    ball.rect.y += speed_y

    if sprite.collide_rect(racket1, ball) or sprite.collide_rect(racket2, ball):
        speed_x *= -1
        speed_y *= 1

    if ball.rect.y <= 0 or ball.rect.y >= win_height - ball.rect.height:
        speed_y *= -1 
        
    display.update()
    clock.tick(FPS)
