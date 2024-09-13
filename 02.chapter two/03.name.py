'''
字符串
'''

#* 使⽤⽅法修改字符串的⼤⼩写
name = "ada lovelace"
print(name.title())

'''
title() ⽅法以⾸字⺟⼤写的⽅式显⽰每个单词，即将每个单词的⾸字⺟都改为⼤写。
这很有⽤，因为你经常需要将名字视为信息。
例如，你可能希望程序将值 Ada、ADA 和 ada 视为同⼀个名字，并将它们都显⽰为Ada。
'''

#* 将字符串改为全⼤写或全⼩写的
print(name.upper())
print(name.lower())