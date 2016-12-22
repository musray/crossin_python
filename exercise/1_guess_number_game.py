#!/usr/bin/env python3
# crossin练习1 - 猜数字

import random

def _numberGenerator(): # 被主函数调用的helper function, 名称用'_'开头; 个人习惯
    '''产生一个随机数'''
    num = random.randint(1, 11)  # 范围1-10

    return num

def _gameRound(num, initial):
    '''猜一个数字，判断结果并将其return'''

    # 用initial判断是否是第一次猜测(用户看到的文字提示不同)
    if initial == True:  # 第一次猜测
        userGuess = input('请输入你的猜测：-->\n ')
    else:                # 否则，不是第一次猜测
        userGuess = input('猜错，请再次输入你的猜测：-->\n ')

    guessWrong = True  # 对猜测对错的判断结果

    # 如果用户输入了整数以外的内容，可以用try/except/finally防止程序崩溃
    try:
        # 比如，用户输入了一个a, int(a)会抛出一个名为ValueError的Exception
        if int(userGuess) != num:
            guessWrong = True  # 猜错
        else:
            guessWrong = False # 猜对

    # 用except语句接住这个ValueError的Exception
    except ValueError:
        print('输入错误！\n请输入一个整数，例如0，1，3，6...')

    # 无论是否出现ValueError，都要将结果return
    finally:
        return guessWrong


def main():
    '''主程序，设置一些基本的参数，并控制游戏的开始、结束'''
    needGoOn      = True   # 判断程序是否需要继续（取决于用户猜对还是猜错）
    initial       = True   # 是否是本次游戏的第一轮猜数
    roundCounter  = 0      # 轮次计数
    machineNumber = _numberGenerator()  # 调用上面的函数，将生成的随机数存到变量里
    print('欢迎进入本游戏。\n已经为你生成1-10之间的一个整数。')

    # DEGUG 调试的时候用的语句，显示本次游戏的答案
    # print('DEBUG machineNumber is {}'.format(machineNumber))

    while(needGoOn):

        # 调用函数，进行一轮猜数; 猜对needGoOn=False, 退出while循环
        needGoOn = _gameRound(machineNumber, initial)
        # 玩了一轮，给计数器加 1
        roundCounter  = roundCounter + 1
        # 第一次猜数已结束，让initial=False
        initial  = False

    # 用户猜对之后，needGoOn=False，退出while到这里
    print('恭喜，猜对了！正确答案为: {}'.format(machineNumber)) # '{} {}'.format('a', 'b') 是字符串“ 造型 ”语句
    print('总计作答次数：{}次'.format(roundCounter))

# 如果在命令行里执行python script_name.py
# 系统变量__name__会等于'__main__'
# 此时游戏才会正式开始
# 另外一种情况，如果在其他代码中使用 import script_name
# __name__不会等于'__main__', 游戏不会开始
if __name__ == '__main__':
    try:
        main()
    # 在任意时刻，如果用户使用ctrl+c，会终止游戏
    # Python会抛出KeyboardInterrupt，并在命令行中出现一串traceback
    # 用try/except语句接住这个KeyboardInterrupt
    # 可以防止traceback的输出，并提升用户体验
    except KeyboardInterrupt:
        print('您已退出游戏')
