def topk_expensive_neighbourhoods(f,k):
 r,d=read_csv(f)[1:],{}
 for w in r:s=int(w[6]);d[s]=d.get(s,[])+[eval(w[0])/int(w[3])]
 l=sorted([(-round(sum(d[t])/len(d[t]),2),t)for t in d]);return[(b,-a)for a,b in l if a<=l[:k][-1][0]]