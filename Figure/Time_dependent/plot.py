import numpy as np
import matplotlib.pyplot as plt
import scienceplots

# Plot style
plt.style.use(['science', 'no-latex'])

# Load data
x = np.loadtxt('output/nonsteady/xavgunddr.dat')
x_theory = np.loadtxt('output/nonsteady/xtunddr.dat')

f = np.loadtxt('output/nonsteady/favgunddr.dat')
f_theory = np.loadtxt('output/nonsteady/ftunddr.dat')

Ko = np.loadtxt('output/nonsteady/Kavgunddr.dat')
Ko_theory = np.loadtxt('output/nonsteady/Kotunddr.dat')

fig, ax = plt.subplots(figsize=(6, 4))
ax.tick_params(axis='both', labelsize=16)
ax.ticklabel_format(axis='both', style='sci', scilimits=(0, 0))
ax.xaxis.get_offset_text().set_fontsize(16)
ax.yaxis.get_offset_text().set_fontsize(16)

ax.plot(x[:, 0], x[:, 1], '--', linewidth=2, label=r'$x_1$')
ax.plot(x[:, 0], x[:, 2], '--', linewidth=2, label=r'$x_2$')
# ax.plot(x[:, 0], x[:, 4], '--', linewidth=2, label=r'$x_4$')
ax.plot(x_theory[:, 0], x_theory[:, 1], '-', linewidth=2, label=r'$x_1$ (Theory)')
ax.plot(x_theory[:, 0], x_theory[:, 2], '-', linewidth=2, label=r'$x_2$ (Theory)')
# ax.plot(x_theory[:, 0], x_theory[:, 4], '-', linewidth=2, label=r'$x_4$')
ax.set_xlabel('t', fontsize=24)
ax.set_ylabel(r'$\langle x_i(t) \rangle-\langle x_i(0) \rangle$', fontsize=24)
ax.legend(fontsize=16)
plt.savefig('nonsteady_response_x.eps', bbox_inches='tight')
plt.show()

fig, ax = plt.subplots(figsize=(7.5, 6))
ax.tick_params(axis='both', labelsize=16)
ax.ticklabel_format(axis='both', style='sci', scilimits=(0, 0))
ax.xaxis.get_offset_text().set_fontsize(16)
ax.yaxis.get_offset_text().set_fontsize(16)

ax.plot(f[:, 0], f[:, 1], '--', linewidth=2, label=r'$F_1$')
ax.plot(f[:, 0], f[:, 2], '--', linewidth=2, label=r'$F_2$')
ax.plot(f_theory[:, 0], f_theory[:, 1], '-', linewidth=2, label=r'$F_1$ (Theory)')
ax.plot(f_theory[:, 0], f_theory[:, 2], '-', linewidth=2, label=r'$F_2$ (Theory)')
ax.set_xlabel('t', fontsize=24)
ax.set_ylabel(r'$\langle F_i(t) \rangle$', fontsize=24)
ax.legend(fontsize=16)

plt.savefig('nonsteady_response_f.eps', bbox_inches='tight')
plt.show()

fig, ax = plt.subplots(figsize=(7.5, 6))
ax.tick_params(axis='both', labelsize=16)
ax.ticklabel_format(axis='both', style='sci', scilimits=(0, 0))
ax.xaxis.get_offset_text().set_fontsize(16)
ax.yaxis.get_offset_text().set_fontsize(16)

ax.plot(Ko[:, 0], Ko[:, 1], '--', linewidth=2, label=r'$K_{11}$')
ax.plot(Ko[:, 0], Ko[:, 2], '--', linewidth=2, label=r'$K_{12}$')
ax.plot(Ko_theory[:, 0], Ko_theory[:, 1], '-', linewidth=2, label=r'$K_{11}$ (Theory)')
ax.plot(Ko_theory[:, 0], Ko_theory[:, 2], '-', linewidth=2, label=r'$K_{12}$ (Theory)')
ax.set_xlabel('t', fontsize=24)
ax.set_ylabel(r'$K_{ij}(t,t)$', fontsize=24)
ax.legend(fontsize=16)

plt.savefig('nonsteady_response_Ko.eps', bbox_inches='tight')
plt.show()