"""画出A扫结果"""
import os
from gprMax.receivers import Rx
from tools.plot_Ascan import mpl_plot
dmax=r"./" # pycharm项目当前目录
filename = os.path.join(dmax,'user_models', 'cylinder_Ascan_2D.out')
outputs = Rx.defaultoutputs
outputs = ['Ez'] # Ez分量
plt = mpl_plot(filename,outputs, fft=True) #波形图，fft：频谱图