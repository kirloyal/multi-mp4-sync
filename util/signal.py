
import sys
import os
import numpy as np
import scipy

class MySignal:
	# x, t0, f
	def __init__(self, *args, **kwargs):
		self.x = kwargs['x'] 
		self.f = kwargs['f'] 

		if 't0' in kwargs.keys():
			self.t0 = kwargs['t0']
		else:
			self.t0 = 0

	def getLength(self):
		return self.x.size

	def getTEnd(self):
		return self.t0 + (self.x.size - 1.0)/self.f

	def getTimeAxis(self):
		return np.linspace(self.t0, self.getTEnd(), num=self.x.size)

	def shiftSample(self, nShift):
		self.t0 = self.t0 + float(nShift)/self.f
		

	# def removePadding(self):
	# 	xNew = self.x[:-self.padding]
	# 	tNew = self.t[:-self.padding]
	# 	return Signal(x=xNew, t=tNew, nShift=self.nShift)

	# def shiftSample(self, nShift):
	# 	tShift = self.t[nShift]
		
	# 	# padding zero from 0 sec
	# 	tNew = np.linspace(self.t[0], self.T + tShift, num = self.t.size + nShift)
	# 	xNew = np.pad(self.x, (nShift, 0), 'constant', constant_values = 0)

	# 	return Signal(x=xNew, t=tNew, padding = self.padding, nShift=self.nShift+nShift)


	# def riseUnit(self):
	# 	dec = len(str(self.l))
	# 	if dec > 2:
	# 		# lTarget = (int(self.l/np.power(10,dec-2))+1) * np.power(10,dec-2)
	# 		den = np.power(10,dec-2)
	# 		pre = np.ceil(self.l/den)
	# 		candidate = np.array([16,20,40,80,100])
	# 		preTarget = candidate[np.where(pre <= candidate)[0][0]]
	# 		lTarget = preTarget * den
			
	# 		return self.setLength(lTarget)			
		
	# def zeropadding(self, nPadding):
	# 	tTTarget = self.T + nPadding/self.f
	# 	tExt = np.linspace(self.T, tTTarget, num=nPadding+1)[1:]
	# 	tNew = np.concatenate((self.t, tExt))
	# 	xNew = np.pad(self.x, (0, nPadding), 'constant', constant_values = 0)
	# 	return Signal(x=xNew, t=tNew, padding = self.padding + nPadding)
	
	# def setLength(self, lTarget):
	# 	if lTarget <= self.l:
	# 		return Signal(x=self.x[:lTarget], t=self.t[:lTarget], padding = self.padding - (self.l - lTarget))
	# 	else:
	# 		lExt = lTarget - self.l
	# 		return self.zeropadding(lExt)
			

# class Signal:
# 	# x, t, l, T, f, padding, tShift, nShift
# 	# x, t0, f
# 	def __init__(self, *args, **kwargs):
# 		self.x = kwargs['x'] 
# 		self.l = self.x.size
# 		if 't' in kwargs.keys():
# 			self.t = kwargs['t']
# 			self.T = self.t[-1]
# 			self.f = (self.l - 1.0)/(self.T - self.t[0])
# 		elif 'f' in kwargs.keys(): 
# 			self.f = kwargs['f'] 
# 			self.T = (self.l - 1.0)/self.f
# 			self.t = np.linspace(0, self.T, num=self.l)
			
# 		if 'padding' in kwargs.keys():
# 			self.padding = kwargs['padding']
# 		else:
# 			self.padding = 0

# 		if 'tShift' in kwargs.keys():
# 			self.tShift = kwargs['tShift']
# 			self.nShift = self.f * self.tShift
# 		elif 'nShift' in kwargs.keys():
# 			self.nShift = kwargs['nShift']
# 			self.tShift = self.nShift/self.f
# 		else:
# 			self.nShift = 0
# 			self.tShift = 0.

# 	def removePadding(self):
# 		xNew = self.x[:-self.padding]
# 		tNew = self.t[:-self.padding]
# 		return Signal(x=xNew, t=tNew, nShift=self.nShift)

# 	def shiftSample(self, nShift):
# 		tShift = self.t[nShift]
		
# 		# padding zero from 0 sec
# 		tNew = np.linspace(self.t[0], self.T + tShift, num = self.t.size + nShift)
# 		xNew = np.pad(self.x, (nShift, 0), 'constant', constant_values = 0)

# 		return Signal(x=xNew, t=tNew, padding = self.padding, nShift=self.nShift+nShift)


# 	def riseUnit(self):
# 		dec = len(str(self.l))
# 		if dec > 2:
# 			# lTarget = (int(self.l/np.power(10,dec-2))+1) * np.power(10,dec-2)
# 			den = np.power(10,dec-2)
# 			pre = np.ceil(self.l/den)
# 			candidate = np.array([16,20,40,80,100])
# 			preTarget = candidate[np.where(pre <= candidate)[0][0]]
# 			lTarget = preTarget * den
			
# 			return self.setLength(lTarget)			
		
# 	def zeropadding(self, nPadding):
# 		tTTarget = self.T + nPadding/self.f
# 		tExt = np.linspace(self.T, tTTarget, num=nPadding+1)[1:]
# 		tNew = np.concatenate((self.t, tExt))
# 		xNew = np.pad(self.x, (0, nPadding), 'constant', constant_values = 0)
# 		return Signal(x=xNew, t=tNew, padding = self.padding + nPadding)
	
# 	def setLength(self, lTarget):
# 		if lTarget <= self.l:
# 			return Signal(x=self.x[:lTarget], t=self.t[:lTarget], padding = self.padding - (self.l - lTarget))
# 		else:
# 			lExt = lTarget - self.l
# 			return self.zeropadding(lExt)
# 			