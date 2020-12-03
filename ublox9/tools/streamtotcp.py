#!/usr/bin/env python3
'''
'''
import socket

class StreamToTCP:
	"""docstring for StreamToSocket"""
	def __init__(self, address, timeout=1):
		# super(StreamToSocket, self).__init__()
		self._socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		self._socket.settimeout(timeout)
		self._socket.connect(address)

	def read(self, amount=1) -> bytes:
		return self._socket.recv(amount)

	def write(self, data: bytes):
		return self._socket.send(data)

	def readline(self, amount=0) -> bytes:
		return self._socket.recv(amount)

	def close(self):
		self._socket.close()
