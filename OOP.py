class Car:
    def sound(self):
        sound='beepbeep'
        print(sound)
    def longsound(self):
        longsound='beepbeppbeep'
        print(longsound)

car = Car()
car.sound()
car.longsound()
class Button:
    _click_count=0
    def click(self):
        self._click_count+= 1

    def click_count(self):
        return self._click_count
    def reset(self):
       self._click_count=0
b1=Button()
b2=Button()

b1.click()
b1.click()
b2.click()
print(b1.click_count(),b2.click_count())
b1.reset()
print(b1.click_count(),b2.click_count())
class c:
    def __init__(self,name):
        self.name=name
    def meo(self):
        print(self.name,':bbbbbb')
cat=c('ghjdjndnhddh')
cat.meo()