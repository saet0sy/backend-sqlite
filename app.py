from fastapi import FastAPI, HTTPException
from models.product import Product, ProductInput
import sqlite3
app = FastAPI()

def mappingProduct(products: list):
    result = []
    for product in products:
        result.append(Product(product[0], product[1], product[2]))
    return result

# get products

@app.get("/products")
async def get_products():
    products = []
    with sqlite3.connect("eshop.db") as connection:
        cursor = connection.cursor()
        cursor.execute("SELECT id, title, price FROM products")
        products = cursor.fetchall()
    return mappingProduct(products)

# get products by id

@app.get("/products/{id}")
async def get_product(id: int):
    with sqlite3.connect("eshop.db") as connection:
        cursor = connection.cursor()
        cursor.execute("SELECT id, title, price FROM products WHERE id=?", (id,))
        product = cursor.fetchone()
        if product is None:
            raise HTTPException(status_code=404, detail="Product not found")
    return Product(product[0], product[1], product[2])

#post products

@app.post("/products")
async def create_product(product: ProductInput):
    with sqlite3.connect("eshop.db") as connection:
        cursor = connection.cursor()
        cursor.execute(f"INSERT INTO products(title, price) VALUES('{product.title}', {product.price})")
        connection.commit()
        return product

# put products

@app.put("/products/{id}")
async def update_product(id: int, product: ProductInput):
    with sqlite3.connect("eshop.db") as connection:
        cursor = connection.cursor()
        cursor.execute("UPDATE products SET title=?, price=? WHERE id=?",(product.title, product.price, id,))
        connection.commit()
        return product

# delete products

@app.delete("/products/{id}")
async def delete_product(id: int):
    with sqlite3.connect("eshop.db") as connection:
        cursor = connection.cursor()
        cursor.execute("DELETE FROM products WHERE id=?",(id,))
        connection.commit()
        return {"message": "Product deleted"}
    
# add min price max price query

@app.get("/products")
async def get_products(min_price: int = 0, max_price: int = 1000):
    products = []
    with sqlite3.connect("eshop.db") as connection:
        cursor = connection.cursor()
        cursor.execute(f"SELECT id, title, price FROM products WHERE price BETWEEN ? AND ?", (min_price, max_price))
        products = cursor.fetchall()
    return mappingProduct(products)




