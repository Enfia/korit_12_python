li4 = []
li5 = []

for i in range(1, 11):
    li4.append(i)

for i in range(len(li4)):
    li4[i] *= 2

print(li4)

for i in li4:
    li5.append(i*2)

print(li5)

# 파이썬에서는 람다식 잘 안씀
modified_li4 = list(map(lambda num : num*2, li4))
print(modified_li4)