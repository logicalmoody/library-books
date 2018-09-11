#!/usr/bin/env python

import RPi.GPIO as GPIO
import SimpleMFRC522

reader = SimpleMFRC522.SimpleMFRC522()

def read():
	try:
			id = reader.read()
			# print(id)
			return id
	except:
		print("failed")
	finally:
			GPIO.cleanup()
