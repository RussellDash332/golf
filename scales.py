def scales(n):[*map(print,[' _  '*n,('_/ \\'*n)[1:],*['  '*i+'\_/ '*(n-i)for i in range(n)]])]