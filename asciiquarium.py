import random
import math
from fishes import Fish

from asciimatics.screen import Screen
from asciimatics.paths import Path
from asciimatics.sprites import Sprite
from asciimatics.renderers import StaticRenderer
from asciimatics.scene import Scene
from asciimatics.effects import Cycle, Print, Stars

def demo(screen):
  centre = (screen.width // 2, screen.height // 2)
  fish = Fish()
  effects = []
  colors = [Screen.COLOUR_RED, Screen.COLOUR_BLUE, Screen.COLOUR_GREEN, Screen.COLOUR_WHITE, Screen.COLOUR_YELLOW]
  for _ in range(0,500):
    path = Path()
    # Spawn object on scene. Or teleport it to that cords.
    path.jump_to(0, random.randint(0, screen.height))
    # Move object to that cords in stright line. 3rd argument is how many steps it takes to complete this path.
    path.move_straight_to(screen.width, random.randint(0, screen.height), random.randint(200,500))
    # Create sprite. Sprite is an effect, which can follow path.
    sprite = Sprite(
        screen,
        renderer_dict={
            "default": StaticRenderer(images=[fish.small_fish])
        },
        path=path,
        colour=random.choice(colors))
    # Add effect to effect list. Effect is basically anything that will be displayed on scene.
    effects.append(sprite)
  # Add all effects yo this scene
  scene = [Scene(effects)]
  # Play scene, auto reprat, stop when window is resized.
  screen.play(scene, stop_on_resize=True)

# Start scene
Screen.wrapper(demo)
