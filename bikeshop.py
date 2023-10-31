class Component:
    def __init__(self, current_state, max_lifespan):
        self.current_state = current_state
        self.max_lifespan = max_lifespan
    
    def check_condition(self):
        if self.max_lifespan*0.7 < self.current_state <= self.max_lifespan:
            return "Pristine"
        elif self.max_lifespan*0.3 < self.current_state < self.max_lifespan:
            return "Good"
        elif  0 < self.current_state < self.max_lifespan*0.3:
            return "Fragile"
        elif self.current_state == 0:
            return "Broken"

class Bell(Component):
    def ring_the_bell(self):
        if self.current_state != 0:
            self.current_state -= 1
        if self.current_state < 0:
            self.current_state = 0
class Brake(Component):
    def press_the_brakes(self):
        if self.current_state !=0:
            self.current_state -=1
        if self.current_state < 0:
            self.current_state = 0
class Chain(Component):
    def ching_chain(self):
        if self.current_state != 0:
            self.current_state -= 1
        if self.current_state < 0:
            self.current_state = 0
class Tyres(Component):
    def run_run_tyres(self):
        if self.current_state != 0:
            self.current_state -= 1
        if self.current_state < 0:
            self.current_state = 0

class Bike():
    def __init__(self, bell, brake, chain, tyres):
        self.bell = bell
        self.brake = brake
        self.chain = chain
        self.tyres = tyres
    
    def ride(self):
        print('bell',self.bell.current_state, 'brake', self.brake.current_state, 'chain', self.chain.current_state, 'tyres', self.tyres.current_state)

        components = [self.bell, self.brake, self.chain, self.tyres]

        if all(component.max_lifespan *0.7 <= component.current_state <= component.max_lifespan for component in components):
            print( "Perfect condition. Good to go!.")
        elif all(component.max_lifespan *0.3 <= component.current_state < component.max_lifespan  for component in components):
            print( "Good condition. safe drive!.")
        elif (1 <= component.current_state < component.max_lifespan *0.3 for component in components):
            print( "Warning, Your bike needs repair. Please go to service centre.")

    def ring_bell(self):
        
        if all(component.check_condition() == "Pristine" for component in [self.bell, self.brake, self.chain, self.tyres]):
            return "Ring! Ring! Ring!"
        else:
            for component in [self.bell, self.brake, self.chain, self.tyres] :
                if (component.check_condition() == "Broken") :
                    print( "The ring fell off!")
                elif (component.check_condition() == "Fragile") :
                    print("Ring! cling...")

class Racing(Bike):
    def __init__(self, bell, brake, chain, tyres):
        super().__init__(bell, brake, chain, tyres)

    def run_run_tyres(self):
        if self.tyres.current_state != 0:
            self.tyres.current_state -= 1+(5/100)
        if self.tyres.current_state < 0:
            self.tyres.current_state =0
        
    def ching_chain(self):
        if self.chain.current_state != 0:
            self.chain.current_state -= 1+(5/100)
        if self.chain.current_state < 0:
            self.chain.current_state = 0

class BMX(Bike):
    def __init__(self, bell, chain, tyres):
        super().__init__(bell, None, chain, tyres)

    def run_run_tyres(self):
        if self.tyres.current_state != 0:
            self.tyres.current_state -= 1+(15/100)
        if self.tyres.current_state < 0:
            self.tyres.current_state = 0

    def ride(self):
        print('bell',self.bell.current_state,'chain', self.chain.current_state, 'tyres', self.tyres.current_state)

        components = [self.bell, self.chain, self.tyres]

        if all(component.max_lifespan *0.7 <= component.current_state <= component.max_lifespan for component in components):
            print( "Perfect condition. Good to go!.")
        elif all(component.max_lifespan *0.3 <= component.current_state < component.max_lifespan *0.7 for component in components):
            print( "Good condition. safe drive!.")
        elif (1 <= component.current_state < component.max_lifespan *0.3 for component in components):
            print( "Warning, Your bike needs repair. Please go to service centre.")

