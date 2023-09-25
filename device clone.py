import smtplib
import os

class Device:
    def __init__(self):
        self.is_turned_on = False
        self.block_network = False
        self.data = ""

    def turn_on(self):
        self.is_turned_on = True
        print("Device has been turned on.")

    def turn_off(self):
        self.is_turned_on = False
        self.block_network = False
        print("Device has been turned off.")

    def block_outgoing_communication(self):
        self.block_network = True
        print("Outgoing communication with the network has been blocked.")

    def send_data(self, data):
        self.data += data
        if self.block_network:
            print("Outgoing communication with the network is blocked.")
        else:
            # send data over the network
            print(f"Sending data: {data}")

    def compile_data(self, filename):
        with open(filename, 'w') as file:
            file.write(self.data)
        print(f"Data has been written to {filename}.")

    def send_email(self, recipient, subject, filename):
        try:
            server = smtplib.SMTP("smtp.gmail.com", 587)
            server.ehlo()
            server.starttls()
            server.login("youremail@gmail.com", "yourpassword")
            with open(filename, 'r') as file:
                msg = file.read()
            message = f"Subject: {subject}\n\n{msg}"
            server.sendmail("youremail@gmail.com", recipient, message)
            print("Email sent successfully.")
        except Exception as e:
            print(f"Error sending email: {e}")

device = Device()

# Turn the device on
device.turn_on()

# Add some data
device.send_data("Important data 1\n")
device.send_data("Important data 2\n")

# Block outgoing communication with the network
device.block_outgoing_communication()

# Try to send data
device.send_data("Important data 3\n")

# Compile data into a file
device.compile_data("device_data.txt")

# Send the data to an email address
device.send_email("recipient@email.com", "Device Data", "device_data.txt")

# Turn the device off
device.turn_off()
