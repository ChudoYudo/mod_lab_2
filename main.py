import functions
import matplotlib.pyplot as plt
N = 100000
R = []
# A = -20
# M = 20
# a = -20
# b = 21
# seed = 1.0
# seeed = seed


#-------------------------------------------------------------------------------------------------------------
#Равномерное распределение
a=5
# b=10
# for i in range(N):
#     seed = functions.ravnom_ras(a, b)
#     R.append(seed)
#     print('R' + str(i) + ':' + str(seed))
#
#
# plt.hist(R, bins=25, normed=True, alpha=0.6, color='g')
# plt.show()
# Mx=functions.M_colcuate(R)
# Dx=functions.D_colculate(R)
# Sk=functions.sko_colculate(R)
#
# print('Mx: '+str(Mx)+' Dx: '+str(Dx)+' Sko: '+str(Sk) )

#-------------------------------------------------------------------------------------------------------------
#Экспотенциальное распределение
# lam = 3
# for i in range(N):
#     seed = functions.expon(lam)
#     R.append(seed)
#     print('R' + str(i) + ':' + str(seed))
# plt.hist(R, bins=25, normed=True, alpha=0.6, color='g')
# plt.show()
# Mx=functions.M_colcuate(R)
# Dx=functions.D_colculate(R)
# Sk=functions.sko_colculate(R)
#
# print('Mx: '+str(Mx)+' Dx: '+str(Dx)+' Sko: '+str(Sk) )

#-------------------------------------------------------------------------------------------------------------
#Треугольное распределение
# a=3
# b=9
# for i in range(N):
#     seed = functions.treug(a,b)
#     R.append(seed)
#     print('R' + str(i) + ':' + str(seed))
# plt.hist(R, bins=25, alpha=0.6, color='g')
# plt.show()
# Mx=functions.M_colcuate(R)
# Dx=functions.D_colculate(R)
# Sk=functions.sko_colculate(R)
#
# print('Mx: '+str(Mx)+' Dx: '+str(Dx)+' Sko: '+str(Sk))


#-------------------------------------------------------------------------------------------------------------
#распределение Симпсона
# a=18
# b=30
# for i in range(N):
#     seed = functions.simps(a,b)
#     R.append(seed)
#     print('R' + str(i) + ':' + str(seed))
# plt.hist(R, bins=40, alpha=1, color='g')
# plt.show()
# Mx=functions.M_colcuate(R)
# Dx=functions.D_colculate(R)
# Sk=functions.sko_colculate(R)
# print('Mx: '+str(Mx)+' Dx: '+str(Dx)+' Sko: '+str(Sk))



#-------------------------------------------------------------------------------------------------------------
#распределение Гауса
# m=5
# q=10
# n=6
#
# for i in range(N):
#     seed = functions.gaus(n,m,q)
#     R.append(seed)
#     print('R' + str(i) + ':' + str(seed))
# plt.hist(R, bins=25, alpha=0.6, color='g')
# plt.show()
# Mx=functions.M_colcuate(R)
# Dx=functions.D_colculate(R)
# Sk=functions.sko_colculate(R)
# print('Mx: '+str(Mx)+' Dx: '+str(Dx)+' Sko: '+str(Sk))

#-------------------------------------------------------------------------------------------------------------
#Гамма распределение
hi=18
lam=2.5
for i in range(N):
    seed = functions.gamma(lam, hi)
    R.append(seed)
    print('R' + str(i) + ':' + str(seed))
plt.hist(R, bins=25, alpha=0.6, color='g')
plt.show()
Mx=functions.M_colcuate(R)
Dx=functions.D_colculate(R)
Sk=functions.sko_colculate(R)
print('Mx: '+str(Mx)+' Dx: '+str(Dx)+' Sko: '+str(Sk))



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


