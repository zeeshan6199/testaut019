from playwright.sync_api import Page,expect

class ProductsPage:
    def __init__(self,page):
        self.page=page
        self.title=page.locator("span[class='title']")
        self.shoppingcart=page.locator(".shopping_cart_link")
        self.filterbtn=page.locator("span[class='select_container']")
        self.products=page.locator(".inventory_item")
        self.shoppingcartcount=page.locator("span[class='shopping_cart_badge']")
        self.prices=page.locator(".inventory_item_price").element_handles()
        
    
    def sort_ascending(self,page):
        initialorder=[]
        for num in self.prices:
            numb=num.text_content()
            initialorder.append(float(numb[1:]))
        page.locator(".product_sort_container").select_option("lohi")
        newprices=page.locator(".inventory_item_price").element_handles()
        comparelist=[]
        for num in newprices:
            numb=num.text_content()
            comparelist.append(float(numb[1:]))
        initialorder.sort()
        if(comparelist==initialorder):
            assert True
        else:
            assert False
        

    def sort_descending(self,page):
        initialorder=[]
        for num in self.prices:
            numb=num.text_content()
            initialorder.append(float(numb[1:]))
        page.locator(".product_sort_container").select_option("hilo")
        newprices=page.locator(".inventory_item_price").element_handles()
        comparelist=[]
        for num in newprices:
            numb=num.text_content()
            comparelist.append(float(numb[1:]))
        initialorder.sort(reverse=True)
        if(comparelist==initialorder):
            assert True
        else:
            assert False

        
       





        

    



    def addproducts(self,*items):
        for item in items:
            card=self.products.filter(has=self.page.locator(".inventory_item_name ",has_text=item))
            card.get_by_role("button",name="Add to cart").click()
            

    def verifytitle(self):
        return self.title

    def countcartprods(self):
        number=self.shoppingcartcount.text_content()
        return number
    
    def carticon(self):
        return self.shoppingcart
    


    


    


    
        
        
        





