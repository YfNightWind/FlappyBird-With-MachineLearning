import sys

sys.path.append("game/")
import game.wrapped_flappy_bird as game

#  创建实例
game_state = game.GameState()

while True:
    do = [1, 0]
    image, reward, terminal = game_state.frame_step(do, manual=True)
