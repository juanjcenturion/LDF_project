import sqlite3

def readRows():
    conn= sqlite3.connect("Databases/phones.db") #Connect to .db 
    cursor = conn.cursor() 
    instruccion = f"SELECT * FROM phones"
    cursor.execute(instruccion) 
    datos= cursor.fetchall()
    conn.close()
    return datos

def createCartTable():
    conn= sqlite3.connect("Databases/phones.db") #Connect to .db
    cursor= conn.cursor()
    instruccion= """CREATE TABLE IF NOT EXISTS cart(
        model text,
        price integer
    ) """
    cursor.execute(instruccion)
    conn.commit()
    conn.close()

def insertProdToCart(model, price):
    conn= sqlite3.connect("Databases/phones.db") #Connect to .db
    cursor= conn.cursor()
    instruccion= f"INSERT INTO cart VALUES ('{model}', {price})"
    cursor.execute(instruccion)
    conn.commit()
    conn.close()

def readCart():
    conn= sqlite3.connect("Databases/phones.db") #Connect to .db 
    cursor = conn.cursor() 
    instruccion = f"SELECT * FROM cart" 
    cursor.execute(instruccion) 
    datos= cursor.fetchall()
    conn.close()
    return datos

def deleteCart():
    conn= sqlite3.connect("Databases/phones.db") #Connect to .db
    cursor= conn.cursor()
    instruccion= "DELETE FROM cart"
    cursor.execute(instruccion)
    conn.commit()
    conn.close()



if __name__ == "__main__":
    print(readRows())