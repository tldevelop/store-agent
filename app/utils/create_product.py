import requests

def create_product(payload:dict, headers:dict, endpoint:str) -> str:
    product = {
        'name':payload.get('product_name'),
        'price':float(payload.get('price')),
        'description':payload.get('description'),
        'stock':int(payload.get('stock'))
    }

    try:
        requests.post(endpoint,headers=headers,json=product)
        print("request successful")
    except:
        print("something went wrong")
        

    