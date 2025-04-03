### Python Virtual Environment

Path Operations

#### Why We need Schema

* it's a pain to get all the values from the body.
* The client can send whatever data they want.
* The data isn't getting validated.
* We ultimately want to force  the client to send data in a schema  that we exepect.

### Pydantic

CRUD

```
Create         POST     /posts       @app.post('/posts')

Read            GET     /posts/:id   @app.get('/posts/{id}') # id repersent path parameters
                GET     /posts      @app.get('/posts)

Update          PUT/PATCH   /posts/:id  @app.put('/posts/{id}')

Delete          DELETE  /posts/:id  @app.delete("/posts/{id}")
```

Best Practicse to follow

Always use the purals. example users not user


### Install Postman

```
brew install --cask postman
```

> [!Note]
>  Some time try to open postman redirect to open the app via browser. if that issue happens then remove the postman
app and install with brew will fix the issue.


### Create Post Operation

Dummy Route for testing
carefull about the structure your api.
Follow the order
Top Down approach

Create something https status code

client error response

server error response 

we need to manipluate the respone.

how do we manipulate the respone?

import Response in to fastapi

Not return null. looks not good.

#### Status code need to changed according to action of HTTP API calls

#### Builtin Documentation support

# any changes to do changes to you api then you  have to do documentation.

http://localhost:8000/docs

http://localhost:8000/redoc

### What is a database

database is a collection of organized data that can be easily accessed and managed.

We don't work or interact with database directely.

Instead we make use of a software referred to as a Database Management System(DBMS)


| Relational    |     Nosql      |
----------------|-----------------
| Mysql         |  MongoDB       |
| POSTGRESQL    |  DynamoDB      |
| ORACLE        |  ORACLE        |
| SQL SERVER    |  SQL SERVER    |

SQL - Language used to communicate with DBMS

SQL => DBMS => DB

### Postgres

Each instacne of posgres can be carved into multiple separate databases.

APP1 => POSTGRES(DB1)
APP2 => POSTGRES(DB2)

By default every Postgres instaaltion comes with one database already created called `postgres`.

This is important because Postgres requires you to specify the name of a database to make a connection.<br/>
So there needs to always be one database.

Tables

A Tables represents a subject or event in an application.

Users 
Products
Purchases

these all the tables form a relationship.

### Columns vs Rows

A table is made up of columns and rows

Each Columns represents a different attribute.

Each row represents a different entry in the table.<br/>
     Colums  Colums Colums Colums<br/>

```
|  ID    | name     |   Age | Sex |
-----------------------------------
| 14642  | Carl     | 40    | M   | 

```

Database have datatypes just like any programming language.<br/>

```
| Data Type   | Postgres                |  Python    |
------------------------------------------------------
| Numeric     | Int, decimal, Precision | Int, float |
| Text        | Varchar, Text           | String     |
| Bool        | Boolean                 | boolean    |
| Sequence    | Array                   | list       |
```
### Primary Key

Is a column or group of columns that uniquely identities each row in a table

Table can have one and only `one Primary Key`.
                           
Primary Key (id) => Each Entry must be unique, no Duplicates

The Primary key does not have to be the ID column always. it's up to you to decide which column uniquely defines each record.

In this example, since an email can only be registered once, the email column can also be used as the primary key

Primary Key: xxxxxxx@gmail.cvom

### Unique Contraints

A UNIQUE constraint can be applied to any column to amke sure every record has a unique value for that column.

name is not same for 

### Null Constraints


 By default, when adding a new entry to a database, any column can be left blank. when a column is left blank, it has a null value.

 If you need column to be properely filled in to create a new record, a NOT NULL constraint can be added to the column to ensure that the column is never left blank.

```
--------------------------------
| 7   | Carl    |    NULL  |  M |
--------------------------------
```
Cannot be Null

### SemiColoum at the end of the every SQL command

```
* means every single column

* SELECT id, name, price FROM products

* SELECT name, id, price FROM products # Order matter here
```

