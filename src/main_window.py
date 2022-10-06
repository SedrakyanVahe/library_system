from PyQt5 import QtCore, QtGui
from PyQt5.QtCore import QPropertyAnimation, Qt
from PyQt5.QtGui import (QColor)
from PyQt5.QtWidgets import QMainWindow, QGraphicsDropShadowEffect, QSizeGrip
from mysql_dbconfig import db
from app_main_ui import *


# Global value for the windows status
WINDOW_SIZE = 0
# This will help us determine if the window is minimized or maximized

# Main class


class MainWindow(QMainWindow):
  def __init__(self):
    QMainWindow.__init__(self)
    self.ui = Ui_MainWindow()
    self.ui.setupUi(self)

    # Set window Icon
    # This icon and title will not appear on our app main window because we removed the title bar
    self.setWindowIcon(QtGui.QIcon("images/logo.webp"))
    # Set window tittle
    self.setWindowTitle("Library-Management App")

    # Remove window tlttle bar
    self.setWindowFlags(QtCore.Qt.FramelessWindowHint)

    # Set main background to transparent
    self.setAttribute(QtCore.Qt.WA_TranslucentBackground)

    # Apply shadow effect
    self.shadow = QGraphicsDropShadowEffect(self)
    self.shadow.setBlurRadius(20)
    self.shadow.setXOffset(0)
    self.shadow.setYOffset(0)
    self.shadow.setColor(QColor(0, 92, 157, 150))
    # Appy shadow to central widget
    self.ui.centralwidget.setGraphicsEffect(self.shadow)

    # Button click events to our top bar buttons
    #
    # Minimize window
    self.ui.minimizeButton.clicked.connect(lambda: self.showMinimized())
    # Close window
    self.ui.closeButton.clicked.connect(lambda: self.close())
    # Restore/Maximize window
    self.ui.restoreButton.clicked.connect(
        lambda: self.restore_or_maximize_window())

    # ###############################################
    # Move window on mouse drag event on the tittle bar
    # ###############################################
    def moveWindow(e):
      # Detect if the window is  normal size

      if self.isMaximized() == False:  # Not maximized
        # Move window only when window is normal size
        # if left mouse button is clicked (Only accept left mouse button clicks)
        if e.buttons() == Qt.LeftButton:
          # Move window
          self.move(self.pos() + e.globalPos() - self.clickPosition)
          self.clickPosition = e.globalPos()
          e.accept()

    # ###############################################
    # Add click event/Mouse move event/drag event to the top header to move the window
    # ###############################################
    self.ui.main_header.mouseMoveEvent = moveWindow

    # SLIDABLE LEFT MENU
    # Left Menu toggle button
    self.ui.left_menu_toggle_btn.clicked.connect(
        lambda: self.slideLeftMenu())

    # STACKED PAGES (DEFAUT /CURRENT PAGE)
    # Set the page that will be visible by default when the app is opened
    self.ui.stackedWidget.setCurrentWidget(self.ui.home_page)

    # STACKED PAGES NAVIGATION
    # Using side menu buttons
    # navigate to Home page
    self.ui.home_button.clicked.connect(
        lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.home_page)
    )

    # navigate to Accounts page
    self.ui.accounts_button.clicked.connect(
        lambda: self.ui.stackedWidget.setCurrentWidget(
            self.ui.accounts_page)
    )

    # navigate to about page
    self.ui.about_button.clicked.connect(
        lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.about_page)
    )

    ########################################################################
    # Start Menu buttons styling
    ########################################################################

    for w in self.ui.left_side_menu.findChildren(QPushButton):
      # Add click event listener
      w.clicked.connect(self.applyButtonStyle)

    #################################################################################
    # Call to Validate LOGIN Form
    #################################################################################
    # When login button is clicked
    self.ui.sign_in_btn.clicked.connect(self.validateLoginFields)

    # Hide loin response container when application is loaded
    self.ui.sign_in_response_frame.hide()
    # Hide loin response container when OK Button is clicked
    self.ui.sign_in_res_ok_btn.clicked.connect(
        lambda: self.ui.sign_in_response_frame.hide()
    )

    #################################################################################
    # Window Size grip
    #################################################################################
    QSizeGrip(self.ui.size_grip)

    # Show window
    self.show()

  ########################################################################
  # Start Menu buttons styling
  ########################################################################

  def applyButtonStyle(self):
    # Reset style for other buttons
    for w in self.ui.left_side_menu.findChildren(QPushButton):
      # If the button name is not equal to clicked button name
      if w.objectName() != self.sender().objectName():
        # Create default style by removing the left border
        # Lets remove the bottom border style
        defaultStyle = w.styleSheet().replace(
            "border-bottom: 2px solid  rgb(0, 136, 255);", ""
        )

        # Lets also remove the left border style
        defaultStyle = defaultStyle.replace(
            "border-left: 2px solid  rgb(0, 136, 255);", ""
        )

        # Apply the default style
        w.setStyleSheet(defaultStyle)

    # Apply new style to clicked button
    # Sender = clicked button
    # Get the clicked button stylesheet then add new left-border style to it
    # Lets add the bottom border style
    newStyle = self.sender().styleSheet() + (
        "border-left: 2px solid  rgb(0, 136, 255);border-bottom: 2px solid  rgb(0, 136, 255);"
    )
    # Apply the new style
    self.sender().setStyleSheet(newStyle)

    return

  # ###############################################
  # Add mouse events to the window
  # ###############################################
  def mousePressEvent(self, event):

    # Get the current position of the mouse
    self.clickPosition = event.globalPos()
    # We will use this value to move the window

  # Restore or maximize your window
  def restore_or_maximize_window(self):

    # Global windows state
    global WINDOW_SIZE  # The default value is zero to show that the size is not maximized
    win_status = WINDOW_SIZE

    if win_status == 0:
      # If the window is not maximized
      WINDOW_SIZE = 1  # Update value to show that the window has been maxmized
      self.showMaximized()

      # Update button icon  when window is maximized
      self.ui.restoreButton.setIcon(
          QtGui.QIcon("src/icons/cil-window-restore.png")
      )  # Show minized icon

      # Animate the transition
      self.animation = QPropertyAnimation(
          self.ui.right_side_menu, b"minimumWidth"
      )  # Animate minimumWidht
      self.animation.setDuration(250)
      # Start value is the current menu width
      self.animation.setStartValue(100)
      self.animation.setEndValue(350)  # end value is the new menu width
      self.animation.setEasingCurve(QtCore.QEasingCurve.InOutQuart)
      self.animation.start()

    else:
      # If the window is on its default size
      # Update value to show that the window has been minimized/set to normal size (which is 800 by 400)
      WINDOW_SIZE = 0
      self.showNormal()

      # Update button icon when window is minimized
      self.ui.restoreButton.setIcon(
          QtGui.QIcon("src/icons/cil-window-maximize.png")
      )  # Show maximize icon

      # Animate the transition
      self.animation = QPropertyAnimation(
          self.ui.right_side_menu, b"minimumWidth"
      )  # Animate minimumWidht
      self.animation.setDuration(250)
      # Start value is the current menu width
      self.animation.setStartValue(350)
      self.animation.setEndValue(100)  # end value is the new menu width
      self.animation.setEasingCurve(QtCore.QEasingCurve.InOutQuart)
      self.animation.start()

  ########################################################################
  # Slide left menu
  ########################################################################
  def slideLeftMenu(self):
    # Get current left menu width
    width = self.ui.left_side_menu.width()

    # If minimized
    if width == 50:
      # Expand menu
      newWidth = 180
    # If maximized
    else:
      # Restore menu
      newWidth = 50

    # Animate the transition
    self.animation = QPropertyAnimation(
        self.ui.left_side_menu, b"minimumWidth"
    )  # Animate minimumWidht
    self.animation.setDuration(250)
    # Start value is the current menu width
    self.animation.setStartValue(width)
    self.animation.setEndValue(newWidth)  # end value is the new menu width
    self.animation.setEasingCurve(QtCore.QEasingCurve.InOutQuart)
    self.animation.start()

  #################################################################################
  # Validate LOGIN Form
  #################################################################################

  # Show LOGIN response msg
  def showLoginResponse(self, responseMessage):
    # Show the login response container
    self.ui.sign_in_response_frame.show()
    # Update the login response text
    self.ui.sign_in_response_msg.setText(responseMessage)

  # Validate login field values
  def validateLoginFields(self):
    # Styles to be used to highlight input fiels on error or success
    successStyle = "border:3px solid  rgb(0, 255, 255);border-radius: 10px;"
    errorStyle = "border:3px solid  rgb(255, 0, 0);border-radius: 10px;"

    # Check username
    if not self.ui.username.text():
      # Username is empty
      usernameResponse = " User can not be Empyt. "
      self.ui.username.setStyleSheet(errorStyle)
    else:
      usernameResponse = ""

    # Check Password
    if not self.ui.password.text():
      # Password is empty
      passwordResponse = " Password can not be Empyt. "
      self.ui.password.setStyleSheet(errorStyle)
    else:
      passwordResponse = ""

    # View responses
    if passwordResponse != "" or usernameResponse != "":
      loginResponse = usernameResponse + passwordResponse
      self.showLoginResponse(loginResponse)

    else:
      # Check if the field values are correct(By sending values to a database or do a local validation)
      # Lets do a simple validation(local)

      # correct_username = "root"
      # correct_password = "1111"
      try:
        mycursor = db.cursor()

        mycursor.execute(
            f"SELECT user_name FROM Users WHERE user_name = '{self.ui.username.text()}';"
        )
        correct_username = mycursor.fetchall()[0][0]

        mycursor.execute(
            f"SELECT password FROM Users WHERE password = '{self.ui.password.text()}';"
        )
        correct_password = mycursor.fetchall()[0][0]

        # Check if the username is correct
        if self.ui.username.text() == correct_username:
          usernameResponse = ""
          self.ui.username.setStyleSheet(successStyle)

        # Check if the password is correct
        if self.ui.password.text() == correct_password:
          passwordResponse = ""
          self.ui.password.setStyleSheet(successStyle)

        # Create a response msg
        if passwordResponse == "" and usernameResponse == "":
          loginResponse = " Login Successful. "
          self.showLoginResponse(loginResponse)

          if loginResponse == " Login Successful. ":
            sql = f"SELECT user_id FROM Users WHERE user_name = '{correct_username}' AND password = '{correct_password}' "
            mycursor.execute(sql)
            user_id = mycursor.fetchall()[0][0]
            self.ui.stackedWidget.setCurrentWidget(
                self.ui.home_page)
            self.ui.show_favorites(user_id)

        elif passwordResponse != "" and usernameResponse != "":
          loginResponse = usernameResponse + " and " + passwordResponse
          self.showLoginResponse(loginResponse)

        else:
          loginResponse = usernameResponse + passwordResponse
          self.showLoginResponse(loginResponse)

      except Exception as e:
        usernameResponse = "Incorrect username"
        self.ui.username.setStyleSheet(errorStyle)

        passwordResponse = " Incorrect password"
        self.ui.password.setStyleSheet(errorStyle)

        if passwordResponse != "" or usernameResponse != "":
          loginResponse = usernameResponse + " or " + passwordResponse
          self.showLoginResponse(loginResponse)

        else:
          loginResponse = usernameResponse + passwordResponse
          self.showLoginResponse(loginResponse)

        print("error - ", e)
