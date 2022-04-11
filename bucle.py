import pygame as pg

pg.init()

pantalla = pg.display.set_mode((600, 800))

game_over = False

x = 300
y = 400

vx = 1
vy = 1

while not game_over:
    #Primero: procesar eventos
    eventos = pg.event.get()
    for evento in eventos:
        if evento.type == pg.QUIT:
            game_over = True

    #Modificar los objetos del juego   
    x += vx
    y += vy

    if x >= 600:
	    vx = -1
    if x <= 0:
	    vx = 1

    if y >= 800:
	    vy = -1
    if y <= 0:
	    vy = 1

    #Aquí no hay nada que hacer
    #Refrescar pantalla
    pantalla.fill((255, 0, 0))
    bola = pg.draw.circle(pantalla,(255,255,0), (x, y), 10)

    pg.display.flip()
    
pg.quit()