from tkinter import *  
from quiz_brain import QuizBrain 

THEME_COLOR = '#375362'


class QuizUI:
    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title('Quizzler')
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)
        
        # canvas widget:
        self.canvas = Canvas(width=300, height=250, highlightthickness=0, bg='#FFFFFF')
        self.canvas.grid(row=1, column=0, columnspan=2, pady=45)
        self.question_text = self.canvas.create_text(150, 125, text='this text is the best text i have ever seen in my life man!!!!', width=250, font=('Arial', 20, 'italic'), fill=THEME_COLOR)
        
        # labels:
        self.score_label = Label(text='Score: 0', bg=THEME_COLOR)
        self.score_label.grid(row=0, column=1)
        
        # images:
        self.true_image = PhotoImage(file='images/true.png')
        self.false_image = PhotoImage(file='images/false.png')
        
        # buttons:
        self.check_button = Button(image=self.true_image, highlightthickness=0, borderwidth=0, highlightbackground=THEME_COLOR, highlightcolor=THEME_COLOR, command=self.true_answer)
        self.check_button.grid(row=2, column=0)
        
        self.x_button = Button(image=self.false_image, highlightthickness=0, borderwidth=0, highlightbackground=THEME_COLOR, highlightcolor=THEME_COLOR, command=self.false_answer)
        self.x_button.grid(row=2, column=1)
        
        self.get_next_question() 
        
        
        self.window.mainloop() 
        
    def get_next_question(self):
        self.canvas.config(bg='#FFFFFF')
        if self.quiz.still_has_questions():
            self.score_label.config(text=f'Score: {self.quiz.score}')
            q_text = self.quiz.next_question()   
            self.canvas.itemconfig(self.question_text, text=q_text)
        else:
            self.canvas.itemconfig(self.question_text, text='End of quiz')
            self.check_button.config(state='disabled')
            self.x_button.config(state='disabled')
            
    def true_answer(self):
        is_right = self.quiz.check_answer('True')
        self.give_feedback(is_right)
    
    def false_answer(self):
        is_right = self.quiz.check_answer('False')
        self.give_feedback(is_right)
        
    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg='green')
        else:
            self.canvas.config(bg='red')
        self.window.after(1000, self.get_next_question)