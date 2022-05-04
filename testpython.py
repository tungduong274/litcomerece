import requests
import json
import shopify


url = "https://bc193eaa65517fb9bad678ad2c96922f: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@duongkma99.myshopify.com/admin/api/2022-04/"

def get_products():
    endpoint= 'products.json'
    r = requests.get(url+endpoint)
    return
def get_product(productID):
    endpoint= f'product/{productID}.json'
    r = requests.get(url+endpoint)
    return
def change_price(productID,price):
    payload={
                "product" : {
                    "variants" : [{
                        "price" : price
                    }]
                }
    }
    endpoint= f'products/{productID}.json'
    r = requests.put(url+endpoint, json=payload)
    return
def change_productsImage(productID,image):
    payload={
                "product" : {
                    "images" : [{
                        "src" : image
                        }]
                }
        }
    endpoint=f"products/{productID}.json"
    r = requests.put( url +endpoint, json=payload)
    return
    
