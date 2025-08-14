from playwright.sync_api import Page,expect

class CheckoutPage:
    def __init__(self,page):
        self.page=page
        self.username=page.get_by_placeholder("First Name")
        self.password=page.get_by_placeholder("Last Name")
        self.postalcode=page.get_by_placeholder("Zip/Postal Code")
        

    def clickcontinue(self):
        submitbtn=self.page.locator("input[type='submit']")
        submitbtn.click()

    def filldetails(self):
        self.username.fill('abcd')
        self.password.fill('2313')
        self.postalcode.fill('6050')

     

           
        
        
             

        





   


    


    


    
        
        
        





