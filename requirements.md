# Project Requirements

## Functional Requirements

### 1. Report Lost Item
The user can enter details of a lost item such as name, category, location, description, and date.

### 2. Report Found Item
The user can enter details of an item that has been found on campus.

### 3. View All Items
The system displays all stored lost and found item records along with their details and current status.

### 4. Find Possible Matches
The system compares lost and found items using category and location and displays possible matches.

### 5. Claim/Resolve Item
The user can mark an item as resolved by entering its item ID.

### 6. Data Storage
The system saves item records in a JSON file and loads them when the program starts.

## Non-Functional Requirements

### 1. Usability
The system uses a simple menu-based interface so that users can easily select an operation.

### 2. Reliability
The system checks whether an entered item ID is valid before updating an item's status.

### 3. Error Handling
The system handles invalid menu choices, invalid item IDs, and errors while loading JSON data.

### 4. Maintainability
The program is divided into separate Python modules such as item management, storage, matching, and constants.

### 5. Data Persistence
Item records remain available after the program is closed and started again.

### 6. Resource Efficiency
The system uses a lightweight JSON file for storing item records instead of requiring a database.