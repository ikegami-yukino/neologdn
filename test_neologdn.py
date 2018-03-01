# encoding: utf8
from __future__ import unicode_literals
import unittest
from neologdn import normalize


class TestNeologdn(unittest.TestCase):

    def test_normalize(self):
        self.assertEqual(normalize("０"), "0")
        self.assertEqual(normalize("ﾊﾝｶｸ"), "ハンカク")
        self.assertEqual(normalize("o₋o"), "o-o")
        self.assertEqual(normalize("majika━"), "majikaー")
        self.assertEqual(normalize("わ〰い"), "わい")
        self.assertEqual(normalize("スーパーーーー"), "スーパー")
        self.assertEqual(normalize("!#"), "!#")
        self.assertEqual(normalize("ゼンカク　スペース"), "ゼンカクスペース")
        self.assertEqual(normalize("お             お"), "おお")
        self.assertEqual(normalize("      おお"), "おお")
        self.assertEqual(normalize("おお      "), "おお")
        self.assertEqual(normalize("検索 エンジン 自作 入門 を 買い ました!!!"),\
                         "検索エンジン自作入門を買いました!!!")
        self.assertEqual(normalize("アルゴリズム C"), "アルゴリズムC")
        self.assertEqual(normalize("　　　ＰＲＭＬ　　副　読　本　　　"), "PRML副読本")
        self.assertEqual(normalize("Coding the Matrix"), "Coding the Matrix")
        self.assertEqual(normalize("南アルプスの　天然水　Ｓｐａｒｋｉｎｇ　Ｌｅｍｏｎ　レモン一絞り"),\
                         "南アルプスの天然水Sparking Lemonレモン一絞り")
        self.assertEqual(normalize("南アルプスの　天然水-　Ｓｐａｒｋｉｎｇ*　Ｌｅｍｏｎ+　レモン一絞り"),\
                         "南アルプスの天然水- Sparking*Lemon+レモン一絞り")
        self.assertEqual(normalize(u'ﾊﾟﾊﾟ'), u"パパ")
        self.assertEqual(normalize(u'a˗֊‐‑‒–⁃⁻₋−'), "a-")
        self.assertEqual(normalize(u'あ﹣－ｰ—―─━ー'), u"あー")
        self.assertEqual(normalize(u'チルダ~∼∾〜〰～'), u"チルダ")
        self.assertEqual(normalize(u'(ﾟ∀ﾟ )'), u"(゜∀゜)")
        self.assertEqual(normalize('(ﾟ∀ﾟ )'), "(ﾟ∀ﾟ)")
        self.assertEqual(normalize('う゛ほ゜'), "ゔぽ")

    def test_normalize_lengthened(self):
        self.assertEqual(normalize("うまああああああああああああい", repeat=7), "うまあああああああい")
        self.assertEqual(normalize("かわいいいいいるい", repeat=6), "かわいいいいいるい")


if __name__ == '__main__':
    unittest.main()
