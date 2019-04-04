#打印质数表
#质数，又称为素数，prime number 是指大于1的自然数，它的因数只有1和本身
#本程序采用的思想是：所有非质数都是由质数乘积得到的
def primeSel(num):
    primeList = [2]
#设置flag  flag = 0 表示不是质数  flag = 1 表示是质数
    for i in range(2,num,1):
        flag = 1
        j = 0
        while j < len(primeList):
            if i % primeList[j] == 0:
               flag = 0
               break
            else:
                j += 1
        if flag == 1:
            primeList.append(i)
    return primeList
while True:
    userInput = int(input('截止至多少的素数'))
    print(primeSel(userInput))
