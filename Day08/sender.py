# coding: utf-8
from __future__ import unicode_literals
from wxpy import *

bot = Bot('bot.pkl')
bot.groups
# my_friend = bot.friends().search('小柒2012')[0]
# my_friend.send('Hello WeChat!')
print(bot.groups())
my_group = bot.groups().search('Python学习小组')[0]
my_group.send('Python 监控报警')

