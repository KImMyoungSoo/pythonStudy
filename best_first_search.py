class queue :
    def __init__(self):
        self.queue = []
        
    def put(self,obj):
        self.queue.append(obj)
        # self.queue.sort(ket = lambda node : node.bound reverse = True)

    def delItem(self) :
        del(self.queue[0])

    def getItem(self) :
        node = self.queue[0]
        return node

    def isempty(self) :
        if not self.queue :
            return False
        else :
            return True
    
    def qSize(self) :
        return len(self.queue)


    # def printQueue(self) :
    #     for i in self.queue :
    #         print(i, end=' ')
    
class item :
    def __init__(self, a, b):
        self.price = a
        self.weight = b
        self.per = int(self.price/self.weight)

class node :
    def __init__(self):
        self.level = 0
        self.profit = 0
        self.weight = 0
        self.bound = 0
        
    def setdata(self,lvl,pro,wei):
        self.level = lvl
        self.profit = pro
        self.weight = wei
    
    def setbound(self, bou):
        self.bound = bou

def calBound(node,items):
    j=0
    k=0
    totweight = 0
    i = node.level
    profit = node.profit
    weight = node.weight

    j = i+1
    bound = profit
    totweight = weight
    while(j<=n and totweight+items[j].weight<=W):
        totweight = totweight + items[j].weight
        bound = bound + items[j].price
        j = j+1
    k=j
    if(k<=n):
        bound = bound + (W-totweight)*items[k].per
    return bound

# def makeTree(items):
#     v = node(0,0,)
    

def best_first_search(n, items, W):
    pq = queue()
    v = node()
    u = node()
    v.setdata(0,0,0)
    v.setbound(calBound(v,items))
    maxprofit = 0
    pq.put(v)
    while(pq.isempty()) :
        # print(pq.isempty())
        pq.delItem()
        print(pq.isempty())
        if (v.bound > maxprofit) :
            u.setdata(v.level+1,v.profit + items[u.level+1].price,v.weight + items[u.level+1].weight)

            if (u.weight<= W) and (u.profit>maxprofit):
                maxprofit = u.profit
                print(u.profit, u.weight)
            
            u.setbound(calBound(u,items))

            if(calBound(u,items) > maxprofit):
                pq.put(u)

        u.weight = v.weight
        u.profit = v.profit
        u.setbound(calBound(u,items))

        if(u.bound > maxprofit):
            pq.put(u)
    print(2)


if __name__ == "__main__":
    W = 16
    n = 4

    item1 = item(40,2)
    item2 = item(30,5)
    item3 = item(50,10)
    item4 = item(10,5)

    items = [0,item1,item2,item3,item4,0]

    best_first_search(n,items,W)



    # items.sort(key = lambda item : item.price)
    
    # print(items)
    
    # print(items[0].price)
    

    # test
    # v = node()
    # v.setdata(0,0,0)

    # v.setbound(calBound(v,items))
    # print(v.bound)