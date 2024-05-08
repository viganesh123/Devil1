import array as hashTable

# Define the size of the hash table
size = 7

# Initialize the hash table with -1 in each slot
hashTable = hashTable.array('l', [-1] * size)

# Function to display the hash table
def display():
    for i in range(0, 7):
        print("Index[", i, "]=", hashTable[i])

# Function to insert a value into the hash table
def insertHash(value):
    # Calculate the hash key for the value
    key = value % size
    # If the slot at the hash key is empty, insert the value there
    if hashTable[key] == -1:
        hashTable[key] = value
        print(value, "inserted at arr", key)
    else:
        # If there's a collision, resolve it using quadratic probing
        print("Collision : arr", key, "has element", hashTable[key], "already!")
        i = 0
        count = 0
        while i < 7:
            # Count the number of occupied slots in the hash table
            if hashTable[i] != -1:
                count += 1
            i += 1
        # If the hash table is full, print a message and display the hash table
        if count == 7:
            print("Hash Table Is Full Hence", value, "Can not Be Inserted")
            display()
        else:
            # Perform quadratic probing to find an empty slot
            for i in range(0, 7):
                key1 = (key + i * i) % size
                if hashTable[key1] == -1:
                    hashTable[key1] = value
                    print(value, "inserted at arr", key1)
                    break

# Function to search for a value in the hash table
def search(value):
    key = value % size
    if hashTable[key] == value:
        print(value, "Found at", key, "th Index location")
    else:
        print(value, "Not Found at", key, "th Index location")

# Function to delete a value from the hash table
def delHash(value):
    key = value % size
    if hashTable[key] == value:
        hashTable[key] = -1
        print(value, "Successfully deleted from hash table")
    else:
        print(value, "Not Found at", key, "th Index location")

# Function to display the initial state of the hash table
def initial():
    display()

# Function to display the menu
def menu():
    print("\n\n\t-----MENU-----")
    print("1. Display Hash Table")
    print("2. Insert a Number")
    print("3. Search a Number")
    print("4. Delete a Number")
    print("5. Quit")

# Display the initial state of the hash table
initial()

# Main loop for menu-driven program
while True:
    menu()
    # Get user choice
    choice = int(input("Enter your choice: "))
    if choice == 1:
        display()
    elif choice == 2:
        num = int(input("Enter Telephone number to insert into Hash table: "))
        insertHash(num)
    elif choice == 3:
        num = int(input("Enter Telephone number to search in Hash table: "))
        search(num)
    elif choice == 4:
        num = int(input("Enter Telephone number to delete from Hash table: "))
        delHash(num)
    elif choice == 5:
        # Exit the loop if user chooses to quit
        break
    else:
        print("Invalid choice. Please enter a number between 1 and 5.")
