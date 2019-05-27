 [1]: import re

In [2]: re.match(r"\bve\b", " ve ")

In [3]: re.match(r"\bve\b", "vessssve")

In [4]: re.match(r"\bve\b", "ve")
Out[4]: <_sre.SRE_Match object; span=(0, 2), match='ve'>

In [5]: re.match(r"\Bve\B", " ve ")

In [6]: re.match(r"\Bve\B", "a ve c")

In [7]: re.match(r".\Bve\B.", "a ve c")

In [8]: re.match(r"^\Bve\B", "a ve c")

In [9]: re.match(r"^\Bve\B", " ve ")

In [10]: re.match(r"^^123^$", "123")

In [11]: re.match(r"^^123^$", " 123 ")

In [12]: re.match(r"^123$", " 123 ")

In [13]: re.match(r"^[^123$]", " 123 ")
Out[13]: <_sre.SRE_Match object; span=(0, 1), match=' '>

In [14]: re.match(r"^^123^$", "^123^")

In [15]: re.match(r"^\^123\^$", "^123^")
Out[15]: <_sre.SRE_Match object; span=(0, 5), match='^123^'>

In [16]: re.match(r"^\Bve\B", "1 ve 1")

In [17]: re.match(r"^\Bve\B", "1ve1")

In [18]: re.match(r"\Bve\B", "1ve1")

In [19]: re.match(r"\Bve\B", " ve ")

In [20]: re.match(r"\Bve\B", "#ve#")

In [21]: re.match(r"\Bve\B", "\nve\n")

In [22]: re.match(r"\Bve\B", "ve ")

In [23]: re.match(r"\Bve\B", "ve")

In [24]: re.match(r"\Bve\B", "avea")

In [25]: re.match(r"^\Bve\B$", " ve ")

In [26]: re.match(r"^\Bve\B$", " ve")

In [27]: re.match(r"^\Bve\B$", "xx")

In [28]: re.match(r"^\Bve\B$", "00")

In [29]: re.match(r"^.*\Bve\B$", "aave")

In [30]: re.match(r"^.*\Bve\B", "aave ")

In [31]: re.match(r"^.*\Bve.*\B", "aave ")
Out[31]: <_sre.SRE_Match object; span=(0, 5), match='aave '>

In [32]: re.match(r"^\B00\B$", "00")

In [33]: re.match(r"^\B11\B$", "11")

In [34]: re.match(r"^\B11\B$", "1111")

In [35]: re.match(r"\B11\B", "1111")

In [36]: re.match(r"\B  \B", "  ")
Out[36]: <_sre.SRE_Match object; span=(0, 2), match='  '>

In [37]: re.match(r"\Bcd\B", "还好")

In [38]: re.match(r"\B还好\B", "还好")

In [39]: re.match(r"\B@@\B", "@@")
Out[39]: <_sre.SRE_Match object; span=(0, 2), match='@@'>

In [40]: re.match(r"\B--\B", "--")
Out[40]: <_sre.SRE_Match object; span=(0, 2), match='--'>

In [41]: re.match(r"\B__\B", "__")




\b识别空格,  空格表示单词边界利用空格和空字符划分,   ho ve r     单词边界用-表示  : -ho-空格-ve-空格-r-
\B
n [62]: re.match(r"\s\Bve\s\B", " ve ")

In [63]: re.match(r"\s\bve\b\s", " ve ")
Out[63]: <_sre.SRE_Match object; span=(0, 4), match=' ve '>

In [64]: re.match(r"\B\sve\s\B", " ve ")
Out[64]: <_sre.SRE_Match object; span=(0, 4), match=' ve '>

In [65]: re.match(r"\B\sve\B\s", " ve ")
