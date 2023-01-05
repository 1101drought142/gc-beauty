from django.shortcuts import get_object_or_404
from .models import Item

class BaseSessionStored:
    
    def __init__(self, request, session_id : str):
        self.session = request.session
        cart = self.session.get(session_id)
        if not cart:
            cart = self.session[session_id] = {}
        self.cart = cart

    def add(self, item_id : int, quantity : int):
        bd_item = get_object_or_404(Item, pk = item_id)
        str_item_id = str(item_id)
        if not(self.cart.get(str_item_id)):
            self.cart[str_item_id] = {"quantity" : 0}
        self.cart[str_item_id]["quantity"] += int(quantity)
        self.cart[str_item_id]["picture"] = bd_item.main_picture.url
        self.cart[str_item_id]["name"] = bd_item.name
        self.cart[str_item_id]["price"] = float(bd_item.price)
        self.cart[str_item_id]['slug'] = bd_item.slug
        self.cart[str_item_id]['item_price'] = quantity * float(bd_item.price)
        #self.cart[str_item_id]["description"] = bd_item.small_description
        self.save()

    def delete(self, item_id : int) :
        str_item_id = str(item_id)
        if  self.cart.get(str_item_id):
            del self.cart[str_item_id]
            self.save()
        else:
            raise ValueError("No element id in session")
    
    def modify_if_favourite(QuerySetToModify):
        temp_cart = self.cart
        for query in QuerySetToModify:
            if self.cart.get(query.id):
                query.is_favourite = True
            else:
                query.is_favourite = False
        return QuerySetToModify

    def return_cart_contents(self):
        return self.cart

    def save(self):
        self.session.modified = True

class Cart_Session(BaseSessionStored):
    
    def __init__(self, request):
        session_id = "CART"
        super().__init__(request, session_id)

    def change_quantity(self, item_id: int, quantity : int):
        str_item_id = str(item_id)
        if self.cart.get(str_item_id):
            
            self.cart[str_item_id]["item_price"] = float(self.cart[str_item_id]["item_price"] / self.cart[str_item_id]["quantity"])
            self.cart[str_item_id]["item_price"] = self.cart[str_item_id]["item_price"] * quantity
            self.cart[str_item_id]["quantity"] = quantity
            
            self.save()
        else:
            raise ValueError("No element id in session")

    def calc_price(self) -> int:
        res_price = 0
       
        for cart_item in self.cart:
           
            res_price += float(self.cart[cart_item]["price"]) * int(self.cart[cart_item]["quantity"])
        return res_price

class Liked_Session(BaseSessionStored):
    def __init__(self, request):
        session_id = "LIKED"
        super().__init__(request, session_id)
        
    def add(self, item_id : int):
        super().add(item_id, 0)