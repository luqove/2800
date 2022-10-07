import time
import sys
import threading
from PyQt5.QtCore import pyqtSignal,QThread,QMutex
from Lib.IRSensor import IRsensor
from Lib.servo_motor_test import ServoMotor
from Lib.stepper_motor import StepperMotor
from Lib.TofSensor import TofSensor
from Lib.limit_switch import LimitSwitch
from Lib.DcMotor import DcMotor
from Lib.DCEncoder import DCEncoder



class System(QThread):
    """
    Contains all the function of the motor, sensor, gripper
    """

    # def push_start_button(self):
    #     pass

    def __init__(self):
        # TODO 需要填入pin 的number
        super().__init__(self)
        self.clock = Clock()
        self.servo_G = ServoMotor()
        self.servo_H = ServoMotor()
        self.limit_switch = LimitSwitch()
        self.stepper_motor_vertical =StepperMotor()
        self.DC_transverse = DcMotor()
        self.DC_rotate = DcMotor()
        self.ir_sensor = IRsensor()
        self.DC_encoder = DCEncoder()
        self.Tof_sensor = TofSensor()

        
        
###不知道encoder 怎么加进去
    def IDLE(self):
        # 闲置
        self.sleep()

    # 重置所有数据
    #def reset(self):
    #    pass

    # 安全打包，也就是抓取圆盘
    def secure_package(self):
        self.ir_sensor.read_data()<10
        self.start_gripper()
        
    def release_package(self):
        self.ir_sensor.read_data()<10
        #? 转多少可以不清楚
        self.servo_G.act(180)

    # 伸出机械臂
    def extend_arm(self):
        # ??不确定怎么让servo 推着rack往前走
        self.servo_H.act(90)

    def retract_arm(self):
        #?? 反转180回来
        self.servo_H.act(180)

    #伸出爪子抓取
    def start_gripper(self):
        # 60 degree? limit_switch需要被触发
        if self.limit_switch_closed():
            self.servo_G.act(60)
        
    # 关闭爪子
    def close_gripper(self):
        self.servo_G.act(0)
        self.limit_switch.SIG[int].connect(lambda: self.stop_gripper)
        self.limit_switch.start()

    # 停止关闭爪子
    def stop_gripper(self, limit_switch_value):
        if limit_switch_value < 1:
            # 停止舵机
            pass
            self.stop_listen_switch()

    def stop_listen_switch(self):
        pass

    def limit_switch_closed(self):
        #让limit switch run 触发?
        self.limit_switch.run()

    def lift_arm(self):
        self.stepper_motor_vertical.act(90,cw)
    
    def lower_arm(self):
        #不确定是不是正反转90 可以
        self.stepper_motor_vertical.act(90,ccw)
    
    def move_backward_arm(self):
        #这里收回胳膊是靠servo_H.反转180收回去?
        self.servo_H.act(180)
    
    def tof_sensor_distance(self):
        #这里几乎直接调read_data
        self.Tof_sensor.read_data()
        
    def distance_correct_height(self):
        pass
    
    def reach_end(self):
        #?要不在10cm 处停下来？
        if self.tof_sensor_distance()<10:
            self.DC_transverse.turn_off()
    
    def move_backword(self):
        #直接DC transverse 反转回去
        self.DC_transverse.turn_backward() 


# 定义一个多线程时钟
class Clock(threading):
    """
    根据输入的时间计时
    """
    def __init__(self, time_count):
        super(Clock, self).__init__()



