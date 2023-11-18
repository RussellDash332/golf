M='mounted ';Z=f'Nothing {M}at '
class Part:
 def __init__(s,n,x):s.n=n;s.x=x;s.t=0;s.m=0;s.p=0
class Satellite:
 def __init__(s,n,*p):s.n=n;s.o={x:0for x in p}
 def mount(s,p,*t):
  if p.m:return f'{p.n} already {M}on {p.m.n}'
  if len(t)!=p.x:return'Wrong number of points'
  if(v:=[x for x in t if s.o[x]]):return f'Point {v[0]} is not available'
  p.p=t;p.m=s;s.o.update({x:p for x in t});return f'{p.n} successfully {M}on {s.n}'
 def unmount(s,t):
  if(p:=s.o[t])==0:return f'{Z}{t}'
  p.m=0;s.o.update({x:0for x in p.p});p.p=0;return f'{p.n} un{M}from {s.n}'
 def test(s,t):
  if(p:=s.o[t])==0:return f'{Z}{t}'
  p.t+=1;return f'{p.n} test count is {p.t}'