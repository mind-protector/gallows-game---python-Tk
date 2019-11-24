import subprocess
import os, sys


class Installer:

	"""Game Pack Installer
	and other settings and configs"""

	def __init__(self):

		"""Game datas"""

		self.WDIR = os.getcwd()
		self.STDIR = os.path.join(self.WDIR, 'game', 'stages')
		self.DICDIR = os.path.join(self.WDIR, 'game', 'dicts')

		self.STAGES = {

			'1.txt':

"""\n
        ___________]
    |        |
    |        |
    |        |
             |
             |
             |
             |
             |
             |
             |
             |
             |
             |
             |
            (___________|__________)
""",

			'2.txt':

"""\n
  ___________]
    |        |
    |        |
 ___|_____   |
|         |  |
|  0   0  |  |
|____*____|  |
             |
             |
             |
             |
             |
             |
             |
             |
            (___________|__________)
 """,

			'3.txt':

"""\n
  ___________]
    |        |
    |        |
 ___|_____   |
|         |  |
|  0   0  |  |
|____*____|  |
    | |      |
    | |      |
    | |      |
    | |      |
             |
             |
             |
             |
            (___________|__________)
""",

			'4.txt':

"""\n
  ___________]
    |        |
    |        |
 ___|_____   |
|         |  |
|  0   0  |  |
|____*____|  |
    | |      |
   /| |      |
  { | |      |
    | |      |
             |
             |
             |
             |
            (___________|__________)
""",

			'5.txt':

"""\n
  ___________]
    |        |
    |        |
 ___|_____   |
|         |  |
|  0   0  |  |
|____*____|  |
    | |      |
   /| |\     |
  { | | }    |
    | |      |
             |
             |
             |
             |
            (___________|__________)
""",

			'6.txt':

"""\n
  ___________]
    |        |
    |        |
 ___|_____   |
|         |  |
|  0   0  |  |
|____*____|  |
    | |      |
   /| |\     |
  { | | }    |
    | |      |
   /         |
  (          |
             |
             |
            (___________|__________)
""",

			'7.txt':

"""\n
  ___________]
    |        |
    |        |
 ___|_____   |
|         |  |
|  x   x  |  |
|____*____|  |
    | |      |
   /| |\     |
  { | | }    |
    | |      |
   /   \     |
  (     )    |
             |
             |
            (___________|__________)
"""
		}

		self.DICTS = {

			'easy.txt':

"""
ball
game
stick
zoo
bear
wisp
box
apple
line
front 
""",

			'medium.txt':

"""
sniper
tkinter
master
mistake
rainbow
multiply
random
integer
string
double
""",

			'hard.txt':

"""
spiderman
beastmaster
apparation
randomize
civilization
guardians
developer
javascript
generator
refrigerator
"""
		}

		self.SCR_TEXT = r'''
from tkinter import *
import os, sys
from random import randint


class Main():

  """The gallows game:
  - player choose the letter and if the word includes this letter player get 1 point (if: 0 < points < 7)
  - elif get -1 point (if: 0 < points < 7)
  - else game is over"""

  def __init__(self):

    """Create windows and settings"""

    self.root = Tk()
    self.WDIR = os.getcwd()

    self.BG = '#000000'
    self.FG = '#ffffff'
    self.FONT = 'Courier 20'

    self.answer = []
    self.question = 'Play'

    self.questL = None
    self.ansL = None
    self.wordL = None
    self.gallows = None

    self.points = 1
    self.dictionary = None
    self.word = None
    self.users_word = None
    self.result = None

    self.root.attributes('-fullscreen', True)
    self.root.config(background=self.BG, cursor='none')

    self.GUI()


  def _show_gallows(self):

    """Return gallows stage by .txt file in game data"""

    with open(os.path.join(self.WDIR, 'game', 'stages', f'{self.points}.txt'), 'r', encoding='utf-8') as f:
      return f.read()
    

  def _random_word(self):

    """Gets a random word from the current dictionary"""

    with open(os.path.join(self.WDIR, 'game', 'dicts', self.dictionary), 'r', encoding='utf-8') as f:
      lines = f.readlines()
      return lines[randint(1, len(lines)-1)][0:-1]


  def _Gameplay(self):

    """Gameplay process: questions-answers (word guessing)"""

    def create_widgets():

      self.questL['text'] = '>>> Guess letter or write full word: '
      self.question = 'Game'

      self.ansL.place(relx=.37,rely=.02)

      w = Label(self.root,
        text=self.users_word,
        background=self.BG,
        foreground=self.FG,
        font=self.FONT,
        pady=20)

      w.pack()
      w.place(relx=0.02,rely=0.75)

      return w

    self.word = self._random_word().lower()
    self.users_word = ['_' for i in self.word]

    self.wordL = create_widgets()


  def GUI(self):

    """Main loop of draw labels and choice the level hard"""

    def inp(event):

      """Control user's input:
      Esc - exit,
      Backspace - delete symbol,
      [a-zA-z0-9] - append symbol,
      Enter - Do something"""

      textAns = ''.join(self.answer).lower()

      # Service keys:
      if event.keysym == 'Escape':
        sys.exit()

      elif event.keysym == 'BackSpace':
        del self.answer[-1]
        self.ansL['text'] = ''.join(self.answer)
        return

      elif event.keysym == 'Return':

        if self.question == 'Play':

          if textAns == 'y':

            self.answer.clear()
            self.ansL['text'] = '_'
            self.ansL.place(relx=.56,rely=.02)

            self.question = 'Difficulty'
            self.questL['text'] = '>>> Choose difficulty (e - Easy, m - Medium, h - Hard): '

          elif textAns == 'n':
            sys.exit()

          else:
            self.answer.clear()
            self.ansL['text'] = '_'
            return

        elif self.question == 'Difficulty':

          if textAns == 'e':
            self.dictionary = 'easy.txt'
            self._Gameplay()

          elif textAns == 'm':
            self.dictionary = 'medium.txt'
            self._Gameplay()

          elif textAns == 'h':
            self.dictionary = 'hard.txt'
            self._Gameplay()

          self.answer.clear()
          self.ansL['text'] = '_'

        elif self.question == 'Game':

          if (self.word.count(textAns) == 0) or (self.users_word.count(textAns) > 0):

            if self.points == 6:
              self.result = False

            self.points += 1

          elif self.word == textAns:
            self.result = True

          else:
            if self.points > 1:
              self.points -= 1
            for n,i in enumerate(self.word):
              if self.word[n] == textAns:
                self.users_word[n] = textAns

          self.answer.clear()
          self.gallows['text'] = self._show_gallows()

          self.ansL['text'] = '_'
          self.wordL['text'] = self.users_word

          if ''.join(self.users_word) == self.word:
            self.result = True

          # If won:
          if self.result:

            self.questL['text'] = f'>>> You won! This word is {self.word}!'
            self.ansL.destroy()
            self.ansL.after(2000, self.__init__)

          # If lose:
          elif self.result is False:

            self.questL['text'] = f'>>> You won! This word is {self.word}...'
            self.ansL.destroy()
            self.ansL.after(2000, self.__init__)


      # An other:
      if len(event.keysym) == 1:
        self.answer.append(event.keysym)
        self.ansL['text'] = ''.join(self.answer)


    def create_widgets():

      """Create a question, an invisible text form and show gallows"""

      q = Label(self.root,
          text='>>> Wanna play a game (Y/n): ',
          background=self.BG,
          foreground=self.FG,
          font=self.FONT,
          pady=20)

      q.pack()
      q.place(relx=0,rely=0)

      a =  Label(self.root,
          text='_',
          background=self.BG,
          foreground=self.FG,
          font=self.FONT)

      a.pack()
      a.place(relx=.29,rely=.02)

      g = Label(self.root,
        text=self._show_gallows(),
        background=self.BG,
        foreground=self.FG,
        font=self.FONT)

      g.pack()
      g.place(relx=0,rely=.06)

      return q, a, g

    self.questL, self.ansL, self.gallows = create_widgets()
    self.root.bind("<Key>", inp)


if __name__ == '__main__':
  main = Main()
  main.root.mainloop()
'''


	def unpacking(self):

		"""Unpacking game datas and remove itself"""

		os.makedirs(self.STDIR)
		os.makedirs(self.DICDIR)

		for i in self.STAGES:
			with open(os.path.join(self.STDIR, i), 'w', encoding='utf-8') as f:
				f.write(self.STAGES[i])

		for i in self.DICTS:
			with open(os.path.join(self.DICDIR, i), 'w', encoding='utf-8') as f:
				f.write(self.DICTS[i])

		with open('main.pyw', 'w', encoding='utf-8') as scr:
			scr.write(self.SCR_TEXT)

		os.remove('installer.py')

if __name__ == '__main__':
	main = Installer()
	main.unpacking()