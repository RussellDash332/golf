results=lambda y,f,k=dict.__setitem__:[z:={},r:=[x for x in read_csv(f)if str(y)==x[0]],h:={s[1]:{}for s in r},[k(h[s],c,h[s].get(c,0)+int(v))for _,s,_,c,_,v in r],[[a:=max(h[s],key=h[s].get),k(z,a,z.get(a,0)+1)]for s in h]][0]