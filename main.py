import functions
import numpy as np
import scipy.stats as stats
import matplotlib.pyplot as plt
N = 100000
R = []
A = -20
M = 20
a = -20
b = 21
seed = 1.0
seeed = seed


# for i in range(N):
#     seed = functions.ravnom_ras(a, b, functions.get_rand(A, M))
#     R.append(seed)
#     print('R' + str(i) + ':' + str(seed) + '   X' + str(i) + ':' + str(seed / M))
#
#
# plt.hist(R, bins=25, normed=True, alpha=0.6, color='g')
# plt.show()


# for i in range(N):
#     seed = functions.expon(functions.get_rand(A, M),3)
#     R.append(seed)
#     print('R' + str(i) + ':' + str(seed) + '   X' + str(i) + ':' + str(seed / M))
#
#
# plt.hist(R, bins=25, normed=True, alpha=0.6, color='g')
# plt.show()



for i in range(N):
    seed = functions.treug(a,b)
    R.append(seed)
    print('R' + str(i) + ':' + str(seed) + '   X' + str(i) + ':' + str(seed / M))


plt.hist(R, bins=25, alpha=0.6, color='g')
plt.show()


# functions.show_plt(R)
# Mo = functions.M_colcuate(R)
# print('----------------------------------------------------')
# print('Ocenka Mx: ' + str(Mo))
# D = functions.D_colculate(R)
# print('Ocenka Dx: ' + str(D))
# Sko = functions.sko_colculate(R)
# print('Ocenka sko: ' + str(Sko))
# checker = functions.check_ravn(R)
# print('2k/n = ' + str(checker))
# pp = functions.period(seeed, A, M)


