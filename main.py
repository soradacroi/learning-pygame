import pygame, math

pygame.init()
screen = pygame.display.set_mode((1080, 700))
clock = pygame.time.Clock()


G = 6.6743e-11
m1, m2, m3 = 9.9891e19, 5.972e20, 2e21
dt = 0
x1, y1 = 50, 89
x2, y2 = 490, 510
x3, y3 = 900, 100

running = True
while running:

  for event in pygame.event.get():
    if event.type== pygame.QUIT:
      running = False

  #<program logic>#


  p1 = [x1, y1]
  p2 = [x2, y2]
  p3 = [x3, y3]
  r12 = ((p1[0]-p2[0])**2 + (p1[1]-p2[1])**2)  # no power of 1/2 because we do squre of it later 
  r13 = ((p1[0]-p3[0])**2 + (p1[1]-p3[1])**2)
  r23 = ((p3[0]-p2[0])**2 + (p3[1]-p2[1])**2)
  #angles

  #theta_1 = math.atan((x2-x1)/(y1-y2))
  #theta_2 = math.atan((x1-x2)/(y2-y1))

  # i just realoze we dont need theta lol

  #acceleration

  a1 = (G*m2)/r12   # r is not squared because we didnt square root it before
  a2 = (G*m1)/r12   # same logic
  a3 = (G*m1)/r13 

  screen.fill("#141614")
  pygame.draw.circle(screen, "blue", p1, 20)
  pygame.draw.circle(screen, "red", p2, 20)
  pygame.draw.circle(screen, "green", p3, 20)
  
  


  if r12 > 100000:
    #movement in x-axis
    ax = a1*((x2-x1)/r12)
    bx = a2*((x1-x2)/r12)
    x1 += ax*dt
    x2 += bx*dt

    #movement in y-axis
    ay = a1*((y1-y2)/r12)
    by = a2*((y2-y1)/r12)
    y1 -= ay*dt
    y2 -= by*dt
  else:
    #movement in x-axis
    ax = a1*((x2-x1)/r12)
    bx = a2*((x1-x2)/r12)
    x1 -= ax*dt
    x2 -= bx*dt

    #movement in y-axis
    ay = a1*((y1-y2)/r12)
    by = a2*((y2-y1)/r12)
    y1 += ay*dt
    y2 += by*dt
  


  pygame.display.flip()
  dt = clock.tick(60) / 1000
  