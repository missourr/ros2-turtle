#!/usr/bin/env python3

import rclpy
from rclpy.node import Node
from std_msgs.msg import String
import threading


class ShapeNode(Node):
    def __init__(self):
        super().__init__("ShapeNode") #set up node with name
        self.publisher_ = self.create_publisher(String, 'shape_command', 10) #topic type and name and qeue size
        self.get_logger().info("ShapeNode started")
        self.input_thread = threading.Thread(target=self.get_shape_input) 
        self.input_thread.daemon = True
        self.input_thread.start()

    def get_shape_input(self):
        while rclpy.ok():
            try:
                shape = input("Choose a shape (spiral/star/pentagon/stop): ").strip().lower() #handle input, remove spaces, converts to lowercase
                if shape in ['spiral', 'star', 'pentagon', 'stop']:
                    msg = String()
                    msg.data = shape
                    self.publisher_.publish(msg)
                    self.get_logger().info(f"Published shape: {shape}") # Log the published shape
                    if shape == 'stop': # Stop the loop
                        break
                else:
                    self.get_logger().warn("Invalid shape! Choose: spiral, star, pentagon, or stop")
            except KeyboardInterrupt: # Handle Ctrl+C
                break

def main(args=None):
    rclpy.init(args=args)
    node = ShapeNode() #create node in main
    node.get_shape_input()  
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()

