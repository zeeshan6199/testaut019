from playwright.sync_api import Page

class LoginPage:
    def __init__(self,page:Page):
        self.page=page
        self.username=page.get_by_placeholder("Username")
        self.password=page.get_by_placeholder("Password")
        self.loginbtn=page.locator("input[type='submit']")

    def goto(self):
        self.page.goto("https://www.saucedemo.com/")
    
    def login(self,u,p):
        self.username.fill(u)
        self.password.fill(p)
        self.loginbtn.click()




