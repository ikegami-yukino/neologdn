neologdn
===========

|downloads| |pyversion| |version| |license|

neologdn is a Japanese text normalizer for `mecab-neologd <https://github.com/neologd/mecab-ipadic-neologd>`_.

The normalization is based on the neologd's rules:
https://github.com/neologd/mecab-ipadic-neologd/wiki/Regexp.ja


Contributions are welcome!

NOTE: Installing this module requires C++11 compiler.

Installation
------------

::

 $ pip install neologdn

Usage
-----

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
----------

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
-------

Apache Software License.


Contribution
------------

Contributions are welcome! See: https://github.com/ikegami-yukino/neologdn/blob/master/.github/CONTRIBUTING.md

.. |downloads| image:: https://static.pepy.tech/personalized-badge/neologdn?period=total&units=international_system&left_color=black&right_color=orange&left_text=Downloads
 :target: https://pepy.tech/project/neologdn

.. |version| image:: https://img.shields.io/pypi/v/neologdn.svg
    :target: http://pypi.python.org/pypi/neologdn/
    :alt: latest version

.. |pyversion| image:: https://img.shields.io/pypi/pyversions/neologdn.svg

.. |license| image:: https://img.shields.io/pypi/l/neologdn.svg
    :target: http://pypi.python.org/pypi/neologdn/
    :alt: license

