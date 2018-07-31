import sys, time, datetime
sys.path.append("/home/el-psy/Documents/Programming/TravelPlanner")
from Controller.StateMachine import StateMachine
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow, QLabel, QStackedWidget, QGridLayout


class GUI(QMainWindow):
    state_names = [state.name for state in StateMachine]
    current_state = StateMachine.WELCOME
    state_changed = pyqtSignal(object)
    left = 400
    top = 200
    width = 1200
    height = 700

    def __init__(self):
        super().__init__()

        # self.grid = QGridLayout()
        # self.setLayout(self.grid)
      
        self.central_widget = QStackedWidget()
        self.setCentralWidget(self.central_widget)
        self.initUI()

        self.welcome_view = prep_welcome_view(self)
        self.login_view = prep_login_view(self)
        self.central_widget.addWidget(self.welcome_view)

        self.central_widget.addWidget(self.login_view)



    def get_current_state(self):
        return self.current_state

    def set_current_state(self, new_state):
        self.current_state = new_state
        self.state_changed.emit(new_state)

    def attempt_state_update(self, new_state):
        if new_state in self.state_names:  # and self.current_state.name != new_state:
            new_state_index = self.state_names.index(new_state)
            if new_state_index == 0:
                self.set_current_state(StateMachine.WELCOME)
                # self.central_widget.setCurrentWidget(self.welcome_view)
            elif new_state_index == 1:
                self.set_current_state(StateMachine.LOGIN)
            elif new_state_index == 2:
                self.set_current_state(StateMachine.HOME)
            elif new_state_index == 3:
                self.set_current_state(StateMachine.SETTINGS)
            else:   
                pass

        print("Switching to %s state @ %s" % (self.current_state.name, datetime.datetime.now()))

    def update_view(self):
        self.central_widget.setCurrentIndex(self.current_state.value)
        # self.update()

    def initUI(self):
        self.setGeometry(self.left, self.top, self.width, self.height)
        self.setWindowTitle("Travel Planner")
        self.state_changed.connect(self.update_view)
        # self.setAutoFillBackground(True)
        # p = self.palette()
        # p.setColor(self.backgroundRole(), Qt.green)
        # self.setPalette(p)
        # self.setWindowIcon(QIcon('web.png'))
        self.attempt_state_update("WELCOME")  # TODO: Only ever updates to show last state
        self.show()

    
def prep_welcome_view(main_window):
    welcome_widget = QWidget()
    welcome_message = QLabel(welcome_widget)
    welcome_message.setText("Travel Planner \n\n Welcome!")
    grid = QGridLayout()
    grid.addWidget(welcome_message, 0, 0)
    return welcome_widget
    # main_window.setLayout(grid)


def prep_login_view(main_window):
    login_widget = QWidget()
    login_message = QLabel(login_widget)
    login_message.setText("Login")
    grid = QGridLayout()
    grid.addWidget(login_message, 0, 0)
    return login_widget


if __name__=='__main__':
    app = QApplication(sys.argv)
    gui = GUI()
    time.sleep(3)
    gui.attempt_state_update("LOGIN")
    sys.exit(app.exec_())
