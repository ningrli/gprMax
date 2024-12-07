"""B扫描绘图"""
import os
import numpy
from tools.plot_Bscan import get_output_data, mpl_plot

dmax=r"./"   # 项目当前目录
filename = os.path.join(dmax, 'iofiles', 'concrete_merged.out')
rxnumber = 1
rxcomponent = 'Ez'
#获取回波数据
outputdata, dt = get_output_data(filename, rxnumber, rxcomponent)
#保存回波数据
numpy.savetxt('wavedata.txt',outputdata,delimiter=' ')
#绘图
plt = mpl_plot(filename,outputdata, dt, rxnumber, rxcomponent)
