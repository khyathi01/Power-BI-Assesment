inventory = [
    # name,       category,   unit_price, units_sold, units_left
    ["Strawberry", "Fruit",      3.50,        40,          10],
    ["Broccoli",   "Vegetable",  2.20,        25,           8],
    ["Cheddar",    "Dairy",      5.00,        18,           4],
    ["Baguette",   "Bakery",     2.80,        35,           2],
    ["Blueberry",  "Fruit",      4.00,        22,           6],
    ["Spinach",    "Vegetable",  1.80,        30,          12],
    ["Yogurt",     "Dairy",      1.20,        50,          15],
    ["Croissant",  "Bakery",     3.00,        28,           3],
]
total = 0
revenue = 0
for items in inventory:
    name,category,unit_price,units_sold,unit_left = items
    total += int(units_sold*unit_price)
    #calculte the categorywise Revenue
    revenue = int(unit_price*units_sold)
    print(f"category : {category}  totalrevenue : {revenue}\n")
    #List Low stock item if stock is less than 5
    if(unit_left<5):
        print(f'the unit left less than 5 are : {name}\n')
#calculate the TotalRevenue
print(f'The total revenue is : {total}\n')

    