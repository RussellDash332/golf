class Product:
 def __init__(s,*a):s.n,s.p=a
 get_price=lambda s:s.p
class DiscountedProduct(Product):
 def __init__(s,n,p,d):super().__init__(n,round(p-p*d/100,2))
class Cart:
 def __init__(s):s.c={};s.checkout=lambda:s.c;s.add_item=lambda t:[s.c.update({t.n:s.c.get(t.n,0)+t.get_price()}),f'Adding {t.n} to the cart.'][1]if isinstance(t,Product)else'Invalid item.'