# Task 1
class Device:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def turn_on(self):
        print(f"{self.brand} {self.model} включено")

    def turn_off(self):
        print(f"{self.brand} {self.model} выключено")


class CoffeeMachine(Device):
    def __init__(self, brand, model, coffee_type):
        super().__init__(brand, model)
        self.coffee_type = coffee_type

    def brew_coffee(self):
        print(f"{self.brand} {self.model} готовит кофе типа {self.coffee_type}")


class Blender(Device):
    def __init__(self, brand, model, speed_levels):
        super().__init__(brand, model)
        self.speed_levels = speed_levels

    def blend(self):
        print(
            f"{self.brand} {self.model} мешает продукты на {self.speed_levels} уровне")


class MeatGrinder(Device):
    def __init__(self, brand, model, motor_power):
        super().__init__(brand, model)
        self.motor_power = motor_power

    def grind_meat(self):
        print(
            f"{self.brand} {self.model} молет мясо с мотором мощностью {self.motor_power} Вт")


coffee_machine = CoffeeMachine("Philips", "HM324", "Американо")
coffee_machine.turn_on()
coffee_machine.brew_coffee()
coffee_machine.turn_off()

blender = Blender("Bosch", "BF32344", 5)
blender.turn_on()
blender.blend()
blender.turn_off()

meat_grinder = MeatGrinder("Kenwood", "GH584", 450)
meat_grinder.turn_on()
meat_grinder.grind_meat()
meat_grinder.turn_off()

# Task 2
class Ship:
    def __init__(self, name, displacement, crew):
        self.name = name
        self.displacement = displacement
        self.crew = crew

    def sail(self):
        print(f"{self.name} отправляется в морское плавание")

    def fire(self):
        print(f"{self.name} открывает огонь по врагу")


class Frigate(Ship):
    def __init__(self, name, displacement, crew, missile_count):
        super().__init__(name, displacement, crew)
        self.missile_count = missile_count

    def launch_missiles(self):
        print(f"{self.name} выпускает {self.missile_count} ракеты")


class Destroyer(Ship):
    def __init__(self, name, displacement, crew, gun_caliber):
        super().__init__(name, displacement, crew)
        self.gun_caliber = gun_caliber

    def fire_main_gun(self):
        print(
            f"{self.name} открывает огонь {self.gun_caliber}")


class Cruiser(Ship):
    def __init__(self, name, displacement, crew, missile_defense):
        super().__init__(name, displacement, crew)
        self.missile_defense = missile_defense

    def activate_missile_defense(self):
        print(f"{self.name} противоракетная оборона")

frigate = Frigate("KABAN", 5000, 200, 32)
frigate.sail()
frigate.launch_missiles()

destroyer = Destroyer("BOTTZ", 8000, 350, 127)
destroyer.sail()
destroyer.fire_main_gun()

cruiser = Cruiser("FAER", 9000, 400, "Aegis")
cruiser.sail()
cruiser.activate_missile_defense()
