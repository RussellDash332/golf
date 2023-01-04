class COVID:
 def __init__(s,n,l={1}):s.n,s.l=n,l|{s}
 mutate=lambda s,n:COVID(n,s.l)
class Person:
 def __init__(s,n):s.n,s.m,s.f=n+' ',{1},[]
 infect,recover,meet=lambda s,v:s.n+[k:={v}&s.m,'is immune to 'if k else[s.m.update(v.l),s.f.append(v),'contracted '][2]][1]+v.n,lambda s:s.n+['is COVID negative','recovers from COVID',k:=bool(s.f),s.f.clear()][k*1],lambda s,o:[[p.infect(v)for p in[s,o]for v in s.f+o.f],None][1]