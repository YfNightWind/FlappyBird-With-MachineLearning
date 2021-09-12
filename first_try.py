import sys
sys.path.append('game/')
import cv2
import game.wrapped_flappy_bird as game


# 创建实例
game_state = game.GameState()

# 将一个动作输入到游戏中，获得游戏返回的结果
do = [0, 1]  # [0, 1]表示点击屏幕，让小鸟飞起来，[1, 0]表示什么也不做

'''
image 为游戏下一帧的图像。在 Python 中表现为一个三维的矩阵。
reward 是一个浮点数，表示得分，+0.1 表示存活，+1 表示通过管道，-1 表示死亡。
terminal 是一个布尔值，表示游戏是否结束。
'''
image, reward, terminal = game_state.frame_step(do)

# 打印 image 的大小， reward 和 terminal 的值
print(image.shape, reward, terminal)
image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)  # 转换成RGB显示模式
cv2.imshow("image", image)
cv2.waitKey(0)
