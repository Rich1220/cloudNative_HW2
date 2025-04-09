import shlex
from marketplace import Marketplace

def main():
    market = Marketplace()

    print("# CloudShop CLI 已啟動，請輸入指令，輸入 'EXIT' 離開")

    while True:
        try:
            command = input("# ").strip()
            if not command:
                continue

            # Parse the user input, supporting single quotes
            parts = shlex.split(command)

            if parts[0].upper() == "EXIT":
                print("退出 CloudShop CLI")
                break

            action = parts[0].upper()

            if action == "REGISTER":
                if len(parts) != 2:
                    print("Error - 請輸入 REGISTER <username>")
                    continue
                username = parts[1]
                print(market.register_user(username))

            elif action == "CREATE_LISTING":
                if len(parts) != 6:
                    print("Error - 請輸入 CREATE_LISTING <username> <title> <description> <price> <category>")
                    continue
                username, title, description, price, category = parts[1], parts[2], parts[3], parts[4], parts[5]
                try:
                    price = int(price)  # ensure the price is number
                except ValueError:
                    print("Error - 價格必須是數字")
                    continue
                print(market.create_listing(username, title, description, price, category))

            elif action == "DELETE_LISTING":
                if len(parts) != 3:
                    print("Error - 請輸入 DELETE_LISTING <username> <listing_id>")
                    continue
                username, listing_id = parts[1], parts[2]
                print(market.delete_listing(username, listing_id))

            elif action == "GET_LISTING":
                if len(parts) != 3:
                    print("Error - 請輸入 GET_LISTING <username> <listing_id>")
                    continue
                username, listing_id = parts[1], parts[2]
                print(market.get_listing(username, listing_id))

            elif action == "GET_CATEGORY":
                if len(parts) != 3:
                    print("Error - 請輸入 GET_CATEGORY <username> <category>")
                    continue
                username, category = parts[1], parts[2]
                print(market.get_category(username, category))

            elif action == "GET_TOP_CATEGORY":
                if len(parts) != 2:
                    print("Error - 請輸入 GET_TOP_CATEGORY <username>")
                    continue
                username = parts[1]
                print(market.get_top_category(username))

            else:
                print("Error - 未知指令，請重新輸入")

        except Exception as e:
            print(f"Error - {e}")

if __name__ == "__main__":
    main()

# I am from hw1-p