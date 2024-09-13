'''
使⽤制表符或换⾏符来添加空⽩
在编程中，空⽩泛指任何⾮打印字符，如空格、制表符和换⾏符。
可以使⽤空⽩来组织输出，让⽤户阅读起来更容易
'''

#* 在字符串中添加制表符，可使⽤字符组合 \t
print("Python")
print("\tPython")

#* 在字符串中添加换⾏符，可使⽤字符组合 \n
print("Languages:\nPython\nC\nJavaScript")


#* 还可以在同⼀个字符串中同时包含制表符和换⾏符。
#* 字符串 "\n\t" 让 Python 换到下⼀⾏，并在下⼀⾏开头添加⼀个制表符。
print("Languages:\n\tPython\n\tC\n\tJavaScript")

print("\n----------分界线----------\n")

'''
删除空白
'''

#* Python 能够找出字符串左端和右端多余的空⽩。
#* 要确保字符串右端没有空⽩，可使⽤ rstrip() ⽅法
#* rstrip()清除字符串末尾的空白
favorite_language_1 = 'python '
print(favorite_language_1)
favorite_language_1 = favorite_language_1.rstrip()
print(favorite_language_1)

#* 还可以删除字符串左端的空⽩或同时删除字符串两端的空⽩，分别使⽤lstrip() ⽅法和 strip() ⽅法即可
#* lstrip()清除字符串开头的空白
#* strip()清除开头和结尾的空白
favorite_language_2 = ' python '
print(favorite_language_2.rstrip())
print(favorite_language_2.lstrip())

#* 对变量 favorite_language_2 调⽤ rstrip() ⽅法后，这个多余的空格被删除了。
#* 然⽽，这种删除只是暂时的，如果再次输出 favorite_language 的值，这个字符串会与输⼊时⼀样，依然包含多余的空⽩
print(favorite_language_2)

#* 要永久删除这个字符串中的空⽩，必须将删除操作的结果关联到变量
favorite_language_2 = favorite_language_2.strip()
print(favorite_language_2)

print("\n----------分界线----------\n")

'''
删除前缀
'''

#* 另⼀个常⻅的字符串处理任务是删除前缀。
#* 假设有⼀个 URL 包含常⻅的前缀 https://，⽽你想删除这个前缀，只关注⽤户需要输⼊地址栏的部分。
nostarch_url = 'https://nostarch.com' 
print(nostarch_url.removeprefix('https://'))

simple_url = nostarch_url.removeprefix('https://')
print(simple_url)