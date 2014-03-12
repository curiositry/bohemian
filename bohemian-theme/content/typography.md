Title: Bohemian’s Typography
Summary: A demonstration of the Bohemian Theme’s eye-catching and altogether hip typography.

Handsome headers typeset in Alegreya SC:
# Header Level One
## Header Level Two
### Header Level Three
#### Header Level Four
##### Header Level Five
###### Header Level Six


### Paragraphs

A paragraph is one or more lines of text followed by one or more blank line. Newlines are treated as spaces. If you need a hard line break, put two or more spaces at the end of a line, or type a backslash at the end of a line.

### Block quotations

Block quotations in markdown use the same convention as in emails. A generic block quote looks like this: 

>This is a block quote — a long and presumably witty quote that happened to agree with whatever point your were trying to make.
> — **Vaguely Famous Person**

### Code blocks

Bohemian supports syntax-highlighting for codeblocks and *pre* elements with Pygments.css:

```python
def helloWorld:
	print("Hello world")
```

You can use 

### Lists

#### Bullet List:

* one
* two
* three  
<br>


#### Numbered Lists:

1. Item 1
2. Item 2
3. Item 3  
<br>



### Inline formatting

Emphasizing some text is done by surrounding it with *s:

This is *emphasized with asterisks*, and this will be a **bold text**. And even more ***krass***.


### Horizontal Rules

Horizontal rules are easily created by putting three or more `***` or `---` on a line:

*****


### Super- and subscripts

Superscripts may be written by surrounding the superscripted text by ^ characters; subscripts may be written by surrounding the subscripted text by ~ characters. Thus, for example,

H~2~O is a liquid.  2^10^ is 1024.


### Links

Using the normal markdown syntax: `[Text](http://example.com/url)`

This is an [inline link](/url), and here's [one with
a title](http://fsf.org "click here for a good time!").

If the link is to a common site (like [Github](http://github.com/omphalosskeptic), or [Stackoverflow](http://stackoverflow.com) ), Bohemian will perpend the site’s icon.


### Images

![Example Image](images/omphalosskeptic.png)

Using the normal markdown image syntax: 
`![Example Image](path/to/image.png)`

