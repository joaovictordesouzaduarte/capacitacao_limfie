#### Saving on data base sqlite
#%% 
import pandas as pd
import numpy as np
import sqlite3
from sqlalchemy import create_engine
from sqlalchemy.log import echo_property
from sqlalchemy.sql.expression import false
#
##%% 
##IMPORTS Data
#customers = pd.read_csv('./data/raw/olist_customers_dataset.csv')
#geolocation = pd.read_csv('./data/raw/olist_geolocation_dataset.csv')
#order_items = pd.read_csv('./data/raw/olist_order_items_dataset.csv')
#payments = pd.read_csv('./data/raw/olist_order_payments_dataset.csv')
#order_reviews = pd.read_csv('./data/raw/olist_order_reviews_dataset.csv')
#orders = pd.read_csv('./data/raw/olist_orders_dataset.csv')
#products = pd.read_csv('./data/raw/olist_products_dataset.csv')
#sellers = pd.read_csv('./data/raw/olist_sellers_dataset.csv')
#product_category_name = pd.read_csv('./data/raw/product_category_name_translation.csv')
#
#
##%% CREATE DATABASE
db = create_engine ('sqlite:///C:\\Users\\victo\\Music\\Projetos\\Curso_html_css_js\\codigo\\data\\raw\\db_olist.sqlite', echo = False)
conn = db.connect() #connecting to database
#
#
##%%
##Inserting in database
#schema_customer = """
#    CREATE TABLE customer(
#        customer_id                     TEXT,
#        customer_unique_id              TEXT,
#        customer_zip_code_prefix        INTEGER,
#        customer_city                   TEXT,
#        customer_state                  TEXT
#    )
#"""
##%% GEOLOCATION
#schema_geolocation = """
#    CREATE TABLE geolocation(
#    geolocation_zip_code_prefix      INTEGER,
#    geolocation_lat                  REAL,
#    geolocation_lng                  REAL,
#    geolocation_city                 TEXT,
#    geolocation_state                TEXT
#
#    )
#
#"""
#
##%% ORDER ITEMS
#schema_order_items = """
#    CREATE TABLE order_items(
#    order_id                 TEXT,
#    order_item_id            INTEGER,
#    product_id               TEXT,
#    seller_id                TEXT,
#    shipping_limit_date      TEXT,
#    price                    REAL,
#    freight_value            REAL
#
#    )
#
#"""
##%% PAYMENTS
#schema_payments = """
#    CREATE TABLE payments(
#        order_id                TEXT,
#        payment_sequential      INTEGER,
#        payment_type            TEXT,
#        payment_installments    INTEGER,
#        payment_value           REAL
#    )
#
#"""
##create a schema
#conn.execute(schema_payments)
#
##Insert data into table
#payments.to_sql('payments', con= conn, if_exists= 'append', index= False)
#
##%% ORDER_REVIEWS
#schema_order_review = """
#    CREATE TABLE order_review(   
#        review_id                  TEXT,
#        order_id                   TEXT,
#        review_score               INTEGER,
#        review_comment_title       TEXT,
#        review_comment_message     TEXT,
#        review_creation_date       TEXT,
#        review_answer_timestamp    TEXT
#
#    )
#"""
##create a schema
#conn.execute(schema_order_review)
##insert data into table
#order_reviews.to_sql('order_review', con= conn, if_exists= 'append', index= False)
#
#
#
#
##%%
##ORDERS
#schema_orders = """
#    CREATE TABLE orders (
#        order_id                         TEXT,
#        customer_id                      TEXT,
#        order_status                     TEXT,
#        order_purchase_timestamp         TEXT,
#        order_approved_at                TEXT,
#        order_delivered_carrier_date     TEXT,
#        order_delivered_customer_date    TEXT,
#        order_estimated_delivery_date    TEXT
#    )
#
#"""
#conn.execute(schema_orders)
#orders.to_sql('orders', con = conn, if_exists = 'append', index = False)
#
#
##%%
#schema_products = """
#    CREATE TABLE products (
#    product_id                      TEXT,
#    product_category_name           TEXT,
#    product_name_lenght             REAL,
#    product_description_lenght      REAL,
#    product_photos_qty              REAL,
#    product_weight_g                REAL,
#    product_length_cm               REAL,
#    product_height_cm               REAL,
#    product_width_cm                REAL
#    
#    )
#"""
#conn.execute(schema_products)
#products.to_sql('products', con = conn, if_exists = 'append', index = False)
#
#
##%%
#schema_sellers = """
#    CREATE TABLE sellers(
#        seller_id                 TEXT,
#        seller_zip_code_prefix    INTEGER,
#        seller_city               TEXT,
#        seller_state              TEXT
#
#    )
#
#"""
##create a schema
#conn.execute(schema_sellers)
##insert data
#sellers.to_sql('sellers', con = conn, if_exists = 'append', index = False)
#
#
##%%
#schema_product_category_name = """
#    CREATE TABLE product_category_name (
#        
#        product_category_name            TEXT,
#        product_category_name_english    TEXT
#        
#        
#    )
#
#"""
#conn.execute(schema_product_category_name)
#product_category_name.to_sql('product_category_name', con = conn, if_exists = 'append', index = False)
#
#
#%%
#product_category_name.head()
#
# %%
##Check if have a schema
##query = """
##    select name
##    from sqlite_master
##    where type = 'table'
##
##"""
##%%
#table = pd.read_sql_query(query, conn)
#table
# %% Query
df_qry = """
    SELECT *
    FROM customer c 
    left join orders o on o.customer_id  = c.customer_id 
"""


# %% CREATE A DF
df = pd.read_sql(df_qry, con= conn)
# %% 

# %%
