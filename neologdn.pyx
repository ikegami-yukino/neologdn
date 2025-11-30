# distutils: language=c++
# cython: language_level=3
# -*- coding: utf-8 -*-

import itertools
from libc.stdlib cimport malloc, free
from libcpp.unordered_map cimport unordered_map
from libcpp.unordered_set cimport unordered_set

VERSION = (0, 5, 5)
__version__ = '0.5.5'

cdef extern from "Python.h":
    object PyUnicode_DecodeUTF32(const char *s, Py_ssize_t size, const char *errors, int *byteorder)


cdef py_ucs4_to_unicode(Py_UCS4 *ucs4_ptr, Py_ssize_t length):
    return PyUnicode_DecodeUTF32(<char*>ucs4_ptr, sizeof(Py_UCS4)*length, NULL, NULL)


ASCII = (
    ('ａ', 'a'), ('ｂ', 'b'), ('ｃ', 'c'), ('ｄ', 'd'), ('ｅ', 'e'),
    ('ｆ', 'f'), ('ｇ', 'g'), ('ｈ', 'h'), ('ｉ', 'i'), ('ｊ', 'j'),
    ('ｋ', 'k'), ('ｌ', 'l'), ('ｍ', 'm'), ('ｎ', 'n'), ('ｏ', 'o'),
    ('ｐ', 'p'), ('ｑ', 'q'), ('ｒ', 'r'), ('ｓ', 's'), ('ｔ', 't'),
    ('ｕ', 'u'), ('ｖ', 'v'), ('ｗ', 'w'), ('ｘ', 'x'), ('ｙ', 'y'),
    ('ｚ', 'z'),
    ('Ａ', 'A'), ('Ｂ', 'B'), ('Ｃ', 'C'), ('Ｄ', 'D'), ('Ｅ', 'E'),
    ('Ｆ', 'F'), ('Ｇ', 'G'), ('Ｈ', 'H'), ('Ｉ', 'I'), ('Ｊ', 'J'),
    ('Ｋ', 'K'), ('Ｌ', 'L'), ('Ｍ', 'M'), ('Ｎ', 'N'), ('Ｏ', 'O'),
    ('Ｐ', 'P'), ('Ｑ', 'Q'), ('Ｒ', 'R'), ('Ｓ', 'S'), ('Ｔ', 'T'),
    ('Ｕ', 'U'), ('Ｖ', 'V'), ('Ｗ', 'W'), ('Ｘ', 'X'), ('Ｙ', 'Y'),
    ('Ｚ', 'Z'),
    ('！', '!'), ('”', '"'), ('＃', '#'), ('＄', '$'), ('％', '%'),
    ('＆', '&'), ('’', '\''), ('（', '('), ('）', ')'), ('＊', '*'),
    ('＋', '+'), ('，', ','), ('−', '-'), ('．', '.'), ('／', '/'),
    ('：', ':'), ('；', ';'), ('＜', '<'), ('＝', '='), ('＞', '>'),
    ('？', '?'), ('＠', '@'), ('［', '['), ('¥', '\\'), ('］', ']'),
    ('＾', '^'), ('＿', '_'), ('‘', '`'), ('｛', '{'), ('｜', '|'),
    ('｝', '}')
)
KANA = (
    ('ｱ', 'ア'), ('ｲ', 'イ'), ('ｳ', 'ウ'), ('ｴ', 'エ'), ('ｵ', 'オ'),
    ('ｶ', 'カ'), ('ｷ', 'キ'), ('ｸ', 'ク'), ('ｹ', 'ケ'), ('ｺ', 'コ'),
    ('ｻ', 'サ'), ('ｼ', 'シ'), ('ｽ', 'ス'), ('ｾ', 'セ'), ('ｿ', 'ソ'),
    ('ﾀ', 'タ'), ('ﾁ', 'チ'), ('ﾂ', 'ツ'), ('ﾃ', 'テ'), ('ﾄ', 'ト'),
    ('ﾅ', 'ナ'), ('ﾆ', 'ニ'), ('ﾇ', 'ヌ'), ('ﾈ', 'ネ'), ('ﾉ', 'ノ'),
    ('ﾊ', 'ハ'), ('ﾋ', 'ヒ'), ('ﾌ', 'フ'), ('ﾍ', 'ヘ'), ('ﾎ', 'ホ'),
    ('ﾏ', 'マ'), ('ﾐ', 'ミ'), ('ﾑ', 'ム'), ('ﾒ', 'メ'), ('ﾓ', 'モ'),
    ('ﾔ', 'ヤ'), ('ﾕ', 'ユ'), ('ﾖ', 'ヨ'),
    ('ﾗ', 'ラ'), ('ﾘ', 'リ'), ('ﾙ', 'ル'), ('ﾚ', 'レ'), ('ﾛ', 'ロ'),
    ('ﾜ', 'ワ'), ('ｦ', 'ヲ'), ('ﾝ', 'ン'),
    ('ｧ', 'ァ'), ('ｨ', 'ィ'), ('ｩ', 'ゥ'), ('ｪ', 'ェ'), ('ｫ', 'ォ'),
    ('ｯ', 'ッ'), ('ｬ', 'ャ'), ('ｭ', 'ュ'), ('ｮ', 'ョ'),
    ('｡', '。'), ('､', '、'), ('･', '・'), ('゛', 'ﾞ'), ('゜', 'ﾟ'),
    ('｢', '「'), ('｣', '」'), ('ｰ', 'ー')
)
DIGIT = (
    ('０', '0'), ('１', '1'), ('２', '2'), ('３', '3'), ('４', '4'),
    ('５', '5'), ('６', '6'), ('７', '7'), ('８', '8'), ('９', '9')
)
KANA_TEN = (
    ('カ', 'ガ'), ('キ', 'ギ'), ('ク', 'グ'), ('ケ', 'ゲ'), ('コ', 'ゴ'),
    ('サ', 'ザ'), ('シ', 'ジ'), ('ス', 'ズ'), ('セ', 'ゼ'), ('ソ', 'ゾ'),
    ('タ', 'ダ'), ('チ', 'ヂ'), ('ツ', 'ヅ'), ('テ', 'デ'), ('ト', 'ド'),
    ('ハ', 'バ'), ('ヒ', 'ビ'), ('フ', 'ブ'), ('ヘ', 'ベ'), ('ホ', 'ボ'),
    ('ウ', 'ヴ'), ('う', 'ゔ')
)
KANA_MARU = (
    ('ハ', 'パ'), ('ヒ', 'ピ'), ('フ', 'プ'), ('ヘ', 'ペ'), ('ホ', 'ポ'),
    ('は', 'ぱ'), ('ひ', 'ぴ'), ('ふ', 'ぷ'), ('へ', 'ぺ'), ('ほ', 'ぽ')
)
SYMBOLS = (('“', '"'),)

