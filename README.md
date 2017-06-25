# Writing Style Analysis

Novels.py provides a class Novel with many useful methods.(including the SNA in novels)
Analysis.py mainly provide method to calculate the td-idf of words in each novel.


```
import Novels
book = Novels.Novel("war_peace.txt")
book.term_frequency()
book.time_density("Prince Valisi")
book.grades("Prince Valisi","Princess Anna")

import Analysis
tf-idf(["war_peace.txt","flatland.txt","the_old_man_and_the_sea.txt"])
```

![id](http://imglf2.nosdn.127.net/img/UnhEMnlSbXBDeGdWcnNZNm9lNjYzaVFlVXcvRmNMdHc3NHVJb0MwL1diRjZrb3RMMXdBbXlRPT0.png "tf-idf of war and peace")

![id](http://imglf2.nosdn.127.net/img/UnhEMnlSbXBDeGdWcnNZNm9lNjYzajNVKzlVVlRSTDdZMlgvSVNnaDhpdW1jdXpsNmp0Wnd3PT0.png "tf-idf of the old man and the sea")


Blog: http://ooerx.lofter.com/post/1ec94e0f_1041b25a
