def find_matches(lost_item, items):
    matches = []

    for item in items:
        if item["type"] == "Found" and item["status"] == "Active":
            if (item["category"].lower() == lost_item["category"].lower()
                    and item["location"].lower() == lost_item["location"].lower()):
                matches.append(item)

    return matches