class Mountain(Bike):
    def __init__(self, bell, brake, chain, tyres):
        super().__init__(bell, brake, chain, tyres)

    def ching_chain(self):
        if self.chain.current_state != 0:
            self.chain.current_state -= 0.85
        if self.chain.current_state < 0:
            self.chain.current_state = 0

class Street(Bike):
    def __init__(self, bell, brake, chain, tyres):
        super().__init__(bell, brake, chain, tyres)    

    def press_the_brakes(self):
        if self.brake.current_state !=0:
            self.brake.current_state -=1+(5/100)
        if self.brake.current_state < 0:
            self.brake.current_state = 0
        
class Service_person:
    def order_parts(self, bike):
        components = [bike.bell, bike.brake, bike.chain, bike.tyres]

        for component in components:
            if component.check_condition() == "Broken":
                component.current_state = component.max_lifespan
                

    def service_parts(self, bike):
        components = [bike.bell, bike.brake, bike.chain, bike.tyres]

        for component in components:
            if component.check_condition() == "Fragile":
                component.current_state = component.max_lifespan*0.7     

    def oil(self, bike):
        components = [bike.brake, bike.chain, bike.tyres]

        for component in components:
            if component.check_condition() == "Good":
                component.current_state = component.max_lifespan    

    def pump_wheels(self, bike):
        components = [bike.tyres]

        for component in components:
            if component.check_condition() == "Good":
                component.current_state = component.max_lifespan

    def service_bike(self, bike):
        self.service_parts(bike)
        self.oil(bike)
        self.pump_wheels(bike)

    def check_safety(self, bike):
        components = [bike.bell, bike.brake]

        if all(component.check_condition() == "Fragile" or component.check_condition() == "Broken" for component in components):
                print("You have failed safety check.")
        else: print("You have passed safety check.")    
    
    def check_up(self, bike):
        components = [bike.bell, bike.brake, bike.chain, bike.tyres]

        for component in components:
            if component.check_condition() == "Broken":
                self.order_parts(bike)
            elif component.check_condition() == "Fragile":
                self.service_parts(bike)
            elif component.check_condition() == "Pristine" or component.check_condition() == "Good":
                self.service_bike(bike)

        print(self.check_safety(bike))    
        print(bike.ride())





a=Bell(70,100)
b=Brake(70,100)
c=Chain(70,100)
d=Tyres(70,100)




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

# #Mountain
# ford.bell.ring_the_bell()
# ford.brake.press_the_brakes()
# ford.ching_chain()
# ford.tyres.run_run_tyres()

