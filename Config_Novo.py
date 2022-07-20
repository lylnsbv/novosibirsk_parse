from Proxy import Proxies as Prx


'''   url address   '''
url = 'https://novosibirsk.cian.ru/'
card_url = 'https://novosibirsk.cian.ru/sale/{}/{}/'
captcha_url = 'https://novosibirsk.cian.ru/captcha/?redirect_url=https://novosibirsk.cian.ru/'

vtorichka_cat = 'cat.php?deal_type=sale&engine_version=2&object_type%5B0%5D=1&offer_type=flat&p={}&region=4897'
newbuild_cat = 'cat.php?deal_type=sale&engine_version=2&object_type%5B0%5D=2&offer_type=flat&p={}&region=4897'
commercial_cat = 'cat.php?deal_type=sale&engine_version=2&offer_type=offices&office_type%5B0%5D=1&' \
                 'office_type%5B1%5D=2&office_type%5B2%5D=3&office_type%5B3%5D=4&office_type%5B4%5D=5&' \
                 'office_type%5B5%5D=7&office_type%5B6%5D=9&office_type%5B7%5D=10&office_type%5B8%5D=11&p={}' \
                 '&region=4897'
commercialLand_cat = 'cat.php?cats%5B0%5D=commercialLandSale&deal_type=sale&engine_version=2&offer_type=offices&p={}&' \
                     'region=4897'
landPlot_cat = 'cat.php?deal_type=sale&engine_version=2&object_type%5B0%5D=3&offer_type=suburban&p={}&region=4897'


'''  url list   '''
url_list = [url + vtorichka_cat, url + newbuild_cat, url + commercial_cat, url + commercialLand_cat, url + landPlot_cat]
url_n = [1, 2, 3, 4, 5]


'''   proxy list   '''
proxy_list = Prx().get_proxy_online_proxy()


'''   header list  '''
header = {
    "userAgent": "Mozilla\u002F5.0 (Windows NT 6.3; Win64; x64) "
                 "AppleWebKit\u002F537.36 (KHTML, like Gecko) "
                 "Chrome\u002F83.0.4103.61 Safari\u002F537.36"
}
user_agent_list = [
    # Chrome
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) '
    'AppleWebKit/537.36 (KHTML, like Gecko) '
    'Chrome/60.0.3112.113 Safari/537.36',
    'Mozilla/5.0 (Windows NT 6.1; Win64; x64) '
    'AppleWebKit/537.36 (KHTML, like Gecko) '
    'Chrome/60.0.3112.90 Safari/537.36',
    'Mozilla/5.0 (Windows NT 5.1; Win64; x64) '
    'AppleWebKit/537.36 (KHTML, like Gecko) '
    'Chrome/60.0.3112.90 Safari/537.36',
    'Mozilla/5.0 (Windows NT 6.2; Win64; x64) '
    'AppleWebKit/537.36 (KHTML, like Gecko) '
    'Chrome/60.0.3112.90 Safari/537.36',
    'Mozilla/5.0 (X11; Linux x86_64) '
    'AppleWebKit/537.36 (KHTML, like Gecko) '
    'Chrome/44.0.2403.157 Safari/537.36',
    'Mozilla/5.0 (Windows NT 6.3; Win64; x64) '
    'AppleWebKit/537.36 (KHTML, like Gecko) '
    'Chrome/60.0.3112.113 Safari/537.36',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) '
    'AppleWebKit/537.36 (KHTML, like Gecko) '
    'Chrome/57.0.2987.133 Safari/537.36',
    'Mozilla/5.0 (Windows NT 6.1; Win64; x64) '
    'AppleWebKit/537.36 (KHTML, like Gecko) '
    'Chrome/57.0.2987.133 Safari/537.36',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) '
    'AppleWebKit/537.36 (KHTML, like Gecko) '
    'Chrome/55.0.2883.87 Safari/537.36',
    'Mozilla/5.0 (Windows NT 6.1; Win64; x64) '
    'AppleWebKit/537.36 (KHTML, like Gecko) '
    'Chrome/55.0.2883.87 Safari/537.36',
    # Firefox
    'Mozilla/4.0 (compatible; MSIE 9.0; Windows NT 6.1)',
    'Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; rv:11.0) like Gecko',
    'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; WOW64; Trident/5.0)',
    'Mozilla/5.0 (Windows NT 6.1; Trident/7.0; rv:11.0) like Gecko',
    'Mozilla/5.0 (Windows NT 6.2; WOW64; Trident/7.0; rv:11.0) like Gecko',
    'Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; rv:11.0) like Gecko',
    'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.0; Trident/5.0)',
    'Mozilla/5.0 (Windows NT 6.3; WOW64; Trident/7.0; rv:11.0) like Gecko',
    'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0)',
    'Mozilla/5.0 (Windows NT 6.1; Win64; x64; Trident/7.0; rv:11.0) like Gecko',
    'Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.1; WOW64; Trident/6.0)',
    'Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.1; Trident/6.0)',
    'Mozilla/4.0 ('
    'compatible; MSIE 8.0; Windows NT 5.1; Trident/4.0; .NET CLR 2.0.50727; .NET CLR 3.0.4506.2152; .NET CLR 3.5.30729'
    ')'
]
