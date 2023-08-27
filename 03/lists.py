my_list = [1,2,3]
print(my_list)

# Length
print(len(my_list))

# Indexing
print(my_list[0])
print(my_list[1::])

# Concatenating
new_list = [4,5,6]
even_newer_list = my_list + new_list
print(even_newer_list)

# Mutation
even_newer_list[0] = 10
print(even_newer_list)

# Add element
even_newer_list.append(7)
print(even_newer_list)

# Remove element
even_newer_list.pop()
print(even_newer_list)

# Indexed removal
even_newer_list.pop(3)
print(even_newer_list)

# Sort
even_newer_list.sort()
print(even_newer_list)

alpha_list = ['a','z','x','b']
alpha_list.sort()
print(alpha_list)

# Reverse
alpha_list.reverse()
print(alpha_list)