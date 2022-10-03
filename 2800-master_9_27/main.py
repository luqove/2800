import RPi.GPIO as GPIO
import time
from sys_lib import *
from PyQt5.QtCore import pyqtSignal,QThread,QMutex
from Lib.servo_motor import servo_motor


class state:
    def LimitSwitch_closed(self):
        pass
    
    def Rotate_arm(self):
        pass
    
    def Extend(self):
        pass
    
    def Secure_package(self):
        pass
    
    def Retract_arm(self):
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
            
                
                
                
                
                
                
            
                
                
                
            
            
            
            
        
        
        