top_K_disproportionate_courses=lambda k,y,f:[d:={},[d.update({r:d.get(r,[])+[int(i)]})for x,_,r,i,_ in read_csv(f)[1:]if int(x)==y],s:=sorted([-round(abs(b-c)/(b+c),2),a]for a,(b,c)in d.items()),[(b,-a)for a,b in s if a<=s[:k][-1][0]]][3]