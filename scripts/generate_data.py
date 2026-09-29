import pandas as pd
import random
from datetime import datetime, timedelta
import os

# ============ SET WORKING DIRECTORY ============
# Script ke saath hi data folder banega
BASE_DIR = r"D:\Flipkart Project Data Analytics"
DATA_DIR = os.path.join(BASE_DIR, "data")
os.makedirs(DATA_DIR, exist_ok=True)

random.seed(42)

# ============ CUSTOMERS (500 rows) ============
first_names = ["Rahul","Priya","Amit","Sneha","Vikram","Ananya","Rohit","Kavya","Arjun","Deepa",
               "Suresh","Nisha","Karan","Pooja","Ravi","Meera","Aditya","Shreya","Nikhil","Ritu",
               "Sahil","Tanvi","Harsh","Divya","Manish","Aisha","Vivek","Neha","Raj","Simran"]
last_names = ["Sharma","Patel","Kumar","Reddy","Singh","Iyer","Das","Nair","Mehta","Joshi",
              "Rao","Verma","Malhotra","Gupta","Teja","Pillai","Banerjee","Kulkarni","Jain","Choudhary"]
cities = {
    "Mumbai":"Maharashtra","Delhi":"Delhi","Bangalore":"Karnataka","Hyderabad":"Telangana",
    "Chennai":"Tamil Nadu","Kolkata":"West Bengal","Pune":"Maharashtra","Jaipur":"Rajasthan",
    "Ahmedabad":"Gujarat","Lucknow":"Uttar Pradesh"
}
tiers = ["Bronze","Silver","Gold","Platinum"]

customers = []
for i in range(1, 501):
    cid = f"C{i:03d}"
    name = f"{random.choice(first_names)} {random.choice(last_names)}"
    email = f"user{i}@{random.choice(['gmail','yahoo','outlook'])}.com"
    phone = f"9{random.randint(100000000,999999999)}"
    city = random.choice(list(cities.keys()))
    state = cities[city]
    signup = datetime(2023,1,1) + timedelta(days=random.randint(0,700))
    tier = random.choices(tiers, weights=[40,30,20,10])[0]
    customers.append([cid,name,email,phone,city,state,signup.strftime("%Y-%m-%d"),tier])

pd.DataFrame(customers, columns=["customer_id","name","email","phone","city","state","signup_date","loyalty_tier"]).to_csv(os.path.join(DATA_DIR, "customers.csv"), index=False)
print("✅ customers.csv — 500 rows")

# ============ SELLERS (500 rows) ============
seller_prefix = ["Tech","Fashion","Home","Beauty","Gadget","Style","Kitchen","Sports","Book","Toy",
                 "Mega","Super","Prime","Elite","Smart","Urban","Royal","Star","Global","Quick"]
seller_suffix = ["World","Hub","Essentials","Bar","Store","Craft","King","Zone","Mart","Land",
                 "Bazaar","Point","Center","Shop","Trade"]

sellers = []
for i in range(1, 501):
    sid = f"S{i:03d}"
    sname = f"{random.choice(seller_prefix)}{random.choice(seller_suffix)}"
    city = random.choice(list(cities.keys()))
    rating = round(random.uniform(3.5, 5.0), 1)
    join = datetime(2022,1,1) + timedelta(days=random.randint(0,800))
    sellers.append([sid,sname,city,rating,join.strftime("%Y-%m-%d")])

pd.DataFrame(sellers, columns=["seller_id","seller_name","city","rating","join_date"]).to_csv(os.path.join(DATA_DIR, "sellers.csv"), index=False)
print("✅ sellers.csv — 500 rows")

