M='mounted ';Z=f'Nothing {M}at ';E=exec
class Part:
 def __init__(s,n,x):s.n=n;s.x=x;s.t=s.m=0
class Satellite:
 def __init__(s,n,*p):s.n=n;s.o={x:0for x in p};s.mount=lambda p,*t:f'{p.n} already {M}on {p.m[0].n}'if p.m else'Wrong number of points'if len(t)!=p.x else f'Point {v[0]} is not available'if(v:=[x for x in t if s.o[x]])else[E('p.m=[s,t]'),s.o.update({x:p for x in t}),f'{p.n} successfully {M}on {s.n}'][2];s.unmount=lambda t:f'{Z}{t}'if(p:=s.o[t])==0else[s.o.update({x:0for x in p.m[1]}),E('p.m=0'),f'{p.n} un{M}from {s.n}'][2];s.test=lambda t:f'{Z}{t}'if(p:=s.o[t])==0else[E('p.t+=1'),f'{p.n} test count is {p.t}'][1]