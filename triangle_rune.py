triangle_rune=t=lambda p,n:beside_frac(1/n,stackn(v:=2*n-1,p),(f:=stack_frac)(1-1/v,f(1/(v-1),b:=blank_bb,t(p,n-1)),b))if n>1 else p