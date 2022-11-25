#!/usr/bin/env python
# coding: utf-8

# In[3]:


import mysql.connector
import requests
import csv
import json


# In[4]:


conn = mysql.connector.connect(
      host ="localhost",
      user ="root",
      passwd ="kimtoan123",
      database = "QlSinhVien1"
)


# In[5]:


cursor = conn.cursor()


# In[6]:


customer1 = '''create table customers1(
    Ten varchar(255),
    DiaChi varchar(255),
    SoDienThoai varchar(30)

);'''


# In[271]:


customer = '''create table customers(
    Ten varchar(255),
    DiaChi varchar(255),
    SoDienThoai varchar(30),

);'''


# In[7]:


cursor.execute(customer1)


# In[17]:


response_get_customer = requests.get("https://007af9e4efaee0e02d3101cce3eb07b3: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@luxury-4832.myshopify.com/admin/api/2022-10/customers.json?limit=100")


# In[18]:


json_file=response_get_customer.json()
json_file


# In[19]:


json_file['customers'][0]['first_name']


# In[20]:


arr_ten = []
arr_diachi = []
arr_sdt = []
data_customer = []
for i in range(3):
    ten = json_file['customers'][i]['first_name']
    diachi = json_file['customers'][i]['addresses'][0]['city']
    sdt = json_file['customers'][i]['phone']
    arr_ten.append(ten)
    arr_diachi.append(diachi)
    arr_sdt.append(sdt)
    val = [arr_ten[i],arr_diachi[i],arr_sdt[i]]
    data_customer.append(val)
data_customer


# In[280]:


sql  = "INSERT INTO customers1(Ten,DiaChi,SoDienThoai) values (%s, %s, %s)"

        
cursor.executemany(sql,arr_cus)
conn.commit()


# In[10]:


sql_update_customer = """
UPDATE customers1 
SET DiaChi ='HCM'
WHERE Ten='Toan'
"""
cursor.execute(sql_update_dustomer)
conn.commit()


# In[290]:


sql_delete_customer = """
DELETE FROM customers1 WHERE Ten = 'Toan'
"""
cursor.execute(sql_delete)
conn.commit()


# In[281]:


product = '''create table products(
    Ten varchar(255),
    Gia varchar(255),
    SoLuong varchar(10)
);'''
cursor.execute(product)


# In[4]:


response_get_product = requests.get("https://007af9e4efaee0e02d3101cce3eb07b3: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@luxury-4832.myshopify.com/admin/api/2022-10/products.json?limit=100")


# In[5]:


data_product = response_get_product.json()
data_product


# In[283]:


len((data_product)['products'])


# In[8]:


data_product['products'][0]['title']


# In[284]:


data_product['products'][0]['variants'][0]['price']


# In[14]:


arr_title = []
arr_price = []
arr_quantity = []
data = []
for i in range(18):
    title = data_product['products'][i]['title']
    price = data_product['products'][i]['variants'][0]['price']
    quantity = data_product['products'][i]['variants'][0]['inventory_quantity']
    arr_title.append(title)
    arr_price.append(price)
    arr_quantity.append(quantity)
    ttin= [arr_title[i],arr_price[i],arr_quantity[i]]
    data.append(ttin)
data


# In[288]:


sql  = "INSERT INTO products(Ten,Gia,SoLuong) values (%s, %s, %s)"
        
cursor.executemany(sql,data)
conn.commit()


# In[289]:


sql_update_product = """
UPDATE products
SET Gia = Gia + 10
Where SoLuong = 0
"""
cursor.execute(sql_update_product)
conn.commit()


# In[ ]:


sql_delete_product = """
DELETE
FROM products
WHERE SoLuong = 0
"""
cursor.execute(sql_delete_product)
conn.commit()

