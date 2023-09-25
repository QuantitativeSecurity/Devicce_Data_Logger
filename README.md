Device Data Logger and Emailer

This script simulates a device that can log data, block outgoing communication, and send the logged data via email.
Description

The Device class represents a device with the following functionalities:

    Turning the device on and off.
    Blocking outgoing communication with the network.
    Logging and sending data.
    Compiling the logged data into a file.
    Sending the compiled data to an email address.

Requirements

    Python 3.x
    smtplib library (included in the Python standard library)

Usage

    Setup:
        Replace youremail@gmail.com and yourpassword with your Gmail email and password.
        Replace recipient@email.com with the recipient's email address.
        Ensure that you have enabled "less secure apps" in your Gmail settings to allow sending emails through the script. Learn more.

    Run the script:

    bash

    python3 device_logger_emailer.py

    Expected Output:
        The script will simulate turning the device on, logging some data, blocking outgoing communication, attempting to send data while communication is blocked, compiling the logged data into a file, sending the compiled data via email, and finally turning the device off.

Note

    This script is a simulation and does not interact with real devices or networks.
    Be cautious when embedding email credentials in scripts. Consider using environment variables or other secure methods to store sensitive information.
    Ensure you have the necessary permissions and are not violating any terms of service when sending emails.