ford = Street(a,b,c,d)
#Street
ford.bell.ring_the_bell()
ford.press_the_brakes()
ford.chain.ching_chain()
ford.tyres.run_run_tyres()
ford.bell.ring_the_bell()
ford.press_the_brakes()
ford.chain.ching_chain()
ford.tyres.run_run_tyres()
ford.bell.ring_the_bell()
ford.press_the_brakes()
ford.chain.ching_chain()
ford.tyres.run_run_tyres()
ford.bell.ring_the_bell()
ford.press_the_brakes()
ford.chain.ching_chain()
ford.tyres.run_run_tyres()
ford.bell.ring_the_bell()
ford.press_the_brakes()
ford.chain.ching_chain()
ford.tyres.run_run_tyres()
ford.bell.ring_the_bell()
ford.press_the_brakes()
ford.chain.ching_chain()
ford.tyres.run_run_tyres()
ford.bell.ring_the_bell()
ford.press_the_brakes()
ford.chain.ching_chain()
ford.tyres.run_run_tyres()
ford.bell.ring_the_bell()
ford.press_the_brakes()
ford.chain.ching_chain()
ford.tyres.run_run_tyres()
ford.bell.ring_the_bell()
ford.press_the_brakes()
ford.chain.ching_chain()
ford.tyres.run_run_tyres()
ford.bell.ring_the_bell()
ford.press_the_brakes()
ford.chain.ching_chain()
ford.tyres.run_run_tyres()
ford.bell.ring_the_bell()
ford.press_the_brakes()
ford.chain.ching_chain()
ford.tyres.run_run_tyres()
ford.bell.ring_the_bell()
ford.press_the_brakes()
ford.chain.ching_chain()
ford.tyres.run_run_tyres()
ford.bell.ring_the_bell()
ford.press_the_brakes()
ford.chain.ching_chain()
ford.tyres.run_run_tyres()
ford.bell.ring_the_bell()
ford.press_the_brakes()
ford.chain.ching_chain()
ford.tyres.run_run_tyres()
ford.bell.ring_the_bell()
ford.press_the_brakes()
ford.chain.ching_chain()
ford.tyres.run_run_tyres()
ford.bell.ring_the_bell()
ford.press_the_brakes()
ford.chain.ching_chain()
ford.tyres.run_run_tyres()
ford.bell.ring_the_bell()
ford.press_the_brakes()
ford.chain.ching_chain()
ford.tyres.run_run_tyres()
ford.bell.ring_the_bell()
ford.press_the_brakes()
ford.chain.ching_chain()
ford.tyres.run_run_tyres()
ford.bell.ring_the_bell()
ford.press_the_brakes()
ford.chain.ching_chain()
ford.tyres.run_run_tyres()
ford.bell.ring_the_bell()
ford.press_the_brakes()
ford.chain.ching_chain()
ford.tyres.run_run_tyres()
ford.bell.ring_the_bell()
ford.press_the_brakes()
ford.chain.ching_chain()
ford.tyres.run_run_tyres()
ford.bell.ring_the_bell()
ford.press_the_brakes()
ford.chain.ching_chain()
ford.tyres.run_run_tyres()
ford.bell.ring_the_bell()
ford.press_the_brakes()
ford.chain.ching_chain()
ford.tyres.run_run_tyres()
ford.bell.ring_the_bell()
ford.press_the_brakes()
ford.chain.ching_chain()
ford.tyres.run_run_tyres()
ford.bell.ring_the_bell()
ford.press_the_brakes()
ford.chain.ching_chain()
ford.tyres.run_run_tyres()
ford.bell.ring_the_bell()
ford.press_the_brakes()
ford.chain.ching_chain()
ford.tyres.run_run_tyres()
ford.bell.ring_the_bell()
ford.press_the_brakes()
ford.chain.ching_chain()
ford.tyres.run_run_tyres()
ford.bell.ring_the_bell()
ford.press_the_brakes()
ford.chain.ching_chain()
ford.tyres.run_run_tyres()
ford.bell.ring_the_bell()
ford.press_the_brakes()
ford.chain.ching_chain()
ford.tyres.run_run_tyres()
ford.bell.ring_the_bell()
ford.press_the_brakes()
ford.chain.ching_chain()
ford.tyres.run_run_tyres()
ford.bell.ring_the_bell()
ford.press_the_brakes()
ford.chain.ching_chain()
ford.tyres.run_run_tyres()
ford.bell.ring_the_bell()
ford.press_the_brakes()
ford.chain.ching_chain()
ford.tyres.run_run_tyres()
ford.bell.ring_the_bell()
ford.press_the_brakes()
ford.chain.ching_chain()
ford.tyres.run_run_tyres()
ford.bell.ring_the_bell()
ford.press_the_brakes()
ford.chain.ching_chain()
ford.tyres.run_run_tyres()
ford.bell.ring_the_bell()
ford.press_the_brakes()
ford.chain.ching_chain()
ford.tyres.run_run_tyres()
ford.bell.ring_the_bell()
ford.press_the_brakes()
ford.chain.ching_chain()
ford.tyres.run_run_tyres()
ford.bell.ring_the_bell()
ford.press_the_brakes()
ford.chain.ching_chain()
ford.tyres.run_run_tyres()
ford.bell.ring_the_bell()
ford.press_the_brakes()
ford.chain.ching_chain()
ford.tyres.run_run_tyres()
ford.bell.ring_the_bell()
ford.press_the_brakes()
ford.chain.ching_chain()
ford.tyres.run_run_tyres()
ford.bell.ring_the_bell()
ford.press_the_brakes()
ford.chain.ching_chain()
ford.tyres.run_run_tyres()
ford.bell.ring_the_bell()
ford.press_the_brakes()
ford.chain.ching_chain()
ford.tyres.run_run_tyres()
ford.bell.ring_the_bell()
ford.press_the_brakes()
ford.chain.ching_chain()
ford.tyres.run_run_tyres()
ford.bell.ring_the_bell()
ford.press_the_brakes()
ford.chain.ching_chain()
ford.tyres.run_run_tyres()
ford.bell.ring_the_bell()
ford.press_the_brakes()
ford.chain.ching_chain()
ford.tyres.run_run_tyres()
ford.bell.ring_the_bell()
ford.press_the_brakes()
ford.chain.ching_chain()
ford.tyres.run_run_tyres()
ford.bell.ring_the_bell()
ford.press_the_brakes()
ford.chain.ching_chain()
ford.tyres.run_run_tyres()
ford.bell.ring_the_bell()
ford.press_the_brakes()
ford.chain.ching_chain()
ford.tyres.run_run_tyres()
ford.bell.ring_the_bell()
ford.press_the_brakes()
ford.chain.ching_chain()
ford.tyres.run_run_tyres()
ford.bell.ring_the_bell()
ford.press_the_brakes()
ford.chain.ching_chain()
ford.tyres.run_run_tyres()
ford.bell.ring_the_bell()
ford.press_the_brakes()
ford.chain.ching_chain()
ford.tyres.run_run_tyres()
ford.bell.ring_the_bell()
ford.press_the_brakes()
ford.chain.ching_chain()
ford.tyres.run_run_tyres()
ford.bell.ring_the_bell()
ford.press_the_brakes()
ford.chain.ching_chain()
ford.tyres.run_run_tyres()
ford.bell.ring_the_bell()
ford.press_the_brakes()
ford.chain.ching_chain()
ford.tyres.run_run_tyres()
ford.bell.ring_the_bell()
ford.press_the_brakes()
ford.chain.ching_chain()
ford.tyres.run_run_tyres()
ford.bell.ring_the_bell()
ford.press_the_brakes()
ford.chain.ching_chain()
ford.tyres.run_run_tyres()
ford.bell.ring_the_bell()
ford.press_the_brakes()
ford.chain.ching_chain()
ford.tyres.run_run_tyres()
ford.bell.ring_the_bell()
ford.press_the_brakes()
ford.chain.ching_chain()
ford.tyres.run_run_tyres()

