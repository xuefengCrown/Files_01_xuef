
#https://spec.commonmark.org/0.18/#appendix-a-a-parsing-strategy

"""
3 Blocks and inlines
We can think of a document as a sequence of blocks—structural elements like paragraphs,
block quotations, lists, headers, rules, and code blocks.

Blocks can contain other blocks, or they can contain inline content: words, spaces,
links, emphasized text, images, and inline code.

3.1 Precedence 优先级

This means that parsing can proceed in two steps:
first, the block structure of the document can be discerned;(识别)
second, text lines inside paragraphs, headers, and other block constructs can be parsed
for inline structure.

The second step requires information about link reference definitions that will be available
only at the end of the first step.
Note that the first step requires processing lines in sequence, but the second can be parallelized,
since the inline parsing of one block element does not affect the inline parsing of any other.

3.2 Container blocks and leaf blocks
We can divide blocks into two types: container blocks, which can contain other blocks,
and leaf blocks, which cannot.


4.2 ATX headers
###h3
parsed as inline content
"""

#4.5 Fenced code blocks
"""
```
code
```
"""

#4.6 HTML blocks
"""
An HTML block begins with an HTML block tag, HTML comment, processing instruction,
declaration, or CDATA section. It ends when a blank line or the end of the input is
encountered.

The contents of the HTML block are interpreted as raw HTML, and will not be escaped in HTML output.

"""

#4.7 Link reference definitions ???


#4.8 Paragraphs
"""
A sequence of non-blank lines that cannot be interpreted as other kinds of blocks forms a paragraph.

The contents of the paragraph are the result of parsing the paragraph’s raw content as inlines.
The paragraph’s raw content is formed by concatenating the lines and removing initial and
final whitespace.


aaa

bbb

<p>aaa</p>
<p>bbb</p>


aaa
bbb

ccc
ddd


<p>aaa
bbb</p>
<p>ccc
ddd</p>

Multiple blank lines between paragraph have no effect:
Leading spaces are skipped:
"""

#4.9 Blank lines
##Blank lines between block-level elements are ignored, except for the role they play
##in determining whether a list is tight or loose.


#5 Container blocks
"""
A container block is a block that has other blocks as its contents.
There are two basic kinds of container blocks: block quotes and list items.
Lists are meta-containers for list items.

"""
#5.1 block quotes
"""
> # Foo
> bar
"""

#5.2 List items


#6 Inlines
##Inlines are parsed sequentially from the beginning of the character stream to the
##end (left to right, in left-to-right languages).


#6.4 Emphasis and strong emphasis


#6.5 Links
"""
A link contains link text (the visible text), a link destination (the URI that is the
link destination), and optionally a link title.

There are two basic kinds of links in Markdown. In inline links the destination and title
are given immediately after the link text.
In reference links the destination and title are defined elsewhere in the document.

"""
#Here is a simple inline link:
"""
[link](/uri "title"markdown语法要点.py<p><a href="/uri" title="title">link</a></p>
"""

"""
[foo<http://example.com/?search=][ref]>

[ref]: /uri

<p>[foo<a href="http://example.com/?search=%5D%5Bref%5D">http://example.com/?search=][ref]</a></p>

"""

#6.6 Images
"""
Syntax for images is like the syntax for links, with one difference.
Instead of link text, we have an image description. The rules for this are the same as
for link text, except that (a) an image description starts with ![ rather than [, and
(b) an image description may contain links. An image description has inline elements as
its contents. When an image is rendered to HTML, this is standardly used as the image's
alt attribute.


![foo](/url "title")

<p><img src="/url" alt="foo" title="title" /></p>
"""

#6.7 Autolinks
##Autolinks are absolute URIs and email addresses inside < and >.
##They are parsed as links, with the URL or email address as the link label.
"""
<http://foo.bar.baz>
<p><a href="http://foo.bar.baz">http://foo.bar.baz</a></p>
"""


#6.8 Raw HTML
"""
Text between < and > that looks like an HTML tag is parsed as a raw HTML tag and
will be rendered in HTML without escaping.

"""

#6.9 Hard line breaks


#6.10 Soft line breaks


#6.11 Textual content
##Any characters not given an interpretation by the above rules will be parsed as
##plain textual content.
















