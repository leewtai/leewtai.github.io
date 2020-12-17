#import yaml
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sn

with open('x.yaml', 'r') as f:
    x = yaml.load(f)
with open('y.yaml', 'r') as f:
    y = yaml.load(f)

i = 12
xi = np.array(x[i])
yi = np.array(y[i])


xs = np.linspace(min(xi), max(xi), 100)
params = np.array([0.25, 3])
ys = params[0] + params[1] * xs

ind = np.abs(xi - 0.07).argmin()
xii = xi[ind]
yii = yi[ind]

x_cross = 0.063
y_cross = yi[np.abs(xi - x_cross).argmin()]

sn.scatterplot(xi, yi, size=0.5)
sn.lineplot(xs, ys, color='black')
sn.scatterplot([xii], [yii], marker='x', color='red', size=1.5)
sn.scatterplot([x_cross], [y_cross], marker='x', color='red', size=1.5)
sn.scatterplot([xii], [params[0] + params[1] * xii], marker='x', color='black', size=1.5)
sn.lineplot([x_cross, x_cross], [np.min(yi) - 1, y_cross], marker='x', color='red', size=1.5)
sn.lineplot([xii, xii], [np.min(yi) - 1, yii], marker='x', color='red', size=1.5)
plt.text(xii + 0.001, yii, r'$(X_{i,j}, Y_{i,j})$')
plt.text(x_cross + 0.001, y_cross - 0.05, r'$(X_{i,\hat{\beta}}^*, X_{i, \hat{\beta}}^* \hat{\beta})$')
plt.text(xii + 0.001, params[0] + params[1] * xii - 0.05, r'$(X_{i,j}, X_{i,j} \hat{\beta})$')
plt.legend([], [], frameon=False)
plt.ylim([np.min(yi), np.max(yi)])
plt.xlabel(r'$q^2_{cm}/m^2_{\pi}$')
plt.ylabel(r'$q\cot\delta/m_{\pi}$')
plt.savefig('demo_plot.png')
plt.close()


i = 6
xi = np.array(x[i])
yi = np.array(y[i])
sn.scatterplot(xi, yi, size=0.5)
plt.legend([], [], frameon=False)
plt.savefig('crossing_critical_point.png')
plt.close()



