from pycreate2 import Create2
import sys
import time


def main(serial_device: str):
  bot = Create2(serial_device)

  bot.start()
  bot.safe()

  # # You are responsible for handling issues, no protection/safety in
  # # this mode ... becareful
  # bot.full()

  # # directly set the motor speeds ... move forward
  # bot.drive_direct(100, 100)
  # time.sleep(2)

  # # turn in place
  # bot.drive_direct(200, -200)  # inputs for motors are +/- 500 max
  # time.sleep(2)

  # # Stop the bot
  # bot.drive_stop()

  # # query some sensors
  # sensors = bot.get_sensors()  # returns all data
  # print(sensors.light_bumper_left)

  # # Close the connection
  # # bot.close()


if __name__ == "__main__":
  serial_port = sys.argv[1] if len(sys.argv) > 1 else "/dev/usbTTY0"
  main(serial_port)
