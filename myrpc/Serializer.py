# -*- coding: utf-8 -*-
"""
序列化和反序列化是rpc中比较重要的一环，涉及rpc的性能问题。好的序列化和反序列化工具具备数据小、速度快、
是否可读需要根据业务逻辑自己去确定。

一般需要在众多的序列化和反序列化框架中自己去根据业务逻辑去选择对应的序列化和反序列化框架。
"""


class ISerializer(object):
	"""
	[序列化接口]
	"""
	def put(data):
		raise NotImplementedError


class IDeserializer(object):
	"""
	反序列化接口
	"""
	pass


