# You will have to write your own class for the QTabBar. The plus button can be added by using absolute positioning.

# I have some code here for PySide; it should give you the basic idea.
from PyQt4 import QtGui, QtCore


class TabBarPlus(QtGui.QTabBar):
    """Tab bar that has a plus button floating to the right of the tabs."""

    # plusClicked = QtCore.Signal()

    def __init__(self):
        super(TabBarPlus, self).__init__()

        # Plus Button
        self.plusButton = QtGui.QPushButton("+")
        self.plusButton.setParent(self)
        self.plusButton.setMaximumSize(20, 20) # Small Fixed size
        self.plusButton.setMinimumSize(20, 20) # Small Fixed size
        # self.plusButton.clicked.connect(self.plusClicked.emit)
        self.movePlusButton() # Move to the correct location
    # end Constructor

    def sizeHint(self):
        """Return the size of the TabBar with increased width for the plus button."""
        sizeHint = QtGui.QTabBar.sizeHint(self)
        width = sizeHint.width()
        height = sizeHint.height()
        return QtCore.QSize(width+25, height)
    # end tabSizeHint

    def resizeEvent(self, event):
        """Resize the widget and make sure the plus button is in the correct location."""
        super().resizeEvent(event)

        self.movePlusButton()
    # end resizeEvent

    def tabLayoutChange(self):
        """This virtual handler is called whenever the tab layout changes.
        If anything changes make sure the plus button is in the correct location.
        """
        super().tabLayoutChange()

        self.movePlusButton()
    # end tabLayoutChange

    def movePlusButton(self):
        """Move the plus button to the correct location."""
        # Find the width of all of the tabs
        size = 0
        for i in range(self.count()):
            size += self.tabRect(i).width()

        # Set the plus button location in a visible area
        h = self.geometry().top()
        w = self.width()
        if size > w: # Show just to the left of the scroll buttons
            self.plusButton.move(w-54, h)
        else:
            self.plusButton.move(size, h)
    # end movePlusButton
# end class MyClass

class CustomTabWidget(QtGui.QTabWidget):
    """Tab Widget that that can have new tabs easily added to it."""

    def __init__(self, parent=None):
        super(CustomTabWidget, self).__init__(parent)

        # Tab Bar
        self.tab = TabBarPlus()
        self.setTabBar(self.tab)

        # Properties
        self.setMovable(True)
        self.setTabsClosable(True)

        # Signals
        # self.tab.plusClicked.connect(self.addTab)
        self.connect(self.tab.plusButton, QtCore.SIGNAL('clicked()'), self.addTab)
        # self.tab.tabMoved.connect(self.moveTab)
        self.tabCloseRequested.connect(self.removeTab)
    # end Constructor
# end class CustomTabWidget


class AppDemo(QtGui.QMainWindow):
    def __init__(self):
        super(AppDemo, self).__init__()
        self.centralwidget = QtGui.QWidget(self)
        self.horizontalLayout = QtGui.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setContentsMargins(0, -1, 0, -1)

        self.playlist_manager = CustomTabWidget(self.centralwidget)
        #self.tabbar = TabBarPlus(self.centralwidget)

        self.horizontalLayout.addWidget(self.playlist_manager)
        #self.horizontalLayout.addWidget(self.tabbar)
        #string = QtCore.QString('Ha')
        #self.tabbar.addTab(string)

        self.playlist_manager.addTab()
        self.setCentralWidget(self.centralwidget)

        self.show()
# end class AppDemo


def main():
    import sys
    app = QtGui.QApplication(sys.argv)

    w = AppDemo()
    w.setWindowTitle('AppDemo')
    with open('style.qss', 'r') as style:
        w.setStyleSheet(style)
    w.show()

    sys.exit(app.exec_())

if __name__ == '__main__':
    main()