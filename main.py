def find_candies(pinatas):
    n = len(pinatas)
    max_candies = 0

    for i in range(n):
        left = pinatas[i-1] if i > 0 else 1
        right = pinatas[i+1] if i < n-1 else 1
        current_candies = left * pinatas[i] * right
        max_candies = max(max_candies, current_candies)

    return max_candies


while (True):
	pinatas = list(map(int, input("Enter the array of nums separated by space: ").split()))
	result = find_candies(pinatas)
	print("Maximum amount of candies:", result)
	if (input("Do you want to run the program again? (y/n): ").lower() != 'y'):
		break
