class MissingParameterError:
    pass

class InvalidParameterError(Exception):
    def __init__(self, invalid_param, *args):
        output = f"Invalid class parameter: {invalid_param}"
        super().__init__(output, *args)

class InvalidAgeError(InvalidParameterError):
    def __init__(self, age, *args):
        output = f"Invalid parameter: {age}"
        super().__init__(output, *args)

class JungleAnimal:
    def __init__(self, name, age, sound):
        self.name = name
        self.age = age
        self.sound = sound

        if type(name) != str:
            raise InvalidParameterError(name)

        if type(age) != int:
            raise InvalidAgeError

        if type(sound) != str:
            raise InvalidSoundError

    def make_sound(self):
        return f"{self.name} says {self.sound}!"

    def print(self):
        pass

    def daily_task(self):
        pass

class Jaguar(JungleAnimal):
    def __init__(self,  name, age, sound):
        super().__init__(name, age, sound)
        if age > 15:
            raise InvalidAgeError(age)
