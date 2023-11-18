class Student:
 def __init__(s,n):s.n=n;s.p=0
 get_name=lambda s:s.n;get_points=lambda s:s.p
 def add_points(s,p):s.p+=p
class Resident(Student):
 def __init__(s,n):super().__init__(n);s.c=0
 get_points=lambda s:s.c+super().get_points();get_cca_points=lambda s:s.c;participate=lambda s,a:[exec('s.c+=a.get_points()'),f'{s.get_name()} participated in {a.get_name()}.'][1]