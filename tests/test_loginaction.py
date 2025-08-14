from playwright.sync_api import Page,expect
from pages.login_page import LoginPage
from pages.products_page import ProductsPage
def test_loginaction(postive_logged_in,page):
    #visit page and logging in
    LoginPage(postive_logged_in)
    prodpage=ProductsPage(page)
    expect(prodpage.verifytitle()).to_be_visible()
   
    


    








