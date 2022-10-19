from Lib.TMF8701_lib import DFRobot_TMF8701


class Horizontal_TOF(object):
    def __init__(self):
        self.horizontal_tof = DFRobot_TMF8701()


if __name__ == '__main__':
    sensor = Horizontal_TOF()
    #sensor.start_measurement()