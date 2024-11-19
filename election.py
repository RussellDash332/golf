class Candidate:
 def __init__(s,n):s.i=[1];s.v=[];s.get_name=lambda:n;s.count=lambda:len([x for x in s.v if x.c()==s]);a=' the election';s.withdraw=lambda:s.i.clear()or n+' withdraws from'+a;s.reinstate=lambda:s.i.append(1)or n+' is reinstated to run for'+a
class Voter:
 def __init__(s,*c):[x.v.append(s)for x in c];s.c=s.choice=lambda:next((x for x in c if x.i),None)