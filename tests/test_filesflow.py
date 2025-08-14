from playwright.sync_api import Page,expect
from pathlib import Path

def test_fileflows(page):
    page.goto("https://www.ilovepdf.com/pdf_to_word")
    pdfbtn=page.locator("input[type='file']").nth(0)
    pdfbtn.set_input_files(Path("invoicesample.pdf"))

    #convert to word
    convertbtn=page.locator("button[id='processTask']")
    expect(convertbtn).to_be_visible()
    convertbtn.click()

    #downloadfolder
    downloadbtn=page.locator("a[slot='downloadUrl']")
    expect(downloadbtn).to_be_visible()
    downloadbtn.click()
  


   

    

 




   


