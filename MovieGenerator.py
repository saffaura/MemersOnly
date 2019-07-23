import random

def again(res):
	res = res.lower()
	return res == "yes" or res == "y" or res == "Y"

min = 0
max = 101
res = "y"

while again(res):
    
	num = random.randint(min, max)
	
	with open("movies.txt") as file:
		for i, line in enumerate(file):
			if i == num:
				print("\nJack has not seen: " + line.strip());
				break;
	
	res = raw_input("Continue? ")
