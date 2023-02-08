numdict = {'ZRO':0,'ONE':1,'TWO':2,'THR':3,'FOR':4,'FIV':5,'SIX':6,'SVN':7,'EGT':8,'NIN':9}
T = int(input())
for _ in range(T):
    testidx = input()
    strlist = list(input().split())
    translist = sorted(strlist,key=lambda num :numdict[num])
    print(testidx[:3])
    print(*translist)