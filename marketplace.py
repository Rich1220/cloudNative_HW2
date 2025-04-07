from database import Database

class Marketplace:
    def __init__(self):
        # initialize  the Marketplace
        self.db = Database()

    def register_user(self, username):
        # register user
        username = username.lower()
        success = self.db.add_user(username)
        return "Success" if success else "Error - user already existing"

    def create_listing(self, username, title, description, price, category):
        # create listing
        username = username.lower()
        listing_id = self.db.add_listing(username, title, description, price, category)
        return str(listing_id) if listing_id else "Error - unknown user"

    def get_listing(self, username, listing_id):
        # get listing information
        username = username.lower()
        listing_id = int(listing_id)  

        if not self.db.listing_exists(listing_id):
            return "Error - not found"
        if not self.db.user_exists(username):
            return "Error - unknown user"
        
        return self.db.get_listing(listing_id)

    def delete_listing(self, username, listing_id):
        # delete the listing
        username = username.lower()
        listing_id = int(listing_id)  # make sure listing_id is int

        if not self.db.user_exists(username):
            return "Error - unknown user"

        if not self.db.listing_exists(listing_id):
            return "Error - listing does not exist"

        if not self.db.is_listing_owerner(listing_id,username):
              return "Error - listing owner mismatch"  

        self.db.delete_listing(listing_id)

        return "Success"

    def get_category(self, username, category):
        # get the listings of specific category
        username = username.lower()

        if not self.db.category_exist(category):
            return "Error - category not found"
        if not self.db.user_exists(username):
            return "Error - unknown user"

        return self.db.get_category(category)


    def get_top_category(self, username):
        # get the category with most listing
        username = username.lower()

        if not self.db.user_exists(username):
            return "Error - unknown user"

        top = self.db.get_top_category()
        return top if top else "Error - no categories"


