import RPi.GPIO as GPIO
import time
from sys_lib import *
from PyQt5.QtCore import pyqtSignal,QThread,QMutex
from Lib.servo_motor import servo_motor



class LimitSwitch_closed(QThread):
    Pass
    
    
class Rotate_arm(QThread):
    pass
    
class Extend(self):
    pass
class Secure_package(self):
    pass

class Retract_arm(self):
        pass
    
    
class MainSystem(QThread):
    """the main logic for the system"""
    
    signal = pyqtSignal(str)
    value = pyqtSignal(int)
    
    def __init__(self):
        super(MainSystem,self).__init()
        self.system = System()
        
    def run(self):
        while True:
            if state == LimitSwitch_closed:
                state == rotate_arm
                
            if state == rotate_arm:
                pass
            
                
                
if __name__ == "main":
    print(1)
    print('1')
    

                
                
                
            
                
                
                
            
            
            
            
        
        
        