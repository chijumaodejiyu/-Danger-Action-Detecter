#!/usr/bin/python
# -*- coding: UTF-8 -*-
import time
from modules.pca9685 import PCA9685
import threading

pwm = PCA9685(0x40, debug=True)  # 对象初始化，指定IIC地址
pwm.setPWMFreq(50)  # 设置PWM的频率
thread_lock = threading.Lock()  # 全局线程锁
thread_exit = False  # 定义全局变量thread_exit,标志主线程退出，初始化False


class Servo:
    def __init__(self, cel):
        self.nextAngle = None
        self.cel = cel  # 通道设置
        self.deg = 0  # 舵机角度记忆
        self.time_stamp = round(time.time(), 3)  # 时间戳
        self.now_time = None
        print("舵机初始化时间" + str(self.time_stamp))
        pwm.set_servo_angle(cel, 90)  # 重置舵机

    def check(self, track_angle):
        if track_angle < 0 or track_angle > 180:
            print("超出角度限制")
            return False
        self.now_time = round(time.time(), 3)
        if self.now_time - self.time_stamp >= 0.050:  # 时间检测
            if abs(track_angle - self.deg) >= 2:  # 角度检测
                return True
            else:
                return False
        else:
            return False

    def run(self, angle):
        global thread_exit
        if self.check(angle):
            thread_lock.acquire()
            pwm.set_servo_angle(self.cel, angle)
            self.deg = angle
            thread_lock.release()

    def information(self):
        print(self.deg)
        print(self.time_stamp)


if __name__ == '__main__':
    test = Servo(0)
    test.information()
