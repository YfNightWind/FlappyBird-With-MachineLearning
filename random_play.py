import sys

sys.path.append("game/")
import numpy as np
import game.wrapped_flappy_bird as game

# 创建实例
game_state = game.GameState()

while True:
    do = np.random.choice([True, False], p=[0.2, 0.8])
    do = [0, 1] if do else [1, 0]  # 随机挑选操作
    image, reward, terminal = game_state.frame_step(do)  # 将动作输入到游戏中，获得返回的结果