ford.bell.ring_the_bell()
ford.press_the_brakes()
ford.chain.ching_chain()
ford.tyres.run_run_tyres()
ford.bell.ring_the_bell()
ford.press_the_brakes()
ford.chain.ching_chain()
ford.tyres.run_run_tyres()
ford.bell.ring_the_bell()
ford.press_the_brakes()
ford.chain.ching_chain()
ford.tyres.run_run_tyres()
ford.bell.ring_the_bell()
ford.press_the_brakes()
ford.chain.ching_chain()
ford.tyres.run_run_tyres()
ford.bell.ring_the_bell()
ford.press_the_brakes()
ford.chain.ching_chain()
ford.tyres.run_run_tyres()
ford.bell.ring_the_bell()
ford.press_the_brakes()
ford.chain.ching_chain()
ford.tyres.run_run_tyres()
ford.bell.ring_the_bell()
ford.press_the_brakes()
ford.chain.ching_chain()
ford.tyres.run_run_tyres()
ford.bell.ring_the_bell()
ford.press_the_brakes()
ford.chain.ching_chain()
ford.tyres.run_run_tyres()
ford.bell.ring_the_bell()
ford.press_the_brakes()
ford.chain.ching_chain()
ford.tyres.run_run_tyres()
ford.bell.ring_the_bell()
ford.press_the_brakes()
ford.chain.ching_chain()
ford.tyres.run_run_tyres()
ford.bell.ring_the_bell()
ford.press_the_brakes()
ford.chain.ching_chain()
ford.tyres.run_run_tyres()




ford.ride()
joe = Service_person()

joe.check_up(ford)
joe.check_safety(ford)
# print(ford.ride())

# ford.ride()







