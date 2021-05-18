from selenium import webdriver
from features.Page.Base_page import Browser

def before_feature(context):
    context.browser = Browser()

def after_feature(context):
    context.browser.browser_quit()