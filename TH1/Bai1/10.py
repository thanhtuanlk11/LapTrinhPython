a = int(input("nhập 1 số : "))
n1 = int( "%s" % a )
n2 = int( "%s%s" % (a,a) )
n3 = int( "%s%s%s" % (a,a,a) )
print ("Giai thừa là " , n1+n2+n3)