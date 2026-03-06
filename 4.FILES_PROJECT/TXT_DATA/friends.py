# Ask the user for a list of 3 friends
# For each friend, we'll tell the user whether they are nearby
# For each nearby friend, we'll save their name to `nearby_friends.txt' 
import os
script_dir = os.path.dirname((os.path.abspath(__file__)))
people_path = os.path.join(script_dir, 'people.txt')
nearby_path = os.path.join(script_dir,'nearby_friends.txt')


friends = input('Enter three friend names, separated by commas (no spaces, please): ').split(',')
# ['rolf', 'santi', 'charlie'] esto hace split

people = open(people_path, 'r')
#people_nearby = people.readlines() # [line1,line2,line3,line4]
people_nearby = [line.strip('\n') for line in people.readlines()]
people.close()

friends_set = set(friends)
people_nearby_set = set(people_nearby)

friends_neraby = friends_set.intersection(people_nearby_set)


nearby_friends = open(nearby_path, 'w')

for friend in friends_neraby:
    print(f'{friend} is nearby! Meet up with them.')
    nearby_friends.write(f'{friend}\n')

nearby_friends.close()