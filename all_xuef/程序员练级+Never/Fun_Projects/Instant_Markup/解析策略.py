#满屏的正则是写不好 markdown 渲染的，好好学编译原理吧少年
#大哥，一看你就没学好编译原理啊，markdown 就是正则文法啊。连 CFG 都用不上。
#并没有那么简单，你需要的是编译原理，而不是无脑用正则匹配。

#https://css-tricks.com/choosing-right-markdown-parser/
"""
最基本的一个md引擎,应该需要能够解析: Inline HTML, Automatic paragraphs, headers, blockquotes,
lists, code blocks, horizontal rules, links, emphasis, inline code and images 这几种。
"""

#Overview
##Parsing has two phases:
"""
In the first phase, lines of input are consumed and the block structure of the document—its
division into paragraphs, block quotes, list items, and so on—is constructed.
Text is assigned to these blocks but not parsed. Link reference definitions are parsed and
a map of links is constructed.

In the second phase, the raw text contents of paragraphs and headers are parsed into sequences
of Markdown inline elements (strings, code spans, links, emphasis, and so on), using the map of
link references constructed in phase 1.
"""

#How source lines alter the document tree
##Each line that is processed has an effect on this tree. The line is analyzed and,
##depending on its contents, the document may be altered in one or more of the following ways:
"""
One or more open blocks may be closed.
One or more new blocks may be created as children of the last open block.
Text may be added to the last (deepest) open block remaining on the tree.
"""
##Once a line has been incorporated(加入) into the tree in this way, it can be discarded,(丢弃)
##so input can be read in a stream.


#From block structure to the final document
##Once all of the input has been parsed, all open blocks are closed.
"""
We then “walk the tree,” visiting every node, and parse raw string contents of paragraphs
and headers as inlines. At this point we have seen all the link reference definitions,
so we can resolve reference links as we go.
"""













