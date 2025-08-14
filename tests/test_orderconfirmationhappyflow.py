from playwright.sync_api import Page,expect
from pages.login_page import LoginPage
from pages.products_page import ProductsPage
from pages.cart_page import CartsPage
from pages.checkout_page import CheckoutPage
from  pages.summarypage import SummaryPage
def test_addtocart(postive_logged_in):
    #visiting page and logging in
    LoginPage(postive_logged_in)
    prodpage=ProductsPage(postive_logged_in)
    prodpage.addproducts("Sauce Labs Backpack","Sauce Labs Bike Light","Sauce Labs Bolt T-Shirt")
    assert prodpage.countcartprods()=='3'
    prodpage.carticon().click()
    cart=CartsPage(postive_logged_in)
    cart.verifycartitems("Sauce Labs Backpack","Sauce Labs Bike Light","Sauce Labs Bolt T-Shirt")
    cart.clickcheckout()

    #checkout page actions 
    checkpage=CheckoutPage(postive_logged_in)
    checkpage.filldetails()
    checkpage.clickcontinue()
    
    
    #summary page checking
    sumpage=SummaryPage(postive_logged_in)
    sumpage.verifysummaryitems("Sauce Labs Backpack","Sauce Labs Bike Light","Sauce Labs Bolt T-Shirt")
    sumpage.clickfinish()

    #Order confirmation
    finishindicator=postive_logged_in.locator("h2[class='complete-header']")
    expect(finishindicator).to_contain_text("Thank you for your order!")



    

    





    




    

    




    
    


    


    








