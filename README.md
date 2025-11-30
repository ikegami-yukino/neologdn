# neologdn

[![PyPI Downloads](https://static.pepy.tech/badge/neologdn)](https://pepy.tech/projects/neologdn)![PyPI - Version](https://img.shields.io/pypi/v/neologdn)![PyPI - Python Version](https://img.shields.io/pypi/pyversions/neologdn)![PyPI - License](https://img.shields.io/pypi/l/neologdn)

neologdn is a Japanese text normalizer for [mecab-neologd](https://github.com/neologd/mecab-ipadic-neologd).

The normalization is based on the neologd's rules:
https://github.com/neologd/mecab-ipadic-neologd/wiki/Regexp.ja

And also some optional features are added.

Contributions are welcome!

NOTE: Installing this module requires C++11 compiler.

## Installation

```sh
pip install neologdn
```

If setuptools is not installed, you must install it:

```sh
pip install setuptools
```

If you encountered the following error:

```sh
ERROR: Could not find a version that satisfies the requirement setuptools (from versions: none)
```

Then execute the following commands to may solve this error:

```sh
pip install wheel
pip install --no-build-isolation neologdn
```

## Usage

```python
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
```


## Benchmark

```python

# Sample code from
# https://github.com/neologd/mecab-ipadic-neologd/wiki/Regexp.ja#python-written-by-hideaki-t--overlast
import normalize_neologd

%timeit normalize(normalize_neologd.normalize_neologd)
# => 9.55 s ± 29.4 ms per loop (mean ± std. dev. of 7 runs, 1 loop each)

import neologdn
%timeit normalize(neologdn.normalize)
# => 6.66 s ± 35.8 ms per loop (mean ± std. dev. of 7 runs, 1 loop each)
```

neologdn is about x1.43 faster than sample code.

details are described as the below notebook:
https://github.com/ikegami-yukino/neologdn/blob/master/benchmark/benchmark.ipynb

## License

Apache Software License.

## CHANGES

### 0.5.5 (2025-12-01)

- Support Python 3.14 and 3.14t (free-treaded)
- Normalize the left double quotation ” (U+201C) to double quotation " (U+0022)

### 0.5.4 (2025-03-15)

- Support Python 3.13
- Fix tilde loss after latin and whitespace (Many thanks @a-lucky)

### 0.5.3 (2024-05-03)

- Support Python 3.12

### 0.5.2 (2023-08-03)

- Support Python 3.10 and 3.11 (Many thanks @polm)

### 0.5.1 (2021-05-02)

- Improve performance of shorten_repeat function (Many thanks @yskn67)
- Add tilde option to normalize function

### 0.4 (2018-12-06)

- Add shorten_repeat function, which shortening contiguous substring. For example: neologdn.normalize("無駄無駄無駄無駄ァ", repeat=1) -> 無駄ァ

### 0.3.2 (2018-05-17)

- Add option for suppression removal of spaces between Japanese characters

### 0.2.2 (2018-03-10)

- Fix bug (daku-ten & handaku-ten)
- Support mac osx 10.13 (Many thanks @r9y9)

### 0.2.1 (2017-01-23)

- Fix bug (Check if a previous character of daku-ten character is in maps) (Many thanks @unnonouno)

### 0.2 (2016-04-12)

- Add lengthened expression (repeating character) threshold

### 0.1.2 (2016-03-29)

- Fix installation bug

### 0.1.1.1 (2016-03-19)

- Support Windows
- Explicitly specify to -std=c++11 in build (Many thanks @id774)

### 0.1.1 (2015-10-10)

Initial release.

## Contribution

Contributions are welcome! See: https://github.com/ikegami-yukino/neologdn/blob/master/.github/CONTRIBUTING.md

## Cited by

### Book

- 山本 和英. テキスト処理の要素技術. 近代科学者. P.41. 2021.

### Blog

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
