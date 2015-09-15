# find length of a list without using len()

def lenlst(lst):
	#base case (fail statement)
	if lst == 0:
		return 0

	#Go through lst and return count of how many items
	return 1 + lst[1:]

lenlst([5,6,7,9])