x = 'Hello World'
print(type(x))

# Indexing
greeting = 'Hello'
print(greeting[0])

# Reverse Indexing
print(greeting[-1])

# Slicing - Upto but not including stop
sliced_greeting = greeting[0:3]
print(sliced_greeting)

# Step size
sliced_step_size_greeting = greeting[::2]
print(sliced_step_size_greeting)

# Reverse
reversed_greeting = greeting[::-1]
print(reversed_greeting)

# Length
greeeting_length = len(greeting)
print(greeeting_length)

# Methods
print(x.upper())

# Split
print(x.split())

# Print formatting
# Interpolation
print(greeting + ' World')
# .format()
print('{} World'.format(greeting))
# .format() indexed
print('{1} of the {0}'.format('morning', 'top'))
# .format named
print('{ab} dias {cd}'.format(ab = 'buenos', cd= 'muchachos'))
# f strings
print(f'{greeting} is {greeeting_length} characters long')