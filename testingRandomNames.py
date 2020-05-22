import random
import time

def choose_name_from_list(name):
	"""insert the name of a list to randomly choose """
	choose_name = random.choice(name)
	#a sleep delay is added to see progam run
	time.sleep(3)
	return choose_name

#list of names to be passed in choose_name function
names  = ['achilles', 'espy','achilles jr', 'mike', 'mikayla', 'trey','jackie', 'joann']

#dictionary list compreshenion to inster values of zero
count_dict = {i:0 for i in names}

#get number from person to execute random number of time a name to be picked
choose = int(input("pick a number 1 -10: "))
print(f"the first one to get picked {str(choose)} times will win\n")

#run while loop until choose is satisfied the number given
while choose:
        if choose > 10:
                print("You must pick a number 1-10 please program terminated")
                break
        #randomly pick a name from a list
        random_choice = choose_name_from_list(names)

        #check if name in dictionary that is made and add to value of that name increments of 1
        if random_choice in count_dict:
                count_dict[random_choice] += 1
        if count_dict[random_choice] >= choose:
                break
        
        print(count_dict)
        print("\n")

#a for loop to print out the actual winner
for key, value in count_dict.items():
        if value == choose:
                print(f"The winner is {key.title()} with {value} picks")

#print final conclusion
print(f"totals: {count_dict}")
