class Human:
    laugh = "hahahahaha"

    def show_laugh(self):
        print(self.laugh)  #　打印laugh

    def laugh_100th(self):  # 调用show_laugh100次
        for i in range(100):
            print(i)
            self.show_laugh()

li_lei = Human()
li_lei.laugh_100th()