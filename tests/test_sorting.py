from playwright.sync_api import Page,expect
from pages.login_page import LoginPage
from pages.products_page import ProductsPage

def test_sorting(postive_logged_in):
    #visit page and logging in
    LoginPage(postive_logged_in)
    prodpage=ProductsPage(postive_logged_in)
    prodpage.sort_ascending(postive_logged_in)
    prodpage.sort_descending(postive_logged_in)



    
    
    





    




    

    




    
    


    


    








