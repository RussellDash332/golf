year_of_max_graduates=lambda c,f:max([d:={},[d.update({int(y):d.get(int(y),0)+int(g)*(c==r)})for y,_,r,_,g in read_csv(f)[1:]]][0].items(),key=lambda x:x[::-1])