#Liskov substitution principle
#A derive class can assume the place of its super class ,and everything should work
class KichtecnAppliance():
    def on():
        pass
    def off():
      pass

   
        
class Temp(KichtecnAppliance):
    def set_temparature():
        pass
class Toaster(Temp):
        def on():
            pass
        def off():
            pass
        def set_temparature():
            pass
   