# 解析两个多项式相加

# 1. 接收输入数据
str1 = input()
str2 = input()
target_exp = int(input())  # 我们要查找的目标指数

# 2. 创建一个空字典，作为我们的“多项式总账本”
# 键(Key)存指数，值(Value)存系数
poly = {}

# 3. 把第一个多项式存入账本
terms1 = str1.split(',')
for term in terms1:
    parts = term.split()
    coef = int(parts[0])  # 系数
    exp = int(parts[1])   # 指数
    
    # 【核心魔法】：把系数累加到对应的指数上
    poly[exp] = poly.get(exp, 0) + coef

# 4. 把第二个多项式也存入账本（相同的指数会自动相加）
terms2 = str2.split(',')
for term in terms2:
    parts = term.split()
    coef = int(parts[0])
    exp = int(parts[1])
    
    # 依然用这一行魔法，自动处理“存在就相加，不存在就创建”
    poly[exp] = poly.get(exp, 0) + coef

# 5. 在账本里收账！
# 看看有没有我们要找的 target_exp，如果没有，说明这项不存在（系数为 0）
print(poly.get(target_exp, 0))