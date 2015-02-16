# -*- coding: utf-8 -*-

import sys
from ipa_auto import ipa_auto

if __name__ == "__main__":
    label = ""
    pub = False
#     url = "http://192.168.0.33/publish/ipapub/"
#     url = "http://127.0.0.1:8000/ipapub/"
    url = ''
    if len(sys.argv) > 1:
        if '-publish' in sys.argv:
            pub = True
        if '-url' in sys.argv:
            url = sys.argv[sys.argv.index('-url') + 1]
 
    print("请输入标签（无标签的包可能被删除，无需标签直接按回车）：".decode('utf-8'))
    label = raw_input()

    ipa_auto(label, pub, url)
    print("结束，按回车退出。".decode('utf-8'))
    raw_input()