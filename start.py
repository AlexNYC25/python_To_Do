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
	choice_Decision(choice)
	return;

# set codntion for if number is not one of the options specified
def choice_Decision(x):
	if (int(x) == 1):
		printAll()
	if (int(x) == 2):
		newItem()
	if (int(x) == 3):
		deleteItem()
	if (int(x) == 4):
		return;
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
def deleteItem():
	toBeDeleted = input("What item number would you like to delete: ")

	count = 0
	with open("schedule.txt","w") as f:
		f_txt = f.readlines()
		del f_txt[toBeDeleted-1]

	return;

# divider for start and end of list of items
# TODO: instead of a fixed size instead make it to be the size of the length of the biggest item in list
def divSec():
	for x in range(10):
		print("*", end = '')
	print()

start_Message()