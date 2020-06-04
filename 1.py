'''有四个数字：1、2、3、4，能组成多少个互不相同且无重复数字的三位数？各是多少？'''

x=0
for i in range(1,5):
	for j in range(1,5):
		for k in range(1,5):
			if (i!=j)and(j!=k)and(i!=k):
				x=x+1
				sum = i*100+j*10+k
				print(sum)
print(x)
print("能组成{m}个".format(m=x))
