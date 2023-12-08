from tkinter import *
from functions import *


class Gui:
    phase: int = 0
    students: int = 0
    scores: List[int] = []

    def __init__(self, window: Tk) -> None:
        """
        Start of the GUI
        Has labels for displaying info, and radio buttons for selecting student number.
        Has hidden labels and entry windows for the second step.
        """

        self.window = window

        self.frame_1 = Frame(self.window)
        self.label_name = Label(self.frame_1, text='Select the number of students.')
        self.label_name.pack(side='top')
        self.frame_1.pack(anchor='center', padx=10, pady=5)

        self.frame_2 = Frame(self.window)
        self.radio_answer = IntVar()
        self.radio_answer.set(0)
        self.radiobutton_2 = Radiobutton(self.frame_2, text='two', variable=self.radio_answer, value=2)
        self.radiobutton_3 = Radiobutton(self.frame_2, text='three', variable=self.radio_answer, value=3)
        self.radiobutton_4 = Radiobutton(self.frame_2, text='four', variable=self.radio_answer, value=4)
        self.radiobutton_2.pack(side='left')
        self.radiobutton_3.pack(side='left')
        self.radiobutton_4.pack(side='left')
        self.frame_2.pack(anchor='center', padx=10, pady=5)

        self.frame_3 = Frame(self.window)
        self.label_1 = Label(self.frame_3, text='Enter the scores of the students.')
        self.label_2 = Label(self.frame_3, text='(Each score in a seperate field.)')
        self.input_score1 = Entry(self.frame_3)
        self.input_score2 = Entry(self.frame_3)
        self.input_score3 = Entry(self.frame_3)
        self.input_score4 = Entry(self.frame_3)
        self.frame_3.pack(anchor='center', padx=10, pady=5)

        self.frame_4 = Frame(self.window)
        self.button_save = Button(self.frame_4, text='ENTER', command=self.submit)
        self.button_save.pack(side='top')
        self.frame_4.pack(anchor='center', padx=10, pady=5)

        self.frame_5 = Frame(self.window)
        self.label_alert = Label(text='')
        self.label_alert.pack(side='top')
        self.frame_5.pack(anchor='center', padx=10, pady=5)

    def submit(self) -> None:
        """
        Process the number of students the first time it runs, calculates grades the second time.
        When calculating, it raises a ValueError if an entry isn't a number,
        a TypeError if it isn't positive, or a RuntimeError if it's missing an entry
        """
        if Gui.phase == 0:
            Gui.students = self.radio_answer.get()
            self.label_1.pack(side='top')
            self.label_2.pack(side='top')
            self.input_score1.pack(padx=15, pady=5, side='top')
            self.input_score2.pack(padx=15, pady=5, side='top')
            if Gui.students == 3:
                self.input_score3.pack(padx=15, pady=5, side='top')
            elif Gui.students == 4:
                self.input_score3.pack(padx=15, pady=5, side='top')
                self.input_score4.pack(padx=15, pady=5, side='top')
            Gui.phase = 1
        elif Gui.phase == 1:
            try:
                if Gui.students == 2:
                    Gui.scores = [int(self.input_score1.get()), int(self.input_score2.get())]
                elif Gui.students == 3:
                    Gui.scores = [int(self.input_score1.get()), int(self.input_score2.get()), int(self.input_score3.get())]
                elif Gui.students == 4:
                    Gui.scores = [int(self.input_score1.get()), int(self.input_score2.get()), int(self.input_score3.get()), int(self.input_score4.get())]

                for i in Gui.scores:
                    if isinstance(i, str):
                        raise ValueError
                    if i <= 0:
                        raise TypeError
                if len(Gui.scores) != Gui.students:
                    raise RuntimeError
                Gui.scores = [int(i) for i in Gui.scores]
                calculate(Gui.students, Gui.scores)
                self.label_alert.config(text='Scores have been recorded and scaled accordingly.')
            except ValueError:
                self.label_alert.config(text='Entries must be a number!')
            except TypeError:
                self.label_alert.config(text='Entries must be positive!')
            except RuntimeError:
                self.label_alert.config(text='Must have an entry for each student!')
