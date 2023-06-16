class Hello_world:
    helloZeroUnderLIne = "Hello"
    _hello1UnderLine = "_Hello"
    __hello2UnderLines = "__Hello"
    def __init__(self):
        self.World = "World"
        self._World = "_World"
        self.__World = "__World"
    def Printer(self):
        print(self.helloZeroUnderLIne)
        print(self._hello1UnderLine)
        print(self.__hello2UnderLines)
        print(self.World)
        print(self._World)
        print(self.__World)
class Hi(Hello_world):
    def Hi_Print(self):
        print(self.helloZeroUnderLIne)
        print(self._hello1UnderLine)
        print(self.World)
        print(self._World)
        #are not inherited
        #print(self.__hello2UnderLines)#AttributeError: 'Hi' object has no attribute '_Hi__hello2UnderLines'
        #print(self.__World)#AttributeError: 'Hi' object has no attribute '_Hi__World'

hello = Hello_world()
print(hello.helloZeroUnderLIne)
print(hello._hello1UnderLine)
#are not available
#print(hello.__hello2UnderLines)#AttributeError: 'Hello_world' object has no attribute '__hello2UnderLines'.
#print(hello.__World)#AttributeError: 'Hello_world' object has no attribute '__World'.
hello.Printer()
hi = Hi()
hi.Hi_Print()