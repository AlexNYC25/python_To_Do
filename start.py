# currently todo list is only as a simple list that is not saved, possibly use txt or sqlite
# fix txt list open and close


totalItems = []

# to be removed
'''
try:
	txtList = open("schedule.txt", "a")
except IOError:
	print("There is a problem")
'''


def start_Message():
	print("What would you like to do today")
	print("1. View current list")
	print("2. Add new item")
	print("3. Delete item")
	print("4. End program")

	choice = input()
	

	# error catching to enusre an int value is passed
	try:
		print(int(choice))
	except ValueError:
		print("not valid")
		start_Message()
		return;

	choice_Decision(choice)
	return;

# set codntion for if number is not one of the options specified
def choice_Decision(x):
	if(int(x) > 4):
		print("\nnope try again\n")

	if (int(x) == 1):
		printAll()
	if (int(x) == 2):
		newItem()
	if (int(x) == 3):
		deleteItem()
	if (int(x) == 4):
		return;
	else:
		start_Message()
	return;

def newItem():
	tempItem = input("What would you like to add: ")
	# totalItems.append(tempItem)
	# old code to be deleted
	#txtList.write("\n"+str(tempItem))

	with open("schedule.txt", "a") as txtList:
		print(tempItem, file=txtList)
		#txtList.write("\n"+str(tempItem))

	return;

# TODO: fix numering system from (0,1,...) to (1,2,...)
def printAll():
	divSec()

	with open("schedule.txt", "r") as txtList:
		count = 0
		for line in txtList:
			if not line.isspace():
				count += 1
				print(str(count) + ": " + line)
		


	# old iterator for local list
	'''
	for x in range(len(toalItems)):
		print(str(x)+". ", end='')
		print(totalItems[int(x)])
	'''
	divSec()

# TODO: fix numering system from (0,1,...) to (1,2,...)
# ISSSUE: having problems deleting item from txt line
def deleteItem():
	toBeDeleted = input("What item number would you like to delete: ")

	with open("schedule.txt","r") as f:
		# get list of items in txt file 
		f_txt = f.readlines()

		with open("schedule.txt", "w") as current:
			print("", file=current)

		del f_txt[int(toBeDeleted)]

		# currently works in editing a list of items, and deleting a specific value
		# next is to add items one at a time 
		# print(f_txt)

		# loads all values back in. except for 0, since it is ""
		with open("schedule.txt", "a") as newFILE:
			for l in range(1, len(f_txt)):
				print(f_txt[l], file = newFILE)

	'''
	currently this code shows that the entire txt file in empty
	with open("schedule.txt", "r") as toBeRead:
			for line in toBeRead:
				print(line)	
	'''

	return;

# divider for start and end of list of items
# TODO: instead of a fixed size instead make it to be the size of the length of the biggest item in list
def divSec():
	for x in range(10):
		print("*", end = '')
	print()

start_Message()