import serial
import time

def send_gcode(gcode_command, ser):
    """Send a G-code command to the 3D printer."""
    ser.write((gcode_command + '\r\n').encode('utf-8'))  # send gcode
    time.sleep(0.1)  # give some time to process
    while ser.in_waiting:
        print(ser.readline().decode('utf-8').strip())  # print printer response

def main():
    port = '/dev/ttyUSB0'  # You might need to change this. On Windows, it might be COM3 or similar.
    baudrate = 115200  # default for many printers, but check your printer's settings
    
    with serial.Serial(port, baudrate, timeout=2) as ser:
        # Optionally: Give the printer a bit of time to initialize after opening the port
        time.sleep(2)

        # For this example, we'll home the printer and then move the X-axis to position 50
        send_gcode("G28", ser)  # home all axes
        time.sleep(3)
        send_gcode("G28", ser)
        send_gcode("G1 X50 F1200", ser)  # move X to 50 at speed of 1200mm/min

if __name__ == "__main__":
    main()

