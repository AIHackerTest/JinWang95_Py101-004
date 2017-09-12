# 文件编码
## 基本处理
字符必须被编码后才能被计算机处理，比如你输入“A”，计算机怎么知道你输入的是A呢，就需要把A转换为计算机能够识别的二进制数。早期的编码规则是ASCII码，用于处理26个字母的大小写，以及各种符号。

## 不同的编码规则
### GBK
ASCII并不足以处理几万个汉字，于是有了汉字的编码规则GB，历代版本如下：
- **GB2312**：(1980年)收录了7445个字符，包括6763个汉字和682个其它符号。
- **GBK1.0**：(1995年)收录了21886个符号，它分为汉字区和图形符号区。汉字区包括21003个字符。
- **GB18030**：(2000年)收录了27484个汉字，同时还收录了藏文、蒙文、维吾尔文等主要的少数民族文字。是取代了GBK1.0的正式国家标准。

从ASCII、 GB2312、GBK到GB18030，这些编码方法是向下兼容的，即同一个字符在这些方案中总是有相同的编码，后面的标准支持更多的字符。在这些编码中，英文和中文可以统一地处理。区分中文编码的方法是高字节的最高位不为0。

GB2312、GBK到GB18030都属于双字节字符集 (DBCS)，存储格式始终是big endian，即高位在前。

有的中文Windows的缺省内码还是GBK，可以通过GB18030升级包升级到GB18030。不过GB18030相对GBK增加的字符，普通人是很难用到的，通常我们还是用GBK指代中文Windows内码。


### Unicode
只有编码与解码的规则一致，才能保证得到正确的信息。

国际上也有一套编码规则——Unicode，希望能够成为世界标准编码，当然也包括了汉字编码，Unicode学名是Universal Multiple-Octet Coded Character Set，简称UCS。

Unicode也兼容ASCII，但是与GBK编码规则是不兼容的，比如“汉”字的Unicode编码是6C49，而GBK编码是BABA。

> UCS也分为两种格式：UCS-2、UCS-4。顾名思义，UCS-2就是用两个字节编码，有2^16=65536个码位；UCS-4就是用四个字节编码（最高位必须为0，实际上只用了31位），故有2^31=2147483648个码位。第一个字节称为group，总共有2^7=128个group，第二个字节称为plane,每个group有256个plane，第三个字节称为rows，第四个字节称为cells。UCS-4中group为0，plane为0的码位被称作Basic Multilingual Plane, 即BMP。BMP去掉前两个为0的字节就得到了UCS-2。目前还没有任何字符被分配在BMP之外。

## 编码的传输
UCS只是规定了怎么用多个字节表示各种字符，而这种编码的传输方式（例如是以8位为一个单元进行传输，还是以16位为一个单元传输），则是由UTF（UCS Transformation Format）规定。常见的UTF规范有UTF-8、UTF-7、UTF-16。

### UTF-8
UTF-8就是以8位（即1个字节）为单元对UCS进行编码。从UCS-2到UTF-8的编码方式如下：

UCS-2编码(16进制) |	UTF-8 字节流(二进制)
----------|------------
0000 - 007F |	0xxxxxxx
0080 - 07FF |	110xxxxx 10xxxxxx
0800 - FFFF |	1110xxxx 10xxxxxx 10xxxxxx

0开头表示就是一个单元就是一个字符，110开头表示两个单元是一个字符，1110开头表示三个单元是一个字符。

例如“汉”字的Unicode编码是6C49。6C49在0800-FFFF之间，所以肯定要用3字节模板了：1110xxxx 10xxxxxx 10xxxxxx。将6C49写成二进制是：0110 110001 001001， 用这个比特流依次代替模板中的x，得到：11100110 10110001 10001001，即E6 B1 89。

### UTF-16
UTF-16是以16位（即2个字节）为一个单元，与UCS-2编码其实一致，只是UCS-2只是编码方案，而UTF-16用于实际传输，需要考虑字节序（endian）问题。

字节序分为两种：
- big endian(大尾)
- little endian(小尾)

例如“汉”字的Unicode编码是6C49。那么写到文件里时，是先写6C还是先写49？如果将6C写在前面，就是big endian；如果将49写在前面，就是little endian。

> “endian”这个词出自《格列佛游记》。小人国的内战就源于吃鸡蛋时是究竟从大头(Big-Endian)敲开还是从小头(Little-Endian)敲开。计算机界其实也为大小尾的事情吵过。

于是就需要一个标记来表示用的是big endian还是little endian。Unicode规范中推荐的方法是BOM(Byte Order Mark)，其作用原理如下：

在传输字节流前，先传输一个叫做"ZERO WIDTH NO-BREAK SPACE"的字符，它的UCS编码是FEFF，实际上是不存在的字符。
- 如果收到FEFF，就表明这个字节流是Big-Endian
- 如果收到FFFE，就表明这个字节流是Little-Endian

### UTF-8与BOM
UTF-8不需要BOM来表明字节顺序，但可以用BOM来表明编码方式。字符"ZERO WIDTH NO-BREAK SPACE"的UTF-8编码是EF BB BF（读者可以用我们前面介绍的编码方法验证一下）。所以如果接收者收到以EF BB BF开头的字节流，就知道这是UTF-8编码了。

Windows就是使用BOM来标记txt的编码方式的。如果使用UTF-8解码，第一行可能会有/ufeff字样，因为编码时使用了BOM，当使用UTF-8-SIG解码就会移除这个字样，表示我知道你在编码时使用了BOM。

## 代码示范
Examples:

	#!python2
	#coding: utf8
	u = u'ABC'
	e8 = u.encode('utf-8')        # encode without BOM
	e8s = u.encode('utf-8-sig')   # encode with BOM
	e16 = u.encode('utf-16')      # encode with BOM
	e16le = u.encode('utf-16le')  # encode without BOM
	e16be = u.encode('utf-16be')  # encode without BOM
	print 'utf-8     %r' % e8
	print 'utf-8-sig %r' % e8s
	print 'utf-16    %r' % e16
	print 'utf-16le  %r' % e16le
	print 'utf-16be  %r' % e16be
	print
	print 'utf-8  w/ BOM decoded with utf-8     %r' % 	e8s.decode('utf-8')
	print 'utf-8  w/ BOM decoded with utf-8-sig %r' % e8s.decode('utf-8-sig')
	print 'utf-16 w/ BOM decoded with utf-16    %r' % e16.decode('utf-16')
	print 'utf-16 w/ BOM decoded with utf-16le  %r' % e16.decode('utf-16le')

Output:

	utf-8     'ABC'
	utf-8-sig '\xef\xbb\xbfABC'
	utf-16    '\xff\xfeA\x00B\x00C\x00'    # Adds BOM and encodes using native processor endian-ness.
	utf-16le  'A\x00B\x00C\x00'
	utf-16be  '\x00A\x00B\x00C'

	utf-8  w/ BOM decoded with utf-8     u'\ufeffABC'    # doesn't remove BOM if present.
	utf-8  w/ BOM decoded with utf-8-sig u'ABC'          # removes BOM if present.
	utf-16 w/ BOM decoded with utf-16    u'ABC'          # *requires* BOM to be present.
	utf-16 w/ BOM decoded with utf-16le  u'\ufeffABC'    # doesn't remove BOM if present.

# 参考文献
http://www.cnblogs.com/imissherso/articles/640727.html

https://stackoverflow.com/questions/17912307/u-ufeff-in-python-string
