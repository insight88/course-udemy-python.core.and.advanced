class ObjectCounter:

    numberOfObjects = 0

    def __init__(self):
        ObjectCounter.numberOfObjects += 1

    # ? static function을 선언하는 방법
    @staticmethod
    def displayCount():
        print(ObjectCounter.numberOfObjects)


o1 = ObjectCounter()
o2 = ObjectCounter()

ObjectCounter.displayCount()
