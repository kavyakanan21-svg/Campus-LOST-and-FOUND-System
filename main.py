from item_manager import get_item_details, display_items
from matching import find_matches
from storage import (
    add_item,
    get_all_items,
    update_item_status,
    save_items,
    load_items
)


load_items()

print("========================================")
print("       CAMPUS LOST & FOUND SYSTEM")
print("========================================")

while True:
    print("\n---------- MAIN MENU ----------")
    print("1. Report Lost Item")
    print("2. Report Found Item")
    print("3. View All Items")
    print("4. Find Matches")
    print("5. Claim/Resolve Item")
    print("6. Exit")

    choice = input("Enter your choice: ").strip()

    if choice == "1":
        item = get_item_details("Lost")
        add_item(item)
        save_items()
        print("\nLost item reported successfully!")

    elif choice == "2":
        item = get_item_details("Found")
        add_item(item)
        save_items()
        print("\nFound item reported successfully!")

    elif choice == "3":
        display_items(get_all_items())

    elif choice == "4":
        lost_item_name = input("\nEnter the name of the lost item: ").strip()

        lost_item = None

        for item in get_all_items():
            if item["type"] == "Lost" and item["name"].lower() == lost_item_name.lower():
                lost_item = item
                break

        if lost_item is None:
            print("\nLost item not found.")
        else:
            matches = find_matches(lost_item, get_all_items())

            if matches:
                print("\nPossible matches found:")
                display_items(matches)
            else:
                print("\nNo possible matches found.")

    elif choice == "5":
        item_id = input("\nEnter the ID of the item to resolve: ").strip()

        if item_id.isdigit():
            if update_item_status(int(item_id), "Resolved"):
                save_items()
                print("\nItem marked as Resolved successfully!")
            else:
                print("\nItem ID not found.")
        else:
            print("\nPlease enter a valid numeric ID.")

    elif choice == "6":
        print("\nThank you for using Campus Lost & Found System!")
        break

    else:
        print("\nInvalid choice. Please enter 1, 2, 3, 4, 5, or 6.")