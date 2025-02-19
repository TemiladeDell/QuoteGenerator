quotes = [
    "Success is not final, failure is not fatal: it is the courage to continue that counts. ~Winston Churchill",
    "Believe you can and you’re halfway there. ~Theodore Roosevelt",
    "Do what you can, with what you have, where you are. ~Theodore Roosevelt",
    "Courage is resistance to fear, mastery of fear—not absence of fear. ~Mark Twain",
    "You miss 100 percent of the shots you don’t take. ~Wayne Gretzky",
    "The best way to predict the future is to create it. ~Peter Drucker",
    "Act as if what you do makes a difference. It does. ~William James",
    "Nothing in the world can take the place of persistence. ~Calvin Coolidge",
    "Well done is better than well said. ~Benjamin Franklin",
    "It does not matter how slowly you go as long as you do not stop. ~Confucius",
    "If you're going through hell, keep going. ~Winston Churchill",
    "Quality is not an act, it is a habit. ~Aristotle",
    "Opportunities don't happen. You create them. ~Chris Grosser",
    "Doubt kills more dreams than failure ever will. ~Suzy Kassem",
    "He who opens a school door, closes a prison. ~Victor Hugo",
    "Do what you love and you will never work a day in your life. ~Confucius",
    "To succeed in life, you need two things: ignorance and confidence. ~Mark Twain",
    "Happiness is not something ready-made. It comes from your own actions. ~Dalai Lama",
    "A journey of a thousand miles begins with a single step. ~Lao Tzu",
    "Success is how high you bounce when you hit bottom. ~George S. Patton",
    "If you cannot do great things, do small things in a great way. ~Napoleon Hill",
    "Change your thoughts and you change your world. ~Norman Vincent Peale",
    "Whether you think you can or you think you can't, you're right. ~Henry Ford",
    "Don't wait. The time will never be just right. ~Napoleon Hill",
    "An investment in knowledge pays the best interest. ~Benjamin Franklin",
    "Live as if you were to die tomorrow. Learn as if you were to live forever. ~Mahatma Gandhi",
    "Do what you feel in your heart to be right—for you’ll be criticized anyway. ~Eleanor Roosevelt",
    "It is never too late to be what you might have been. ~George Eliot",
    "A person who never made a mistake never tried anything new. ~Albert Einstein",
    "The way to get started is to quit talking and begin doing. ~Walt Disney",
    "The secret of getting ahead is getting started. ~Mark Twain",
    "We become what we think about. ~Earl Nightingale",
    "Success is walking from failure to failure with no loss of enthusiasm. ~Winston Churchill",
    "Strive not to be a success, but rather to be of value. ~Albert Einstein",
    "Innovation distinguishes between a leader and a follower. ~Steve Jobs",
    "The only limit to our realization of tomorrow is our doubts of today. ~Franklin D. Roosevelt",
    "The harder I work, the luckier I get. ~Samuel Goldwyn",
    "Genius is 1 percent inspiration and 99 percent perspiration. ~Thomas Edison",
    "I have not failed. I’ve just found 10,000 ways that won’t work. ~Thomas Edison",
    "The successful warrior is the average man, with laser-like focus. ~Bruce Lee",
    "I find that the harder I work, the more luck I seem to have. ~Thomas Jefferson",
    "The function of leadership is to produce more leaders, not more followers. ~Ralph Nader",
    "If opportunity doesn’t knock, build a door. ~Milton Berle",
    "Leadership and learning are indispensable to each other. ~John F. Kennedy",
    "Perfection is not attainable, but if we chase perfection we can catch excellence. ~Vince Lombardi",
    "If you want to live a happy life, tie it to a goal, not to people or things. ~Albert Einstein",
    "A fool thinks himself to be wise, but a wise man knows himself to be a fool. ~William Shakespeare",
    "The only place where success comes before work is in the dictionary. ~Vidal Sassoon",
    "Hardships often prepare ordinary people for an extraordinary destiny. ~C.S. Lewis",
    "We may encounter many defeats but we must not be defeated. ~Maya Angelou",
    "Do not dwell in the past, do not dream of the future, concentrate the mind on the present moment. ~Buddha",
    "What lies behind us and what lies before us are tiny matters compared to what lies within us. ~Ralph Waldo Emerson",
    "It is our choices that show what we truly are, far more than our abilities. ~J.K. Rowling",
    "A champion is someone who gets up when he can’t. ~Jack Dempsey",
    "Education is the most powerful weapon which you can use to change the world. ~Nelson Mandela",
    "Don't cry because it's over, smile because it happened. ~Dr. Seuss",
    "To handle yourself, use your head; to handle others, use your heart. ~Eleanor Roosevelt",
    "You cannot change your future, but you can change your habits, and surely your habits will change your future. ~A.P.J. Abdul Kalam",
    "Your time is limited, so don’t waste it living someone else’s life. ~Steve Jobs",
    "Act as if what you do makes a difference. It does. ~William James",
    "Do what you can with all you have, wherever you are. ~Theodore Roosevelt",
    "You are never too old to set another goal or to dream a new dream. ~C.S. Lewis",
    "It’s not whether you get knocked down, it’s whether you get up. ~Vince Lombardi",
    "Life is 10 percent what happens to us and 90 percent how we react to it. ~Charles R. Swindoll",
    "If you are not willing to risk the usual, you will have to settle for the ordinary. ~Jim Rohn",
    "You may be disappointed if you fail, but you are doomed if you don’t try. ~Beverly Sills",
    "A mind is like a parachute. It doesn’t work if it isn’t open. ~Frank Zappa",
    "No one can make you feel inferior without your consent. ~Eleanor Roosevelt",
    "Happiness depends upon ourselves. ~Aristotle",
    "Don’t let what you cannot do interfere with what you can do. ~John Wooden",
    "Start where you are. Use what you have. Do what you can. ~Arthur Ashe",
    "Success is not the key to happiness. Happiness is the key to success. ~Albert Schweitzer",
    "If you think you are too small to make a difference, try sleeping with a mosquito. ~Dalai Lama",
    "The only way to do great work is to love what you do. ~Steve Jobs",
    "There is nothing impossible to him who will try. ~Alexander the Great",
    "Do what is right, not what is easy nor what is popular. ~Roy T. Bennett",
]



