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
        self.assertEqual(shorten_repeat('うまああああああああああああい', 7, 0), 'うまあああああああい')
        self.assertEqual(shorten_repeat('かわいいいいいるい', 6, 0), 'かわいいいいいるい')
        self.assertEqual(shorten_repeat('オラオラオラオラーッ', 2, 0), 'オラオラーッ')
        self.assertEqual(shorten_repeat('無駄無駄無駄無駄ァ', 1, 0), '無駄ァ')
        self.assertEqual(shorten_repeat('隣の客はよく柿食う客だ、隣の客はよく柿食う客だ、隣の客はよく柿食う客だ、言えた！', 1, 0),
                         '隣の客はよく柿食う客だ、言えた！')
        self.assertEqual(shorten_repeat('隣の客はよく柿食う客だ、隣の客はよく柿食う客だ、隣の客はよく柿食う客だ、言えた！', 1, 11),
                         '隣の客はよく柿食う客だ、隣の客はよく柿食う客だ、隣の客はよく柿食う客だ、言えた！')

    def test_suppress_removal_of_spaces_between_Japanese(self):
        self.assertEqual(normalize('巴 マミ', remove_space=False), '巴 マミ')

    def test_handling_tilde(self):
        self.assertEqual(normalize('1467〜1487年', tilde='normalize'), '1467~1487年')
        self.assertEqual(normalize('1467~1487年', tilde='normalize_zenkaku'), '1467〜1487年')
        self.assertEqual(normalize('1467〜1487年', tilde='ignore'), '1467〜1487年')
        self.assertEqual(normalize('1467〜1487年', tilde='remove'), '14671487年')
        self.assertEqual(normalize('1467〜1487年'), '14671487年')

    def test_tilde_boundary_handling(self):
        self.assertEqual(normalize('A ˗あ'), 'A -あ')
        self.assertEqual(normalize('A ーあ'), 'A ーあ')
        self.assertEqual(normalize('A ～あ', tilde='normalize'), 'A ~あ')
        self.assertEqual(normalize('A ~あ', tilde='normalize_zenkaku'), 'A 〜あ')
        self.assertEqual(normalize('A ～あ'), 'Aあ')

if __name__ == '__main__':
    unittest.main()
