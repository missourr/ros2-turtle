#!/usr/bin/env python3
import rclpy, time
from rclpy.node import Node
from std_msgs.msg import String
from geometry_msgs.msg import Twist

class TurtleCommander(Node):
    def __init__(self):
        super().__init__('turtle_commander')
        self.sub = self.create_subscription(String, 'shape_command', self.callback, 10)
        self.pub = self.create_publisher(Twist, '/turtle1/cmd_vel', 10)
    
    def move(self, linear, angular, steps=20, dt=0.1): 
        t = Twist()
        for _ in range(steps):
            t.linear.x = float(linear)
            t.angular.z = float(angular)
            self.pub.publish(t)
            time.sleep(dt)
        self.pub.publish(Twist())
    
    def callback(self, msg):
        if msg.data == "spiral": self.spiral()
        elif msg.data == "star": self.star()
        elif msg.data == "pentagon": self.pentagon()
        elif msg.data == "stop": self.stop()
    
    def spiral(self):
        for i in range(1, 20):  
            self.move(i*.2, 1, 10) 
    
    def star(self):
        for _ in range(5):
            self.move(1, 0, 20)      
            self.move(0, 2.51, 10)  
    
    def pentagon(self):
        for _ in range(5):
            self.move(1, 0, 20)      
            self.move(0, 2.51, 5)  

    def stop(self):
        self.get_logger().info("Stopping turtle.")
        self.pub.publish(Twist())

def main():
    rclpy.init()
    rclpy.spin(TurtleCommander())
    rclpy.shutdown()

if __name__ == "__main__": 
    main()