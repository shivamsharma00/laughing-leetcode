def findCheapFlight(n, flight, src, dist, k):

    tempList = [[99999] * n for _ in range(n)]
    
    for j in range(n):
        tempList[0][j] = 0       

    for vertex in range(1, k):
        for j in range(n):
            
            for i in flight:
                
                s = i[0]
                d = i[1]
                w = i[2]
                # print(s, d)
                if src == j and dist == d:
                    print(f"j-{j}, node-{node}")
                    tempList[j][node] = min(tempList[j][node], tempList[j-1][node+1]+w)
                

    for i in tempList:
        print(i)

if __name__ == '__main__':
    n = 4
    flights = [[0,1,100], [1,2,100], [2,0,100], [1,3,600], [2,3,200]]
    src = 0
    dist = 3
    k = 1
    findCheapFlight(n, flights, src, dist, k)