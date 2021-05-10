import sys
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtWebEngineWidgets import *

# Concepts:
# 1. The * means everything
# 2. All of the code that starts with Q (i.e. QToolBar) is a class
# 3. The self.browser and self.url_bar are instance attributes

# The class below builds the main application window
class MainWindow(QMainWindow): 
    # This MainWindow class inherits the QMainWindow properties
    def __init__(self):
        super(MainWindow, self).__init__() 
        # The line above initializes the parent class
        self.browser = QWebEngineView() # This line creates a instance of the QWebEngineView class.
        # This class adds more functionality to the window
        self.browser.setUrl(QUrl('http://google.com')) # This sets the default url of the program
        self.setCentralWidget(self.browser) # This sets the QWebEngineView as the main window's central Widget
        self.showMaximized() # This makes the window be maximized by default
        '''
        self.setWindowTitle("Hello")
        '''
    
        # Navigation bar
        navbar = QToolBar() # It creates a QToolBar object from the QToolBar class and sets it to be the "navbar"
        self.addToolBar(navbar)

        # Back button
        back_button = QAction('⏪Back', self)
        back_button.triggered.connect(self.browser.back)
        navbar.addAction(back_button)

        # Forward button
        forward_button = QAction('⏩Forward', self)
        forward_button.triggered.connect(self.browser.forward)
        navbar.addAction(forward_button)

        # Reload button
        reload_button = QAction('🔄Reload', self)
        reload_button.triggered.connect(self.browser.reload)
        navbar.addAction(reload_button)

        # Home button
        home_button = QAction('🏠Home', self)
        home_button.triggered.connect(self.navigate_home)
        navbar.addAction(home_button)

        # URL bar
        self.url_bar = QLineEdit() # It adds a line that can receive written information
        self.url_bar.returnPressed.connect(self.navigate_to_url)
        # returnPressed -> the signal is emited when the Enter or the Return key is presses it will make an action
        navbar.addWidget(self.url_bar)

        # Update url
        self.browser.urlChanged.connect(self.update_url) # When the url is changed it'll update the url

    # Navigate to home
    def navigate_home(self):
        self.browser.setUrl(QUrl('http://google.com'))
    
    # Navigate to url
    def navigate_to_url(self):
        url = self.url_bar.text()
        if 'http://' or 'https://' in url:
            self.browser.setUrl(QUrl(url))
        else: self.browser.setUrl(QUrl('http://' + url))
    
    # Update url
    def update_url(self, q):
        self.url_bar.setText(q.toString())
        # setText() clears the selection and make the text bal show the current url

# Browser Window
app = QApplication(sys.argv)
QApplication.setApplicationName('My Cool Browser') 
# The line above do the same as this: self.setWindowTitle("Hello"). But the difference is that the
# second one needs to be inside the class MainWindow to work
window = MainWindow()
app.exec_()
