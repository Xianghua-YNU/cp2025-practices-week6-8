import numpy as np
import matplotlib.pyplot as plt
from matplotlib import animation

# 任务1：实现波函数 simplewzferpPhi
def simplewzferpPhi(x, t, A, omega, k):
    """返回驻波函数值"""
    return A * np.sin(k * x - omega * t)

# 创建Figure和Axes
fig = plt.figure()
ax = plt.axes(xlim=(0, 10), ylim=(-8, 8))
ax.set_xlabel("x")
ax.set_ylabel("y")

# 初始化三条线：两个原始波和驻波
line1, = ax.plot([], [], lw=2, label='Wave 1')
line2, = ax.plot([], [], lw=2, label='Wave 2')
line3, = ax.plot([], [], lw=2, linestyle='--', color='red', label='Standing Wave')
lines = [line1, line2, line3]
plt.legend()

# 初始化函数
def init():
    for line in lines:
        line.set_data([], [])
    return lines

# 空间变量x
x = np.linspace(0, 10, 1000)

# 动画更新函数
def animate(i):
    A = 4          # 振幅固定为4
    omega = 2 * np.pi  # 角频率
    k = np.pi / 2     # 波数
    t = 0.1 * i      # 时间递增

    # 生成两个方向相反的波
    y1 = simplewzferpPhi(x, t, A, omega, k)
    y2 = simplewzferpPhi(x, t, A, -omega, k)  # 负角频率表示反向传播

    # 驻波叠加（相加）
    y3 = y1 + y2

    # 更新数据
    lines[0].set_data(x, y1)
    lines[1].set_data(x, y2)
    lines[2].set_data(x, y3)
    return lines

# 运行动画
if __name__ == "__main__":
    anim = animation.FuncAnimation(
        fig, animate, init_func=init,
        frames=200, interval=50, blit=True
    )
    plt.show()
    # 提示：waveFunctions = [[x, y1], [x, y2], [x, y3]]可以帮助组织数据

    return lines
if __name__ == '__main__':
    # TODO: 创建动画对象并显示
    # 提示：使用animation.FuncAnimation创建动画
    # 提示：使用plt.show()显示动画
    pass

