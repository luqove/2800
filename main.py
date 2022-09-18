import RPi.GPIO as GPIO
import time
from sys_lib import *
from PyQt5.QtCore import pyqtSignal,QThread,QMutex

class MainSystem(object):
    """the main logic for the system"""
    def __init__(self):
        super(MainSystem,self).__init()
        self.system = System()
        
    def run(self):
        while True:
            self.system.push_start_button()
            self.system.extend_arm()
            
            if self.system.tof_sensor_distance < 30:
                self.system.close_arm()
            else:
                time.sleep(1)
            
            if self.system.limit_switch_closed:
                self.system.retract_arm()
            else:
                self.system.reset()
                
            if self.system.tof_sensor_distance()<30:
                self.system.lift_arm()
            
            if self.system.distance_correct_height:
                self.system.rotate_arm()
                self.system.move_forward_arm()
            else:
                self.system.reset()
            
            #determine whether reach the end
            if self.system.reach_end:
                self.system.lower_arm()
                
            if self.system.distance_correct_height:
                self.system.extend_arm()
                self.system.release_arm()
                
            if self.system.limit_switch_closed:
                self.system.retract_arm()

            if self.system.distance_correct_height:
                self.system.retract_arm()
                
            if self.system.tof_sensor_distance()<30:
                self.system.move_backword()
                
            if self.system.ir_sensor_distance:
                self.system.lower_arm()
                
                
                
                
            
                
                
                
            
            
            
            
        
        
        