# ============ PRODUCTS (500 rows) — REAL PRODUCTS WITH REAL PRICES ============
real_products = {
    "Electronics": [
        ("Apple iPhone 15", "Mobiles", "Apple", 79900),
        ("Apple iPhone 15 Pro", "Mobiles", "Apple", 134900),
        ("Apple iPhone 14", "Mobiles", "Apple", 69900),
        ("Samsung Galaxy S24", "Mobiles", "Samsung", 74999),
        ("Samsung Galaxy S23", "Mobiles", "Samsung", 64999),
        ("OnePlus 12", "Mobiles", "OnePlus", 64999),
        ("OnePlus Nord CE 4", "Mobiles", "OnePlus", 24999),
        ("Redmi Note 13 Pro", "Mobiles", "Redmi", 23999),
        ("Realme 12 Pro", "Mobiles", "Realme", 25999),
        ("Vivo V30", "Mobiles", "Vivo", 33999),
        ("MacBook Air M2", "Laptops", "Apple", 99900),
        ("MacBook Pro M3", "Laptops", "Apple", 169900),
        ("HP Pavilion 15", "Laptops", "HP", 55999),
        ("Dell Inspiron 15", "Laptops", "Dell", 52999),
        ("Lenovo IdeaPad", "Laptops", "Lenovo", 47999),
        ("ASUS VivoBook", "Laptops", "ASUS", 44999),
        ("Sony WH-1000XM5", "Audio", "Sony", 29990),
        ("Apple AirPods Pro", "Audio", "Apple", 24900),
        ("Boat Airdopes 141", "Audio", "Boat", 1299),
        ("JBL Tune 770NC", "Audio", "JBL", 6999),
        ("Samsung Galaxy Buds", "Audio", "Samsung", 9999),
        ("Sony Bravia 55 4K", "TV", "Sony", 79990),
        ("Samsung Crystal 43", "TV", "Samsung", 32990),
        ("LG OLED 55", "TV", "LG", 129990),
        ("Mi 5X 50 inch", "TV", "Mi", 29999),
        ("LG Refrigerator 260L", "Appliances", "LG", 27990),
        ("Samsung Refrigerator", "Appliances", "Samsung", 32990),
        ("Whirlpool Washing Machine", "Appliances", "Whirlpool", 24990),
        ("Bosch Dishwasher", "Appliances", "Bosch", 45990),
        ("Dell 24 Monitor", "Monitors", "Dell", 12999),
        ("LG 27 4K Monitor", "Monitors", "LG", 32999),
    ],
    "Fashion": [
        ("Levis 511 Jeans", "Men", "Levis", 2799),
        ("Levis 501 Original", "Men", "Levis", 3499),
        ("Allen Solly Formal Shirt", "Men", "Allen Solly", 1799),
        ("Peter England Shirt", "Men", "Peter England", 1299),
        ("US Polo T-Shirt", "Men", "US Polo", 999),
        ("Van Heusen Trouser", "Men", "Van Heusen", 1999),
        ("FabIndia Kurta Men", "Men", "FabIndia", 2499),
        ("Nike Air Max", "Footwear", "Nike", 8999),
        ("Nike Revolution", "Footwear", "Nike", 3999),
        ("Adidas Ultraboost", "Footwear", "Adidas", 12999),
        ("Puma Running Shoes", "Footwear", "Puma", 4999),
        ("Bata Formal Shoes", "Footwear", "Bata", 2499),
        ("Womens Saree Silk", "Women", "FabIndia", 4999),
        ("Womens Kurti Cotton", "Women", "Libas", 899),
        ("Womens Top", "Women", "H&M", 1299),
        ("Womens Jeans", "Women", "Levis", 2499),
        ("Womens Dress", "Women", "Zara", 2999),
        ("Kids T-Shirt", "Kids", "H&M", 499),
        ("Kids Jeans", "Kids", "Levis", 999),
        ("Fastrack Watch", "Men", "Fastrack", 1999),
        ("Titan Watch", "Men", "Titan", 4999),
    ],
    "Home": [
        ("Prestige Pressure Cooker", "Kitchen", "Prestige", 2499),
        ("Hawkins Cooker 5L", "Kitchen", "Hawkins", 2199),
        ("Philips Mixer Grinder", "Kitchen", "Philips", 3499),
        ("Bajaj Mixer 750W", "Kitchen", "Bajaj", 2999),
        ("Prestige Induction", "Kitchen", "Prestige", 2299),
        ("Wakefit Mattress Queen", "Furniture", "Wakefit", 12999),
        ("Sleepwell Mattress", "Furniture", "Sleepwell", 9999),
        ("Godrej Almirah", "Furniture", "Godrej", 18999),
        ("Nilkamal Chair Set", "Furniture", "Nilkamal", 4999),
        ("Wakefit Sofa", "Furniture", "Wakefit", 24999),
        ("Bombay Dyeing Bedsheet", "Decor", "Bombay Dyeing", 999),
        ("Home Centre Cushion", "Decor", "Home Centre", 499),
        ("Philips LED Bulb 9W", "Decor", "Philips", 149),
        ("Syska LED Strip", "Decor", "Syska", 599),
    ],
    "Beauty": [
        ("Lakme Face Wash", "Skincare", "Lakme", 299),
        ("Lakme Sunscreen SPF50", "Skincare", "Lakme", 499),
        ("Mamaearth Face Wash", "Skincare", "Mamaearth", 249),
        ("Mamaearth Shampoo", "Haircare", "Mamaearth", 399),
        ("Dove Shampoo 650ml", "Haircare", "Dove", 499),
        ("Head & Shoulders", "Haircare", "H&S", 399),
        ("Nivea Body Lotion", "Skincare", "Nivea", 349),
        ("Nivea Soft Cream", "Skincare", "Nivea", 299),
        ("Loreal Serum", "Skincare", "Loreal", 799),
        ("Himalaya Face Pack", "Skincare", "Himalaya", 199),
        ("Maybelline Lipstick", "Makeup", "Maybelline", 399),
        ("Lakme Kajal", "Makeup", "Lakme", 199),
        ("Loreal Foundation", "Makeup", "Loreal", 899),
        ("Himalaya Neem Soap", "Skincare", "Himalaya", 99),
        ("Ponds Powder", "Makeup", "Ponds", 249),
    ],
    "Books": [
        ("Atomic Habits", "Self-Help", "Penguin", 499),
        ("Rich Dad Poor Dad", "Finance", "Penguin", 399),
        ("The Psychology of Money", "Finance", "Jaico", 349),
        ("Ikigai", "Self-Help", "Penguin", 399),
        ("Think and Grow Rich", "Self-Help", "Rupa", 249),
        ("Wings of Fire", "Biography", "Universities Press", 299),
        ("The Alchemist", "Fiction", "HarperCollins", 349),
        ("Sapiens", "History", "HarperCollins", 599),
        ("Harry Potter Boxset", "Fiction", "Bloomsbury", 2499),
        ("The Hobbit", "Fiction", "HarperCollins", 449),
        ("Zero to One", "Business", "Random House", 499),
        ("Deep Work", "Self-Help", "Grand Central", 399),
        ("The Lean Startup", "Business", "Crown", 549),
        ("7 Habits", "Self-Help", "Simon", 449),
        ("Do Epic Shit", "Self-Help", "Penguin", 299),
    ],
    "Toys": [
        ("LEGO Classic Bricks", "Building", "LEGO", 2999),
        ("LEGO Technic Car", "Building", "LEGO", 4999),
        ("Barbie Doll Classic", "Dolls", "Barbie", 999),
        ("Barbie Dreamhouse", "Dolls", "Barbie", 4999),
        ("Hot Wheels Set 5", "Building", "Hot Wheels", 799),
        ("Funskool Monopoly", "Outdoor", "Funskool", 899),
        ("Funskool Chess", "Outdoor", "Funskool", 599),
        ("Nerf Gun Blaster", "Outdoor", "Nerf", 1999),
        ("Remote Control Car", "Outdoor", "Funskool", 1499),
        ("Rubiks Cube", "Building", "Rubiks", 399),
        ("Hamleys Teddy Bear", "Dolls", "Hamleys", 799),
        ("Hamleys Puzzle 500", "Building", "Hamleys", 499),
        ("Play Doh Set", "Building", "Play-Doh", 599),
        ("Melissa Art Set", "Building", "Melissa", 899),
        ("Card Game Uno", "Outdoor", "Mattel", 199),
    ]
}

