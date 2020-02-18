"""输入骰子数量和阈值，可以得出达到阈值的骰子的数量"""
import random
from tkinter import *

def GreaterThan(list1,threshold):
    count_result = 0
    for i in list1:
        if i >=threshold:
            count_result += 1
    return count_result

def roll(dice_amount):
    cycle_amount = 0    #重置已循环次数
    dice_result = []    #创建空列表
    import random
    while 1:
        if cycle_amount < dice_amount:
            dice_temp = random.randint(1,6)
            dice_result.append(dice_temp)
            print(dice_temp,end=' ')
            cycle_amount = cycle_amount + 1
        else :
            print('\n')
            break
    return (dice_result)

def roll_dice():
    global list_dice_result
    global list_dice_button_chosen
    global list_dice_button
    global list_display_result
    global str_dice_result
    amount = int(amount_dice_1.get())
    list_dice_result = roll(amount)
    list_dice_amount = [0,0,0,0,0,0,0]
    for i in range(7):
        list_dice_amount[i] = GreaterThan(list_dice_result,i)
    str_dice_result.set('''
2+: %s
3+: %s
4+: %s
5+: %s
6+: %s

总和: %s'''%(list_dice_amount[2],list_dice_amount[3],list_dice_amount[4],list_dice_amount[5],list_dice_amount[6],sum(list_dice_result)))
    #删除原本的骰子按钮
    if list_dice_button:
        for i in list_dice_button:
            i.destroy()
        list_dice_button = []
    #产生新的骰子按钮
    list_display_result = []
    list_dice_button_chosen = []
    for i in range(len(list_dice_result)):
        list_display_result.append(IntVar())
        list_display_result[i].set(list_dice_result[i])
        list_dice_button_chosen.append(IntVar())
        db = Checkbutton(sw_group,textvariable=list_display_result[i],variable=list_dice_button_chosen[-1],indicatoron=0)
        db.grid(row=i//10,column=i%10)
        list_dice_button.append(db)

def reroll_dice():
    global list_dice_result
    global list_display_result
    global str_dice_result
    list_chosen_temp = []
    for each in enumerate(list_dice_button_chosen):
        if each[1].get() == 1:
            list_chosen_temp.append(each[0])
    print('list_chosen_temp:',list_chosen_temp)
    reroll_result = roll(len(list_chosen_temp))
    for number in range(len(list_chosen_temp)):
        list_dice_result[list_chosen_temp[number]] = reroll_result [number]
        list_display_result[list_chosen_temp[number]].set(reroll_result [number])
    list_dice_amount = [0,0,0,0,0,0,0]
    for i in range(7):
        list_dice_amount[i] = GreaterThan(list_dice_result,i)
    str_dice_result.set('''
2+: %s
3+: %s
4+: %s
5+: %s
6+: %s

总和: %s'''%(list_dice_amount[2],list_dice_amount[3],list_dice_amount[4],list_dice_amount[5],list_dice_amount[6],sum(list_dice_result)))


def amount_validity(content):
    if content.isdigit():
        return True
    elif content == '':
        return True
    else:
        return False

def unchoose():
    global list_dice_button
    for i in list_dice_button:
        i.deselect()

def choose_1():
    choose(1)

def choose_2():
    choose(2)

def choose_3():
    choose(3)

def choose_4():
    choose(4)

def choose_5():
    choose(5)

def choose_6():
    choose(6)

def choose(max_number):
    global list_dice_button
    for i in list_dice_button:
        i.deselect()
    number = max_number
    pre_choose_list = []
    while number > 0:
        for each in enumerate(list_dice_result):
            if each[1] == number:
                pre_choose_list.append(each[0])
        number -= 1
    print('pre_choose_list:',pre_choose_list)
    for i in pre_choose_list:
        list_dice_button[i].select()
        
    
    
    

root = Tk()
root.title('Warhammer Dice')

list_dice_button = []


nw_group = LabelFrame(root, padx=5, pady=5)
nw_group.grid(row=0,column=0,sticky=NW)

sw_group = LabelFrame(root,text='骰子',padx=5,pady=5)
sw_group.grid(row=1,column=0,sticky=NW)

se_group = LabelFrame(root, padx=5, pady=5)
se_group.grid(row=1,column=1,sticky=NW)

ne_group = LabelFrame(root, padx=5, pady=5)
ne_group.grid(row=0,column=1,sticky=NW)

amount_validity_CMD = root.register(amount_validity)

amount_dice_1 = StringVar()
str_dice_result = StringVar()


Label(nw_group,text='骰子数量:').grid(row=0,column=0)
Entry(nw_group,textvariable=amount_dice_1,width=8,validate="key",validatecommand=(amount_validity_CMD,'%P')).grid(row=0,column=1)

Button(nw_group, text="投骰子", command=roll_dice).grid(row=0,column=2,padx=5)

Label(nw_group,textvariable=str_dice_result,justify=LEFT).grid(row=1,column=0)

Button(se_group, text="重投已选", command=reroll_dice).pack()

Button(ne_group, text="取消选择", command=unchoose).pack()
Button(ne_group, text="选择1-", command=choose_1).pack()
Button(ne_group, text="选择2-", command=choose_2).pack()
Button(ne_group, text="选择3-", command=choose_3).pack()
Button(ne_group, text="选择4-", command=choose_4).pack()
Button(ne_group, text="选择5-", command=choose_5).pack()
Button(ne_group, text="选择全部", command=choose_6).pack()


mainloop()
