import time
import sys
import threading
from PyQt5.QtCore import pyqtSignal, QThread, QMutex
from Lib.IRSensor import IRsensor
from Lib.ServoMotor import ServoMotor
from Lib.StepperMotor import StepperMotor
from Lib.VL53L3CX_TofSensor import TofSensor
from Lib.horizontal_tof import Horizontal_TOF 
from Lib.LimitSwitch import LimitSwitch
from Lib.DcMotor import DcMotor
from Lib.DCEncoder import *
from Lib.timer import TimerCount



class System(QThread):
    """
    Contains all the function of the motor, sensor, gripper
    """

    # def push_start_button(self):
    #     pass

    def __init__(self):
        # TODO 需要填入pin 的 number
        super().__init__(self)
        self.clock = TimerCount(120)
        self.servo_G = ServoMotor()
        self.servo_H = ServoMotor()
        self.stepper_motor_vertical = StepperMotor()
        self.DC_transverse = DcMotor()
        self.DC_rotate = DcMotor()
        self.ir_sensor = IRsensor()
        self.DC_encoder = DCEncoder()
        self.Tof_sensor_vertical = TofSensor()
        self.horizontal_tof = Horizontal_TOF()
        self.Tof_sensor_horizontal = TofSensor()
        self.limit_switch_gripper = LimitSwitch()
        #self.limit_switch_start = LimitSwitch()

        # 额外的参数
        self.arm_length = 0  # 手臂伸出的长度
        self.start_length = 0  # TODO 手臂的初始长度

    def rotate_arm(self):
        self.DC_rotate.turn_forward()
    # 伸出机械臂
    def extend_arm(self):
        # ??不确定怎么让servo 推着rack往前走
        self.servo_H.act(self.arm_length)
        self.arm_length += 1

    def reset_arm(self):
        self.arm_length = 0
        

    # 收回手臂
    # TODO 机器测试的时候，测量机械臂的初始长度对应的舵机角度
    def retract_arm(self):
        # ?? 反转180回来
        self.servo_H.act(180)


    # 关闭爪子
    # TODO 角度可能要改
    def close_gripper(self):
        self.servo_G.act(0)
        
    def release_gripper(self):
        #TODO 需要明白servo_angle
        self.servo_G.act(180)

    # TODO 一点一点的转Stepper
    def lift_arm(self):
        self.stepper_motor_vertical.act(steps=10)

    # TODO 不确定怎么放机械臂
    def lower_arm(self):
        # 不确定是不是正反转90 可以
        self.stepper_motor_vertical.act()

    def move_backward_arm(self):
        # 这里收回胳膊是靠servo_H.反转180收回去?
        self.servo_H.act(180)

    def vertical_height(self):
        # TODO 可能需要对 TOFSensor的读数进行处理，让它以 cm 为单位
        height = self.Tof_sensor_vertical.read_data()
        '''对 height 的处理'''
        return height

    def horizontal_distance(self):
        # TODO 可能需要对 TOFSensor的读数进行处理，让它以 cm 为单位
        distance = self.Tof_sensor_horizontal.read_data()
        '''对 height 的处理'''
        return distance

    def reach_end(self):
        # ?要不在10cm 处停下来？
        if self.tof_sensor_distance() < 10:
            self.DC_transverse.turn_off()

    # TODO 0.1的移动时间可能需要修改
    def move_forward(self):
        self.DC_transverse.turn_forward()
        time.sleep(0.1)
        self.DC_transverse.turn_off()

    def move_backword(self):
        # 直接DC transverse 反转回去
        self.DC_transverse.turn_backward()

    def ir_sensor_find_package(self):
        return self.ir_sensor.read_data()

    def release_package(self):
        #ir 读数<10cm
        if self.ir_sensor.read_data() == 0:
        # TODO servo_G转多少?
            self.servo_G.act(180)



