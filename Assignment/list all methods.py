List
1)
list() Constructor
thislist = list(("apple", "banana", "cherry")) # note the double round-brackets
print(thislist)
output:
['apple', 'banana', 'cherry']

2)
Indexing:
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[-4:-1])
output:
['orange', 'kiwi', 'melon']

3)Change range of item values
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "mango"]
thislist[1:3] = ["blackcurrant", "watermelon"]
print(thislist)

output:
['apple', 'blackcurrant', 'watermelon', 'orange', 'kiwi', 'mango']
4) insert()
'''To insert a new list item, without replacing any of the existing values, we can use the insert() method.'''
thislist = ["apple", "banana", "cherry"]
thislist.insert(2, "watermelon")
print(thislist)

Output:
['apple', 'banana', 'watermelon', 'cherry']
5)append()
'''To add an item to the end of the list, use the append() method:'''
thislist = ["apple", "banana", "cherry"]
thislist.append("orange")
print(thislist)
Output:
['apple', 'banana', 'cherry', 'orange']
6)extend()
To append elements from another list to the current list, use the extend() method.
thislist = ["apple", "banana", "cherry"]
tropical = ["mango", "pineapple", "papaya"]
thislist.extend(tropical)# adding string 2 with string 1 and update string 1
print(thislist)
print(tropical)
Output:
['apple', 'banana', 'cherry', 'mango', 'pineapple', 'papaya']
['mango', 'pineapple', 'papaya']
7) remove()
The remove() method removes the specified item
thislist = ["apple", "banana", "cherry"]
thislist.remove("banana")
print(thislist)
Output:
['apple', 'cherry']
8)pop()
The pop() method removes the specified index.
The pop() method removes the specified index.
thislist = ["apple", "banana", "cherry"]
thislist.pop(1)
print(thislist)
Output:
['apple', 'cherry']
9)del keyword
The del keyword also removes the specified index:
The del keyword can also delete the list completely.
thislist = ["apple", "banana", "cherry"]
del thislist
10) clear()
The clear() method empties the list.
The list still remains, but it has no content.
thislist = ["apple", "banana", "cherry"]
thislist.clear()
print(thislist)

Output:
[]


11) Looping Using List Comprehension


thislist = ["apple", "banana", "cherry"]
[print(f"{x} is my fav fruit") for x in thislist]
Output:
apple is my fav fruit
banana is my fav fruit
cherry is my fav fruit


fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = []

[newlist.append(x) for x in fruits if "a" in x]

print(newlist)
Output:
['apple', 'banana', 'mango']

fruits = ["apple", "banana", "cherry", "kiwi", "mango"]

newlist = [x if x != "banana" else "orange" for x in fruits]#for banana , the value will be changed to orange

print(newlist)
output:
['apple', 'orange', 'cherry', 'kiwi', 'mango']
12)sort()
List objects have a sort() method that will sort the list alphanumerically, ascending, by default:
To sort descending, use the keyword argument reverse = True:



thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort()
print(thislist)
Output:
['banana', 'kiwi', 'mango', 'orange', 'pineapple']

thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort(reverse = True)
print(thislist)

Output:
['pineapple', 'orange', 'mango', 'kiwi', 'banana']
13)copy()
thislist = ["apple", "banana", "cherry"]
mylist = thislist.copy()
print(mylist)
output:
['apple', 'banana', 'cherry']
14)list()




List to list
thislist = ["apple", "banana", "cherry"]
mylist = list(thislist)
print(mylist)
output:

['apple', 'banana', 'cherry']

15) count()
points = [1, 4, 2, 9, 7, 8, 9, 3, 1]

x = points.count(9)
print(x)
output:
2
16)reverse()
fruits = ['apple', 'banana', 'cherry']

fruits.reverse()
print(fruits)

output:
['cherry', 'banana', 'apple']
17)index()
fruits = [4, 55, 64, 32, 16, 32]

x = fruits.index(32)
print(x)
output:
3
