class Gym:
 def __init__(s,n,l):s.n=n;s.l=l;s.d=[];s.t={};s.defenders=lambda:[p.n for p in s.d if p.d[-1]==s]
class Pokemon:
 def __init__(s,n):s.n=n;s.d=[0];s.train=lambda g:g.t.update({s:g.t.get(s,0)+1})or f'{s.n} {["has completed training", "trains"][g.t[s]<g.l]} at {g.n}';s.defend=lambda g:f'{s.n} is too weak to defend {g.n}'if g.t.get(s,0)<g.l else g.d.append(s)or s.d.append(g)or f'{s.n} defends {g.n}'