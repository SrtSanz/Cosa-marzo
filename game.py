import pygame as pg
pg.init()

class Vigneta:
    def __init__(self, mama, x, y, ancho, alto, color = (255,255,0)):
        self.mama = mama
        self.x = x
        self.y = y
        self.ancho = ancho
        self.alto = alto
        self.color = color
        self.vx = 0
        self.vy = 0

    def dibujar(self):
        pass

    def mover(self):
        pass

class Ladrillo(Vigneta):
    def dibujar(self):
       pg.draw.rect(self.mama, self.color, (self.x, self.y, self.ancho, self.alto))

    def chokladri(self, bola):
        pass

class Raqueta(Vigneta):
    def __init__(self, mama, x, y, ancho, alto, color = (255, 255, 0)):
        super().__init__(mama, x, y, ancho, alto, color)
        self.vx = 1
        

    def dibujar(self):
        pg.draw.rect(self.mama, self.color, (self.x, self.y, self.ancho, self.alto))

    def mover(self):
        tecla = pg.key.get_pressed()
        if tecla[pg.K_LEFT]:
            self.x -= self.vx
        if tecla[pg.K_RIGHT]:
            self.x += self.vx

        if self.x < 0:
            self.x = 0
        if self.x + self.ancho >= self.mama.get_width():
            self.x = self.mama.get_width() - self.ancho
       
class Bola:
    def __init__(self, mama: pg.surface, x, y, color = (255,255,255), radio = 10):
        self.x = x
        self.y = y
        self.color = color
        self.radio = radio
        self.vx = 0.15
        self.vy = 0.15
        self.mama = mama

    def mover(self):
        self.x += self.vx
        self.y += self.vy

        if self.x <= self.radio or self.x >= self.mama.get_width() - self.radio:
            self.vx *= -1

        if self.y <= self.radio or self.y >= self.mama.get_height()- self.radio:
            self.vy *= -1

    def dibujar(self):
        pg.draw.circle(self.mama, self.color, (self.x, self.y), self.radio)
    
    def choque(self, otro):
        if (self.x - self.radio in range(otro.x + otro.ancho) or \
           self.x + self.radio in range(otro.x + otro.ancho)) and \
           (self.y - self.radio in range(otro.y + otro.alto) or \
           self.y + self.radio in range(otro.y + otro.alto)):
          
           self.y *= -1

class Game:
    def __init__(self, ancho=600, alto=400):
        self.pantalla = pg.display.set_mode((ancho, alto))
        self.bola = Bola(self.pantalla, ancho // 2, alto // 2, (255,255,0))
        self.raqueta = Raqueta(self.pantalla, ancho//2, alto - 30, 100, 20 )
        self.ladrillo = Ladrillo(self.pantalla, 10, 10, 100, 50)

        self.reloj = pg.time.Clock()


    def bucle_ppal(self):
        game_over = False

        while not game_over:
            milisegundo = self.reloj.tick(100)
            print (milisegundo)

            eventos = pg.event.get()
            for evento in eventos:
                if evento.type == pg.QUIT:
                    game_over = True

                
               # if evento.type == pg.KEYDOWN:
               #     if evento.key == pg.K_LEFT:
               #         self.raqueta.vx = -8

#                    if evento.key == pg.K_RIGHT:
 #                       self.raqueta.vx= 5
#
 #               if evento.type == pg.KEYUP:
  #                  if evento.key in (pg.K_LEFT, pg.K_RIGHT):
   #                     self.raqueta.vx = 0
               
            
            
            self.pantalla.fill((255, 0, 0))

            self.ladrillo.dibujar()
            self.ladrillo.mover()

            self.bola.dibujar()
            self.bola.mover()
            self.bola.choque(self.raqueta)

            self.raqueta.dibujar()
            self.raqueta.mover()
                 
            pg.display.flip()

if __name__ == '__main__':
    pg.init()
    game = Game()
    game.bucle_ppal()

    pg.quit()