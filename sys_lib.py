import time
import sys
import threading
from PyQt5.QtCore import pyqtSignal, QThread, QMutex
from Lib.IRSensor import IRsensor
from Lib.ServoMotor import ServoMotor
from Lib.StepperMotor import StepperMotor
from Lib.horizontal_tof import Horizontal_TOF 
from Lib.LimitSwitch import LimitSwitch
from Lib.DcMotor import DcMotor
from Lib.DCEncoder import DCEncoder
from Lib.timer import TimerCount
from gpiozero import Servo
from const import *


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
        self.servo_G = Servo(Servo_G_pin)
        self.servo_H = Servo(Servo_H_pin)
        self.stepper_motor_vertical = StepperMotor(stepper_motor_vertical_pin)
        self.DC_transverse = DcMotor(DC_transverse_pin)
        self.DC_rotate = DcMotor(DC_rotate_pin)
        self.ir_sensor = IRsensor(ir_sensor_pin)
        self.DC_encoder = DCEncoder(DC_encoder_pin1, DC_encoder_pin2)
        self.Tof_sensor_vertical = TofSensor()
        self.horizontal_tof = Horizontal_TOF()
        self.Tof_sensor_horizontal = TofSensor()
        self.limit_switch_gripper = LimitSwitch(limit_switch_gripper_pin)

        # 额外的参数
        self.arm_length = 0  # 手臂伸出的长度
        self.start_length = 0  # TODO length

    def rotate_arm(self):
        self.DC_rotate.turn_forward()

    # 伸出机械臂
    def extend_arm(self):
        # ??不确定怎么让servo 推着rack往前走
        self.servo_H.value(self.arm_length-1)
        self.arm_length += 0.01

    def reset_arm(self):
        self.arm_length = 0

    # 收回手臂
    # TODO angle
    def retract_arm(self):
        # ?? 反转180回来
        self.servo_H.value(-1)


    # 关闭爪子
    # # TODO 爪子松开对应的是 1 还是 0
    def close_gripper(self):
        self.servo_G.value(-1)
        
    def release_gripper(self):
        self.servo_G.value(1)

    # TODO Stepper
    def lift_arm(self):
        self.stepper_motor_vertical.act(steps=10)

    def lower_arm(self):
        # TODO 90?
        self.stepper_motor_vertical.act()

    def move_backward_arm(self):
        # TODO 180?
        self.servo_H.value(-1)

    def vertical_height(self):
        # TODO 可能需要对 TOFSensor的读数进行处理，让它以 cm 为单位
        height = self.Tof_sensor_vertical.read_data()
        '''对 height 的处理'''
        return height

    def horizontal_distance(self):
        # TODO start_measurement 怎么处理
        distance = self.horizontal_tof.start_measurement()
        '''对 height 的处理'''
        return distance

    def reach_end(self):
        # TODO 10cm?
        if self.horizontal_distance() < 10:
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

    # 机械臂
    def arm_reach_end(self):
        self.servo_H.max()
        # TODO 秒数
        time.sleep(2)
        

