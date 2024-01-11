neologdn
#########

|downloads| |pyversion| |version| |license|

neologdn is a Japanese text normalizer for `mecab-neologd <https://github.com/neologd/mecab-ipadic-neologd>`_.

The normalization is based on the neologd's rules:
https://github.com/neologd/mecab-ipadic-neologd/wiki/Regexp.ja


Contributions are welcome!

NOTE: Installing this module requires C++11 compiler.

Installation
*************

::

 $ pip install neologdn

Usage
******

.. code:: python

    import neologdn
    neologdn.normalize("ﾊﾝｶｸｶﾅ")
    # => 'ハンカクカナ'
    neologdn.normalize("全角記号！？＠＃")
    # => '全角記号!?@#'
    neologdn.normalize("全角記号例外「・」")
    # => '全角記号例外「・」'
    neologdn.normalize("長音短縮ウェーーーーイ")
    # => '長音短縮ウェーイ'
    neologdn.normalize("チルダ削除ウェ~∼∾〜〰～イ")
    # => 'チルダ削除ウェイ'
    neologdn.normalize("いろんなハイフン˗֊‐‑‒–⁃⁻₋−")
    # => 'いろんなハイフン-'
    neologdn.normalize("　　　ＰＲＭＬ　　副　読　本　　　")
    # => 'PRML副読本'
    neologdn.normalize(" Natural Language Processing ")
    # => 'Natural Language Processing'
    neologdn.normalize("かわいいいいいいいいい", repeat=6)
    # => 'かわいいいいいい'
    neologdn.normalize("無駄無駄無駄無駄ァ", repeat=1)
    # => '無駄ァ'
    neologdn.normalize("1995〜2001年", tilde="normalize")
    # => '1995~2001年'
    neologdn.normalize("1995~2001年", tilde="normalize_zenkaku")
    # => '1995〜2001年'
    neologdn.normalize("1995〜2001年", tilde="ignore")  # Don't convert tilde
    # => '1995〜2001年'
    neologdn.normalize("1995〜2001年", tilde="remove")
    # => '19952001年'
    neologdn.normalize("1995〜2001年")  # Default parameter
    # => '19952001年'


Benchmark
**********

.. code:: python

    # Sample code from
    # https://github.com/neologd/mecab-ipadic-neologd/wiki/Regexp.ja#python-written-by-hideaki-t--overlast
    import normalize_neologd

    %timeit normalize(normalize_neologd.normalize_neologd)
    # => 9.55 s ± 29.4 ms per loop (mean ± std. dev. of 7 runs, 1 loop each)


    import neologdn
    %timeit normalize(neologdn.normalize)
    # => 6.66 s ± 35.8 ms per loop (mean ± std. dev. of 7 runs, 1 loop each)


neologdn is about x1.43 faster than sample code.

details are described as the below notebook:
https://github.com/ikegami-yukino/neologdn/blob/master/benchmark/benchmark.ipynb


License
*********

Apache Software License.


Contribution
*************

Contributions are welcome! See: https://github.com/ikegami-yukino/neologdn/blob/master/.github/CONTRIBUTING.md

Cited by
**********
Book
========
山本 和英. テキスト処理の要素技術. 近代科学者. P.41. 2021.

