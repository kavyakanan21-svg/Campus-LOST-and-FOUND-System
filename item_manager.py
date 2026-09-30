def create_item(item_type, name, category, location, description, date):
    item = {
        "type": item_type,
        "name": name,
        "category": category,
        "location": location,
        "description": description,
        "date": date,
        "status": "Active"
    }

    return item
def get_item_details(item_type):
    print("\n--- Enter Item Details ---")

    name = input("Enter item name: ").strip()
    category = input("Enter category: ").strip()
    location = input("Enter location: ").strip()
    description = input("Enter description: ").strip()
    date = input("Enter date (DD-MM-YYYY): ").strip()

    return create_item(
        item_type,
        name,
        category,
        location,
        description,
        date
    )
def display_items(items):
    if not items:
        print("\nNo items found.")
        return

    print("\n========== ALL ITEMS ==========")

    for item in items:
        print(f"ID: {item['id']}")
        print(f"Type: {item['type']}")
        print(f"Name: {item['name']}")
        print(f"Category: {item['category']}")
        print(f"Location: {item['location']}")
        print(f"Description: {item['description']}")
        print(f"Date: {item['date']}")
        print(f"Status: {item['status']}")
        print("------------------------------")
