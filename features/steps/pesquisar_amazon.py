from behave import given, when, then, step
from features.Page.Base_page import Browser
from features.Page.google_page import GooglePage
from features.Page.amazon_page import AmazonPage
from features.Page.elements_page.google_elements import Google_Locations


GP = GooglePage()
AP = AmazonPage()

@given(u'que acesso a pagina do google')
def step_impl(context):
    GP.go_to_page(Google_Locations().URL_GOOGLE)

@when(u'pesquiso por "Amazon"')
def step_impl(context):
    GP.search_google("Amazon")

@then(u'resultados relacionados ao "Amazon" são exibidos')
def step_impl(context):
    GP.validate_search('Amazon.com.br')
    GP.screenshot('Google.png')

@given(u'que acesso a pagina principal da amazon')
def step_impl(context):
    AP.go_to_page()

@when(u'pesquiso "Livro" na Amazon')
def step_impl(context):
    AP.search_amazon("Livro")

@then(u'livros vendidos são exibidos')
def step_impl(context):
    AP.validate_search("Livro")
    GP.screenshot('Amazon.png')