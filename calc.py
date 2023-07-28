#!/usr/bin/python3

from tkinter import *
from tkinter import ttk
root = Tk()

def add(op1, op2):
	return op1 + op2

def subtract(op1, op2):
    return op1 - op2

def multiply(op1, op2):
	return op1 * op2

def divide(op1, op2):
	return op1 / op2

def assign(op1, op2):
	return op2

def numberKey(num):
	clearError()
	val = (calcState.getEntryValue() * 10) + num
	calcState.setEntryValue(val)

def opKey(op):
	clearError()
	try:
		calcState.operand1 = calcState.operator(calcState.operand1, calcState.getEntryValue())
	except ZeroDivisionError:
		displayError("Divide by zero")
		return

	calcState.setEntryValue(0)
	calcState.operator = op

def equalKey():
	clearError()
	try:
		calcState.operand1 = calcState.operator(calcState.operand1, calcState.getEntryValue())
	except ZeroDivisionError:
		displayError("Divide by zero")
		return

	calcState.setEntryValue(calcState.operand1)
	calcState.operand1 = 0
	calcState.operator = assign

def clearKey():
	clearError()
	calcState.operand1 = 0
	calcState.operator = add
	calcState.setEntryValue(0)

def clearEntryKey():
	clearError()
	calcState.setEntryValue(0)

def createEntryField(frame, fieldVar, validateFn):
	entry = ttk.Entry(frm, textvariable = fieldVar)
	entry.grid(column=0,row=0,columnspan = 2, sticky = W+E)	
	vcmd = (frame.register(validateFn), '%P')
	entry.config(validate="key", validatecommand=vcmd)

def createButtons(frame):
    ttk.Button(frame, text="C", command=clearKey              ).grid(column=0, row=1)
    ttk.Button(frame, text="CE",command=clearEntryKey         ).grid(column=1, row=1)
    ttk.Button(frame, text="/", command=lambda:opKey(divide)  ).grid(column=3, row=1)
    ttk.Button(frame, text="*", command=lambda:opKey(multiply)).grid(column=3, row=2)
    ttk.Button(frame, text="-", command=lambda:opKey(subtract)).grid(column=3, row=3)
    ttk.Button(frame, text="+", command=lambda:opKey(add)     ).grid(column=3, row=4)
    ttk.Button(frame, text="=", command=equalKey              ).grid(column=3, row=5)
    ttk.Button(frame, text=".", command=equalKey              ).grid(column=2, row=5)
    createNumKeys(frame,2)

def createNumKeys(frame, rowOffset):
	for i in range(9):
		row = (i//3) + rowOffset
		col = 2 - (i % 3)
		ttk.Button(frame, text=str(9-i), command=lambda x=i:numberKey(9-x)).grid(column=col, row=row)
	ttk.Button(frame, text="0", command=lambda:numberKey(0)).grid(column=1, row=3+rowOffset)
   
def validateEntryField(value):
	try:
		float(value)
		clearError()
		return True
	except:
		return False

def createErrorLabel(frame):
	label = Label(frame, bg = "#F00")
	return label

def displayError(msg):
	calcState.errorLabel.config(text=msg)
	calcState.errorLabel.grid(column=2, row=0, columnspan = 2, sticky = W+E)

def clearError():
	calcState.errorLabel.grid_remove()

class CalcState:
	def __init__(self):
		self.operator = add
		self.operand1 = 0
		self.entryString = StringVar()
		self.setEntryValue(0)

	def getEntryValue(self):
		return float(self.entryString.get())

	def setEntryValue(self,val):
		self.entryString.set(str(float(val)))

calcState = CalcState()
root.title("World's Best Calculator")
frm = ttk.Frame(root, padding=10)
frm.grid()

calcState.errorLabel = createErrorLabel(frm)
createEntryField(frm, calcState.entryString, validateEntryField)
createButtons(frm)

root.mainloop()
