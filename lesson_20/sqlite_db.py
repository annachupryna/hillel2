import sqlite3

connection = sqlite3.connect('my_test_db.sqlite')
cursor = connection.cursor()

cursor.execute("""
CREATE TABLE categories (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    category_name TEXT NOT NULL,
    category_description TEXT
);
""")

cursor.execute("""
CREATE TABLE products (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    description TEXT,
    price INTEGER,
    category_id INTEGER NOT NULL,
    FOREIGN KEY (category_id) REFERENCES categories (id)
);
""")

cursor.execute(f"""INSERT INTO categories ("category_name", "category_description") VALUES( "electronics",
"some description");""")
cursor.execute(f"""INSERT INTO categories ("category_name", "category_description") VALUES( "clothes",
"some description");""")
cursor.execute(f"""INSERT INTO categories ("category_name", "category_description") VALUES( "shoes",
"some description");""")

cursor.execute(f"""INSERT INTO products ("name", "description", "price", "category_id") VALUES( "New Balance 520",
"some description", "120", "3");""")
cursor.execute(f"""INSERT INTO products ("name", "description", "price", "category_id") VALUES( "Samsung Galaxy 2.0",
"some description", "350", "1");""")

connection.commit()

cursor.execute(f"""Select * from categories;""")
print('UP IS VIEW OF CATEGORIES')
record = cursor.fetchall()
print(record)

cursor.execute(f"""Select * from products;""")
print('UP IS VIEW OF PRODUCTS')
record = cursor.fetchall()
print(record)

cursor.execute(f"""Select products.id as product_id,
products.name as product_name,
products.description as product_description,
products.price as product_price,
categories.category_name AS category_name
from products
join categories
on
products.category_id = categories.id;""")

print('UP IS VIEW OF JOIN QUERY')
record = cursor.fetchall()
print(record)
