stuff = []
#This allows the user to input the 5 items in the array
for i in range(5):
    item = input("Enter item number {}: ".format(i + 1))
    stuff.append(item)

#prints the list of items the user entered
print("The original list of items you entered is:",end= " ")
for i in range(len(stuff) - 1):
    print(stuff[i], end= ", ")
print(f'and {stuff[4]}.')

#Asksthe user to input an item to be changed in the list and which item should be changed
updateItem = int(input("Enter the index you would like to update: "))
while updateItem < 0 or updateItem > 4:
    print("Please enter a valid index between 0 and 4.")
    updateItem = int(input("Enter it again: "))
updatedIndex = input("Enter the new item to replace the old item: ")

#Picks a slice and it's range
sliceRange1 = int(input("Enter the starting index of the slice: "))
while sliceRange1 < 0 or sliceRange1 > 4:
    print("Please enter a valid starting index between 0 and 4.")
    sliceRange1 = int(input("Enter it again: "))
sliceRange2 = int(input("Enter the ending index of the slice: "))
while sliceRange2 < 0 or sliceRange2 > 4:
    print("Please enter a valid ending index between 0 and 4.")
    sliceRange2 = int(input("Enter it again: "))
stuff_but_smaller = stuff[sliceRange1:sliceRange2]
#Asks the user to input a search item
itemSearch = input("Enter your search item in the slice: ")
print("")

#Output
print(f'The index to update is {updateItem}, being replaced with {updatedIndex}.')
stuff[updateItem] = updatedIndex

print('The slice of the list you selected is between index {} and {}.'.format(sliceRange1, sliceRange2 - 1))
for i in range(len(stuff_but_smaller) - 1):
    print(stuff_but_smaller[i], end= ", ")
print(f'and {stuff_but_smaller[-1]}.')

if itemSearch in stuff_but_smaller:
    print(f'Item "{itemSearch}" is found in the slice.')
else:
    print(f'Item "{itemSearch}" is not found in the slice.')

print("The new list of items is: ", end= " ")
for i in range(len(stuff) - 1):
    print(stuff[i], end= ", ")
print(f'and {stuff[-1]}.')