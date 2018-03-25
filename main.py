import random

class Ascenseur():

    def __init__(self):
        self.__floor_resisstance = random.randint(1, 20)
        print("Ressistance: " + str(self.__floor_resisstance))

    def determine_method(self, min, max, elevator):
        #Condition a determiner plus precisement
        simple = 'simple'
        medium = 'medium'
        delta = max - min
        if elevator == 1 or delta <= 5:
            return True
        return False

    def is_broken(self, floor):
        if floor >= self.__floor_resisstance:
            return True
        return False

    def get_average(self, number1, number2):
        return int((int(number1) + int(number2)) / 2)

    def launch_elevator_simple_method(self, min, max):
        for i in range(min, max + 1):
            if self.is_broken(i):
                return i

    def crash_test(self, elevator, max, min=1):
        simple_method = self.determine_method(min, max, elevator)
        if simple_method:
            return self.launch_elevator_simple_method(min, max + 1)
        average = self.get_average(min, max)
        broken = self.is_broken(average)
        if broken:
            max = average - 1
            elevator -= 1
        else:
            min = average
        if min == max:
            return max
        return self.crash_test(elevator, max, min)



if __name__ == '__main__':
    max = Ascenseur().crash_test(4, 21)
    print('max floor: ' + str(max))
