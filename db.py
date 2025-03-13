from tinydb import TinyDB, Query


class ProductsDB:
    def __init__(self, db_path):
        self.db = TinyDB(db_path)
        self.query = Query()
        self.table = self.db.table('Products')
    
    def all_products(self):
        """Returns all products in the database"""
        return self.table.all()
    
    def get_product_id(self, id):
        """Returns all products by id"""
        return self.table.get(self.query.id == 5)
    
    def get_all_product_names(self):
        """Returns all product names"""
        return [product['name'] for product in self.table.all()]

    def get_names(self, name: str):
        """Returns all products by name"""
        return self.table.get(self.query.name == "Mouse")

    def get_all_catagories(self):
        """Returns all catagories name"""
        return [product['category'] for product in self.table.all()]
    
    def get_small_from_price(self, price):
        """Returns products if product's price small from price"""
        return self.table.get(self.query.price <743.17 )

    def expensive_products(self):
        """Returns a top three expensive products"""
        dic={}
        for i in [i['price'] for i in self.table.all()][-3:]:
            dic[i]=self.table.search(self.query.price == i)
        return dic
    
    def get_between_price(self, max_price, min_price):
        """Returns a products between max_price and min_price"""
        max_price =sorted([i['price'] for i in self.table.all()])[-1]
        min_price =sorted([i['price'] for i in self.table.all()])[0]
        return self.table.search((self.query.price >= min_price) & (self.query.price <= max_price))
        

    def add_product(self, product):
        """Adds a product to the database"""
        data=self.table
        data.insert(product)
        return f'we inserted this product {product}'

    def delete_product(self, doc_id):
        """Deletes a product from the database"""
        Product=Query()
        return self.table.remove(Product.id == doc_id)