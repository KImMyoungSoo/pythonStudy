class test :
    def __init__(self,a,b):
        self.num = a
        self.num2 = b

v1 = test(1,2)
v2 = test(3,5)
v3 = test(7,2)
v4 = test(8,1)

vs = [v1,v2,v3,v4]

vs.sort(key=lambda test : test.num, reverse = True)

for i in vs :
    print(i.num)