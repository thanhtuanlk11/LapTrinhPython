def dictionairy():

	# Declaring the hash function
	key_value = {}

# Initialize value
	key_value[2] = 56
	key_value[1] = 2
	key_value[5] = 12
	key_value[4] = 24
	key_value[6] = 18
	key_value[3] = 323
	
	print("key_value",key_value)

	print("Task 2:-\nKeys and Values sorted in",
		"alphabetical order by the key ")
	
	for i in sorted(key_value):
		print((i, key_value[i]), end=" ")


def main():
		# function calling
	dictionairy()


# main function calling
if __name__ == "__main__":
	main()
