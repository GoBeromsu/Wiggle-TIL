import random

# 비슷한 실력의 3명씩 이름을 입력받아
# 랜덤으로 9개의 팀으로 나눌 것

a, b, c = input().split()
d, e, f = input().split()
g, h, i = input().split()
j, k, l = input().split()
m, n, o = input().split()
p, q, r = input().split()
s, t, u = input().split()
v, w, x = input().split()
y, z, aa = input().split()

at = random.randint(1, 3)
bt = 2 - at
ct = 2 - at
dt = 1
et = 2 
ft = 3
gt = random.randint(1, 3)
ht = 2 - gt
it = 2 - ht
jt = random.randint(1, 3)
kt = 2 - jt
lt = 2 - kt
mt = random.randint(1, 3)
nt = 2 - mt
ot = 2 - nt
pt = random.randint(1, 3)
qt = 2 - pt
rt = 2 - qt
st = random.randint(1, 3)
tt = 2 - st
ut = 2 - tt
vt = random.randint(1, 3)
wt = 2 - vt
xt = 2 - wt
yt = random.randint(1, 3)
zt = 2 - yt
aat = 2 - zt
player_names = [a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, r, s, t, u, v, w, x, y, z, aa]
team_indexs = [at, bt, ct, dt, et, ft, gt, ht, it, jt, kt, lt, mt, nt, ot, pt, qt, rt, st, tt, ut, vt, wt, xt, yt, zt, aat]

print("1팀")
for i in range(0,27):
    if team_indexs[i] % 3 == 0:
        print(player_names[i])

print("2팀")
for i in range(0,27):
    if team_indexs[i]% 3 == 1:
        print(player_names[i])
        
print("3팀")
for i in range(0,27):
    if team_indexs[i] % 3 == 2:
        print(player_names[i])