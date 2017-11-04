def longestprefixNumbers(inp):
	i=0
	d=""
	while i<=(len(inp)-1) and 48<= ord(inp[i]) <=57 :
		d+=inp[i]
		i+=1
	return d
