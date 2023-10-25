class Component:
    def __init__(self, current_state, max_lifespan):
        self.current_state = current_state
        self.max_lifespan = max_lifespan
    
    def check_condition(self):
        if self.max_lifespan*0.7 < self.current_state <= self.max_lifespan:
            return "Pristine"
        elif self.max_lifespan*0.3 < self.current_state < self.max_lifespan*0.7:
            return "Good"
        elif  0 < self.current_state < self.max_lifespan*0.3:
            return "Fragile"
        elif self.current_state == 0:
            return "Broken"

class Bell(Component):
    def ring_the_bell(self):
        if self.current_state != 0:
            self.current_state -= 1
            return "ring ring -1"
class Brake(Component):
    def press_the_brakes(self):
        if self.current_state !=0:
            self.current_state -=1
            return "gigggggg!!! -1"
class Chain(Component):
    def ching_chain(self):
        if self.current_state != 0:
            self.current_state -= 1
            return "ching ching -1"
class Tyres(Component):
    def run_run_tyres(self):
        if self.current_state != 0:
            self.current_state -= 1
            return "bump bump -1"

    


class Bike():
    def __init__(self, bell, brake, chain, tyres):
        self.bell = bell
        self.brake = brake
        self.chain = chain
        self.tyres = tyres
    
    def ride(self):
        # self.bell.ring_the_bell()
        # self.brake.press_the_brakes()
        # self.chain.ching_chain()
        # self.tyres.run_run_tyres()
        
        print('bell',self.bell.current_state, 'brake', self.brake.current_state, 'chain', self.chain.current_state, 'tyres', self.tyres.current_state)

        if all(component.max_lifespan *0.7 <= component.current_state <= component.max_lifespan for component in [self.bell, self.brake, self.chain, self.tyres]):
            return "Perfect condition. Good to go!."
        elif all(component.max_lifespan *0.3 <= component.current_state < component.max_lifespan *0.7 for component in [self.bell, self.brake, self.chain, self.tyres]):
            return "Good condition. safe drive!."
        elif (1 <= component.current_state < component.max_lifespan *0.3 for component in [self.bell, self.brake, self.chain, self.tyres]):
            return "Warning, Your bike needs repair. Please go to service centre."

    def ring_bell(self):
        
        if all(component.check_condition() == "Pristine" for component in [self.bell, self.brake, self.chain, self.tyres]):
            return "Ring! Ring! Ring!"
        else:
            for component in [self.bell, self.brake, self.chain, self.tyres] :
                if (component.check_condition() == "Broken") :
                    return "The ring fell off!"
                elif (component.check_condition() == "Fragile") :
                    return "Ring! cling..."

class Racing(Bike):
    def __init__(self, bell, brake, chain, tyres):
        super().__init__(bell, brake, chain, tyres)

    def run_run_tyres(self):
        if self.tyres.current_state != 0:
            self.tyres.current_state -= 1+(5/100)
            return self.tyres.current_state
        
    def ching_chain(self):
        if self.chain.current_state != 0:
            self.chain.current_state -= 1+(5/100)
            return self.chain.current_state

class BMX(Bike):
    def __init__(self, bell, chain, tyres):
        super().__init__(bell, None, chain, tyres)

    def run_run_tyres(self):
        if self.tyres.current_state != 0:
            self.tyres.current_state -= 1+(15/100)
            return self.tyres.current_state

    def ride(self):
    
        print('bell',self.bell.current_state, 'chain', self.chain.current_state, 'tyres', self.tyres.current_state)

        if all(component.max_lifespan *0.7 <= component.current_state <= component.max_lifespan for component in [self.bell, self.chain, self.tyres]):
            return "Perfect condition. Good to go!."
        elif all(component.max_lifespan *0.3 <= component.current_state < component.max_lifespan *0.7 for component in [self.bell,  self.chain, self.tyres]):
            return "Good condition. safe drive!."
        elif (1 <= component.current_state < component.max_lifespan *0.3 for component in [self.bell, self.chain, self.tyres]):
            return "Warning, Your bike needs repair. Please go to service centre."    
    

class Mountain(Bike):
    def __init__(self, bell, brake, chain, tyres):
        super().__init__(bell, brake, chain, tyres)

    def ching_chain(self):
        if self.chain.current_state != 0:
            self.chain.current_state -= 0.85
            return self.chain.current_state    

a=Bell(100,100)
b=Brake(100,100)
c=Chain(100,100)
d=Tyres(100,100)

ford = Mountain(a,b,c,d)

# Bike
# ford.bell.ring_the_bell()
# ford.brake.press_the_brakes()
# ford.chain.ching_chain()
# ford.tyres.run_run_tyres()

#Racing
# ford.bell.ring_the_bell()
# ford.brake.press_the_brakes()
# ford.ching_chain()
# ford.run_run_tyres()

#BMX
# ford.bell.ring_the_bell()
# ford.chain.ching_chain()
# ford.run_run_tyres()

#Mountain
ford.bell.ring_the_bell()
ford.brake.press_the_brakes()
ford.ching_chain()
ford.tyres.run_run_tyres()

ford.ride()

