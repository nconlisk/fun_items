import random

########################################################
#                                                      #
#                Author: Noel Conlisk                  #
#               Email: noecon@gmail.com                #
#        Script function: A secret Santa script        #
#                                                      #
########################################################

# Setup input parameters

# Customise names for your draw.

people_list_1 = ['John', 'Jane', 'Bob', 'Mary']

# people_list_2 = people_list_1[:]  # Generates a copy of name list.
people_list_2 = list(people_list_1)

random.shuffle(people_list_2)  # Randomly shuffles copied list.

pairs = []

# Set up matching logic:

a = len(people_list_1)

for i in range(a):
    pair_1 = people_list_1[i]
    pair_2 = people_list_2[i]
    # Below code added to prevent individual names matching with themselves.
    if pair_1 == pair_2:
        people_list_2 += [people_list_2.pop(i)]
        pair_2 = people_list_2[i]
        pairs.append((pair_1, pair_2))
    else:
        pairs.append((pair_1, pair_2))

# Print pairs drawn.
for i in range(len(pairs)):
    message = "%s is matched with %s" % (pairs[i][0], pairs[i][1])
    print(message + "\n")
