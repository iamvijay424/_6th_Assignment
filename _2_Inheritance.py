class Dog:
    def __init__(self,name,age,coat_color):
        self.name=name
        self.age=age
        self.coat_color=coat_color

    def descripation(self):
        print("Name :",self.name,"\nAge:",self.age,"\nCoat Color:",self.coat_color)
 
    def get_coat_color(self):
        print(self.coat_color)

class jackRussellTerrier(Dog):
    def __init__(self,name,age,coat_color,gen,paws):
        super().__init__(name,age,coat_color)
        self.gen=gen
        self.paws=paws

    def dispaly(self):
        print(self.name,self.age,self.coat_color,self.gen,self.paws )

    def gender(self):
        print('gender:',self.gen)

    def paw(self):
        print('no of paws:',self.paws)

class Bulldog(Dog):
    def __init__(self,name,age,coat_color,weight,paws):
        super().__init__(name,age,coat_color)
        self.weigh=weight
        self.paws=paws
        
    def weight(self):
        print('weight:',self.weigh)
    
    def paw(self):
        print('no of paws:',self.paws)



jack=jackRussellTerrier('pinky',4,'brown','female',18)
jack.descripation()
jack.gender()
jack.paw()

bull=Bulldog('Rock',4,'brown','28kgs',20)
bull.descripation()
bull.weight()
bull.paw()
