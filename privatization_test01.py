class privat_test:

    __is_5g_enable = True

    def __check_5g(self):
        if self.__is_5g_enable == True:
            print("5G开启")
        elif self.__is_5g_enable == False:
            print("5G关闭，使用4G网络")

    def call_by_5g(self):
        self.__check_5g()
        print("正在通话中")

privat_test().call_by_5g