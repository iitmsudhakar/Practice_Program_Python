n=int(input()) 
station_dict={} 

for i in range(n): 
    m=input() 
    a=int(input()) 
    d={} 
    for i in range(a): 
        s=input().split(',') 
        d[s[0]]=int(s[1]) 

station_dict[m]=d 