### Basic SQL command and User defined command

Rename Column name using the following command 

```
SELECT id AS products_id, is_sale AS on_sale FROM products

SELECT id, name FROM products WHERE id = 3;

SELECT id, name, price FROM products

SELECT * FROM PRODUCTS;

SELECT id AS products_id, is_sale AS on_sale FROM products

SELECT * FROM products WHERE inventory = 0;

SELECT * FROM products WHERE name = TV;

SELECT * FROM products WHERE price <= 80;

SELECT * FROM products WHERE inventory <> 0;

SELECT * FROM products WHERE inventory > 0 AND price > 20;

SELECT * FROM products WHERE price > 100 OR price < 20;

SELECT * FROM products WHERE id = 1 OR id = 2 OR id = 3 -- Same down query

SELECT * FROM products WHERE id IN (1,2,3);

SELECT * FROM products WHERE name LIKE 'TV%';

SELECT * FROm products WHERE name LIKE 'a%'

SELECT * FROm products WHERE name LIKE '%e'

SELECT * FROm products WHERE name NOT LIKE '%e'

SELECT * FROm products WHERE name NOT LIKE '%en%';

SELECT * FROM products ORDER By price ASC;

SELECT * FROM products ORDER By price DESC;

SELECT * FROM products ORDER By inventory DESC;

SELECT * FROM products ORDER By inventory DESC, price;

SELECT * FROM products ORDER By created_at DESC;

SELECT * FROM products ORDER By created_at DESC;

SELECT * FROM products WHERE price > 20 ORDER By created_at DESC;

SELECT * FROM products LIMIT 5;

SELECT * FROM products WHERE price > 10 LIMIT 5;

SELECT * FROM products ORDER BY id LIMIT 5;  # OFFSET to SKIP 2 first result

SELECT * FROM products ORDER BY id LIMIT 5 OFFSET 5;

SELECT * FROM products;

INSERT INTO products (name, price, inventory ) VALUES ('tortilla', 4, 1000);

INSERT INTO products (name, price, inventory ) VALUES ('car', 10000, 1000) returning *;

INSERT INTO products (name, price, inventory ) VALUES ('car', 10000, 1000), ('laptop', 50, 25), ('monitor', 60, 4) returning *;

INSERT INTO products (name, price, inventory ) VALUES ('car', 10000, 1000), ('laptop', 50, 25), ('monitor', 60, 4) returning id, created_at, name;

DELETE FROM products WHERE id = 12 RETURNING *;

SELECT * FROM products;

DELETE FROM products WHERE inventory = 0 RETURNING *;

UPDATE products SET name = 'flour tortilla', price = 40 WHERE id = 18;

UPDATE products SET is_sale = true WHERE id = 23 RETURNING *;

UPDATE products SET is_sale = true WHERE id > 15 RETURNING *;
```

### Connect To Database Python

Psycopg library used to connect DB from python

python3 -c "import psycopg2; print(psycopg2.__version__)"


### Object Relational Mapper (ORM)

* Layer of abstraction that sits between the database and us.
* we can perform all database operations through traditional python code. No more SQL!

### Traditional

> [!NOTE]
>            SQL
> Fast API <========> DB

### ORM


          Python      psycopg
                      SQL
> [!NOTE]
> Fast API <====>  ORM <=========> DB

### What can ORMs do

Instead of manually defining tables in postgres, we can define out tables as `python models`.
                                                                             
Queries can be made exclusively through python code. No SQL is necessary.

```python
class Post(Base):
     __tablename__ = "posts"

     id = Column(Integer, primary_key=True, index=True)
     title = Column(String, index=True, nullable=False)
     content = Column(String, nullable=False)
     published = Column(Boolean)

db.query(models.Post).filter(models.Post.id == id).first()
```

### SQLALCHEMY

Sqlalchemy is one of the most popular python ORMs

It is standalone library and has no association with FastAPI. it can be
used with any other python web frameworks or any python based application.