Blog
========
- 【ライブラリ紹介】テキスト正規化ライブラリ neologdn: https://diatonic.codes/blog/neologdn/
- 日本語テキストの前処理：neologdn、大文字小文字、Unicode正規化 - tuttieee’s blog: https://tuttieee.hatenablog.com/entry/ja-nlp-preprocess
- ▲本日の関数==neologdn.normalize()== - TPTブログ: https://ds-blog.tbtech.co.jp/entry/2020/05/11/%E2%96%B2%E6%9C%AC%E6%97%A5%E3%81%AE%E9%96%A2%E6%95%B0%3D%3Dneologdn_normalize%28%29%3D%3D
- NLPについて学ぶ: https://zenn.dev/panyoriokome/scraps/d67f68ab50c0c1
- テキスト正規化用PythonライブラリをMATLABからコール #Python - Qiita: https://qiita.com/aoimidori/items/ab5a4383b5a7bb307bad
- 自然言語処理の前処理手順をPythonコード付きでご紹介 | AI活用・AI導入事例の紹介 | AI活用・AI導入事例の紹介: https://www.matrixflow.net/case-study/75/
- pythonによる日本語前処理備忘録 | DATUM STUDIO株式会社: https://datumstudio.jp/blog/python%E3%81%AB%E3%82%88%E3%82%8B%E6%97%A5%E6%9C%AC%E8%AA%9E%E5%89%8D%E5%87%A6%E7%90%86%E5%82%99%E5%BF%98%E9%8C%B2/
- 前処理、前処理、そして、前処理 （自然言語処理：日本語編）｜narudesu: https://note.com/narudesu/n/na35de30a583a
- ショートカットキーでneologd.normalize: https://scrapbox.io/nishio/%E3%82%B7%E3%83%A7%E3%83%BC%E3%83%88%E3%82%AB%E3%83%83%E3%83%88%E3%82%AD%E3%83%BC%E3%81%A7neologd.normalize
- Pythonで自然言語処理を行うための環境構築 #Python - Qiita: https://qiita.com/lawyer_alpaca/items/86b0deda984170203467
- Python normalize Examples: https://python.hotexamples.com/examples/neologdn/-/normalize/python-normalize-function-examples.html
- 株式会社ししまろ (ch-4) 潜在的ディリクレ配分(LDA)によるchABSAデータセットの分析: https://shishimaro.co.jp/blog/ai/538
- 形態素解析前の日本語文書の前処理 (Python) - け日記: https://ohke.hateblo.jp/entry/2019/02/09/141500
- 人工知能に言語を理解させる！？自然言語処理に重要なデータの前処理をPythonで徹底解説 | AI研究所: https://ai-kenkyujo.com/programming/make-ai-understand-the-language/
- 最新wikipediaを反映したMeCabユーザー辞書を作る - NEologd拡張 | ぷらこめ: https://purakome.net/mecab/addwiki/
- 【自然言語処理入門】文に対してストップワードと正規化から処理を施す | マイナビエンジニアブログ: https://engineerblog.mynavi.jp/technology/nlp_stopword/
- 表記統一 [自然言語処理の餅屋]: https://www.jnlp.org/nlp/%E6%A0%A1%E6%AD%A3/%E8%A1%A8%E8%A8%98%E7%B5%B1%E4%B8%80
- Pytorchを使ってテキスト生成モデルのT5を構築 〜Transformersでの転移学習による手軽な実践〜 - 見習いデータサイエンティストの隠れ家: https://www.dskomei.com/entry/2021/09/28/110016
- 象と散歩: Goolge Colabでお手軽テキストマイニング(日本語前処理): https://walking-elephant.blogspot.com/2023/07/text-mining-normalized.html
- 【Pythonで自然言語処理（NLP）を実装してみよう！】学ぶべき知識についても徹底解説！ - ベトナムオフショア開発の最前線 by Mattock inc.: https://mattock.jp/blog/artificial-intelligence/nlp/lets-implement-nlp-in-python/
- tools [Digital Humanities Japan: Resource Wiki]: https://dhjapan.org/wiki/doku.php?id=tools
- Pythonで現代の季語を調べてみた | Aidemy | 10秒で始めるAIプログラミング学習サービスAidemy［アイデミー］: https://aidemy.net/magazine/703/


.. |downloads| image:: https://static.pepy.tech/personalized-badge/neologdn?period=total&units=international_system&left_color=black&right_color=orange&left_text=Downloads
 :target: https://pepy.tech/project/neologdn

.. |version| image:: https://img.shields.io/pypi/v/neologdn.svg
    :target: http://pypi.python.org/pypi/neologdn/
    :alt: latest version

.. |pyversion| image:: https://img.shields.io/pypi/pyversions/neologdn.svg

.. |license| image:: https://img.shields.io/pypi/l/neologdn.svg
    :target: http://pypi.python.org/pypi/neologdn/
    :alt: license

