from kivy.app import App
from kivy.metrics import dp
from kivy.graphics.vertex_instructions import Rectangle
from kivy.uix.widget import Widget
from kivy.uix.button import Button

class mycanvas(Widget):
	def __init__(self,**kwargs):
		super().__init__(**kwargs)
		right = Button(text="right",pos=(20,100),size=(150,150))
		left = Button(text="left",pos=(200,100),size =(150,150))
		up = Button(text="up",pos=(380,100),size=(150,150))
		down = Button(text="down",pos=(560,100),size=(150,150))
		right.bind(on_press = self.right)
		left.bind(on_press = self.left)
		up.bind(on_press = self.up)
		down.bind(on_press = self.down)		
		
		self.add_widget(down)
		self.add_widget(up)
		self.add_widget(left)
		self.add_widget(right)
		
		with self.canvas:
			self.rectangle = Rectangle(pos=(200,700),size=(100,100))
		self.x,self.y = self.rectangle.pos
		self.w,self.h = self.rectangle.size
		self.inc = dp(10)
			
	def right(self,*args):
		if self.x + self.w > self.width-self.inc:
			self.rectangle.pos = (self.width-self.w,self.y)
		else:
			self.x += self.inc
			self.rectangle.pos = (self.x,self.y)
		
	
	def left(self,*args):
		if self.x < 0:
			self.rectangle.pos = (self.x,self.y)
		else:
			self.x -= self.inc
			self.rectangle.pos = (self.x,self.y)
		
	
	def up(self,*args):
		if self.y + self.h > self.height-self.inc:
			self.rectangle.pos = (self.x,self.height-self.h)
		else:
			self.y+= self.inc
			self.rectangle.pos = (self.x,self.y)
		
		
	def down(self,*args):
		if self.y < 0:
			self.rectangle.pos = (self.x,self.y)
		else:
			self.y -= self.inc
			self.rectangle.pos = (self.x,self.y)
	

class myapp(App):
	def build(self):
		return mycanvas()
		
if __name__ == '__main__':
	myapp().run()