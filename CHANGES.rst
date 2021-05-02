CHANGES
========

0.5.1 (2021-05-02)
----------------------------

- Improve performance of shorten_repeat function (Many thanks @yskn67)
- Add tilde option to normalize function

0.4 (2018-12-06)
----------------------------

- Add shorten_repeat function, which shortening contiguous substring. For example: neologdn.normalize("無駄無駄無駄無駄ァ", repeat=1) -> 無駄ァ

0.3.2 (2018-05-17)
----------------------------

- Add option for suppression removal of spaces between Japanese characters

0.2.2 (2018-03-10)
----------------------------

- Fix bug (daku-ten & handaku-ten)
- Support mac osx 10.13 (Many thanks @r9y9)

0.2.1 (2017-01-23)
----------------------------

- Fix bug (Check if a previous character of daku-ten character is in maps) (Many thanks @unnonouno)

0.2 (2016-04-12)
----------------------------

- Add lengthened expression (repeating character) threshold

0.1.2 (2016-03-29)
----------------------------

- Fix installation bug

0.1.1.1 (2016-03-19)
----------------------------

- Support Windows
- Explicitly specify to -std=c++11 in build (Many thanks @id774)

0.1.1 (2015-10-10)
----------------------------

Initial release.
