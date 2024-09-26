import json

class InstaFollowTracker:
    def __init__(self, followers_file, following_file):
        self.followers_file = followers_file
        self.following_file = following_file

    def load_data(self):
    
        with open(self.followers_file) as f:
            insta_followers = json.load(f)
        self.followers = self.extract_values(insta_followers)

        with open(self.following_file) as f:
            insta_following = json.load(f)
        self.following = self.extract_values(insta_following.get('relationships_following', []))

    def extract_values(self, data_list):
        values = []
        for item in data_list:
            string_list = item.get('string_list_data', [])  # Get the string_list_data safely

            for string_data in string_list:
                value = string_data.get('value')  # Safely get the 'value' field
        
            if value:  # If 'value' exists
                values.append(value)
        return values
    
    def find_non_followers(self):
        return list(set(self.following) - set(self.followers))
    
    def display_non_followers(self):
        non_followers = self.find_non_followers()
        print("These are the accounts that are not following me:\n", *non_followers, sep='\n')
        print('\n')


#Usage
followers_file = '/Users/File_Path/followers_and_following/followers_1.json'
following_file = '/Users/File_Path/followers_and_following/following.json'

tracker = InstaFollowTracker(followers_file, following_file)
tracker.load_data()
tracker.display_non_followers()
