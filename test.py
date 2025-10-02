import pygame
from Box2D import b2World, b2PolygonShape, b2CircleShape

# --- Pygame setup ---
pygame.init()
screen_width, screen_height = 600, 400
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Box2D Internal Drawing")

# Scale Box2D units (meters) -> screen pixels
PPM = 21.0   # pixels per meter
TIME_STEP = 1.0 / 60.0
VEL_ITERS, POS_ITERS = 6, 2

def to_pygame(pos):
    """Convert Box2D coordinates to Pygame coordinates"""
    return int(pos[0] * PPM), int(screen_height - pos[1] * PPM)

# --- Box2D world ---
world = b2World(gravity=(0, -10))

# Ground (static body)
ground = world.CreateStaticBody(position=(0, 1))
ground_shape = b2PolygonShape(box=(20, 1))
ground.CreateFixture(shape=ground_shape)

# Ball (dynamic body)
ball = world.CreateDynamicBody(position=(10, 15))
circle_shape = b2CircleShape(radius=1)
ball.CreateFixture(shape=circle_shape, density=1, friction=0.3, restitution=0.6)

# --- Main loop ---
running = True
clock = pygame.time.Clock()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Step physics
    world.Step(TIME_STEP, VEL_ITERS, POS_ITERS)

    # Clear screen
    screen.fill((255, 255, 255))

    # --- Loop through all bodies and fixtures ---
    for body in world.bodies:
        for fixture in body.fixtures:
            shape = fixture.shape

            if isinstance(shape, b2CircleShape):  # Circle
                pos = to_pygame(body.transform * shape.pos)  # transform local -> world
                pygame.draw.circle(screen, (200, 0, 0), pos, int(shape.radius * PPM))

            elif isinstance(shape, b2PolygonShape):  # Polygon (box, etc.)
                vertices = [to_pygame(body.transform * v) for v in shape.vertices]
                pygame.draw.polygon(screen, (0, 0, 0), vertices)

    # Update display
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
