#took some shit from the ballz.py

import pygame, math, random

G = 0.01
H = 0.3

L = ((255, 255, 255), 4)
R = ((20, 255, 251), 2)
Q = ((224, 221, 43), 2)

def create_particle_dic(type_, mass = 1, vel_x = 0, vel_y = 0, x=540, y = 350):
    return {
        "x" : x,
        "y" : y,
        "mass" : mass,
        "type" : type_,
        "vel_x" : vel_x,
        "vel_y" : vel_y
    }

def draw_particle(screen, p):
    pygame.draw.circle(screen, p["type"][0], (p["x"], p["y"]), p["type"][1])


def update_positions(particles):

    forces = [
        {"x": 0, "y": 0} for _ in particles
    ]

    for i, p1 in enumerate(particles):
        for j, p2 in enumerate(particles):
            if i == j:
                continue

            dx = p2["x"] - p1["x"]
            dy = p2["y"] - p1["y"]
            distance = math.sqrt(dx**2 + dy**2)
            
            if distance == 0:
                continue

            force = G * ((p1["mass"] * p2["mass"]) / (distance) - (p1["mass"] * p2["mass"]) / (distance**6))
            angle = math.atan2(dy, dx)
            
            force_x = math.cos(angle) * force
            force_y = math.sin(angle) * force
            
            forces[i]["x"] += force_x
            forces[i]["y"] += force_y
    
    for i, p in enumerate(particles):
        if p["type"] == L:
            continue
        acceleration_x = forces[i]["x"] / p["mass"]
        acceleration_y = forces[i]["y"] / p["mass"]

        p["vel_x"] += acceleration_x
        p["vel_y"] += acceleration_y
        
        p["x"] += p["vel_x"]
        p["y"] += p["vel_y"]

        def lol():
            if p["x"] <= 0:
                p["x"] = 700
            elif p["x"] >= 700:
                p["x"] = 0
            if p["y"] <= 0:
                p["y"] = 700
            elif p["y"] >= 700:
                p["y"] = 0
        #lol()



def main():
    n = int(input(">> ")) + 1
    pygame.init()
    screen = pygame.display.set_mode((1080, 700))
    clock = pygame.time.Clock()
    population = list(range(1, 20))
    weights = [math.exp(-0.3 * i) for i in population]
    #print(weights)
    m = {"0" : create_particle_dic(L, 200, 0, 0)}   
    for i in range(1,n):
        #m[str(i)] = create_particle_dic(Q, random.choices(population, weights, k=1)[0], 0, 0)
        m[str(i)] = create_particle_dic(Q, 20, random.randint(-1, 1), random.randint(-1, 1), random.randint(100, 980), random.randint(100, 600))
        
        #print(m[str(i)])
    #print(m)
    particles = [m[str(i)] for i in range(0,n)]
    #print(particles)

    running = True
    while running:
        clock.tick(60)
        screen.fill("black")

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False


        update_positions(particles)


        for i in range(0,n):
            update_positions([m[str(i)]])
            draw_particle(screen, m[f'{i}'])


        pygame.display.flip()

    pygame.quit()



if __name__ == "__main__":
    main()