from PyQt6 import QtCore, QtWidgets
from PyQt6.QtWidgets import QLabel, QApplication, QMainWindow
import sys
import random
from PyQt6.QtCore import QTimer

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(400, 189)
        MainWindow.setMaximumSize(QtCore.QSize(400, 280))

        MainWindow.setWindowFlags(QtCore.Qt.WindowType.FramelessWindowHint)
        MainWindow.setAttribute(QtCore.Qt.WidgetAttribute.WA_TranslucentBackground)

        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")


        self.DailyQuoteGenerator = DraggableLabel("", parent=self.centralwidget)
        self.DailyQuoteGenerator.setGeometry(QtCore.QRect(4, 29, 391, 111))
        self.DailyQuoteGenerator.setStyleSheet(
            "border-radius: 15px;"
            "color: white;"
            "font-size: 14pt;"
            "font-weight: bold;"
            "font-style: italic;"
            "padding: 20px;"
            "background-color: rgba(0, 0, 0, 150);"
        )
        self.DailyQuoteGenerator.setObjectName("DailyQuoteGenerator")
        self.DailyQuoteGenerator.setWordWrap(True)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 400, 18))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)

        self.statusbar = QtWidgets.QStatusBar(parent=MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.timer = QTimer()
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Daily Quote"))
        self.selectRandomQuote()
        
    def selectRandomQuote(self):
        randomQuote = random.choice(quotes)
        self.DailyQuoteGenerator.setText(randomQuote)
        self.timer.timeout.connect(self.selectRandomQuote)
        self.timer.start(15000)  

class DraggableLabel(QLabel):
    
    def __init__(self, text, parent=None, window = None):
        super().__init__(text, parent)
        self.window = window
        self.setCursor(QtCore.Qt.CursorShape.OpenHandCursor) 
        self._drag_active = False
        self._drag_start_pos = QtCore.QPoint()
        
        

    def mousePressEvent(self, event):
        if event.button() == QtCore.Qt.MouseButton.LeftButton:
            if self.window:
                self.window.selectRandomQuote()
            self._drag_active = True
            self._drag_start_pos = event.globalPosition().toPoint() - self.parent().parent().geometry().topLeft()
               

    def mouseMoveEvent(self, event):
        if self._drag_active:
            new_pos = event.globalPosition().toPoint() - self._drag_start_pos
            self.parent().parent().move(new_pos)

    def mouseReleaseEvent(self, event):
        if event.button() == QtCore.Qt.MouseButton.LeftButton:
            self._drag_active = False

if __name__ == "__main__":
    app = QApplication(sys.argv)
    MainWindow = QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())