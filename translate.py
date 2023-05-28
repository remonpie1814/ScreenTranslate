# -*- coding: utf-8 -*-
"""
Created on Mon Jan 15 20:31:52 2018

@author: Manvenddra
"""

lang={"Bulgarian":"bg",
"Bengali":"bn",
"Catalan":"ca",
"Chinese Simplified":"zh-CN",
"Chinese Traditional":"zh-TW",
"Croatian":"hr",
"Czech":"cs",
"Danish":"da",
"Dutch":"nl",
"English":"en",
"Estonian":"et",
"Filipino":"tl",
"Finnish":"fi",
"French":"fr",
"Galician":"gl",
"German":"de",
"Gujarati":"gu",
"Greek":"el",
"Hebrew":"iw",
"Hindi":"hi",
"Hungarian":"hu",
"Icelandic":"is",
"Indonesian":"id",
"Irish":"ga",
"Italian":"it",
"Japanese":"ja",
"Korean":"ko",
"Kannada":"kn",
"Latvian":"lv",
"Lithuanian":"lt",
"Macedonian":"mk",
"Malay":"ms",
"Maltese":"mt",
"Norwegian":"no",
"Persian":"fa",
"Polish":"pl",
"Portuguese":"pt",
"Romanian":"ro",
"Russian":"ru",
"Serbian":"sr",
"Slovak":"sk",
"Slovenian":"sl",
"Spanish":"es",
"Swahili":"sw",
"Swedish":"sv",
"Tamil":"ta",
"Telugu":"te",
"Thai":"th",
"Turkish":"tr",
"Ukrainian":"uk",
"Vietnamese":"vi",
"Welsh":"cy",
"Yiddish":"yi"}

from googletrans import Translator

def translate(text,lan="Korean"):
    
    translator=Translator()
    
    text=(text.strip()).lower()
    text=text.replace("\n", " ")
    text=text.replace("  ", " ")

    print("번역 전 ",text)

    if text is not None and lan in lang.keys():
        res=translator.translate(text, dest=lang[lan])
        return res.text
    elif text is not None:
        res=translator.translate(text,dest=lan)
        return res.text


if __name__ == '__main__':
    print(translate("Hello World","Korean"))