import datetime
from time import sleep

class Database:
    def __init__(self):
        # initialize the database
        self.users = set()  # register user (case-insensitive)
        self.listings = {} # ID -> Information
        self.categories = {} # category -> listings[List]
        self.next_listing_id = 100001 # listing count

    def add_user(self, username):
        # add user (case-insensitive)
        if username in self.users:
            return False # user exist
        self.users.add(username)
        return True
    
    def add_listing(self, username, title, description, price, category):
        # return listing and return ID
        if username not in self.users:
            return None # user not exist
        
        listing_id = self.next_listing_id
        self.next_listing_id += 1
        sleep(0.01)
        created_at = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")


        self.listings[listing_id] = {
            "title": title,
            "description": description,
            "price": price,
            "category": category,
            "username": username,
            "created_at": created_at
        }

        if category not in self.categories:
            self.categories[category] = []
        self.categories[category].append((created_at, listing_id))

        return listing_id
    
    def listing_exists(self, listing_id):
        return listing_id in self.listings
    
    def user_exists(self, username):
        return username in self.users
    
    def get_listing(self, listing_id):
        item = self.listings[listing_id]
        return f"{item['title']}|{item['description']}|{item['price']}|{item['created_at']}|{item['category']}|{item['username']}"
    
    def is_listing_owerner(self, listing_id, username):
        if self.listings[listing_id]["username"] != username:
            return False
        else:
            return True
    
    def delete_listing(self, listing_id):
        category = self.listings[listing_id]["category"]
        self.categories[category] = [
            item for item in self.categories[category] if item[1] != listing_id
        ]

        del self.listings[listing_id]

        if not self.categories[category]:  # is category is empty, delete it!
            del self.categories[category]
    
    def category_exist(self, category):
        if category not in self.categories or not self.categories[category]:
            return False
        else:
            return True
        
    def get_category(self, category):
        sorted_listings = sorted(
            self.categories[category], key=lambda x: x[0], reverse=True # The latest, the upper
        )

        return "\n".join(
            f"{self.listings[listing_id]['title']}|{self.listings[listing_id]['description']}|"
            f"{self.listings[listing_id]['price']}|{self.listings[listing_id]['created_at']}|"
            f"{category}|{self.listings[listing_id]['username']}"
            for _, listing_id in sorted_listings
        )
    
    
    def get_top_category(self):
        valid_category = {cat: items for cat, items in self.categories.items() if len(items) > 0}
        if not valid_category:
            return None
        reversed_keys = list(valid_category.keys())[::-1]
        return max(reversed_keys, key=lambda cat: len(valid_category[cat]))