products = []
for i in range(1, 501):
    pid = f"P{i:03d}"
    cat = random.choice(list(real_products.keys()))
    product = random.choice(real_products[cat])
    pname, subcat, brand, price = product
    seller_id = f"S{random.randint(1,500):03d}"
    products.append([pid, pname, cat, subcat, brand, price, seller_id])

pd.DataFrame(products, columns=["product_id","product_name","category","subcategory","brand","price","seller_id"]).to_csv(os.path.join(DATA_DIR, "products.csv"), index=False)
print("✅ products.csv — 500 rows (real products)")

# ============ ORDERS (500 rows) ============
statuses = ["Delivered","Cancelled","Returned","Pending"]
payments = ["Credit Card","Debit Card","UPI","COD","Net Banking"]

orders = []
for i in range(1, 501):
    oid = f"O{i:03d}"
    cid = f"C{random.randint(1,500):03d}"
    odate = datetime(2023,6,1) + timedelta(days=random.randint(0,450))
    status = random.choices(statuses, weights=[75,10,10,5])[0]
    pay = random.choice(payments)
    orders.append([oid,cid,odate.strftime("%Y-%m-%d"),status,pay])

pd.DataFrame(orders, columns=["order_id","customer_id","order_date","order_status","payment_method"]).to_csv(os.path.join(DATA_DIR, "orders.csv"), index=False)
print("✅ orders.csv — 500 rows")

