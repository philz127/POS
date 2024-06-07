import csv

fields = [
    ["Name", "SKU", "Aisle", "Quantity", "Price", "Item Type"]
]

rows = [
    ["Apples", "100001", "A1", 50, 0.50, "Fruit"],
    ["Bananas", "100002", "A1", 100, 0.30, "Fruit"],
    ["Oranges", "100003", "A1", 75, 0.60, "Fruit"],
    ["Milk", "100004", "A2", 40, 1.50, "Dairy"],
    ["Eggs", "100005", "A2", 30, 2.00, "Dairy"],
    ["Cheese", "100006", "A2", 20, 3.00, "Dairy"],
    ["Bread", "100007", "A3", 50, 2.50, "Bakery"],
    ["Butter", "100008", "A3", 25, 2.75, "Bakery"],
    ["Cereal", "100009", "A3", 60, 3.50, "Bakery"],
    ["Chicken Breast", "100010", "A4", 35, 5.00, "Meat"],
    ["Ground Beef", "100011", "A4", 40, 4.50, "Meat"],
    ["Pork Chops", "100012", "A4", 30, 4.75, "Meat"],
    ["Shampoo", "100013", "A5", 25, 3.00, "Personal Care"],
    ["Conditioner", "100014", "A5", 20, 3.25, "Personal Care"],
    ["Toothpaste", "100015", "A5", 35, 2.00, "Personal Care"],
    ["Laundry Detergent", "100016", "A6", 15, 8.00, "Household"],
    ["Dish Soap", "100017", "A6", 20, 2.50, "Household"],
    ["Paper Towels", "100018", "A6", 40, 1.50, "Household"],
    ["T-Shirt", "100019", "A7", 50, 10.00, "Clothing"],
    ["Jeans", "100020", "A7", 30, 20.00, "Clothing"],
    ["Jacket", "100021", "A7", 20, 50.00, "Clothing"],
    ["Laptop", "100022", "A8", 10, 500.00, "Electronics"],
    ["Smartphone", "100023", "A8", 15, 700.00, "Electronics"],
    ["Tablet", "100024", "A8", 12, 300.00, "Electronics"],
    ["Headphones", "100025", "A9", 25, 50.00, "Electronics"],
    ["Mouse", "100026", "A9", 30, 25.00, "Electronics"],
    ["Keyboard", "100027", "A9", 20, 30.00, "Electronics"],
    ["Lamp", "100028", "A10", 18, 20.00, "Household"],
    ["Pillow", "100029", "A10", 25, 15.00, "Household"],
    ["Blanket", "100030", "A10", 15, 25.00, "Household"],
    ["Socks", "100031", "A11", 100, 5.00, "Clothing"],
    ["Hat", "100032", "A11", 40, 15.00, "Clothing"],
    ["Scarf", "100033", "A11", 30, 12.00, "Clothing"],
    ["Soap", "100034", "A12", 50, 1.00, "Personal Care"],
    ["Hand Sanitizer", "100035", "A12", 40, 2.00, "Personal Care"],
    ["Lotion", "100036", "A12", 35, 3.00, "Personal Care"],
    ["Coffee", "100037", "A13", 40, 7.00, "Beverage"],
    ["Tea", "100038", "A13", 50, 5.00, "Beverage"],
    ["Juice", "100039", "A13", 30, 4.00, "Beverage"],
    ["Pasta", "100040", "A14", 50, 2.00, "Pantry"],
    ["Rice", "100041", "A14", 45, 1.50, "Pantry"],
    ["Beans", "100042", "A14", 60, 1.00, "Pantry"],
    ["Tomato Sauce", "100043", "A15", 40, 2.50, "Pantry"],
    ["Olive Oil", "100044", "A15", 30, 6.00, "Pantry"],
    ["Vinegar", "100045", "A15", 25, 3.00, "Pantry"],
    ["Chips", "100046", "A16", 50, 2.00, "Snacks"],
    ["Cookies", "100047", "A16", 40, 3.00, "Snacks"],
    ["Candy", "100048", "A16", 70, 1.50, "Snacks"],
    ["Canned Tuna", "100049", "A17", 35, 2.00, "Pantry"],
    ["Canned Corn", "100050", "A17", 40, 1.00, "Pantry"],
    ["Canned Beans", "100051", "A17", 50, 1.00, "Pantry"],
    ["Ice Cream", "100052", "A18", 20, 4.00, "Dairy"],
    ["Frozen Pizza", "100053", "A18", 25, 5.00, "Dairy"],
    ["Frozen Vegetables", "100054", "A18", 30, 2.50, "Dairy"],
    ["Dog Food", "100055", "A19", 40, 10.00, "Pet Supplies"],
    ["Cat Food", "100056", "A19", 35, 8.00, "Pet Supplies"],
    ["Bird Seed", "100057", "A19", 25, 6.00, "Pet Supplies"],
    ["Toilet Paper", "100058", "A20", 50, 0.75, "Household"],
    ["Cleaning Wipes", "100059", "A20", 35, 3.00, "Household"],
    ["Trash Bags", "100060", "A20", 45, 5.00, "Household"],
    ["Soda", "100061", "A21", 60, 1.50, "Beverage"],
    ["Energy Drink", "100062", "A21", 30, 2.50, "Beverage"],
    ["Water", "100063", "A21", 70, 1.00, "Beverage"],
    ["Carrots", "100064", "A22", 40, 1.00, "Vegetable"],
    ["Broccoli", "100065", "A22", 35, 1.50, "Vegetable"],
    ["Lettuce", "100066", "A22", 50, 1.00, "Vegetable"],
    ["Salt", "100067", "A23", 60, 0.50, "Pantry"],
    ["Pepper", "100068", "A23", 55, 0.75, "Pantry"],
    ["Spices", "100069", "A23", 50, 2.00, "Pantry"],
    ["Pencil", "100070", "A24", 80, 0.50, "Stationery"],
    ["Notebook", "100071", "A24", 70, 1.50, "Stationery"],
    ["Eraser", "100072", "A24", 60, 0.25, "Stationery"],
    ["Battery", "100073", "A25", 40, 5.00, "Electronics"],
    ["Flashlight", "100074", "A25", 30, 10.00, "Electronics"],
    ["Extension Cord", "100075", "A25", 25, 15.00, "Electronics"],
    ["Hammer", "100076", "A26", 20, 10.00, "Tools"],
    ["Screwdriver", "100077", "A26", 25, 5.00, "Tools"],
    ["Wrench", "100078", "A26", 30, 8.00, "Tools"],
    ["Teddy Bear", "100079", "A27", 50, 10.00, "Toys"]
     ]

with open("Store_DB.csv", 'w') as store:
    write = csv.writer(store)
    write.writerow(fields)
    write.writerows(rows)
