class MusicalInstruments:
    numberOfKeys = 12


class StringInstruments(MusicalInstruments):
    typeOfWood = "Tonewood"


class Guitar(StringInstruments):
    def __init__(self):
        self.numberOfStrings = 6
        print("This guitar consists of {}string . It is made of {} an it can play {}keys".format(self.numberOfStrings,
                                                                                                 self.typeOfWood,
                                                                                                 self.numberOfKeys))


guitar = Guitar()