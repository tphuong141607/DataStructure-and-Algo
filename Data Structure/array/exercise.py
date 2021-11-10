#------------#
# Exercise 2 #
#------------#
print('--------- Exercise 2 -----------')
heros = ['spider man', 'thor', 'hulk', 'iron man', 'captain america']

# 1. Length of the list
print('Length of the heros list is: ', len(heros))

# 2. Add 'black panther' at the end of this list
heros.append('black panther')
print('heros after 2: ', heros)

# 3. Move 'black panther' to after hulk
heros.pop()
heros.insert(3, 'black panther')
print('heros after 3: ', heros)

# 4. Replace thor and hulk, replace them with doctor strange (in 1 line of code)
heros[1 : 3] = ['doctor strange']
print('heros after 4: ', heros)

# 5. Sort the heros list in alphabetical order 
heros.sort()
print('heros after 5: ', heros)

#------------#
# Exercise 3 #
#------------#
# Create a list of all odd numbers between 1 and a max number. Max number is something you need to take from a user using input() function and
print('\n--------- Exercise 3 -----------')
max = int(input("Enter max number: "))
odd_numbers = []

for i in range(1, max, 2):
    odd_numbers.append(i)

print(odd_numbers)

