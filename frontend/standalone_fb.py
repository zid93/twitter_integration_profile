import requests,json


def main_fb():
    url_fb = 'https://graph.facebook.com/v10.0/me?fields=id,name,email,picture,birthday&access_token=EAAGB5ZCLVYQQBAFiYpJAXLNqZCTBU6FZBdQlZBZCj9qyjzrkV5Ex23Wel4kemaaNZBEGa7lA0QK7fZCsKfNsNe0PXS5ZCi5pNOHONliPuZC9vPVchs3H08N0sVNpfAlUIVXsWRzji3XbMTimEUIOCBwZB2Lf2aOqdLs4c2jm53ywTxIQZBfdjwJrfbqnG0R5fBCWwgZD'
    resp = requests.get(url_fb)
    fb_dtl_resp_json = json.loads(resp.text)
    print(fb_dtl_resp_json)


def feed_fb():
    url_feed = 'https://graph.facebook.com/v10.0/108704644682971/feed?access_token=EAAGB5ZCLVYQQBAFiYpJAXLNqZCTBU6FZBdQlZBZCj9qyjzrkV5Ex23Wel4kemaaNZBEGa7lA0QK7fZCsKfNsNe0PXS5ZCi5pNOHONliPuZC9vPVchs3H08N0sVNpfAlUIVXsWRzji3XbMTimEUIOCBwZB2Lf2aOqdLs4c2jm53ywTxIQZBfdjwJrfbqnG0R5fBCWwgZD'
    resp = requests.get(url_feed)
    fb_dtl_resp_json = json.loads(resp.text)
    print(fb_dtl_resp_json)


def friends_fb():
    url_feed = 'https://graph.facebook.com/v10.0/108704644682971/friends?access_token=EAAGB5ZCLVYQQBAFiYpJAXLNqZCTBU6FZBdQlZBZCj9qyjzrkV5Ex23Wel4kemaaNZBEGa7lA0QK7fZCsKfNsNe0PXS5ZCi5pNOHONliPuZC9vPVchs3H08N0sVNpfAlUIVXsWRzji3XbMTimEUIOCBwZB2Lf2aOqdLs4c2jm53ywTxIQZBfdjwJrfbqnG0R5fBCWwgZD'
    resp = requests.get(url_feed)
    fb_dtl_resp_json = json.loads(resp.text)
    print(fb_dtl_resp_json)


def get_page():
    url_page = 'https://graph.facebook.com/v10.0/me/accounts?limit=50&access_token=EAAGB5ZCLVYQQBAFiYpJAXLNqZCTBU6FZBdQlZBZCj9qyjzrkV5Ex23Wel4kemaaNZBEGa7lA0QK7fZCsKfNsNe0PXS5ZCi5pNOHONliPuZC9vPVchs3H08N0sVNpfAlUIVXsWRzji3XbMTimEUIOCBwZB2Lf2aOqdLs4c2jm53ywTxIQZBfdjwJrfbqnG0R5fBCWwgZD'
    resp = requests.get(url_page)
    fb_dtl_resp_json = json.loads(resp.text)
    print(fb_dtl_resp_json)


def page_feed():
    url_feedpage = 'https://graph.facebook.com/v10.0/107369701486665/feed?access_token=EAAGB5ZCLVYQQBAFiYpJAXLNqZCTBU6FZBdQlZBZCj9qyjzrkV5Ex23Wel4kemaaNZBEGa7lA0QK7fZCsKfNsNe0PXS5ZCi5pNOHONliPuZC9vPVchs3H08N0sVNpfAlUIVXsWRzji3XbMTimEUIOCBwZB2Lf2aOqdLs4c2jm53ywTxIQZBfdjwJrfbqnG0R5fBCWwgZD'
    resp = requests.get(url_feedpage)
    fb_dtl_resp_json = json.loads(resp.text)
    print(fb_dtl_resp_json)


def page_info():
    url_infopage = 'https://graph.facebook.com/v10.0/107369701486665?fields=name,birthday,followers_count,is_verified,hometown,picture&access_token=EAAGB5ZCLVYQQBAFiYpJAXLNqZCTBU6FZBdQlZBZCj9qyjzrkV5Ex23Wel4kemaaNZBEGa7lA0QK7fZCsKfNsNe0PXS5ZCi5pNOHONliPuZC9vPVchs3H08N0sVNpfAlUIVXsWRzji3XbMTimEUIOCBwZB2Lf2aOqdLs4c2jm53ywTxIQZBfdjwJrfbqnG0R5fBCWwgZD'
    resp = requests.get(url_infopage)
    fb_dtl_resp_json = json.loads(resp.text)
    print(fb_dtl_resp_json)


if __name__ == '__main__':
    # main_fb()
    # feed_fb()
    # friends_fb()
    # get_page()
    # page_feed()
    page_info()