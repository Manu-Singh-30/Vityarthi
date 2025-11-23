import time

lost = []
found = []

def get_details():

    name = input("## What is the item? :- ")
    place = input("## Where was it lost or found? :- ")
    contact = input("## Give us your phn No. or Email :-  ")

    item = {
        'name': name.strip(),
        'place': place.strip(),
        'contact': contact.strip(),
        'when': time.strftime("%d-%mnd-%Y")
    }
    return item

def report(type_of_item):

    print(f"==>> Posting a {type_of_item.upper()} Item ~ ")

    new_item = get_details()

    if type_of_item  == 'lost':
        lost.append(new_item)
        print("Posted!!! We hope your item finds its way home!")
    elif type_of_item  == 'found':
        found.append(new_item)
        print("Posted!!! Thank you for being a helpful neighbor!")

    time.sleep(2)

def search():

    if not lost and not found:
        print("Nothing posted yet. Be the first!")
        time.sleep(2)
        return

    word = input("\nEnter one word to search for (like 'keys' or 'dog'): ").strip().lower()

    found_count = 0

    print("~~ Matching FOUND Items ~~")

    for item in found:
        if word in item['name'].lower():
            print(f"  FOUND: {item['name']} on {item['when']}")
            print(f"    -->> Found at: {item['place']}")
            print(f"    -->> Contact: {item['contact']}")
            found_count += 1

    print("~~ Matching LOST Items ~~")

    for item in lost:
        if word in item['name'].lower():
            print(f"  LOST: {item['name']} on {item['when']}")
            print(f"    -->> Lost at: {item['place']}")
            print(f"    -->> Contact: {item['contact']}")
            found_count += 1

    if found_count  == 0:
        print(f"Sorry, we found nothing matching '{word}'.")

    time.sleep(3)

def start_hub():

    print("Hello! Welcome to the Neighborhood Hub.")

    while True:
        print("Select from the options below :")
        print("1. I LOST something")
        print("2. I FOUND something")
        print("3. SEARCH the hub")
        print("4. Exit")

        choice = input("Enter a number (1, 2, 3, or 4): ")

        if choice  == '1':
            report('lost')
        elif choice  == '2':
            report('found')
        elif choice  == '3':
            search()
        elif choice  == '4':
            print("Thanks for being a good neighbor! See you soon.")
            break
        else:
            print("Hmm, that wasn't an option. Try again.")
            time.sleep(1)

if __name__  == "__main__":
    start_hub()
