'''Q7. Using Python, write a program named guestpicnic.py that stores picnic data using a 
dictionary containing dictionaries. Implement a function total_brought 
(picnic_items, item_name) that takes the dictionary and an item name as input and 
returns the total quantity of that item brought by all guests.
Your program should:
1.	Use dictionaries and lists where necessary.
2.	Demonstrate how nested dictionaries are used to represent complex data.
3.	Display the total count of at least three different picnic items.'''
picnicitems = {
    "Pranav": {"sandwhich" : 4, "cake": 3, "chip": 7 },
    "Pratik": {"sandwhich": 5, "juice": 2, "chip": 5},
    "Abhiram": {"sandwhich": 5, "cake":4 ,"juice":7},
    "Aditya":{"juice": 6, "cake": 3, "chip":4}
}
def total_brought (picnicitems, items_name):
    total = 0
    for guest in picnicitems:
        total +=  picnicitems[guest].get(items_name,0)
    return total
items = ["sandwhich","chip","cake","juice"]
for i in items:
    print(f"total {i}s brought :", total_brought(picnicitems, i))
    