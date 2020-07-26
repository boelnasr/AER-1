#include <Arduino.h>
#include <ros.h>
#include <Servo.h> 
#include <std_msgs/Bool.h>
#include <std_msgs/String.h>
#include <math.h>
#include <std_msgs/Int16.h>
#include <std_msgs/UInt16.h>
#include <AccelStepper.h>
#include <MultiStepper.h>
#define MOTOR_STEPS 200
#include <rospy_tutorials/Floats.h>
// Joint 1
#define E1_STEP_PIN        23
#define E1_DIR_PIN         24
#define E1_ENABLE_PIN      25
// Joint 2
#define E2_STEP_PIN        26
#define E2_DIR_PIN         27
#define E2_ENABLE_PIN     28
// Joint 3
#define E3_STEP_PIN        29
#define E3_DIR_PIN         30
#define E3_ENABLE_PIN       31
// Joint 4
#define E4_STEP_PIN        32
#define E4_DIR_PIN         33
#define E4_ENABLE_PIN     34
// Joint 5
#define E5_STEP_PIN        35
#define E5_DIR_PIN         36
#define E5_ENABLE_PIN     37
// Joint 6
#define E6_STEP_PIN        38
#define E6_DIR_PIN         39
#define E6_ENABLE_PIN        40   


AccelStepper joint1(1,E1_STEP_PIN, E1_DIR_PIN);
AccelStepper joint2(1,E2_STEP_PIN, E2_DIR_PIN);
AccelStepper joint3(1,E3_STEP_PIN, E3_DIR_PIN);
AccelStepper joint4(1,E4_STEP_PIN, E4_DIR_PIN);
AccelStepper joint5(1,E5_STEP_PIN, E5_DIR_PIN);
AccelStepper joint6(1,E6_STEP_PIN, E6_DIR_PIN);
MultiStepper steppers;
float joint_step[6];
int joint_status = 0;
ros::NodeHandle nh;
std_msgs::Int16 msg;
void arm_cb(const rospy_tutorials::Floats& cmd_msg){
  joint_status = 1;
  joint_step[0] = cmd_msg.data[0];
  joint_step[1] = cmd_msg.data[1];
  joint_step[2] = cmd_msg.data[2];
  joint_step[3] = cmd_msg.data[3];
  joint_step[4] = cmd_msg.data[4];
  joint_step[5] = cmd_msg.data[5]; 
}
ros::Subscriber<rospy_tutorials::Floats> arm_sub("joints_to_aurdino",arm_cb);
void setup() {
  // put your setup code here, to run once:

}

void loop() {
  // put your main code here, to run repeatedly:

  if (joint_status == 1) // If command callback (arm_cb) is being called, execute stepper command
  { 
    long positions[5];  // Array of desired stepper positions must be long
    positions[0] = joint_step[0]; // negated since the real robot rotates in the opposite direction as ROS
    positions[1] = joint_step[1]; 
    positions[2] = joint_step[2]; 
    positions[3] = joint_step[3]; 
    positions[4] = joint_step[4]; 
    positions[5] = joint_step[5];

    // Publish back to ros to check if everything's correct
    //msg.data=positions[4];
    //steps.publish(&msg);

    steppers.moveTo(positions);
    nh.spinOnce();
    steppers.runSpeedToPosition(); // Blocks until all are in position
    
  }
   
  nh.spinOnce();
  delay(1);

}
