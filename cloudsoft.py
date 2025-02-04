import json
import os

class UserProfile:
    def __init__(self, username, settings=None):
        self.username = username
        self.settings = settings if settings else {
            'theme': 'light',
            'wallpaper': 'default.jpg',
            'notifications': True,
            'auto_update': True
        }

    def update_setting(self, key, value):
        if key in self.settings:
            self.settings[key] = value
            print(f"Updated {key} to {value} for {self.username}.")
        else:
            print(f"Setting {key} not found for {self.username}.")

    def get_settings(self):
        return self.settings


class CloudSoft:
    def __init__(self, data_file='user_profiles.json'):
        self.data_file = data_file
        self.user_profiles = self.load_profiles()

    def load_profiles(self):
        if os.path.exists(self.data_file):
            with open(self.data_file, 'r') as file:
                return json.load(file)
        return {}

    def save_profiles(self):
        with open(self.data_file, 'w') as file:
            json.dump(self.user_profiles, file, indent=4)
        print("User profiles saved.")

    def create_user_profile(self, username):
        if username in self.user_profiles:
            print(f"User profile for {username} already exists.")
        else:
            self.user_profiles[username] = UserProfile(username).__dict__
            self.save_profiles()
            print(f"User profile for {username} created.")

    def update_user_setting(self, username, key, value):
        if username in self.user_profiles:
            user_profile = UserProfile(username, self.user_profiles[username]['settings'])
            user_profile.update_setting(key, value)
            self.user_profiles[username] = user_profile.__dict__
            self.save_profiles()
        else:
            print(f"User profile for {username} does not exist.")

    def get_user_settings(self, username):
        if username in self.user_profiles:
            return self.user_profiles[username]['settings']
        else:
            print(f"User profile for {username} does not exist.")
            return None

# Example usage:
if __name__ == "__main__":
    cloud_soft = CloudSoft()
    cloud_soft.create_user_profile("john_doe")
    cloud_soft.update_user_setting("john_doe", "theme", "dark")
    settings = cloud_soft.get_user_settings("john_doe")
    print(f"John Doe's settings: {settings}")