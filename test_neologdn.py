# encoding: utf8
from __future__ import unicode_literals
import unittest
from neologdn import normalize, shorten_repeat


class TestNeologdn(unittest.TestCase):

    def test_normalize(self):
        self.assertEqual(normalize('０'), '0')
        self.assertEqual(normalize('ﾊﾝｶｸ'), 'ハンカク')
        self.assertEqual(normalize('o₋o'), 'o-o')
        self.assertEqual(normalize('majika━'), 'majikaー')
        self.assertEqual(normalize('わ〰い'), 'わい')
        self.assertEqual(normalize('スーパーーーー'), 'スーパー')
        self.assertEqual(normalize('!#'), '!#')
        self.assertEqual(normalize('ゼンカク　スペース'), 'ゼンカクスペース')
        self.assertEqual(normalize('お             お'), 'おお')
        self.assertEqual(normalize('      おお'), 'おお')
        self.assertEqual(normalize('おお      '), 'おお')
        self.assertEqual(normalize('検索 エンジン 自作 入門 を 買い ました!!!'),\
                         '検索エンジン自作入門を買いました!!!')
        self.assertEqual(normalize('アルゴリズム C'), 'アルゴリズムC')
        self.assertEqual(normalize('　　　ＰＲＭＬ　　副　読　本　　　'), 'PRML副読本')
        self.assertEqual(normalize('Coding the Matrix'), 'Coding the Matrix')
        self.assertEqual(normalize('南アルプスの　天然水　Ｓｐａｒｋｉｎｇ　Ｌｅｍｏｎ　レモン一絞り'),\
                         '南アルプスの天然水Sparking Lemonレモン一絞り')
        self.assertEqual(normalize('南アルプスの　天然水-　Ｓｐａｒｋｉｎｇ*　Ｌｅｍｏｎ+　レモン一絞り'),\
                         '南アルプスの天然水- Sparking*Lemon+レモン一絞り')
        self.assertEqual(normalize('ﾊﾟﾊﾟ'), 'パパ')
        self.assertEqual(normalize('a˗֊‐‑‒–⁃⁻₋−'), 'a-')
        self.assertEqual(normalize('あ﹣－ｰ—―─━ー'), 'あー')
        self.assertEqual(normalize('チルダ~∼∾〜〰～'), 'チルダ')
        self.assertEqual(normalize('う゛ほﾟ'), 'ゔぽ')

    def test_shorten_repeat(self):
        self.assertEqual(shorten_repeat('うまああああああああああああい', 7), 'うまあああああああい')
        self.assertEqual(shorten_repeat('かわいいいいいるい', 6), 'かわいいいいいるい')
        self.assertEqual(shorten_repeat('オラオラオラオラーッ', 2), 'オラオラーッ')
        self.assertEqual(shorten_repeat('無駄無駄無駄無駄ァ', 1), '無駄ァ')

    def test_suppress_removal_of_spaces_between_Japanese(self):
        self.assertEqual(normalize('巴 マミ', remove_space=False), '巴 マミ')


if __name__ == '__main__':
    unittest.main()
