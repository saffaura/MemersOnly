import random

def again(res):
	res = res.lower()
	return res == "yes" or res == "y" or res == "Y"

res = "y"
movies = []

with open("movies.txt") as file:
		for i, line in enumerate(file):
			movies.append(line.strip())

while again(res):
    
	num = random.randint(0, len(movies) - 1)
	
	print("\nJack has not seen: " + movies[num]);
	movies.pop(num);
	
	if len(movies) == 0:
		break;
	
	res = raw_input("Continue? ")
	
