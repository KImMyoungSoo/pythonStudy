class queue :
    def __init__(self,w,n):
        self.queue = []
        self.W = w
        self.n = n
        
    def put(self,obj):
        self.queue.append(obj)
        self.queue.sort(key = lambda node : node.bound, reverse = True)

    def delItem(self) :
        del(self.queue[0])

    def getItem(self) :
        for i in range(0,len(self.queue)) :
            if(self.queue[i].weight <= self.W and self.queue[i].level <= self.n):
                break
        # print("len queue :",len(self.queue))
        # print("i :",i)
        node = self.queue[i]
        node.printnode()
        self.queue = self.queue[i:]
        if(len(self.queue) <= i):
            i = len(self.queue)-1
        del(self.queue[i])
        return node.level, node.profit, node.weight

    def isempty(self) :
        if not self.queue : #empty
            return True
        else :
            return False
    
    def qSize(self) :
        return len(self.queue)


    def printQueue(self) :
        for i in self.queue :
            print("(",i.level,i.profit,i.weight,i.bound,")", end=' ')
        print()
        if not self.queue :
            print("empty queue")
    
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

    def printnode(self) :
        print("(",self.level,self.profit,self.weight,self.bound,")")

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
    

def best_first_search(n, items, W, rq):
    pq = queue(W,n)
    v = node()
    u = node()
    v.setdata(0,0,0)
    v.setbound(calBound(v,items))
    maxprofit = 0
    pq.put(v)
    count = 0
    while(not pq.isempty()):
        count = count + 1
        pq.printQueue()
        lvl, pro, wei = pq.getItem()
        v.setdata(lvl,pro,wei)
        if(v.level >= n):
            break
        if (v.bound > maxprofit) :
            level = v.level
            print("u :",end='')
            u.printnode()
            print("levle :",level)
            u = node()
            u.setdata(v.level+1,v.profit + items[level+1].price,v.weight + items[level+1].weight)
            print("ddd :",items[level+1].price, v.profit, level + 1)
            print("node :",end='')
            u.printnode()
            if (u.weight<=W and u.profit>maxprofit):
                maxprofit = u.profit
            
            u.setbound(calBound(u,items))
            print("bound :",end='')
            u.printnode()

            if(u.bound > maxprofit):
                # u.printnode()
                print("put :",end='')
                u.printnode()
                pq.put(u)
                rq.put(u)

            level = u.level    
            u = node()
            u.setdata(level,v.profit,v.weight)
            # u.level = level
            # u.weight = v.weight
            # u.profit = v.profit
            u.setbound(calBound(u,items))
            # print("node2 :",u.printnode())
            print("put2 :",end='')
            u.printnode()
            if(u.bound > maxprofit):
                pq.put(u)
                rq.put(u)
        pq.printQueue()
        print("------------------------------------")
    return maxprofit, count

if __name__ == "__main__":

    W = 16
    n = 4
    count = 0
    rq = queue(W,n)

    item1 = item(40,2)
    item2 = item(30,5)
    item3 = item(50,10)
    item4 = item(10,5)

    items = [0,item1,item2,item3,item4,0]

    maxpro, count = best_first_search(n,items,W,rq)

    print("--------------------------")

    rq.printQueue()
    print("--------------------------")

    cq = queue(W,n)
    
    for i in range(0,len(rq.queue)) :
            if(rq.queue[i].weight <= rq.W and rq.queue[i].level <= rq.n):
                cq.put(rq.queue[i])
    
    rq.queue = rq.queue[i:]
    
    cq.queue.sort(key = lambda node : node.profit, reverse = True)
    cq.printQueue()

    resultnode = node()

    resultnode = cq.queue[0]

    resultnode.printnode()


    print(maxpro)
    print(count)

    # items.sort(key = lambda item : item.price)
    
    # print(items)
    
    # print(items[0].price)
    

    # test
    # v = node()
    # v.setdata(0,0,0)

    # v.setbound(calBound(v,items))
    # print(v.bound)