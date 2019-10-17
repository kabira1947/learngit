import mechanize

def page_url(url, proxy):
    browser= mechanize.Browser()
    browser.set_proxies(proxy)
    #cookies= mechanize.lwp_cookie_str()
    page = browser.open(url)
    code= page.read()
    print(code)
url = ('http://prabhukalyansamal.esy.es/')

proxy={"http":"192.168.172.100.0255"}


page_url(url,proxy)
