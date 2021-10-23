#Question:
#1)
# # Create an empty dictionary: names_by_rank
#
#
# # Loop over the girl names
# for ____, ____ in ____:
#     # Add each name to the names_by_rank dictionary using rank as the key
#     ____
#
# # Sort the names_by_rank dict by rank in descending order and slice the first 10 items
# for rank in ____:
#     # Print each item
#     print(names_by_rank[rank])

#Instructions:
# Create an empty dictionary called names_by_rank.
# # Loop over female_baby_names_2012.items(), unpacking it into the variables rank and name.
# # Inside the loop, add each name to the names_by_rank dictionary using the rank as the key.
# # Sort the names_by_rank dictionary keys in descending order, select the first ten items. Print each item.


#Solve:
# # Create an empty dictionary: names_by_rank
# names_by_rank = {}
#
# # Loop over the girl names
# for rank, name in female_baby_names_2012.items():
#     # Add each name to the names_by_rank dictionary using rank as the key
#     names_by_rank[rank] = name
#
# # Sort the names_by_rank dict by rank in descending order and slice the first 10 items
#
# for rank in sorted(names_by_rank, reverse=True)[:10]:
#     # Print each item
#     print(names_by_rank[rank])

#2)
#solve:
# # Safely print rank 7 from the names dictionary
# print(names.get(7))
#
# # Safely print the type of rank 100 from the names dictionary
# print(type(names.get(100)))
#
# # Safely print rank 105 from the names dictionary or 'Not Found'
# print(names.get(105, 'Not Found'))

#3)
#solve:
# # Safely print rank 7 from the names dictionary
# print(names.get(7))
#
# # Safely print the type of rank 100 from the names dictionary
# print(type(names.get(100)))
#
# # Safely print rank 105 from the names dictionary or 'Not Found'
# print(names.get(105, 'Not Found'))


#4)
# # Assign the names_2011 dictionary as the value to the 2011 key of boy_names
# boy_names[2011]=names_2011
#
# # Update the 2012 key in the boy_names dictionary
# new_d={(1, 'Casey'), (2, 'Aiden')}
# boy_names[2012].update(new_d)
#
# # Loop over the years in the boy_names dictionary
# for year in boy_names:
#     # Sort the data for each year by descending rank and get the lowest one
#     lowest_ranked =  sorted(boy_names[year], reverse=True)[0]
#     # Safely print the year and the least popular name or 'Not Available'
#     print(year, boy_names[year].get(lowest_ranked,'Not Available'))

