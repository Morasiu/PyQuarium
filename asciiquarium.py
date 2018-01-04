#! /usr/bin/env python3.6
#coding=utf-8
import random
import math
import time
from fishes import Fish

from asciimatics.screen import Screen
from asciimatics.paths import Path
from asciimatics.sprites import Sprite
from asciimatics.renderers import StaticRenderer
from asciimatics.scene import Scene
from asciimatics.exceptions import ResizeScreenError

class ASCIIQuarium:
  @staticmethod
  def start(screen):
    centre = (screen.width // 2, screen.height // 2)
    fish = Fish()
    effects = []
    colors = [Screen.COLOUR_RED, Screen.COLOUR_CYAN, Screen.COLOUR_MAGENTA, Screen.COLOUR_GREEN, Screen.COLOUR_WHITE, Screen.COLOUR_YELLOW]
    for _ in range(0,50):
      path = Path()
      # Spawn object on scene. Or teleport it to that cords.
      path.jump_to(0, random.randint(5, screen.height))
      # Move object to that cords in stright line. 3rd argument is how many steps it takes to complete this path.
      path.move_straight_to(screen.width, random.randint(5, screen.height), random.randint(100,200))
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
    scene = [Scene(effects, -1)]
    screen.set_title('ASCIIQuarium')
    # Play scene, auto reprat, stop when window is resized.
    screen.play(scene, repeat=False)

try:
  # Start scene
  asciiquarium = ASCIIQuarium()
  Screen.wrapper(ASCIIQuarium.start)
except ResizeScreenError:
  # Upsy Daisy, don't panic. Everything will be ok. Oh, I wish nobody read that.
  pass