HIPHENS = ('˗', '֊', '‐', '‑', '‒', '–', '⁃', '⁻', '₋', '−')
CHOONPUS = ('﹣', '－', 'ｰ', '—', '―', '─', '━', 'ー')
TILDES = ('~', '∼', '∾', '〜', '〰', '～')

SPACE = (' ', '　')

cdef unordered_map[Py_UCS4, Py_UCS4] conversion_map, kana_ten_map, kana_maru_map
cdef unordered_set[Py_UCS4] blocks, basic_latin

for (before, after) in (ASCII + DIGIT + KANA + SYMBOLS):
    conversion_map[before] = after

for (before, after) in KANA_TEN:
    kana_ten_map[before] = after

for (before, after) in KANA_MARU:
    kana_maru_map[before] = after

char_codes = itertools.chain(
    range(19968, 40960),  # CJK UNIFIED IDEOGRAPHS
    range(12352, 12448),  # HIRAGANA
    range(12448, 12544),  # KATAKANA
    range(12289, 12352),  # CJK SYMBOLS AND PUNCTUATION
    range(65280, 65520)   # HALFWIDTH AND FULLWIDTH FORMS
)
for c in map(chr, char_codes):
    blocks.insert(c)


for c in map(chr, range(128)):
    basic_latin.insert(c)

