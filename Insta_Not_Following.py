import json

followers_file = '/Users/irvindorado/Documents/Coding/Python/followers_and_following/followers_1.json'
following_file = '/Users/irvindorado/Documents/Coding/Python/followers_and_following/following.json'

with open(followers_file) as f:
    insta_followers = json.load(f)
#print(insta_followers, '\n')

with open(following_file) as f:
    insta_following = json.load(f)
#print(insta_following)

followers = []

for item in insta_followers:
    string_list = item.get('string_list_data', [])  # Get the string_list_data safely
    #print(string_list)

    for string_data in string_list:
        value = string_data.get('value')  # Safely get the 'value' field
        #print(value)
        
        if value:  # If 'value' exists
            followers.append(value)


following_list = insta_following.get('relationships_following', []) #nested
following = []

for item in following_list:
    string_list = item.get('string_list_data', [])  # Get the string_list_data safely

    for string_data in string_list:
        value = string_data.get('value')  # Safely get the 'value' field
        
        if value:  # If 'value' exists
            following.append(value)

not_following_me = list(set(following) - set(followers))

print("These are the accounts that are not following me:\n", *not_following_me, sep='\n')
print('\n')