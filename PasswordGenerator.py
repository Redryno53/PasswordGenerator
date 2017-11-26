#! /usr/bin/python

import tkinter
from tkinter import messagebox
import random
import logging
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s') 
logging.disable(logging.DEBUG)

top = tkinter.Tk()
top.wm_title("Password Generator")

class MyApp():
	def __init__(self):
		logging.debug('Start of MyApp')
		self.Lower    = """abcdefghijklmnopqrstuvwxyz"""
		self.Upper    = """ABCDEFGHIJKLMNOPQRSTUVWXYZ"""
		self.Num      = """1234567890"""
		self.Sym      = """!@#$%^&*(),./<>?'";:"""
		self.startLen = 8
		self.LCalpha = tkinter.IntVar()
		CB1 = tkinter.Checkbutton(top, text='Lower Case Alpha', variable=self.LCalpha)
		CB1.grid(row=0, column=0, columnspan=2, pady=3, padx=10)
		CB1.select()
		self.UCalpha = tkinter.IntVar()
		CB2 = tkinter.Checkbutton(top, text='Upper Case Alpha', variable=self.UCalpha)
		CB2.grid(row=1, column=0, columnspan=2, pady=3)
		CB2.select()
		self.Numbers = tkinter.IntVar()
		CB3 = tkinter.Checkbutton(top, text='Numbers', variable=self.Numbers)
		CB3.grid(row=2, column=0, columnspan=2, pady=3)
		CB3.select()
		self.Symbols = tkinter.IntVar()
		CB4 = tkinter.Checkbutton(top, text='Symbols', variable=self.Symbols)
		CB4.grid(row=3, column=0, columnspan=2, pady=3)
		CB4.select()
		tkinter.Label(top, text='Length').grid(row=4, column=0, pady=3)
		self.Length = tkinter.Spinbox(top, from_=1, to=99, width=2)
		self.Length.grid(row=4, column=1, pady=3)
		self.Length.delete(0, tkinter.END)
		self.Length.insert(0, self.startLen)
		tkinter.Button(top, text='Generate', command=self.MakePW, background='light blue').grid(row=5, column=0, columnspan=2, pady=3)

	def MakePW(self):
		logging.debug('Start of MakePW')
		rndm = random.SystemRandom()
		y = ""
		x = ""
		if self.LCalpha.get() == 1:
			y = y + self.Lower
		if self.UCalpha.get() == 1:
			y = y + self.Upper
		if self.Numbers.get() == 1:
			y = y + self.Num
		if self.Symbols.get() == 1:
			y = y + self.Sym
		for i in range(0, int(self.Length.get())):
			x = x + rndm.choice(y)
		logging.info('Password = ' + x)
		top.clipboard_clear()
		top.clipboard_append(x)
		messagebox.showinfo("Password", "{}\n\nYour Password\nhas been coppied\nto the clipboard".format(x), icon="warning")

if __name__ == "__main__":
	try:
		top.after(100, MyApp)
		top.mainloop()
	except Exception:
		logging.critical('Critical error! Critical error!')
	finally:
		quit()
