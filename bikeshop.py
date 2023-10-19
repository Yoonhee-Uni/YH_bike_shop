class Component:
    def __init__(self, current_state, max_lifespan):
        self.current_state = current_state
        self.max_lifespan = max_lifespan
    
    def check_condition(self):
        if 71 < self.current_state <= 100:
            return "Pristine"
        elif 31 < self.current_state < 70:
            return "Good"
        elif  0 < self.current_state < 30:
            return "Fragile"
        elif self.current_state == 0:
            return "Broken"

class Bell(Component):
    def ring_the_bell(self):
        if self.current_state != 0:
            self.current_state -= 5
            return "ring ring -5"
class Brake(Component):
    def press_the_brakes(self):
        if self.current_state !=0:
            self.current_state -=10
            return "gigggggg!!! -10"
class Chain(Component):
    def ching_chain(self):
        if self.current_state != 0:
            self.current_state -= 10
            return "ching ching -10"
class Tyres(Component):
    def run_run_tyres(self):
        if self.current_state != 0:
            self.current_state -= 8
            return "bump bump -8"

    


class Bike(Component):
    def __init__(self, bell, brake, chain, tyres):
        self.bell = bell
        self.brake = brake
        self.chain = chain
        self.tyres = tyres
    
    def ride(self):
        if all(71 <= component.current_state <= 100 for component in [self.bell, self.brake, self.chain, self.tyres]):
            return "Perfect condition. Good to go!."
        elif all(31 <= component.current_state < 70 for component in [self.bell, self.brake, self.chain, self.tyres]):
            return "Good condition. safe drive!."
        elif (1 <= component.current_state < 30 for component in [self.bell, self.brake, self.chain, self.tyres]):
            return "Warning, Your bike needs repair. Please go to service centre."
        # elif (component.current_state == 0 for component in [self.bell, self.brake, self.chain, self.tyres]):
        #     return "I told you. Your bike is now a rubbish."

    def ring_bell(self):
        
        if all(component.check_condition() == "Pristine" for component in [self.bell, self.brake, self.chain, self.tyres]):
            return "Ring! Ring! Ring!"
        
        # if (component.check_condition() == "Broken" for component in [self.bell, self.brake, self.chain, self.tyres]):
        #     print(component)


        for component in [self.bell, self.brake, self.chain, self.tyres] :
            if (component.check_condition() == "Broken") :
                return "The ring fell off!"
            elif (component.check_condition() == "Fragile") :
                return "Ring! cling..."


a=Bell(10,100)
b=Brake(100,100)
c=Chain(100,100)
d=Tyres(100,100)

ford = Bike(a,b,c,d)

# print(ford.bell.check_condition())
print(ford.ring_bell())

