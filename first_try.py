import sys
import cv2
import game.wrapped_flappy_bird as game

# 创建实例
game_state = game.GameState()

# 将一个动作输入到游戏中，获得游戏返回的结果
do = [0, 1]
image, reward, terminal = game_state.frame_step(do)

# 打印 image 的大小， reward 和 terminal 的值
print(image.shape, reward, terminal)
