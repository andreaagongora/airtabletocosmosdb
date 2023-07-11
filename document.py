import datetime
import uuid

# ---------------------------------------------------------------------
# This functions convert the datatypes gotten from the airtable api
# to document json to post on Cosmo db 
# ---------------------------------------------------------------------

def product_document(product):
    product = {
        'product_id': product["Product ID"],
        'category': product["Category"],
        'sub_category': product["Sub-Category"],
        'product_name': product["Product Name"]
    }

    return product


def customer_document(customer):
    customer = {
        'customer_id': customer["Customer ID"],
        'name': customer["Customer Name"],
        'segment': customer["Segment"]
    }

    return customer


def sales_order_document(sell, customer, product):
    sell = { 
        'id': str(uuid.uuid4()),
        'OrderId': sell["Order ID"], # change to order_id
        'order_date': datetime.date(2005,1,10).strftime('%c'),
        'ship_date': datetime.date(2005,1,10).strftime('%c'),
        'ship Mode': sell["Ship Mode"],
        'customer': customer,
        'country': sell["Country"],
        'city': sell["City"],
        'state': sell["State"],
        'postal_code': sell["Postal Code"],
        'region': sell["Region"],
        'product' : product,
        'sales': sell["Sales"]
    }

    return sell