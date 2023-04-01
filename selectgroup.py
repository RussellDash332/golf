p=lambda t:':'>t[:3][-1]!=exec('m[t[1]]={*t[3:]}')or m.get(k:=t.pop(0))or eval('p(t).'+k)(p(t));m={}
for l in open(0):r=p(l.split());r!=1==print(*sorted(r))