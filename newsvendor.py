c = eval(input()) # cost per unit
r = eval(input()) # price per unit
N = eval(input()) # demand
s = eval(input()) # salvage value

saledPro = []

for i in range(N + 1):
	saledPro.append(eval(input()))

q_Pro = 0
Profit = float(0)
Profit_pre = float(0)
Profit_com = float(0)
Profit_cal = float(0)
Profit_1 = float(0)
Profit_2 = float(0)

for q in range(N + 1):
    Profit_1 = 0.0
    Profit_2 = 0.0

    if q == 0:
        Profit_cal = 0
    else:
        for qn in range (q):
            Profit_1 += saledPro[qn] * (r * qn - c * q + s * (q - qn))
            Profit_2 += saledPro[qn]

        Profit_cal = Profit_1 + (1 - Profit_2) * q * (r - c)
        if Profit_cal < 0 and q == 1:
            Profit = 0
            q_Pro = 0
            break

    Profit_com = Profit_cal if Profit_cal >= 0 else 0

    if Profit_com < Profit_pre:
        Profit = Profit_pre
        q_Pro = q - 1
        break
    else:
        if q == N:
            Profit = Profit_com
            q_Pro = N
            break
        Profit_pre = Profit_com

print(q_Pro, int(Profit))
print(saledPro)