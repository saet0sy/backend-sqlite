from fastapi import FastAPI, HTTPException
from models.product import Product, ProductInput
from models.user import User, UserInput  
from models.article import Article, ArticleInput
import sqlite3
app = FastAPI()

def mappingProduct(products: list):
    result = []
    for product in products:
        result.append(Product(product[0], product[1], product[2]))
    return result

def mappingUser(users: list):
    result = []
    for user in users:
        result.append(User(user[0], user[1], user[2]))
    return result

def mappingArticle(articles: list):
    result = []
    for article in articles:
        result.append(Article(article[0], article[1], article[2]))
    return result

# get products

# @app.get("/products")
# async def get_products():
#     products = []
#     with sqlite3.connect("eshop.db") as connection:
#         cursor = connection.cursor()
#         cursor.execute("SELECT id, title, price FROM products")
#         products = cursor.fetchall()
#     return mappingProduct(products)

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

# users

# add post users

@app.post("/users")
async def create_user(user: UserInput):
    with sqlite3.connect("eshop.db") as connection:
        cursor = connection.cursor()
        cursor.execute(f"INSERT INTO users(username, email) VALUES('{user.username}', '{user.email}')")
        connection.commit()
        return user


@app.get("/users")
async def get_users():
    users = []
    with sqlite3.connect("eshop.db") as connection:
        cursor = connection.cursor()
        cursor.execute("SELECT id, username, email FROM users")
        users = cursor.fetchall()
    return mappingUser(users)



@app.delete("/users/{id}")
async def delete_user(id: int):
    with sqlite3.connect("eshop.db") as connection:
        cursor = connection.cursor()
        cursor.execute("DELETE FROM users WHERE id=?",(id,))
        connection.commit()
        return {"message": "User deleted"}

@app.put("/users/{id}")
async def update_user(id: int, user: UserInput):
    with sqlite3.connect("eshop.db") as connection:
        cursor = connection.cursor()
        cursor.execute("UPDATE users SET username=?, email=? WHERE id=?",(user.username, user.email, id,))
        connection.commit()
        return user

# articles

@app.get("/articles")
async def get_articles():
    articles = []
    with sqlite3.connect("eshop.db") as connection:
        cursor = connection.cursor()
        cursor.execute("SELECT id, title, author FROM articles")
        articles = cursor.fetchall()
    return articles

@app.post("/articles")
async def create_article(article: ArticleInput):
    with sqlite3.connect("eshop.db") as connection:
        cursor = connection.cursor()
        cursor.execute(f"INSERT INTO articles(title, author) VALUES('{article.title}', '{article.author}')")
        connection.commit()
        return article
    
@app.delete("/articles/{id}")
async def delete_article(id: int):
    with sqlite3.connect("eshop.db") as connection:
        cursor = connection.cursor()
        cursor.execute("DELETE FROM articles WHERE id=?",(id,))
        connection.commit()
        return {"message": "Article deleted"}
    
@app.put("/articles/{id}")
async def update_article(id: int, article: ArticleInput):
    with sqlite3.connect("eshop.db") as connection:
        cursor = connection.cursor()
        cursor.execute("UPDATE articles SET title=?, author=? WHERE id=?",(article.title, article.author, id,))
        connection.commit()
        return article





