from flask import (Flask, Response, abort, jsonify, redirect, request,
                   send_from_directory  , send_file)
import uuid , pymongo
from global_variable import secret_key ,  mongo_db as db 
import datetime
app = Flask(__name__)
app.config['JWT_SECRET_KEY'] = secret_key


@app.route("/" )
def hello():
    ''' checking working of flask API
        responses:
        200: Flask APP working
        500:Flask APP not working'''
    
    return jsonify("Health Check ok") , 200
#adding of a category to db and getting data
@app.route("/category" , methods=['GET' , "POST"])
def add_get_category():
    '''getting all category and categories based on category
        response:
        200:all categories and categories are returned 
        404:the given category does not exist
    '''
    if request.method == "GET":
        category_to_find = request.args.get("category" , None)
        if category_to_find == None:
            return jsonify({"success":False , "msg":"No category found"}),404
        category_to_find = category_to_find.lower()
        get_data = db.category.find({"category":category_to_find})
        get_data = list(get_data)
        category_list = [] 
        for  data in (get_data):
            dict_category_data = {}
            dict_category_data["Category"] = data["category"]
            dict_category_data["Id"]  = data.get("ID")
            dict_category_data["child_categories"] = data.get("child_category",[])
            category_list.append(dict_category_data)
        return jsonify({"data ":category_list , "success":True}) , 200
    else :
        '''input : category :string,
            child_categories: comma seperated data
            200:New Category is inserted 
            404:the given category does not exist
            '''



        data = request.get_json()
        category =data.get("category" , None)
        if category !=None:
            category  = category.lower()
        child_category = data.get("child_category" , [])
        if category == None:
            return jsonify({"success":False , "msg":"No category found"}),404
        else :
            find_category = db.category.find_one({"category":category})
            if find_category !=None:
                return jsonify({"msg":"category already exists" , "success":False})
            add_category = db.category.insert_one({"category":category , 'ID':str(uuid.uuid1())[:8] ,  "Parent":True , "child_category":child_category})
            return jsonify({"success":True , "msg":"category is written successfully"}) , 200
# adding of product to db with category
@app.route("/product" , methods = ["POST"])
def add_product():
    ''' input : category :string,
        child_categories: comma seperated list of objects
        200:New product  is created 
        404:the given product list is not passed 
            '''
    
    data = request.get_json()
    products_data = data.get("product_data" , None)
    if products_data == None:
        return jsonify({"success":False , "msg":"Products list not found"}) , 404
    else :
        for data in products_data:
            data["PID"] = datetime.datetime.utcnow().strftime('%d.%m.%Y %H:%M:%S.%f')
            db.products.insert_one(data)
        return jsonify({"success":True , "msg":"products is written successfully"}),200
# getting all categories in db 
#getting product on category
@app.route("/product/<category>"   , methods=["GET"])
def get_products(category):
    ''' input : category from url
        response:products list based on category
        response_code:
        200: All products are returned
        404: category does not exist'''
    #data = request.get_json()
    category = category.lower()
    #category = data.get("category")
    find = db.products.find({"categories":{"$in":[category]}} , {"_id":0})
    ret = list(find)
    if ret == []:
        ret = []
        return jsonify({"category":category , "products":ret , 'msg':"The category does not exist" , "success":False}) , 404
    return jsonify({"category":category , "products":ret , "success":True}),200
#updating data of product based on product name
@app.route("/product" , methods  = ["PATCH"])
def update_data():
    ''' input : category :string,
        child_categories: comma seperated data
        200:Product is updated updated in DB
        404:the given category does not exist
        '''
    data = request.get_json()
    name = data.get("pr_name" , None)
    find = db.products.find_one({"name":name})
    if find == None:
        return jsonify({"success":False , "msg":"the product does not exist"}),404
    update_data = data.get("update_list" , None)
    try:
        for data in update_data:
            result = db.products.update_one({"name":name} , {"$set":data})
        return jsonify({"success":True , "msg":"products is updated successfully"}),200
    except pymongo.errors.PyMongoError as e:
        return jsonify({"success":False , "msg":"error while updating data"}),500


if __name__=='__main__':
    app.run(host="0.0.0.0", port=5050 , debug= True)