# ============ ORDER_ITEMS (500 rows) ============
order_items = []
for i in range(1, 501):
    iid = f"I{i:03d}"
    oid = f"O{random.randint(1,500):03d}"
    pid = f"P{random.randint(1,500):03d}"
    qty = random.randint(1,3)
    price = int(products[int(pid[1:])-1][5])
    disc = random.choice([0,5,10,15,20,25])
    order_items.append([iid,oid,pid,qty,price,disc])

pd.DataFrame(order_items, columns=["order_item_id","order_id","product_id","quantity","unit_price","discount_pct"]).to_csv(os.path.join(DATA_DIR, "order_items.csv"), index=False)
print("✅ order_items.csv — 500 rows")

# ============ EVENTS (500 rows) ============
event_types = ["view","add_to_cart","purchase","search"]

events = []
for i in range(1, 501):
    eid = f"E{i:03d}"
    cid = f"C{random.randint(1,500):03d}"
    sess = f"SESS{random.randint(1,200):04d}"
    etype = random.choices(event_types, weights=[50,25,20,5])[0]
    pid = "NA" if etype == "search" else f"P{random.randint(1,500):03d}"
    ts = datetime(2023,6,1) + timedelta(days=random.randint(0,450), hours=random.randint(0,23), minutes=random.randint(0,59))
    events.append([eid,cid,sess,etype,pid,ts.strftime("%Y-%m-%d %H:%M:%S")])

pd.DataFrame(events, columns=["event_id","customer_id","session_id","event_type","product_id","event_timestamp"]).to_csv(os.path.join(DATA_DIR, "events.csv"), index=False)
print("✅ events.csv — 500 rows")

# ============ DELIVERY (500 rows) ============
partners = ["Ekart Logistics","Delhivery","Blue Dart","DTDC","Shadowfax"]
del_status = ["Delivered","In Transit","Returned","Failed"]

deliveries = []
for i in range(1, 501):
    did = f"D{i:03d}"
    oid = f"O{random.randint(1,500):03d}"
    partner = random.choice(partners)
    dispatch = datetime(2023,6,2) + timedelta(days=random.randint(0,450))
    delivery = dispatch + timedelta(days=random.randint(2,8))
    status = random.choices(del_status, weights=[80,10,7,3])[0]
    city = random.choice(list(cities.keys()))
    deliveries.append([did,oid,partner,dispatch.strftime("%Y-%m-%d"),delivery.strftime("%Y-%m-%d"),status,city])

pd.DataFrame(deliveries, columns=["delivery_id","order_id","delivery_partner","dispatch_date","delivery_date","delivery_status","delivery_city"]).to_csv(os.path.join(DATA_DIR, "delivery.csv"), index=False)
print("✅ delivery.csv — 500 rows")

print("\n🎉 Saari 7 CSV files ban gayi!")
print(f"📁 Location: {DATA_DIR}")