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


# In[ ]:


response_get_customer = requests.get("https://007af9e4efaee0e02d3101cce3eb07b3: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@luxury-4832.myshopify.com/admin/api/2022-10/customers.json?limit=100")


# In[274]:


json_file=response_get_customer.json()
json_file


# In[275]:


json_file['customers'][0]['first_name']


# In[276]:


arr_ten = []
for i in range(3):
    ten = json_file['customers'][i]['first_name']
    arr_ten.append(ten)
arr_ten


# In[277]:


arr_sdt = []

for i in range(3):
    sdt = json_file['customers'][i]['phone']
    sdt = sdt.strip('+')
    arr_sdt.append(sdt)
arr_sdt 



# In[278]:


arr_diachi = []
for i in range(3):
    diachi = json_file['customers'][i]['addresses'][0]['city']
    arr_diachi.append(diachi)
arr_diachi 


# In[279]:



arr_cus = []
for i in range(3):
    val = [arr_ten[i],arr_diachi[i],arr_sdt[i]]
    arr_cus.append(val)
arr_cus
        


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


# In[ ]:





# In[282]:


data_product = response_get_product.json()
data_product


# In[283]:


len((data_product)['products'])


# In[284]:


data_product['products'][0]['variants'][0]['price']


# In[285]:


arr_price = []
for i in range(18):
    price = data_product['products'][i]['variants'][0]['price']
    arr_price.append(price)
arr_price


# In[286]:


arr_quantity = []
for i in range(18):
    quantity = data_product['products'][i]['variants'][0]['inventory_quantity']
    arr_quantity.append(quantity)
arr_quantity


# In[287]:


data = []
for i in range(18):
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

