# **IoT Smart Surveillance Robot**

## **Overview**
In today's world, video surveillance is indispensable for enhancing safety. However, the limitations of stationary systems led us to conceptualize a more mobile solution. We've developed A remotely-controlled robot car, enhanced with a camera. It employs machine learning to detect objects and people, sending this data to the user through an intuitive web interface.

## **Key Functionalities** 
- **Remote Access:** Operate and view from any networked device.
- **Advanced Steering:** Direct the robot's trajectory and speed via the web interface.
- **Camera Flexibility:** Adjust camera angles (pan/tilt) remotely.
- **Live Feed:** Real-time camera visuals accessible through the web, with integrated object detection.
- **Advanced Detection:** Recognizes people and over 80 unique objects seamlessly.

## **Web Features**
- **Home:** Showcases the brand and essence of the robot.
- **About:** Dive deep into the robot's capabilities.
- **Control Panel:** A user-friendly interface for robot and camera controls, including a live feed.
- **Object Detection Mode:** Activate live feed with object detection for enhanced surveillance.

## **Motivation Behind The Project**
The rise of AI in everyday technologies, especially in the realm of security and transport, signals an era of unprecedented advancements. Today, modern automobiles are leveraging object detection to enhance safety, avoid collisions, and even pave the way for autonomous driving. With this backdrop, understanding and innovating within the sphere of surveillance technology is more than just a personal passion—it's a glimpse into the future. This project not only seeks to address limitations in contemporary surveillance systems but also aspires to contribute to the evolving landscape of AI-powered solutions, setting a foundation for the next wave of technological innovations.

## **Challenges & Solutions**
**Website Development & Hosting:**

- Migration to React: Initially began with Node.js and HTML but transitioned to React, altering our approach to server hosting and port assignment. Found a solution by directly writing the port number to the JSON package file.

- URL Redirection: Struggled with linking React.js files and thought of using Node.js for redirection. Initially used localhost for redirection. Overcame this challenge by leveraging react-router, transitioning fully to a React-based website.

- Server Memory Reduction: React.js's significant memory usage reduced available server space. Tried clearing the cache and inadvertently removed critical bin files, causing errors. Resolved by restoring the files and executing clean and update commands on Linux.

**Object Detection/Video Streaming Issues:**

- OpenCV Dependency: Encountered challenges installing the OpenCV library and its dependencies. After intensive efforts, we managed to get OpenCV functioning without errors.

- Camera Device Error: Encountered a "camera device not found" error. Fixed by using “/dev/video0” in the cv2.VideoCapture() function.

- Latency and Power Issues: Noticed a degradation in video latency and robot malfunction. Traced the issue to battery overcurrent protection; resolved by using batteries without a protective board.

**Remote Control Issues:**

- Language Limitation: Python was mandatory for servo/motor controls. Integrated Django to call Python functions from embedded JavaScript in HTML.

- Page Refresh Challenge: The remote control webpage refreshed with each URL extension. We averted this by opening new tabs in the background with the necessary URL extensions.

## **Future Revisions** 
While we aimed for features like activity logs and custom ML implementations, time and resource constraints led to their deferral for future versions.

# **Website**

## **1. Front-end Technologies**
**React & CSS**: Powers the front-end. The `index.js` file outlines the web pages, drawing from other React files and react-router. The integration of JSX makes the design fluid, allowing for HTML within JavaScript.

## **2. Back-end Technologies**
**Node.js & React**: These technologies support the backend framework. We've set up the HTTP server with Node.js, redirecting default port numbers in React's JSON package file to port 80. IP-tables have been crucial for managing port conflicts.

## **3. Front-end Design and Implementation**
The design is crafted with the end-user in mind:
- **General Theme**: A soothing blue background paired with crisp white text.
- **Navigation**: Four accessible buttons - Home, About, Controller, and Object Detection.
- **Homepage**: Features an animated robot logo, styled through `Home.css`.

## **4. Back-end Design and Implementation**
Focusing on seamless navigation and functionality:
- **Page Connections**: Mapped out in `index.js` leveraging `react-dom` and `react-router-dom`.
- **Button Assignments**: Links are specified in `Layout.js`.
- **Content Display**: For instance, `About.js` presents insights and imagery.

# **IoT and Object Detection**

## **1. IoT to Back-end Communication**
Driving the IoT control through a Django app:
- **Django & Python**: Django harnesses Python, pivotal for controlling WALL-E via the `picar` Python library.
- **Flow**: The layout is set in `control_website.html`. Actions from users update the URL (like `"/drive_forward"`), and corresponding backend functions in `views.py` are triggered.

## **2. Machine Learning Dataset**
**COCO Dataset**: The COCO 2017 dataset refines our ML capabilities, detecting a myriad of objects. The object classifications can be explored at COCO Classes.

## **3. ML Model Design, Training, and Implementation**
- **Model**: Leveraging the Efficient-Det Lite 0 from TensorFlow.
- **Execution**: Main object detection coding resides in `ObjStreamFinal.py` within the `cam_stream+obj_det` directory. The camera feed, processed with object detection insights, gets showcased via Flask.
- **Web Framework**: The "templates" directory holds the foundational HTML layouts.

## **4. Libraries Used**
- opencv
- flask
- utils
- argparse
- time
- sys
- Django

# **Links**

[View images of the robot](https://imgur.com/a/ByL4b0q)

[View video demo of the robot](https://imgur.com/a/Ll9a63I)

# **File Structure**

## **1. Video Streaming and Object Detection**
Directory: `/cam_stream+obj_det`
- `ObjStreamFinal.py`
- `StreamFinal.py`
- `templates/Index(obj)`
- `templates/Index.html`

## **2. Remote Control**
Directory: `/control_app`
- `views.py`
- `urls.py`
- `settings.py`
- `templates/control_website.html`

## **3. Website**
Directory: `/walle-se`
- `package.json`
- `/src`
