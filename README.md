Dynamic Traffic Controll System for Ambulanced Clearance

We use the traffic Cam video mounted at each junction and count the traffic density using OpenCv. We set the timer accordingly for a single loop. The timer will be updated for every loop such that efficient clearence of vehicle is possible. In case an Emergency vehicle approaches the junction we pull the green light from the current lane and give it to the Emergency Vehicle's side. We detect the the emergency vehicle(in this case an ambulance) using YOLOV7 which at currently holding an accuracy of 84%.
You can find the code for YOLOV7 in the .zip file and OpenCV code at ambulance.2.py
