# -*- coding: utf-8 -*-
"""
单例模式.
* 饿汉和懒汉单例
* 线程安全
"""

import sys


class SingletonClass(object):
	def __new__(klass, *args, **kwargs):
		if not klass.isInited():
			klass._instance = object.__new__(klass)
			try:
				klass._instance.init(*args, **kwargs)
			except Exception:
				sys.excepthook(*sys.exc_info())
		return klass._instance

	@classmethod
	def isInited(klass):
		return "_instance" in klass.__dict__

	def init(self):
		pass
