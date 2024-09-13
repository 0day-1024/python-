'''
练习 2.3：个性化消息
⽤变量表⽰⼀个⼈的名字，并向其显⽰⼀条消息。显⽰的消息应⾮常简单，如下所⽰。
Hello Eric, would you like to learn some Python today?
'''
name = "Eric"
message = f'Hello {name}, would you like to learn some Python today?'
print(message)

print("\n----------分界线----------\n")

'''
练习 2.4：调整名字的⼤⼩写
⽤变量表⽰⼀个⼈的名字，再分别以全⼩写、全⼤写和⾸字⺟⼤写的⽅式显⽰这个⼈名。
'''
english_name = "joHn doE"
#* 全小写
print(english_name.lower())
#* 全大写
print(english_name.upper())
#* 首字母大写
print(english_name.title())

print("\n----------分界线----------\n")

'''
练习 2.5：名⾔ 1 
找到你钦佩的名⼈说的⼀句名⾔，将这个名⼈的姓名和名⾔打印出来。输出应类似于下⾯这样（包括引号）。
Albert Einstein once said, “A person who never made a mistake never tried anything new.”
'''
print("Albert Einstein once said, \"Imagination is more important than knowledge.\"")

print("\n----------分界线----------\n")

'''
练习 2.6：名⾔ 2
重复练习 2.5，但⽤变量 famous_person 表⽰名⼈的姓名，再创建要显⽰的消息并将其赋给变量 message，
然后打印这条消息。
'''
famous_person = "Albert Einstein"
quote = "Imagination is more important than knowledge."
message = f'{famous_person} once said, "{quote}"'
print(message)

print("\n----------分界线----------\n")

'''
练习 2.7：删除⼈名中的空⽩
⽤变量表⽰⼀个⼈的名字，并在其开头和末尾都包含⼀些空⽩字符。
务必⾄少使⽤字符组合 "\t" 和 "\n" 各⼀次。
打印这个⼈名，显⽰其开头和末尾的空⽩。
然后，分别使⽤函数lstrip()、rstrip() 和 strip() 对⼈名进⾏处理，并将结果打印出来。
'''
person_name = "\t\tJohn Doe\t\n"
print("Unmodified:")
print(person_name)
print("\nUsing lstrip():")
print(person_name.lstrip())
print("\nUsing rstrip():")
print(person_name.rstrip())
print("\nUsing strip():")
print(person_name.strip())

print("\n----------分界线----------\n")

'''
练习 2.8：⽂件扩展名 
Python 提供了 removesuffix() ⽅法，其⼯作原理与 removeprefix() 很像。
请将值 'python_notes.txt'赋给变量 filename，再使⽤ removesuffix() ⽅法来显⽰不包含
扩展名的⽂件名，就像⽂件浏览器所做的那样。
'''
filename = "python_notes.txt"
simple_filename = filename.removesuffix(".txt")
print(simple_filename)