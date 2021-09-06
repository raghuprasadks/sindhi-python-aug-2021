"""
constructor - used to pass parameter
at the time of object creation
"""
class Product():
    '''
    attributes
    '''
    code=0
    name=''
    desc=''
    manu=''
    price=0
    '''
    methods
    '''
    def addProduct(self,code,name,desc,manu,price):
        self.code = code
        self.name = name
        self.desc = desc
        self.manu = manu
        self.price = price
    
    def displayProduct(self):
        info = "Code : ",self.code," Name : ",self.name," Desc : ",self.desc
        return info
        
'''
product1 is an object
'''        
product1 = Product()
product1.addProduct(1,"Laptop 14 inch","14 inch 8 gb ram","hp",67000)
info=product1.displayProduct()
print("Information about product1 ",info)

product2 = Product()
product2.addProduct(2,"Laptop 14 inch","14 inch 8 gb ram","dell",69000)
info=product2.displayProduct()
print("Information about product2 ",info)

'''
creation of product with a constuctor
'''
class ProductWithConstructor():
    '''
    attributes
    '''
    code=0
    name=''
    desc=''
    manu=''
    price=0
    '''
    Constructor
    '''
    def __init__(self,code,name,desc,manu,price):
        self.code = code
        self.name = name
        self.desc = desc
        self.manu = manu
        self.price = price
    
    def displayProduct(self):
        
        info = "Code : ",self.code," Name : ",self.name," Desc : ",self.desc
        
        return info

'''
object creation using a constructor
'''
product1 =ProductWithConstructor(3,"mobile 10 inch","iphonex","apple",120000)
info=product1.displayProduct()
print("Information about product1 using constructor ",info)
