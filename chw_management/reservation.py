


today_menu = ["今天菜单如下", "1  宫保鸡丁", "2  红烧肉", "3  白萝卜焖肉", "4  可乐鸡翅", "5  豆腐包肉 ",
              "6  鲤鱼跃龙门", "7  凉拌莲藕", "8  红烧南瓜", "9  大白菜", "10 青菜", "11 荷包蛋(另加２元）", "12 蛋炒饭(10元)"]
price = [0, 0, 12, 0, 0, 10, 13, 0, 9, 11, 14, 0, 10, 0, 15, 0]


def getTodayMenu():
    return today_menu


def showTodayMenu(interable):
    for today_menu_details in today_menu:
        print(today_menu_details)


def showCombineNote():
    print("提示：一荤一素10，两素菜9元，一荤两素11，，三素菜10，两荤菜12，两荤一素13，两荤两素14，两荤三素15元")
    print("请输入您点餐的编号，编号之间用逗号分开，不同份数之间用空格隔开\n例如输入1,9,10  2,6,8  3,10,谢谢 : ")


def dealWithUserInput():
    user_choise = input()

    user_choise_list = user_choise.split()

    price_total = 0  # 用price_total来记录所点菜的总和
    price_one = 0  # 用来计算每一份菜的价格
    choosed_list = []
    pay_total = 0  # 用来保存优惠后需要支付的价格

    for one_order in user_choise_list:
        count_i = count_j = 0  # count_i用来保存素菜的个数　　count_j用来保存荤菜的个数
        hebaodan = 0  # 用来记录荷包蛋的个数
        danchaofan = 0  # 用来记录蛋炒饭的个数
        one_order_list = one_order.split(",")  # one_order_list 保存的是["1","9","10]
        for menu_item in one_order_list:  # menu_item　就是保存的单个的数字
            # 首先得防止用户输入的不是数字，是数字则处理，不是则提示用户重新输入
            if menu_item.strip().isdigit():
                # 这里防止用户输入的时候跟预期的不一样，可能多了一些空格，所以需要去掉空格后转化为数字
                if int(menu_item.strip()) < 7:
                    count_j += 1
                elif int(menu_item.strip()) < 11:
                    count_i += 1
                elif int(menu_item.strip()) == 11:
                    hebaodan += 1
                elif int(menu_item.strip()) == 12:
                    danchaofan += 1
                choosed_list.append(int(menu_item))
            else:
                print("您输入的有非数字类型，请重新运行程序，谢谢")
                exit()
            choosed_list.append(0)

        # 如果是正确的组合，则price[count_i*4 + count_j]是不会为０的，但是输入一个数字代表特色菜品的时候也是可行的
        # 两种组合都不是的时候就证明不是正确的组合，程序退出
        if price[count_i * 4 + count_j] == 0 and "12" not in one_order:
            print("您输入的不是一个正确的组合，请重新运行程序，　谢谢")
            exit()
        else:
            price_one = price[count_i * 4 + count_j] + hebaodan * 2 + danchaofan * 10
        price_total += price_one

    # 根据计算得到的总需要支付的价格，判断享受哪种优惠，得出优惠后的价格
    if price_total >= 30:
        pay_total = price_total - 4

    elif price_total >= 26:
        pay_total = price_total - 3

    elif price_total >= 20:
        pay_total = price_total - 2
    else:
        pay_total = price_total

    print("您预订了 %d 份美食，具体如下: " % len(user_choise_list))

    for choosed_item in choosed_list:
        if choosed_item == 0:
            print()
        else:
            print(today_menu[choosed_item])
    print("您共需要支付 %d 元,谢谢" % pay_total)


print("欢迎进入点餐系统,下单不可退订呦~")

today_menu1 = getTodayMenu()
showTodayMenu(today_menu1)
showCombineNote()
dealWithUserInput()

