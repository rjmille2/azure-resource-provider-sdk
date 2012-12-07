import untangle
import os
from clint.textui import colored, puts, indent
import sys
import uuid

def die(message=None):
	sys.exit(message) if message else sys.exit(0)

def generate_etag():
	return str(uuid.uuid1())

class Printer:
	@staticmethod
	def start_test(message):
		print(
"""
%s
""" % message
			)

	@staticmethod
	def warn(message):
		with indent(4):
			puts(colored.yellow("[WARN] %s" % message))

	@staticmethod
	def error(message):
		with indent(4):
			puts(colored.red("[FAIL] %s" % message))

	@staticmethod
	def info(message):
		with indent(4):
			puts(colored.white("[INFO] %s" % message))

	@staticmethod
	def success(message):
		with indent(4):
			puts(colored.green("[PASS] %s" % message))