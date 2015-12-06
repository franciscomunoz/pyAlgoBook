
#!/usr/bin/python
#Optimization of page 44 printing ordered values
def factors(n):
	k = 1
	list = []
	while k*k < n:
		if n % k == 0:
			yield k
			list.append(n//k)
		k+=1
	if k * k == n:
		yield k
	i = len(list) - 1
	while i >= 0:
		yield(list[i])
		i-=1

for i in factors(100):
	print i

			
