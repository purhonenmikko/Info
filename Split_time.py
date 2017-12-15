class Triathlon:
    def __init__(self, name, serie):
        self.__name = name
        self.__serie = serie
        self.__swim = 0
        self.__T1 = 0
        self.__bike = 0
        self.__T2 = 0
        self.__run = 0

    def tell_name(self):
        return self.__name

    def tell_serie(self):
        return self.__serie

    def tell_swimtime(self):
        return self.__swim

    def tell_T1(self):
        return self.__T1

    def tell_biketime(self):
        return self.__bike

    def tell_T2(self):
        return self.__T2

    def tell_runningtime(self):
        return self.__run
#-----------------------------------------

    def change_swim(self, swim):
        self.__swim = swim

    def change_T1(self, T1):
        self.__T1 = T1

    def change_bike(self, bike):
        self.__bike = bike

    def change_T2(self, T2):
        self.__T2 = T2

    def change_run(self, run):
        self.__run = run
#-----------------------------------------

def read_name():
    name = input("give competitor's name: \n")
    return name

def read_serie():
    serie = input("give competitor's serie: \n")
    return serie

def main():
    name1 = read_name()
    serie1 = read_serie()
    competitor1 = Triathlon(name1, serie1)
    name2 = read_name()
    serie2 = read_serie()
    competitor2 = Triathlon(name2, serie2)
    print("Name:", competitor1.tell_name())
    print("Serie:", competitor1.tell_serie())
    print("Name:", competitor2.tell_name())
    print("Serie:", competitor2.tell_serie())
    print("-----------------------------------------")
    print(competitor1)
    print(competitor2)
    swim1 = int(input("tell first competitor's swimming time:\n"))
    swim2 = int(input("tell other competitor's swimming time:\n"))
    competitor1.change_swim(swim1)
    competitor2.change_swim(swim2)
    print(competitor1.tell_name(), ":", competitor1.tell_swim())
    print(competitor2.tell_name(), ":", competitor2.tell_swim())

main()












