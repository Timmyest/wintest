# 钱包
money = 100
# 用于结算
MONEY = money
# 购物车
shop_car = []
# 计数器(计算消费金额)
count = 0
# 商店货架
shop = {
    "水果": {
        "1": ["苹果", 50],
        "2": ["香蕉", 60],
        "3": ["草莓", 20]
    },
    "日用品": {
        "1": ["肥皂", 10],
        "2": ["牙膏", 15],
        "3": ["洗发水", 20],
    },
    "服装": {
        "1": ["衬衫", 100],
        "2": ["毛衣", 150],
        "3": ["羽绒服", 300],
    },
    "电子产品": {
        "1": ["手机", 500],
        "2": ["电脑", 1000],
        "3": ["电视机", 450],
    },
}
# 欢迎菜单
info = ('''
    ##################### welcome#########################
    水果
    日用品
    电子产品
    服装
    结账
    离开
    #######################################################
        ''')
while True:
    print(info)
    type = input("输入你想看的种类: ")
    if type == "离开":
        if MONEY == money:
            print("欢迎下次光临")
            exit()
        else:
            for i in shop_car:
                count = count + i[1]
                YE = MONEY - count
                print('''
                       您消费:{}
                       余额:{}
                       '''.format(count, YY))
                exit()
    elif type == "结账":
        if count == 0:
            print("您未消费!")
            exit()
        else:
            for k in shop_car:
                count = count + k[1]
                YE = MONEY - count
                menu = []
                for j in shop_car:
                     menu.append(j[0])

            print('''
                    #######消费列表######
                       {}
                    ####################

                   您消费:{}
                   余额:{}
         '''.format(menu, count - k[1], YY))
            exit()
    else:
        print(info)
        print(shop[type])
        print('''
                       您的余额为:{}'''.format(money))
        # 选择水果里的商品
        SP = input("请选择你想买的商品: ")
        #  加入购物车
        shop_car.append(shop[type][SP])
        JG = shop[type][SP][1]

        if money >= JG:

            for q in shop_car:
                count = 0
                count = count + q[1]

                YE = money - count
                print('''
                              您消费:{}
                              余额:{}
                              '''.format(count, YE))
                # continue
                YY = YE
            # print(YY)
            money = money - JG
            continue
        else:
            # print("余额不足")
            print("\033[31;1;31m余额不足\033[0m")
            continue