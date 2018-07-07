from amazon.models import db
import pymongo
from bson.objectid import ObjectId


def search_by_name(name):
    # lets search for the product here
    query = {'name': name}
    matching_products = db['products'].find(query)
    matching_products.sort([('price', pymongo.DESCENDING)])
    return list(matching_products)


def get_details(p_id):
    cursor = db.products.find({'_id': ObjectId(p_id)})
    if cursor.count() == 1:
        return cursor[0]
    else:
        return None


def add_product(product):
    db['products'].insert_one(product)


def update_product(p_id, updated_product):
    # create filter and update dicts
    filter = {'_id': ObjectId(p_id)}


    # update in DB
    success=db['products'].update_one(filter=filter,update= updated_product)
    if success:
        return True
    else:
        return False