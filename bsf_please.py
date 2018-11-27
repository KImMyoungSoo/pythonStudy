n = 4
W = 16
p=[0,40,30,50,10,0]
w=[0,2,5,10,5,0]

class queue :
    def __init__(self):
        self.queue = []
        
    def put(self,obj):
        self.queue.append(obj)
        self.queue.sort(key = lambda node : node.bound, reverse = True)

    def getItem(self) :
        for i in range(0,len(self.queue)) :
            if(self.queue[i].weight <= W and self.queue[i].level <= n):
                break
        node = self.queue[i]
        # self.queue = self.queue[i:]
        if(len(self.queue)<=i):
            i = len(self.queue) - 1
        del(self.queue[i])
        return node.level, node.profit, node.weight

    def delItem(self) :
        del(self.queue[0])

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
        
def calBound(node):
    j=0
    k=0
    totweight=0
    i = node.level
    profit = node.profit
    weight = node.weight

    j = i + 1
    bound = profit
    totweight=weight
    while(j<=n and totweight+w[j]<=W):
        totweight = totweight + w[j]
        bound = bound + p[j]
        j = j + 1
    k=j
    if(k<=n):
        bound = bound + (W - totweight)*(p[k]/w[k])
    return bound

def best_first_search(tq):
    pq = queue()
    v = node()
    u = node()
    maxprofit = 0
    count = 0
    v.setbound(calBound(v))
    pq.put(v)
    while(not pq.isempty()):
        count = count + 1
        pq.printQueue()
        lvl, pro, wei = pq.getItem()
        # v = node()
        v.setdata(lvl,pro,wei)
        if(v.level >= n):
            break
        if(v.bound > maxprofit):
            level = v.level
            u = node()
            u.setdata(level+1,v.profit+p[level+1],v.weight+w[level+1])

            if(u.weight <= W and u.profit > maxprofit):
                maxprofit = u.profit
            u.setbound(calBound(u))
            if(u.bound > maxprofit):
                pq.put(u)
                tq.put(u)
            level = u.level
            u = node()
            u.setdata(level,v.profit,v.weight)
            u.setbound(calBound(u))
            u.printnode()
            if(u.bound > maxprofit):
                pq.put(u)
                tq.put(u)
    return maxprofit, count

if __name__ == "__main__":

    tq = queue()
    rq = queue()

    maxpro, count = best_first_search(tq)

    print("------------------------------")
    for i in range(0,len(tq.queue)) :
            if(tq.queue[i].weight <= W and tq.queue[i].level <= n):
                rq.put(tq.queue[i])

    rq.queue.sort(key = lambda node : node.profit, reverse = True)

    resultnode = node()
    resultnode = rq.queue[0]

    print("node(level,price,weight,bound) :",end=' ')
    resultnode.printnode()

    print("maxprofit :", maxpro)
    print("count :", count)
