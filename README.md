# speeding-vehicle-identifier
**EECS149 Final Project Repository**

**Branch of Romi Speed Setting**



The implementation of Romi utilizes multiple laboratory techniques as an organic whole.

![Speed Control Architectur](D:\0认真学习\UCB课程\EE149\EE149 Lab\149Project\Speed Control Architectur.png)

In Lab 5, we calculated the tilt from acceleration and took it as feedback to adjust the wheel speeds. In Lab 4, we estimated the distance from the encoder. Our speed-setting methodology is a combination of these two. The speed is obtained from distance while adjusting itself dynamically via a PID controller.

![FSM (1)](D:\0认真学习\UCB课程\EE149\EE149 Lab\149Project\FSM (1).PNG)

The Speed Calibration reactor transforms the speed from the parameters of `romi_drive_direct` to real-life speed, which is intended to be integrated with other parts of the
project.

The BLE taught in Lab 6 was applied to take the place of `scanf`. The data flow among files is illustrated in the figure below. The number read from keyboard indicates the speed level. There are 4 levels in total, 0 for staying still, 1 for 30 cm/s , 2 for 60 cm/s, etc. Level 2 is considered as normal speed while Level 3 would be regarded as speeding in our speeding recognition model.

![Dataflow.drawio](https://github.com/anthony-villegas/speeding-vehicle-identifier/blob/Romi/images/Dataflow.png)