del ASCII, KANA, DIGIT, KANA_TEN, KANA_MARU, char_codes


cpdef unicode shorten_repeat(unicode text, int repeat_threshould, int max_repeat_substr_length=8):
    cdef int text_length, i, repeat_length, right_start, right_end, num_repeat_substrs
    cdef int upper_repeat_substr_length
    cdef unicode substr, right_substr

    i = 0
    while i < len(text):
        text_length = len(text)

        upper_repeat_substr_length = (text_length - i) // 2
        if max_repeat_substr_length and max_repeat_substr_length < upper_repeat_substr_length:
            upper_repeat_substr_length = max_repeat_substr_length + 1

        for repeat_length in range(1, upper_repeat_substr_length):
            substr = text[i:i+repeat_length]
            right_start = i + repeat_length
            right_end = right_start + repeat_length
            right_substr = text[right_start:right_end]
            num_repeat_substrs = 1
            while substr == right_substr and right_end <= text_length:
                num_repeat_substrs += 1
                right_start += repeat_length
                right_end += repeat_length
                right_substr = text[right_start:right_end]
            if num_repeat_substrs > repeat_threshould:
                text = text[:i+repeat_length*repeat_threshould] + text[i+repeat_length*num_repeat_substrs:]
        i += 1
    return text


cpdef unicode normalize(unicode text, int repeat=0, bint remove_space=True,
                        int max_repeat_substr_length=8, unicode tilde='remove'):
    cdef Py_UCS4 *buf = <Py_UCS4 *>malloc(sizeof(Py_UCS4) * (len(text) + 1))

    cdef Py_UCS4 c, prev = '\0'
    cdef int pos = 0
    cdef bint lattin_space = False

    for c in text:
        if c in SPACE:
            c = ' '
            if (prev == ' ' or blocks.count(prev)) and remove_space:
                continue
            elif prev != '*' and pos > 0 and basic_latin.count(prev):
                lattin_space = True
                buf[pos] = c
            elif remove_space:
                pos -= 1
            else:
                buf[pos] = c
        else:
            if c in HIPHENS:
                if prev == '-':
                    continue
                else:
                    buf[pos] = c = '-'
                lattin_space = False
            elif c in CHOONPUS:
                if prev == 'ー':
                    continue
                else:
                    buf[pos] = c = 'ー'
                lattin_space = False
            elif c in TILDES:
                if tilde == 'ignore':
                    buf[pos] = c
                elif tilde == 'normalize':
                    buf[pos] = c = '~'
                elif tilde == 'normalize_zenkaku':
                    buf[pos] = c = '〜'
                else:
                    continue
                lattin_space = False
            else:
                if conversion_map.count(c):
                    c = conversion_map[c]
                if c == 'ﾞ' and kana_ten_map.count(prev):
                    pos -= 1
                    c = kana_ten_map[prev]
                elif c == 'ﾟ' and kana_maru_map.count(prev):
                    pos -= 1
                    c = kana_maru_map[prev]
                if lattin_space and blocks.count(c) and remove_space:
                    pos -= 1
                lattin_space = False
                buf[pos] = c
        prev = c
        pos += 1

    if buf[pos-1] == ' ':
        pos -= 1
    buf[pos] = '\0'

    cdef unicode ret = py_ucs4_to_unicode(buf, pos)
    free(buf)

    if repeat:
        return shorten_repeat(ret, repeat, max_repeat_substr_length)
    return ret
