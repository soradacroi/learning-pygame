import pygame
import math

# --- constants ---
WIDTH, HEIGHT = 1080, 700
pygame.display.set_caption("3-Body Gravity Simulation (Functional)")

# Colors
WHITE = (255, 255, 255)
YELLOW = (255, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

G = 0.5  # Gravitational constant

# --- Functions ---

def create_planet(x, y, mass, color, radius, vel_x=0, vel_y=0):
    """Creates a dictionary to represent a planet."""
    return {
        "x": x,
        "y": y,
        "mass": mass,
        "color": color,
        "radius": radius,
        "vel_x": vel_x,
        "vel_y": vel_y,
    }

def draw_planet(screen, planet):
    """Draws a planet on the screen."""
    pygame.draw.circle(screen, planet["color"], (int(planet["x"]), int(planet["y"])), planet["radius"])

def update_positions(planets):
    """Updates the position of each planet based on gravitational forces."""
    forces = [
        {"x": 0, "y": 0} for _ in planets
    ]

    for i, p1 in enumerate(planets):
        for j, p2 in enumerate(planets):
            if i == j:
                continue

            dx = p2["x"] - p1["x"]
            dy = p2["y"] - p1["y"]
            distance = math.sqrt(dx**2 + dy**2)
            
            if distance == 0:
                continue

            force = G * (p1["mass"] * p2["mass"]) / (distance**2)
            angle = math.atan2(dy, dx)
            
            force_x = math.cos(angle) * force
            force_y = math.sin(angle) * force
            
            forces[i]["x"] += force_x
            forces[i]["y"] += force_y

    for i, planet in enumerate(planets):
        acceleration_x = forces[i]["x"] / planet["mass"]
        acceleration_y = forces[i]["y"] / planet["mass"]

        planet["vel_x"] += acceleration_x
        planet["vel_y"] += acceleration_y
        
        planet["x"] += planet["vel_x"]
        planet["y"] += planet["vel_y"]


# --- main simulation loop ---
def main():
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    clock = pygame.time.Clock()

    # create planets as dictionaries
    sun = create_planet(WIDTH // 2, HEIGHT // 2, 100000, YELLOW, 30, vel_x=0, vel_y=-0.1)
    earth = create_planet(WIDTH // 2 - 200, HEIGHT // 2, 500, BLUE, 15, vel_y=18.1)
    moon = create_planet(WIDTH // 2 - 150, HEIGHT // 2, 0.1, WHITE, 8, vel_y=22.82)
    
    planets = [sun, earth, moon]
    
    running = True
    while running:
        clock.tick(60)
        screen.fill((0, 0, 0))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        update_positions(planets)

        for planet in planets:
            draw_planet(screen, planet)

        pygame.display.flip()

    pygame.quit()

if __name__ == "__main__":
    main()