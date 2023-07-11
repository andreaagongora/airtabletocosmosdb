import os
from pyairtable import Table
from pyairtable.formulas import match
from dotenv import load_dotenv
load_dotenv()

from document import *
from cosmodb import getorcreatecontainer

api_key = os.environ['AIRTABLE_API_KEY']
base_id = os.environ['AIRTABLE_BASE_ID']

table_sells = Table(api_key, base_id, 'sells')
table_products = Table(api_key, base_id, 'products')
table_customers = Table(api_key, base_id, 'products')


#record_sell = table_sells.get('recLmkAn2UuRHwVH4')["fields"]
#record_product = table_products.get(record_sell["Product ID"][0])["fields"]
#record_customer = table_products.get(record_sell["Customer ID"][0])["fields"]

record_sell = table_sells.all(formula=match({"Row ID": 1000}))[0]["fields"]
record_product = table_products.get(record_sell["Product ID"][0])["fields"]
record_customer = table_products.get(record_sell["Customer ID"][0])["fields"]

#product = product_document(record_product)
#customer = customer_document(record_customer)
#sell = sales_order_document(record_sell, customer, product)

#print(record_sell)
#print(sell)
#print(record_product)
#print(product)
#print(record_customer)
#print(customer)

#container = getorcreatecontainer()
#print(container)
# create item
#container.create_item(body=sell)





