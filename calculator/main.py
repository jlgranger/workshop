import tkinter as tk
from simpleeval import simple_eval

class Calculator:

  def __init__(self):

    self.calculation = ''
    self.result = ''

    self.font_header = ('Gujarati', 24)
    self.font_main = ('Gujarati', 15)
    self.button_width = 3

    self.root = tk.Tk()
    self.root.title('Calculator')
    self.root.geometry('273x200')

    self.text_result = tk.Text(self.root, height=1, width=16, font=self.font_header) 
    self.text_result.grid(row=0, columnspan=5)
 
    self.btn_1 = tk.Button(self.root, text='1', command = lambda: self.add_to_calculation(1), width=self.button_width, font=self.font_main)
    self.btn_1.grid(row=1, column = 0)
    self.btn_2 = tk.Button(self.root, text='2', command = lambda: self.add_to_calculation(2), width=self.button_width, font=self.font_main)
    self.btn_2.grid(row=1, column = 1)
    self.btn_3 = tk.Button(self.root, text='3', command = lambda: self.add_to_calculation(3), width=self.button_width, font=self.font_main)
    self.btn_3.grid(row=1, column = 2)
    self.btn_4 = tk.Button(self.root, text='4', command = lambda: self.add_to_calculation(4), width=self.button_width, font=self.font_main)
    self.btn_4.grid(row=2, column = 0)
    self.btn_5 = tk.Button(self.root, text='5', command = lambda: self.add_to_calculation(5), width=self.button_width, font=self.font_main)
    self.btn_5.grid(row=2, column = 1)
    self.btn_6 = tk.Button(self.root, text='6', command = lambda: self.add_to_calculation(6), width=self.button_width, font=self.font_main)
    self.btn_6.grid(row=2, column = 2)
    self.btn_7 = tk.Button(self.root, text='7', command = lambda: self.add_to_calculation(7), width=self.button_width, font=self.font_main)
    self.btn_7.grid(row=3, column = 0)
    self.btn_8 = tk.Button(self.root, text='8', command = lambda: self.add_to_calculation(8), width=self.button_width, font=self.font_main)
    self.btn_8.grid(row=3, column = 1)
    self.btn_9 = tk.Button(self.root, text='9', command = lambda: self.add_to_calculation(9), width=self.button_width, font=self.font_main)
    self.btn_9.grid(row=3, column = 2)
    self.btn_0 = tk.Button(self.root, text='0', command = lambda: self.add_to_calculation(0), width=self.button_width, font=self.font_main)
    self.btn_0.grid(row=4, column = 1)
    
    self.btn_plus = tk.Button(self.root, text='+', command = lambda: self.add_to_calculation('+'), width=self.button_width, font=self.font_main)
    self.btn_plus.grid(row=1, column = 3)
    self.btn_minus = tk.Button(self.root, text='-', command = lambda: self.add_to_calculation('-'), width=self.button_width, font=self.font_main)
    self.btn_minus.grid(row=2, column = 3)
    self.btn_mul = tk.Button(self.root, text='*', command = lambda: self.add_to_calculation('*'), width=self.button_width, font=self.font_main)
    self.btn_mul.grid(row=3, column = 3)
    self.btn_div = tk.Button(self.root, text='/', command = lambda: self.add_to_calculation('/'), width=self.button_width, font=self.font_main)
    self.btn_div.grid(row=4, column = 3)

    self.btn_open_paren = tk.Button(self.root, text='(', command = lambda: self.add_to_calculation('('), width=self.button_width, font=self.font_main)
    self.btn_open_paren.grid(row=4, column = 0)
    self.btn_close_paren = tk.Button(self.root, text=')', command = lambda: self.add_to_calculation(')'), width=self.button_width, font=self.font_main)
    self.btn_close_paren.grid(row=4, column = 2)

    self.btn_clear = tk.Button(self.root, text="C", command=self.clear_field, width = 10, font=self.font_main)
    self.btn_clear.grid(row=5, column=0, columnspan=2)

    self.btn_clear = tk.Button(self.root, text="=", command=self.evaluate_calculation, width = 10, font=self.font_main)
    self.btn_clear.grid(row=5, column=2, columnspan=2)


    self.root.mainloop()

  def add_to_calculation(self, symbol):
    self.calculation += str(symbol)
    self.text_result.delete(1.0, 'end')
    self.text_result.insert(1.0, self.calculation)

  def evaluate_calculation(self):
    try:
      self.calculation=str(simple_eval((self.calculation)))
      self.text_result.delete(1.0, 'end')
      self.text_result.insert(1.0, self.calculation)
    except:
      self.clear_field()
      self.text_result.insert(1.0, 'Error')

  def clear_field(self):
    self.calculation = ''
    self.text_result.delete(1.0, 'end')


Calculator()