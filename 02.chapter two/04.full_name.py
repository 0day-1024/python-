'''
在字符串中使⽤变量
'''

first_name = "ada"
last_name = "lovelace"
full_name = f"{first_name} {last_name}"

print(full_name)

'''
要在字符串中插⼊变量的值，可先在左引号前加上字⺟f，再将要插⼊的变量放在花括号内。
这样，Python 在显⽰字符串时，将把每个变量都替换为其值。
这种字符串称为 f 字符串。f 是 format（设置格式）的简写，
因为 Python 通过把花括号内的变量替换为其值来设置字符串的格式。
'''

#* 使⽤ f 字符串可以完成很多任务，如利⽤与变量关联的信息来创建完整的消息
print(f"Hello, {full_name.title()}!")

#* 还可以使⽤ f 字符串来创建消息，再把整条消息赋给变量
message = f"Hello, {full_name.title()}!"
print(message)