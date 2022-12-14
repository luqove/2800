import time
from sys_lib import System
from PyQt5.QtCore import QThread, QMutex
from Lib.timer import TimerCount
from const import (IDLE, FIND_PACKAGE, CATCH_PACKAGE, LIFT_ARM,
                   START_TRANSVERSE, PUT_DOWN_PACKAGE, RETRACT_ARM,
                   BACK_TRANSVERSE_LIFT_ARM, BACK_TRANSVERSE)
import RPi.GPIO as GPIO


class ConveyorSys(QThread):
    Conv_mutex = QMutex()

    def __init__(self):
        super(ConveyorSys, self).__init__()
        self.state = IDLE
        self.system = System()

    def start_timer(self):
        self.timer = TimerCount(120)
        self.timer.timer_signal.connect(self.return_IDLE)
        self.timer.start()

    def return_IDLE(self):
        self.Conv_mutex.lock()
        self.state = IDLE
        self.Conv_mutex.unlock()

    # TODO 状态机伪代码先写
    # TODO 明确要实现的功能，再回到sys_lib去一步步实现
    def run(self):
        while not self.isInterruptionRequested():
            # 
            #if self.state == IDLE:
            #    #start_time = time.time()
            #    # TODO 按钮返回>0?
            #    while(self.system.limit_switch_start.get_read()>0):
            #        time.sleep(0.5)
            #        #if time.time()-start_time<2:
            #        #    break 

            #    self.Conv_mutex.lock()
            #    self.state = FIND_PACKAGE
            #    self.Conv_mutex.unlock()

            # 
            ##TODO 因为目前没有Find pakcage
            #if self.state == FIND_PACKAGE:
            #    # 
            #    while self.system.ir_sensor_find_package()> 0:
            #        # self.state = CATCH_PACKAGE
            #        time.sleep(0.1)
            #        self.system.rotate_arm()
            #    #if self.timer.time > 120:
            #    #    self.state = IDLE
            #    self.state = CATCH_PACKAGE

            # 
            if self.state == CATCH_PACKAGE:
                # 当Limit switch 关闭的时候
                # TODO 如果第一次爪子没抓住，要缩回，再重新抓，这里尚未实现
                while self.system.limit_switch_gripper.get_read() <= 0:
                    self.system.extend_arm()
                #self.system.reset_arm()
                self.system.close_gripper()
                time.sleep(0.5)
                self.system.retract_arm()
                time.sleep(2)
                self.state = LIFT_ARM

            # 升起手臂
            elif self.state == LIFT_ARM:
                # 当垂直方向 TOFSensor 反馈的高度符合预期
                start_time = time.time()
                # 
                #while self.system.vertical_height() < 20:
                    # 
                self.system.lift_arm()
                if time.time()-start_time > 8:
                    break

                self.state = START_TRANSVERSE

            # 
            elif self.state == START_TRANSVERSE:
                while self.system.horizontal_distance() < 10:
                    self.system.move_forward()

                self.state = PUT_DOWN_PACKAGE


            # 放下包裹
            elif self.state == PUT_DOWN_PACKAGE:
                # 
                self.system.lower_arm()
                time.sleep(0.5)
                self.system.arm_reach_end()
                self.system.release_gripper()
                time.sleep(1)
                self.state = RETRACT_ARM

            # 
            elif self.state == RETRACT_ARM:
                self.system.retract_arm()
                #TODO
                time.sleep(1)
                self.state = BACK_TRANSVERSE_LIFT_ARM

            # 
            elif self.state == BACK_TRANSVERSE_LIFT_ARM:
                self.system.lift_arm()
                time.sleep(2)
                while self.system.vertical_height()<20:
                    self.system.lift_arm()
                self.state = BACK_TRANSVERSE

            # 
            elif self.state == BACK_TRANSVERSE:
                self.system.move_backword()
                    




