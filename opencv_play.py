import sys

sys.path.append("game/")
import cv2
import game.wrapped_flappy_bird as game

#  定义初始化动作
game_state = game.GameState()

# 输入动作，获取图像
init = [1, 0]
# 读取小鸟的图片
im, _, _ = game_state.frame_step(init)
# 读取管道图片
bird = cv2.imread('assets/sprites/redbird-midflap.png')
# 切割管道图片
pipe = cv2.imread('assets/sprites/pipe-green.png')

pipe = pipe[:50, :, :]


def matchTemplate(im, template, mode=cv2.TM_CCOEFF):
    """
    输入：
        im：原图像，在这幅图像中我们希望找到一块和模板相匹配的区域
        template：模板
        mode：匹配算法，这里使用的是相关匹配算法（cv2.TM_CCOEFF）
    输出：
        模板在原图像中匹配位置的上下左右四个值
    """

    #  模板匹配函数，返回一个矩阵
    res = cv2.matchTemplate(im, template, cv2.TM_CCOEFF)
    # 找到值矩阵中最大最小值以及最大最小值的位置
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)

    # 1e7 为人工经验值，在匹配管道时会用到
    if max_val > 1e7:
        # 因为这边选择的是 TM_CCOEFF 算法，所以匹配出来最大值的结果是我们需要的
        left, top = max_loc
        # 换算右边和底部的位置
        right, bottom = left + template.shape[1], top + template.shape[0]
        return left, top, right, bottom

    return None


# 测试一下
find_pipe = False

while True:

    action = [1, 0]
    im = cv2.cvtColor(im, cv2.COLOR_RGB2BGR)
    bird_left, bird_top, bird_right, bird_bottom = matchTemplate(im, bird)
    # 用矩形圈出小鸟的位置
    cv2.rectangle(im, (bird_left, bird_top), (bird_right, bird_bottom), 255, 2)

    # 如果找到管道，则获取小鸟和管道的位置，如果小鸟左侧飞过了管道右侧，则寻找下一个管道
    if find_pipe:
        im = im[:, :pipe_right, :]
        pipe_left, pipe_top, pipe_right, pipe_bottom = matchTemplate(im, pipe)
        # 如果小鸟底部到下管道顶部的距离小于十个像素，则向上飞一下，不然就不操作
        action = [0, 1] if pipe_top < bird_bottom + 10 else [1, 0]

        if bird_left > pipe_right:
            find_pipe = False

    else:
        # 寻找管道
        result = matchTemplate(im, pipe)
        # 若 matchTemplate 返回的函数不为 None，则认为找到了管道。
        if result:
            pipe_left, pipe_top, pipe_right, pipe_bottom = result
            # 如果小鸟底部到下管道顶部的距离小于十个像素，则向上飞一下，不然就不操作
            action = [0, 1] if pipe_top < bird_bottom + 10 else [1, 0]
            find_pipe = True

    if find_pipe:
        # 将管道可视化出来
        cv2.rectangle(im, (pipe_left, pipe_top), (pipe_right, pipe_bottom), 0, 2)

    cv2.imshow("im", im)
    cv2.waitKey(1)
    # 获取下一帧图像
    im, _, t = game_state.frame_step(action)

    if t:
        cv2.waitKey(0)
        break
