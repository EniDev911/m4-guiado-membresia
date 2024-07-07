from abc import ABC, abstractmethod

class Membresia(ABC):
	"""docstring for Membresia"""
	def __init__(self, arg):
		super(Membresia, self).__init__()
		self.arg = arg
		

class Basico(object):
	"""docstring for Basico"""
	def __init__(self, arg):
		super(Basico, self).__init__()
		self.arg = arg

class Familiar(object):
	"""docstring for Familiar"""
	def __init__(self, arg):
		super(Familiar, self).__init__()
		self.arg = arg
		

class SinConexion(object):
	"""docstring for SinConexion"""
	def __init__(self, arg):
		super(SinConexion, self).__init__()
		self.arg = arg

class Pro(object):
	"""docstring for Pro"""
	def __init__(self, arg):
		super(Pro, self).__init__()
		self.arg = arg
