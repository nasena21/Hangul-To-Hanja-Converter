# Hangul to Hanja Converter #

This is a program that can automatically convert Hangul to Hanja and create output that is suitable for use in an Anki card.

## Example Usage ##

For instance, given the input sentence:

```
저는 학생입니다.
```

The output would be:

```
저는 學[학]生[생]입니다.
```

---


# hanja-tagger #

Automatic Korean Hanja tagging tool powered by Hanjaro (hanjaro.juntong.or.kr)

## Getting Started ##

Install this package by running the standard `setup.py` install command, after cloning this repo.

```
   python setup.py install
```

## Tagging Korean with Hanja ##

First, initialize a `Hanjaro` object, which will manage relevants sessions and cookie.
You should be able to obtain raw tagging results from [Hanjaro](http://hanjaro.juntong.or.kr).

```python
>>> from hanjatagger import Hanjaro
>>> with Hanjaro() as hjr:
...     print(hjr.query("안녕하세요"))
"안녕(安寧)하세요"
```

This package comes with a more programming-friendly wrapper for the query results. Use `HanjaroTagger` to obtain more stream-lined tag results from the query.

```python
>>> from hanjatagger import Hanjaro, HanjaroTagger
>>> with Hanjaro() as hjr:
...    tagger = HanjaroTagger(hjr)
...    print(tagger.tag("안녕하세요"))
"安寧   "
```

The return string is as long as the input query (`len(ret) == len(q)`), and all hanja characters will be replaced by chinese characters, while other non-hanja characters replaced by spaces.

Several options can be configured for HanjaroTagger during initization:

  * `simplified_han`: (*bool*) if true, it converts Traditional Chinese characters (zh-cn) into Simplified Chinese characters (hans-cn).
  * `unified_cjk`: (*bool*) if true, it converts Chinese characters possibly encoded in [CJK compatibility unicodes](https://en.wikipedia.org/wiki/Unicode_compatibility_characters) into CJK Unified Ideographs.

## Acknowledgments

This project is based on the [hanja-tagger](https://github.com/kaniblu/hanja-tagger) by Kang Min Yoo, which is licensed under the MIT License.


## Disclaimer ##

This package comes with a crawler that should only be used for non-commercial and research purposes. Furthermore, it is the responsibility of the user to ensure that using this package incurs no damage to the owner of the website.

