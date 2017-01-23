from tkinter import *

class Application(Frame):
	"""docstring for Application"""
	def __init__(self, master):
		super(Application, self).__init__(master)
		self.grid(row=2,column=2)
		self.create_widgets()


	def create_widgets(self):
		self.lbl_path_utc = Label(self, text = 'введите ip адресс ')
		self.lbl_path_utc.grid(row=2,column=0,columnspan=4,sticky=W)
		self.ent_utc = Entry(self,width = 55)
		self.ent_utc.grid(row = 3, column = 0,columnspan=2,sticky = W)

		self.lbl_uname = Label(self, text = 'имя пользователя:')
		self.lbl_uname.grid(row=4,column=0,columnspan=4,sticky=W)
		self.ent_uname = Entry(self,width = 55)
		self.ent_uname.grid(row = 5, column = 0,columnspan=2,sticky = W)
		
		self.ok_bttn = Button(self, text = "Start", command = self.findUser)
		self.ok_bttn.grid(row = 15, column = 0, sticky= W)

	def findUser(self):
		import FindIp
		fp = FindIp.Run_command(self.ent_utc.get())

		self.ent_uname.insert(0, fp)

root = Tk()
root.title("FindUser")
root.geometry("500x150")
app = Application(root)
root.mainloop()
# output[0]