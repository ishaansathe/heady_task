# heady_task
## Table of contents
* [General info](#general-info)
* [Technologies](#technologies)
* [Setup](#setup)
* [API Request and Response Examples](#api)

## General info 
The Task is Building a RESTful APIs from scratch using Python-Flask and Mongo Db 

## Technologies utitlzed 
1) Python-3.6 
2) Flask-1.0.3 
3) Mongo-db-3.6.3 

## Setup 
### This project is developed in Linux-Ubuntu
To run this project you need to install the following in command-line(terminal)
'''
pip3 install flask 

pip3 install pymongo 

sudo apt update && sudo apt upgrade -y

sudo apt install mongodb

sudo systemctl status mongodb

sudo systemctl enable mongodb
'''

Then run app.py then the app will start serving at 0.0.0.0:5050

## API Request and Response Examples
### API Resources
* [GET /](#/)
* [GET /category](#/category)
* [POST /category](#/category)
* [POST /product](#/product)
* [GET /product/[category]](#/category2)
* [PATCH /product](#patch)

## GET /
### Example URL "http://0.0.0.0:5050/"
Response:  
'''
"Health Check ok"
'''

## GET /category
### Example URL http://0.0.0.0:5050/category?category=BOOKS
Input Body:
''' Params:
    {"category":"BOOKS"}
'''






'''
Response:
{
  "data ": [
    {
      "Category": "Electric Appliances",
      "Id": null,
      "child_categories": []
    }
  ],
  "success": true
}
'''




## POST /category
### Example URL "http://0.0.0.0:5050/category"
Input body:
'''
payload = "{\n\t\"category\":\"Books\" , \n\t\"child_category\":[\"Horror\" , \"Fiction\"]\n}"
headers = {
  'Content-Type': 'application/json'
}
'''




'''
Response :
{
  "msg": "category is written successfully",
  "success": true
}
'''

## POST /product
### Example URL "http://0.0.0.0:5050/product"
Input body:
'''
  payload = [{"name": "Mercedes 600 (1967)", "price": "5000000", "categories" : ["Electric Appliances","cars"], "description": "the best mercedes ever"  }]
headers = {
  "Content-Type': 'application/json"
}
'''



'''
Response :
{
  "msg": "products is written successfully",
  "success": true
}
'''

## GET /product/[category]
### Example URL "http://0.0.0.0:5050/product/cars"
Response:
'''
{
  "category": "cars",
  "products": [
    {
      "categories": [
        "Electric Appliances",
        "cars"
      ],
      "description": "the best mercedes ever",
      "name": "Mercedes 600 (1967)",
      "price": "5000000"
    }],
    success:True
}
'''
## PATCH /product
### Example URL "http://0.0.0.0:5050/product"


Input body:
"""
payload = {"pr_name":"Jeans" }
headers = {
  'Content-Type': 'application/json'
}
"""




"""
Response:
"""
{
  "msg": "product updated successfully,
  "success": true
}
"""











