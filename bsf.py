n=4
p=[0,40,30,50,10,0]
w=[0,2,5,10,5,0]
pw=[0,20,6,5,2,0]
include = [0,0,0,0,0,0,0,0,0,0,0,0]
W=16
bound=115
maxprofit=0
bestset = []
def promising(i,profit,weight):
    j=0
    k=0
    totweight=0
    if(weight>=W):
        return 0
    else :
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
        if(bound>maxprofit):
            return 1
        else:
            return 0

def knapsack(i,profit,weight):
    numbest = 0
    global maxprofit
    global bestset, include
    if(i<=n):
        if(weight<=W and profit > maxprofit):
            print(include, "weight:",weight, "maxprofit:",profit)
            maxprofit = profit
            numbest = i
            bestset = include

        if(promising(i,profit,weight)==1):
            include[i+1] = "yes"
            knapsack(i+1,profit+p[i+1],weight+w[i+1])
            include[i+1] = "no"
            knapsack(i+1,profit,weight)
        
knapsack(0,0,0)