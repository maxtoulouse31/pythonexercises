if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    topscore = list(arr)
    topscore.sort()
    topscore.reverse()
    removeme = (max(topscore))
    while removeme in topscore:
        for i in topscore: 
            if i == removeme: topscore.remove(i)
    print (topscore[0])
    
