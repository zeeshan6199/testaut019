from playwright.sync_api import expect,Page

class CartsPage:
    def __init__(self,page):
        self.page=page
        self.cartitems=page.locator(".cart_item")
       

    def clickcheckout(self):
        btn=self.page.get_by_role("button",name="Checkout")
        btn.click()

    def verifycartitems(self,*items):
        cartlist=[]
        prodlist=[]
        for j in range(self.cartitems.count()):
            singlecartitem=self.cartitems.nth(j).locator(".inventory_item_name")
            singlecartitemtext=singlecartitem.text_content()
            cartlist.append(singlecartitemtext)
        for item in items:
            prodlist.append(item)
        if(cartlist==prodlist):
            assert True,"Congrats! it is a match"
        else:
            assert False,"Sorry cart and prod items don't match"
           
        
        
             

        





   


    


    


    
        
        
        





