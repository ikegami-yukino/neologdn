neologdn
===========

|travis| |downloads| |version| |license|

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


Benchmark
----------

.. code:: python

    # Sample code from
    # https://github.com/neologd/mecab-ipadic-neologd/wiki/Regexp.ja#python-written-by-hideaki-t--overlast
    import normalize_neologd

    %timeit normalize(normalize_neologd.normalize_neologd)
    # => 1000 loops, best of 3: 1.18 ms per loop


    import neologdn
    %timeit normalize(neologdn.normalize)
    # => 10000 loops, best of 3: 140 µs per loop


neologdn is about x10 faster than sample code.

details are described as the below notebook:
https://github.com/ikegami-yukino/neologdn/blob/master/benchmark/benchmark.ipynb


License
-------

Apache Software License.


.. |travis| image:: https://travis-ci.org/ikegami-yukino/neologdn.svg?branch=master
    :target: https://travis-ci.org/ikegami-yukino/neologdn
    :alt: travis-ci.org

.. |downloads| image:: https://img.shields.io/pypi/dm/neologdn.svg
    :target: http://pypi.python.org/pypi/neologdn/
    :alt: downloads

.. |version| image:: https://img.shields.io/pypi/v/neologdn.svg
    :target: http://pypi.python.org/pypi/neologdn/
    :alt: latest version

.. |license| image:: https://img.shields.io/pypi/l/neologdn.svg
    :target: http://pypi.python.org/pypi/neologdn/
    :alt: license

