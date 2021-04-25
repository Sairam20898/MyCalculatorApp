import kivy
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.lang import Builder
from kivy.core.window import Window

Window.size = (350, 550)

Builder.load_file('main.kv')
class myCalc(Widget):
    #This is for clear all text from input box
    def clear(self):
        self.ids.input_text.text = ''

    # which is used to call function passing number from input
    def num_button(self,num):
        prev = self.ids.input_text.text
        # adding num to prev num
        if prev == "0":
            self.clear()
            self.ids.input_text.text = f'{num}'
        else:
            self.ids.input_text.text = f'{prev}{num}'

    # this is for dot button
    def dot_button(self):
        prev = self.ids.input_text.text
        if "." in prev:
            pass
        else:
            self.ids.input_text.text = f'{prev}.'

    #this is for sign change button
    def sign_button(self):
        prev =self.ids.input_text.text
        if prev[0] == "-":
            prev = prev[1:]
            self.ids.input_text.text = f'{prev}'
        else:
            pass

    #This is for remove last charecter from string  
    def remove(self):
        prev = self.ids.input_text.text
        self.ids.input_text.text = prev[:-1]

    #This is for return results to the input block
    def equalsto(self):
        import sai
        prev = self.ids.input_text.text
        if prev == "":
            pass
        else:
            if prev.startswith("+") or prev.startswith("-") or prev.startswith("*") or prev.startswith("/"):
                self.ids.input_text.text = ''
            else:
                ans = round(eval(prev),3)
                self.ids.input_text.text = f'{ans}'
        

class CalculatorApp(App):
    def build(self):
        return myCalc()

if __name__ =='__main__':
    CalculatorApp().run()