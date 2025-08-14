from playwright.sync_api import Page,expect

class SummaryPage:
    def __init__(self,page):
        self.page=page
        self.sumitems=page.locator(".cart_item")
        

    def clickfinish(self):
        self.finishbtn=self.page.get_by_role("button",name="Finish")
        self.finishbtn.click()

    def verifysummaryitems(self,*its):
        summarylist=[]
        prodsumlist=[]
        for j in range(self.sumitems.count()):
            nameit=self.sumitems.nth(j).locator(".inventory_item_name")
            singlesumitemtext=nameit.text_content()
            summarylist.append(singlesumitemtext)
        for item in its:
            prodsumlist.append(item)
        if(summarylist==prodsumlist):
            assert True,"Congrats! it is a match"
        else:
            assert False,"Sorry summary and prod items don't match"
           
        
        

       

    

     

           
        
        
             

        





   


    


    


    
        
        
        





