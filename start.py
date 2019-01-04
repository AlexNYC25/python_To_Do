# currently todo list is only as a simple list that is not saved, possibly use txt or sqlite

totalItems = []

try:
	txtList = open("schedule.txt", "a")
except IOError:
	print("There is a problem")


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
	totalItems.append(tempItem)
	txtList.write("\n"+str(tempItem))
	return;

# TODO: fix numering system from (0,1,...) to (1,2,...)
def printAll():
	divSec()
	for x in range(len(totalItems)):
		print(str(x)+". ", end='')
		print(totalItems[int(x)])
	divSec()

# TODO: fix numering system from (0,1,...) to (1,2,...)
def deleteItem():
	toBeDeleted = input("What item number would you like to delete: ")
	del totalItems[int(toBeDeleted)]
	return;

# divider for start and end of list of items
# TODO: instead of a fixed size instead make it to be the size of the length of the biggest item in list
def divSec():
	for x in range(10):
		print("*", end = '')
	print()

start_Message()