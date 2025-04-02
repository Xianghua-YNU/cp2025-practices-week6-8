
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

def sineWaveZeroPhi(x, t, A, omega, k):
    """
    实现波函数 y(x, t) = A sin(kx - ωt)
    
    参数:
    x: 位置数组
    t: 时间
    A: 振幅
    omega: 角频率
    k: 波数
    
    返回:
    y: 对应的y轴数值数组
    """
    return A * np.sin(k * x - omega * t)

def create_standing_wave_animation(A=1, omega=2*np.pi, k=2*np.pi, x_max=10, frames=100, interval=50):
    """
    创建驻波动画
    
    参数:
    A: 振幅
    omega: 角频率
    k: 波数
    x_max: x轴最大值
    frames: 动画帧数
    interval: 帧间隔(毫秒)
    """
    # 创建x轴数据
    x = np.linspace(0, x_max, 500)
    
    # 创建两个方向相反的波
    wave1 = lambda t: sineWaveZeroPhi(x, t, A, omega, k)
    wave2 = lambda t: sineWaveZeroPhi(x, t, A, omega, -k)  # 反向传播
    
    # 驻波是两个波的叠加
    standing_wave = lambda t: wave1(t) + wave2(t)
    
    # 创建图形和轴
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.set_xlim(0, x_max)
    ax.set_ylim(-2*A, 2*A)
    ax.set_xlabel('Position (x)')
    ax.set_ylabel('Amplitude (y)')
    ax.set_title('Standing Wave Animation')
    
    # 初始化线条
    line, = ax.plot([], [], lw=2)
    line1, = ax.plot([], [], lw=1, alpha=0.5)
    line2, = ax.plot([], [], lw=1, alpha=0.5)
    
    # 初始化函数
    def init():
        line.set_data([], [])
        line1.set_data([], [])
        line2.set_data([], [])
        return line, line1, line2
    
    # 更新函数
    def update(frame):
        t = frame * 0.1  # 时间步长
        y = standing_wave(t)
        y1 = wave1(t)
        y2 = wave2(t)
        
        line.set_data(x, y)
        line1.set_data(x, y1)
        line2.set_data(x, y2)
        
        return line, line1, line2
    
    # 创建动画
    anim = FuncAnimation(fig, update, frames=frames, init_func=init, 
                         blit=True, interval=interval)
    
    plt.legend(['Standing Wave', 'Wave 1', 'Wave 2'])
    plt.grid(True)
    plt.show()
    
    return anim

# 运行动画
if __name__ == "__main__":
    # 设置参数
    A = 1.0        # 振幅
    f = 1.0        # 频率 (Hz)
    omega = 2 * np.pi * f  # 角频率
    k = 2 * np.pi  # 波数 (假设波长为1)
    x_max = 10     # x轴范围
    
    # 创建动画
    anim = create_standing_wave_animation(A, omega, k, x_max)
