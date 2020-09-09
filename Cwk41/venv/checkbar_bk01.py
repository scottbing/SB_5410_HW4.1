from tkinter import *
class Checkbar(Frame):

   def __init__(self, parent=None, picks=[], side=LEFT, anchor=W):
      Frame.__init__(self, parent)
      self.vars = []
      for pick in picks:
         var = IntVar()
         chk = Checkbutton(self, text=pick, variable=var)
         chk.pack(side=side, anchor=anchor, expand=YES)
         self.vars.append(var)

   def state(self):
      return map((lambda var: var.get()), self.vars)

if __name__ == '__main__':
   #list of stories
   stories = ["Alice Through the Looking Glass",
                   "Peter Rabit",
                   "King James Bible",
                   "The Time Machine",
                   "A Tale of Two Cities"]
   #liet of story files
   storyFiles = ["alice.txt", "peter_rabit.txt", "the_bible", "time_machine", "two_cities"]

   root = Tk()
   title = Label(root,
         text="Hwk 4.1 - Text Comparison Application",
         font=("Helvetica", 16, 'bold'),
         highlightbackground='#3E4149',
         )
   title.pack()
   instructions = Label(root,
         text="Choose two stories to compare:",
         font=("Helvetica", 14)
         )
   instructions.pack()
   #lng = Checkbar(root, ['Story 1', 'Story 2', 'Story 3', 'Story 4', 'Story 5'])
   select = Checkbar(root, [stories[0], stories[1], stories[2], stories[3], stories[4]])
   select.pack(side=TOP,  fill=X)

   def allstates():
       print(list(select.state()))


   Button(root, text='Process', command=allstates).pack(side=LEFT)
   Button(root, text='Quit', command=root.quit).pack(side=RIGHT)
   Entry(root, bd=5).pack(side=RIGHT)
   Button(root, text='Search', command=allstates).pack(side=RIGHT)


   root.mainloop()