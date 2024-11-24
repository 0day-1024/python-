'''
Author: 0day-1024 2048591453@qq.com
Date: 2024-09-11 21:02:18
LastEditors: 0day-1024 2048591453@qq.com
LastEditTime: 2024-10-12 09:28:37
FilePath: \python_work\05.chapter five\09.Exercise.py
Description: 这是默认设置,请设置`customMade`, 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
'''
'''
练习 5.8：以特殊⽅式跟管理员打招呼 
创建⼀个⾄少包含 5 个⽤户名的列表，并且其中⼀个⽤户名为 'admin'。
想象你要编写代码，在每个⽤户登录⽹站后都打印⼀条问候消息。
遍历⽤户名列表，向每个⽤户打印⼀条问候消息。
如果⽤户名为 'admin'，就打印⼀条特殊的问候消息，如下所⽰。
Hello admin, would you like to see a status report?
否则，打印⼀条普通的问候消息，如下所⽰。
Hello Jaden, thank you for logging in again.
'''
usernames = ['admin', '马文博', '任毅', '马洁', '秦琪']
for username in usernames:
    if username == "admin":
        print("Hello admin, would you like to see a status report?")
    else:
        print(f"Hello {username}, thank you for logging in again.")

print("\n----------分界线----------\n")

'''
练习 5.9：处理没有⽤户的情形 
在为练习 5.8 编写的程序中，添加⼀条 if 语句，检查⽤户名列表是否为空。
如果为空，就打印如下消息。
We need to find some users!
删除列表中的所有⽤户名，确认将打印正确的消息。
'''
usernames = []
if usernames:
    for username in usernames:
        if username == "admin":
            print("Hello admin, would you like to see a status report?")
        else:
            print(f"Hello {username}, thank you for logging in again.")
else:
    print("We need to find some users!")

print("\n----------分界线----------\n")

'''
练习 5.10：检查⽤户名 
按照下⾯的说明编写⼀个程序，模拟⽹站如何确保每个⽤户的⽤户名都独⼀⽆⼆。
创建⼀个⾄少包含 5 个⽤户名的列表，并将其命名为current_users。
再创建⼀个包含 5 个⽤户名的列表，将其命名为 new_users，并确保其中有⼀两个⽤户名也在列表 current_users 中。
遍历列表 new_users，检查其中的每个⽤户名是否已被使⽤。
如果是，就打印⼀条消息，指出需要输⼊别的⽤户名；
否则，打印⼀条消息，指出这个⽤户名未被使⽤。
确保⽐较时 不区分⼤⼩写。换句话说，如果⽤户名 'John' 已被使⽤，应拒绝⽤户名 'JOHN'。
（为此，需要创建列表current_users 的副本，其中包含当前所有⽤户名的全⼩写版本。）
'''
current_users = ['erIc', 'willie', 'admin', 'Erin', 'Ever']
new_users = ['ERIC', 'Willie', 'PHIL', 'ERIN', 'Iona']

current_users_lower = []
for current_user in current_users:
    current_users_lower.append(current_user.lower())

for new_user in new_users:
    if new_user.lower() in current_users_lower:
        print(f"Sorry {new_user}, that name is taken.")
    else:
        print(f"Great, {new_user} is still available.")

print("\n----------分界线----------\n")

'''
练习 5.11：序数 
序数表⽰顺序位置，如 1st 和 2nd。
序数⼤多以 th 结尾，只有 1st、2nd、3rd 例外。
在⼀个列表中存储数字 1〜9。
遍历这个列表。在循环中使⽤⼀个 if-elif-else 结构，打印每个数字对应的序数。
输出内容应为 "1st 2nd 3rd 4th 5th 6th 7th 8th 9th"，每个序数都独占⼀⾏。
'''
numbers = list(range(1,10))

for number in numbers:
    if number == 1:
        print("1st")
    elif number == 2:
        print("2nd")
    elif number == 3:
        print("3rd")
    else:
        print(f"{number}th")        