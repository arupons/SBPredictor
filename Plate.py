class Plate:
    def validate(self, plate):
        if type(plate) == str and (len(plate) > 6 and len(plate) < 9):
            splitedPlate = plate.split('-')
            if len(splitedPlate) == 2:
                if splitedPlate[1].isdigit():
                    result = True
                else:
                    result = False
            else:
                result = False
        else:
            result = False
        return result
