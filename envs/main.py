import gymnasium as gym
import math
import pygame 
import numpy as np 





try:
    import Box2D
    from Box2D.b2 import (
            edgeShape,
            circleShape,
            fixtureDef,
            polygonShape,
            revoluteJointDef,
            distanceJointDef,
            contactListener

        )
except ImportError as e:
    raise ImportWarning( 
        'Box2D Not Installed '
    ) from e




'''
For GitHUB Write the things for motive/Maksad of this env after finshing 

'''


# init_parameters
FPS = 90
VEL_STATUS = True
CONST_SCALE = 0.33 # Scale at which the froce to be applied 
STARTING_HEIGHT = 1000.0
STARTING_SPEED = 90.0
PPM =20.0



# Rocket 
MIN_THROTTLE  = 0.4
GIMBAL_THRESHOLD = 0.4 
MAIN_ENGINE_POWER = 1600 * CONST_SCALE
SIDE_ENGINE_POWER = 100 / FPS * CONST_SCALE
TIME_STEPS=1/FPS

ROCKET_WIDTH = 3.66 * CONST_SCALE
ROCKET_HEIGHT = ROCKET_WIDTH / (3.7*47.9)
ENGINE_HEIGHT = ROCKET_WIDTH*0.5
ENGINE_WIDTH = ENGINE_HEIGHT*0.7
THRUSTER_HEIGHT = ROCKET_HEIGHT *0.86


# LEGS 
LEG_LENGTH = ROCKET_WIDTH * 0.7
BASE_ANGLE = -0.27
SPRING_ANGLE = -0.27
LEG_AWAY = ROCKET_WIDTH/2



# Landing Platform
LP_HEIGHT = ROCKET_WIDTH
LP_WIDTH = LP_HEIGHT*40


# PREVIEW_WINDOW SETTINGS 
W_H = 700
W_W= 504
H = 1.1 * STARTING_HEIGHT * CONST_SCALE
W = float(W_W) / W_H * H

# OPTIONAL SMOKE EFFECT 
# MAX_SMOKE_LIFETIME = 2 * FPS

# MEAN = np.array([-0.034, -0.15, -0.016, 0.0024, 0.0024, 0.137,
#                  - 0.02, -0.01, -0.8, 0.002])
# VAR = np.sqrt(np.array([0.08, 0.33, 0.0073, 0.0023, 0.0023, 0.8,
#                         0.085, 0.0088, 0.063, 0.076]))


class RocketLander(gym.env):
    def __init__(self):
        super.__init__()
    
    def reset():
        pass
    
    def step(step,action):
        pass

    def render(self):
        pass

    def close(self):
        pass
