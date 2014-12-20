def revlist(listsam):
	print listsam[-1]
	if len(listsam) == 1:
		print listsam
		print "if"
		return listsam
	else:
		print listsam 
		print "else"
		return [listsam.pop()]+ revlist(listsam[0:])

# def revlist(listsam):
# 	item1=listsam[-1]
# 	print item1
# 	print listsam

# 	item2=listsam[0:-1]
# 	print item2
# 	print listsam

# 	print [listsam[-1]] + listsam[0:-1]

print revlist([1,2,14,3])