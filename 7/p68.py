qus=input("輸入第一組數字 : ")
ans=input("輸入第二組數字 : ")
a=0
b=0

for i in qus:
    for j in ans:
        if i == j:
            if qus.index(i) == ans.index(j):
                a=a+1
            else:
                b=b+1
if a == 4 and b == 0 :
    print(a,"A",b,"B    全對")
else:
    print(a,"A",b,"B    加油")     