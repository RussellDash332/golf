class Token:
 def __init__(s,*a):s.i,s.m=a
class Wallet:
 get_balance=lambda s:s.a
 def __init__(s,*a):s.d,s.a=a;s.t=[]
 def token_bought(s,t,p):s.t+=[t];s.a-=p
 def token_sold(s,t,p):s.t.remove(t);s.a+=p
 def sell(s,b,p,i):
  if i not in[t.i for t in s.t]:return f'NFT #{i} does not exist in wallet {s.d}.'
  if b.get_balance()<p:return'Buyer does not have enough funds to make the purchase.'
  t=[x for x in s.t if x.i==i][0];s.token_sold(t,p);b.token_bought(t,p);return f'NFT #{i} transferred from wallet {s.d} to wallet {b.d}.'
class Contract:
 def __init__(s,*a):s.n,s.v,s.l=a
 def mint(s,w,n):
  if n*s.v>w.get_balance():return'Buyer does not have enough funds to mint.'
  if n<1:return'You need to mint at least one NFT.'
  if n>len(s.l):return'Max supply of NFTs exceeded.'
  o,c=[],"t=Token(*s.l.pop(0));w.token_bought(t,s.v);o+=[f'NFT #{t.i} minted to wallet {w.d}, '];"*n;exec(c);return''.join(o)