from PyQt5.QtWidgets import (
    QWidget,
    QFrame,
    QHBoxLayout,
    QPushButton,
    QLabel,
    QStackedWidget,
    QTableWidget,
    QTableWidgetItem,
    QFormLayout,
    QLineEdit,
    QMessageBox,
    QVBoxLayout,
    QComboBox,
)
from PyQt5.QtCore import Qt, QCoreApplication, QMetaObject, QRect, QSize
from PyQt5.QtGui import QCursor, QFont, QIcon
from functions import *
from styles import Styles
from mysql_dbconfig import db


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName("MainWindow")

        #################################################################################
        # Main window
        #################################################################################
        MainWindow.resize(1500, 800)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.centralwidget.setStyleSheet("background-color: rgb(25, 25, 25);")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.main_header = QFrame(self.centralwidget)
        self.main_header.setObjectName("main_header")
        self.main_header.setMaximumSize(QSize(16777215, 50))
        self.main_header.setFrameShape(QFrame.WinPanel)
        self.main_header.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.main_header)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.tittle_bar_container = QFrame(self.main_header)
        self.tittle_bar_container.setObjectName("tittle_bar_container")
        self.tittle_bar_container.setFrameShape(QFrame.StyledPanel)
        self.tittle_bar_container.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.tittle_bar_container)
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        #################################################################################
        # Left menu
        #################################################################################
        self.left_menu_toggle = QFrame(self.tittle_bar_container)
        self.left_menu_toggle.setObjectName("left_menu_toggle")
        self.left_menu_toggle.setMinimumSize(QSize(50, 0))
        self.left_menu_toggle.setMaximumSize(QSize(50, 16777215))
        self.left_menu_toggle.setFrameShape(QFrame.StyledPanel)
        self.left_menu_toggle.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.left_menu_toggle)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.left_menu_toggle_btn = QPushButton(self.left_menu_toggle)
        self.left_menu_toggle_btn.setObjectName("left_menu_toggle_btn")
        self.left_menu_toggle_btn.setMinimumSize(QSize(0, 50))
        self.left_menu_toggle_btn.setMaximumSize(QSize(50, 16777215))
        self.left_menu_toggle_btn.setCursor(QCursor(Qt.PointingHandCursor))
        icon = QIcon()
        icon.addFile("icons/cil-menu.png", QSize(), QIcon.Normal, QIcon.Off)
        self.left_menu_toggle_btn.setIcon(icon)
        self.left_menu_toggle_btn.setIconSize(QSize(24, 24))
        self.horizontalLayout_4.addWidget(self.left_menu_toggle_btn)
        self.horizontalLayout_5.addWidget(self.left_menu_toggle)
        self.tittle_bar = QFrame(self.tittle_bar_container)
        self.tittle_bar.setObjectName("tittle_bar")
        self.tittle_bar.setFrameShape(QFrame.StyledPanel)
        self.tittle_bar.setFrameShadow(QFrame.Raised)
        self.verticalLayout_9 = QVBoxLayout(self.tittle_bar)
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.label_6 = QLabel(self.tittle_bar)
        self.label_6.setObjectName("label_6")
        font = QFont()
        font.setFamily("Open Sans Semibold")
        font.setPointSize(12)
        self.label_6.setFont(font)
        self.label_6.setAlignment(Qt.AlignCenter)
        self.verticalLayout_9.addWidget(self.label_6)
        self.horizontalLayout_5.addWidget(self.tittle_bar)
        self.horizontalLayout_2.addWidget(self.tittle_bar_container)

        #################################################################################
        # Top right buttons
        #################################################################################
        self.top_right_btns = QFrame(self.main_header)
        self.top_right_btns.setObjectName("top_right_btns")
        self.top_right_btns.setMaximumSize(QSize(100, 16777215))
        self.top_right_btns.setFrameShape(QFrame.StyledPanel)
        self.top_right_btns.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.top_right_btns)
        self.horizontalLayout_3.setSpacing(10)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.minimizeButton = QPushButton(self.top_right_btns)
        self.minimizeButton.setObjectName("minimizeButton")
        self.minimizeButton.setCursor(QCursor(Qt.PointingHandCursor))
        icon2 = QIcon()
        icon2.addFile("icons/cil-minus.png", QSize(), QIcon.Normal, QIcon.Off)
        self.minimizeButton.setIcon(icon2)
        self.minimizeButton.setIconSize(QSize(24, 24))
        self.horizontalLayout_3.addWidget(self.minimizeButton)
        self.restoreButton = QPushButton(self.top_right_btns)
        self.restoreButton.setObjectName("restoreButton")
        self.restoreButton.setCursor(QCursor(Qt.PointingHandCursor))
        icon1 = QIcon()
        icon1.addFile("icons/cil-window-maximize.png", QSize(), QIcon.Normal, QIcon.Off)
        self.restoreButton.setIcon(icon1)
        self.restoreButton.setIconSize(QSize(24, 24))
        self.horizontalLayout_3.addWidget(self.restoreButton)
        self.closeButton = QPushButton(self.top_right_btns)
        self.closeButton.setObjectName("closeButton")
        self.closeButton.setCursor(QCursor(Qt.PointingHandCursor))
        icon3 = QIcon()
        icon3.addFile("icons/cil-x.png", QSize(), QIcon.Normal, QIcon.Off)
        self.closeButton.setIcon(icon3)
        self.closeButton.setIconSize(QSize(24, 24))
        self.horizontalLayout_3.addWidget(self.closeButton)
        self.horizontalLayout_2.addWidget(self.top_right_btns)
        self.verticalLayout.addWidget(self.main_header)

        #################################################################################
        # Main body
        #################################################################################
        self.main_body = QFrame(self.centralwidget)
        self.main_body.setObjectName("main_body")
        self.main_body.setStyleSheet("")
        self.main_body.setFrameShape(QFrame.StyledPanel)
        self.main_body.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.main_body)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)

        #################################################################################
        # Left menu
        #################################################################################
        self.left_side_menu = QFrame(self.main_body)
        self.left_side_menu.setObjectName("left_side_menu")
        self.left_side_menu.setMaximumSize(QSize(50, 16777215))
        self.left_side_menu.setFrameShape(QFrame.NoFrame)
        self.left_side_menu.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.left_side_menu)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)

        #################################################################################
        # Left buttons
        #################################################################################
        self.left_menu_top_buttons = QFrame(self.left_side_menu)
        self.left_menu_top_buttons.setObjectName("left_menu_top_buttons")
        self.left_menu_top_buttons.setFrameShape(QFrame.StyledPanel)
        self.left_menu_top_buttons.setFrameShadow(QFrame.Raised)
        self.formLayout = QFormLayout(self.left_menu_top_buttons)
        self.formLayout.setObjectName("formLayout")
        self.formLayout.setHorizontalSpacing(0)
        self.formLayout.setVerticalSpacing(0)
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.accounts_button = QPushButton(self.left_menu_top_buttons)
        self.accounts_button.setObjectName("accounts_button")
        self.accounts_button.setMinimumSize(QSize(100, 0))
        self.formLayout.setWidget(1, QFormLayout.SpanningRole, self.accounts_button)
        self.home_button = QPushButton(self.left_menu_top_buttons)
        self.home_button.setObjectName("home_button")
        self.home_button.setMinimumSize(QSize(100, 0))
        self.formLayout.setWidget(0, QFormLayout.SpanningRole, self.home_button)
        self.verticalLayout_3.addWidget(self.left_menu_top_buttons)
        self.about_button = QPushButton(self.left_side_menu)
        self.about_button.setObjectName("about_button")
        self.about_button.setMinimumSize(QSize(100, 0))
        self.verticalLayout_3.addWidget(self.about_button)
        self.horizontalLayout.addWidget(self.left_side_menu)

        #################################################################################
        # Center section
        #################################################################################
        self.center_main_items = QFrame(self.main_body)
        self.center_main_items.setObjectName("center_main_items")
        self.center_main_items.setStyleSheet("")
        self.center_main_items.setFrameShape(QFrame.StyledPanel)
        self.center_main_items.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.center_main_items)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.stackedWidget = QStackedWidget(self.center_main_items)
        self.stackedWidget.setObjectName("stackedWidget")
        self.home_page = QWidget()
        self.home_page.setObjectName("home_page")
        self.home_page.setStyleSheet("")

        #################################################################################
        # Table
        #################################################################################
        self.main_table = QTableWidget(self.home_page)
        self.main_table.setObjectName("tableWidget")
        self.main_table.setGeometry(QRect(0, 0, 1150, 680))
        self.main_table.setShowGrid(True)
        self.main_table.setGridStyle(Qt.SolidLine)
        self.main_table.setWordWrap(True)
        self.main_table.setColumnCount(0)
        self.main_table.setRowCount(0)
        self.verticalLayout_7 = QVBoxLayout(self.home_page)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.stackedWidget.addWidget(self.home_page)
        self.accounts_page = QWidget()
        self.accounts_page.setObjectName("accounts_page")
        self.accounts_page.setStyleSheet("")
        self.verticalLayout_6 = QVBoxLayout(self.accounts_page)
        self.verticalLayout_6.setSpacing(10)
        self.verticalLayout_6.setObjectName("verticalLayout_6")

        #################################################################################
        # Sign in page
        #################################################################################
        self.sign_in_response_frame = QFrame(self.accounts_page)
        self.sign_in_response_frame.setObjectName("sign_in_response_frame")
        self.sign_in_response_frame.setMinimumSize(QSize(300, 100))
        self.sign_in_response_frame.setMaximumSize(QSize(400, 200))
        self.sign_in_response_frame.setFrameShape(QFrame.StyledPanel)
        self.sign_in_response_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_11 = QVBoxLayout(self.sign_in_response_frame)
        self.verticalLayout_11.setObjectName("verticalLayout_11")
        self.sign_in_response_msg = QLabel(self.sign_in_response_frame)
        self.sign_in_response_msg.setObjectName("sign_in_response_msg")
        font1 = QFont()
        font1.setFamily("Open Sans")
        self.sign_in_response_msg.setFont(font1)
        self.sign_in_response_msg.setAlignment(Qt.AlignCenter)
        self.verticalLayout_11.addWidget(self.sign_in_response_msg)
        self.sign_in_res_ok_btn = QPushButton(self.sign_in_response_frame)
        self.sign_in_res_ok_btn.setObjectName("sign_in_res_ok_btn")
        self.sign_in_res_ok_btn.setMinimumSize(QSize(80, 50))
        self.sign_in_res_ok_btn.setMaximumSize(QSize(80, 50))
        font2 = QFont()
        font2.setBold(True)
        font2.setWeight(75)
        self.sign_in_res_ok_btn.setFont(font2)
        self.sign_in_res_ok_btn.setCursor(QCursor(Qt.PointingHandCursor))
        self.verticalLayout_11.addWidget(self.sign_in_res_ok_btn, 0, Qt.AlignHCenter)
        self.verticalLayout_6.addWidget(self.sign_in_response_frame, 0, Qt.AlignHCenter)

        #################################################################################
        # Sign in form
        #################################################################################
        self.sign_in_form_frame = QFrame(self.accounts_page)
        self.sign_in_form_frame.setObjectName("sign_in_form_frame")
        self.sign_in_form_frame.setMinimumSize(QSize(750, 320))
        self.sign_in_form_frame.setMaximumSize(QSize(750, 320))
        self.sign_in_form_frame.setStyleSheet("border-radius: 20px;\n")
        self.sign_in_form_frame.setFrameShape(QFrame.StyledPanel)
        self.sign_in_form_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_8 = QVBoxLayout(self.sign_in_form_frame)
        self.verticalLayout_8.setSpacing(0)
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.input_fileds_frame = QFrame(self.sign_in_form_frame)
        self.input_fileds_frame.setObjectName("input_fileds_frame")
        self.input_fileds_frame.setFrameShape(QFrame.StyledPanel)
        self.input_fileds_frame.setFrameShadow(QFrame.Raised)
        self.formLayout_2 = QFormLayout(self.input_fileds_frame)
        self.formLayout_2.setObjectName("formLayout_2")
        self.username = QLineEdit(self.input_fileds_frame)
        self.username.setObjectName("username")
        self.username.setMinimumSize(QSize(300, 50))
        self.username.setMaximumSize(QSize(300, 16777215))
        self.username.setAlignment(Qt.AlignCenter)
        self.formLayout_2.setWidget(1, QFormLayout.FieldRole, self.username)
        self.password = QLineEdit(self.input_fileds_frame)
        self.password.setObjectName("password")
        self.password.setMinimumSize(QSize(300, 50))
        self.password.setMaximumSize(QSize(300, 16777215))
        self.password.setEchoMode(QLineEdit.Password)
        self.password.setAlignment(Qt.AlignCenter)
        self.formLayout_2.setWidget(2, QFormLayout.FieldRole, self.password)
        self.sign_in_btn = QPushButton(self.input_fileds_frame)
        self.sign_in_btn.setObjectName("sign_in_btn")
        self.sign_in_btn.setMinimumSize(QSize(0, 50))
        self.sign_in_btn.setMaximumSize(QSize(300, 16777215))
        self.sign_in_btn.setCursor(QCursor(Qt.PointingHandCursor))
        self.formLayout_2.setWidget(3, QFormLayout.FieldRole, self.sign_in_btn)
        self.sign_up_btn = QPushButton(self.input_fileds_frame)
        self.sign_up_btn.setObjectName("sign_up_btn")
        self.sign_up_btn.setMinimumSize(QSize(0, 50))
        self.sign_up_btn.setMaximumSize(QSize(300, 16777215))
        self.sign_up_btn.setCursor(QCursor(Qt.PointingHandCursor))
        self.sign_up_btn.clicked.connect(Functions.add_new_user)
        self.formLayout_2.setWidget(4, QFormLayout.FieldRole, self.sign_up_btn)
        self.profile_icon_frame = QFrame(self.input_fileds_frame)
        self.profile_icon_frame.setObjectName("profile_icon_frame")
        self.profile_icon_frame.setStyleSheet(Styles.profile_icon_frame_styles)
        self.profile_icon_frame.setMinimumSize(QSize(300, 50))
        self.profile_icon_frame.setMaximumSize(QSize(300, 50))
        self.profile_icon_frame.setFrameShape(QFrame.StyledPanel)
        self.profile_icon_frame.setFrameShadow(QFrame.Raised)
        self.formLayout_2.setWidget(0, QFormLayout.FieldRole, self.profile_icon_frame)
        self.verticalLayout_8.addWidget(self.input_fileds_frame, 0, Qt.AlignHCenter)
        self.verticalLayout_6.addWidget(
            self.sign_in_form_frame, 0, Qt.AlignHCenter | Qt.AlignVCenter
        )
        self.stackedWidget.addWidget(self.accounts_page)

        #################################################################################
        # About page
        #################################################################################
        self.about_page = QWidget()
        self.about_page.setObjectName("about_page")
        self.about_page.setStyleSheet("")
        self.verticalLayout_5 = QVBoxLayout(self.about_page)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.label_4 = QLabel(self.about_page)
        self.label_4.setObjectName("label_4")
        self.label_4.setMaximumWidth(400)
        font3 = QFont()
        font3.setPointSize(50)
        font3.setBold(True)
        font3.setWeight(200)
        self.label_4.setFont(font3)
        self.label_4.setStyleSheet("background-color: rgb(84, 84, 84);")
        self.verticalLayout_5.addWidget(
            self.label_4, 0, Qt.AlignHCenter | Qt.AlignVCenter
        )
        self.stackedWidget.addWidget(self.about_page)
        self.verticalLayout_2.addWidget(self.stackedWidget)
        self.horizontalLayout.addWidget(self.center_main_items)

        #################################################################################
        # Right menu
        #################################################################################
        self.right_side_menu = QFrame(self.main_body)
        self.right_side_menu.setObjectName("right_side_menu")
        self.right_side_menu.setMaximumSize(QSize(250, 16777215))
        self.right_side_menu.setStyleSheet("background-color: rgb(0, 0, 0);")
        self.right_side_menu.setFrameShape(QFrame.NoFrame)
        self.right_side_menu.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.right_side_menu)
        self.verticalLayout_4.setObjectName("verticalLayout_4")

        # search
        self.search_input = QLineEdit(self.centralwidget)
        self.search_input.setObjectName("search_input")
        self.search_input.setPlaceholderText("Search...")
        self.search_input.textChanged.connect(self.search_in_table)

        # combo box for tables from db
        self.combo_box = QComboBox(self.centralwidget)
        self.combo_box.setObjectName("combo_box")
        self.combo_box.addItems(["", "", "", "", ""])

        # show data btn
        self.show_data_btn = QPushButton(self.input_fileds_frame)
        self.show_data_btn.setObjectName("show_data_btn")
        self.show_data_btn.setMinimumSize(QSize(100, 0))
        self.show_data_btn.clicked.connect(self.select_data)
        self.show_data_btn.clicked.connect(
            lambda: self.stackedWidget.setCurrentWidget(self.home_page)
        )

        # Add book
        self.add_book_btn = QPushButton(self.centralwidget)
        self.add_book_btn.setObjectName("add_book_btn")
        self.add_book_btn.clicked.connect(Functions.add_book)

        # Update book
        self.update_book_btn = QPushButton(self.centralwidget)
        self.update_book_btn.setObjectName("update_book_btn")
        self.update_book_btn.clicked.connect(Functions.update_book)

        # Delete book
        self.delete_book_btn = QPushButton(self.centralwidget)
        self.delete_book_btn.setObjectName("delete_book_btn")
        self.delete_book_btn.clicked.connect(Functions.delete_book)

        # Show favorites
        self.show_favorites_btn = QPushButton(self.centralwidget)
        self.show_favorites_btn.setObjectName("show_favorites_btn")
        self.show_favorites_btn.clicked.connect(
            lambda: self.stackedWidget.setCurrentWidget(self.accounts_page)
        )

        # Add favorite book
        self.add_favorites_btn = QPushButton(self.centralwidget)
        self.add_favorites_btn.setObjectName("add_favorites_btn")
        self.add_favorites_btn.clicked.connect(Functions.add_favorite)
        self.verticalLayout_4.addWidget(self.search_input)
        self.verticalLayout_4.addWidget(self.combo_box)
        self.verticalLayout_4.addWidget(self.show_data_btn)
        self.verticalLayout_4.addWidget(self.add_book_btn)
        self.verticalLayout_4.addWidget(self.update_book_btn)
        self.verticalLayout_4.addWidget(self.delete_book_btn)
        self.verticalLayout_4.addWidget(self.show_favorites_btn)
        self.verticalLayout_4.addWidget(self.add_favorites_btn)

        #################################################################################
        # Right side menu
        #################################################################################
        self.label_3 = QLabel(self.right_side_menu)
        self.label_3.setObjectName("label_3")
        font4 = QFont()
        font4.setFamily("a_Concepto")
        font4.setPointSize(15)
        font4.setBold(True)
        font4.setWeight(75)
        self.label_3.setFont(font4)
        self.label_3.setStyleSheet("color: rgb(255, 255, 255);")  # open
        self.label_3.setWordWrap(True)
        self.verticalLayout_4.addWidget(self.label_3)
        self.horizontalLayout.addWidget(self.right_side_menu)
        self.verticalLayout.addWidget(self.main_body)

        #################################################################################
        # Footer
        #################################################################################
        self.main_footer = QFrame(self.centralwidget)
        self.main_footer.setObjectName("main_footer")
        self.main_footer.setMinimumSize(QSize(0, 50))
        self.main_footer.setMaximumSize(QSize(16777215, 30))
        self.main_footer.setFrameShape(QFrame.WinPanel)
        self.main_footer.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_6 = QHBoxLayout(self.main_footer)
        self.horizontalLayout_6.setSpacing(0)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.label_7 = QLabel(self.main_footer)
        self.label_7.setObjectName("label_7")
        self.horizontalLayout_6.addWidget(self.label_7)
        self.size_grip = QFrame(self.main_footer)
        self.size_grip.setObjectName("size_grip")
        self.size_grip.setMinimumSize(QSize(20, 20))
        self.size_grip.setMaximumSize(QSize(20, 20))
        self.size_grip.setStyleSheet("")
        self.size_grip.setFrameShape(QFrame.StyledPanel)
        self.size_grip.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_6.addWidget(
            self.size_grip, 0, Qt.AlignRight | Qt.AlignBottom
        )
        self.verticalLayout.addWidget(self.main_footer, 0, Qt.AlignTop)
        MainWindow.setCentralWidget(self.centralwidget)
        self.retranslateUi(MainWindow)
        QMetaObject.connectSlotsByName(MainWindow)

    #################################################################################
    # setupUi
    #################################################################################
    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(
            QCoreApplication.translate("MainWindow", "MainWindow", None)
        )
        self.left_menu_toggle_btn.setText("")
        self.label_6.setText(
            QCoreApplication.translate("MainWindow", "Library Management App", None)
        )
        self.restoreButton.setText("")
        self.minimizeButton.setText("")
        self.closeButton.setText("")
        self.accounts_button.setText(
            QCoreApplication.translate("MainWindow", "ACCOUNT", None)
        )
        self.home_button.setText(QCoreApplication.translate("MainWindow", "HOME", None))
        self.about_button.setText(
            QCoreApplication.translate("MainWindow", "ABOUT", None)
        )
        self.sign_in_response_msg.setText(
            QCoreApplication.translate("MainWindow", "Sign in Response Msg", None)
        )
        self.sign_in_res_ok_btn.setText(
            QCoreApplication.translate("MainWindow", "Ok", None)
        )
        self.username.setPlaceholderText(
            QCoreApplication.translate("MainWindow", "Username", None)
        )
        self.password.setPlaceholderText(
            QCoreApplication.translate("MainWindow", "Password", None)
        )
        self.sign_up_btn.setText(
            QCoreApplication.translate("MainWindow", "Sign Up", None)
        )
        self.sign_in_btn.setText(
            QCoreApplication.translate("MainWindow", "Sign_in", None)
        )
        self.about_page_content = "\nVersion: 1.0\n\
Date: 2021-12-15T09:39:46.686Z\n\
Python: 3.10.1\n\
Chromium: 91.0.4472.164\n\
V8: 9.1.269.39-electron.0\n\
OS: Linux x64 5.11.0-43-generic snap\n "

        self.label_4.setText(
            QCoreApplication.translate("MainWindow", self.about_page_content, None)
        )
        self.label_7.setText(QCoreApplication.translate("MainWindow", "v 1.0", None))
        ## buttons
        self.show_data_btn.setText(
            QCoreApplication.translate("MainWindow", "SHOW DATA")
        )
        self.add_book_btn.setText(QCoreApplication.translate("MainWindow", "ADD BOOK"))
        self.update_book_btn.setText(
            QCoreApplication.translate("MainWindow", "UPDATE BOOK")
        )
        self.delete_book_btn.setText(
            QCoreApplication.translate("MainWindow", "DELETE BOOK")
        )
        self.show_favorites_btn.setText(
            QCoreApplication.translate("MainWindow", "SHOW FAVORITES")
        )
        self.add_favorites_btn.setText(
            QCoreApplication.translate("MainWindow", "ADD FAVORITES")
        )
        ## combo box
        self.combo_box.setItemText(
            0, QCoreApplication.translate("MainWindow", "Sections")
        )
        self.combo_box.setItemIcon(0, QIcon("icons/section.png"))
        self.combo_box.setItemText(
            1, QCoreApplication.translate("MainWindow", "Genres")
        )
        self.combo_box.setItemIcon(1, QIcon("icons/genre.png"))
        self.combo_box.setItemText(2, QCoreApplication.translate("MainWindow", "Books"))
        self.combo_box.setItemIcon(2, QIcon("icons/book.png"))
        self.combo_box.setItemText(
            3, QCoreApplication.translate("MainWindow", "Comments")
        )
        self.combo_box.setItemIcon(3, QIcon("icons/Comments.png"))
        self.combo_box.setItemText(
            4, QCoreApplication.translate("MainWindow", "Download_history")
        )
        self.combo_box.setItemIcon(4, QIcon("icons/down.png"))

        #################################################################################
        # Styles
        #################################################################################
        self.main_header.setStyleSheet(Styles.main_header_styles)
        self.left_menu_toggle.setStyleSheet(Styles.left_menu_toggle_styles)
        self.tittle_bar.setStyleSheet(Styles.tittle_bar_styles)
        self.top_right_btns.setStyleSheet(Styles.top_right_btns_styles)
        self.left_side_menu.setStyleSheet(Styles.left_side_menu_styles)
        self.accounts_button.setStyleSheet(Styles.accounts_button_styles)
        self.home_button.setStyleSheet(Styles.home_button_styles)
        self.about_button.setStyleSheet(Styles.about_button_styles)
        self.sign_in_response_frame.setStyleSheet(Styles.sign_in_response_frame_styles)
        self.input_fileds_frame.setStyleSheet(Styles.input_fileds_frame_styles)
        self.username.setStyleSheet(Styles.username_and_password_styles)
        self.password.setStyleSheet(Styles.username_and_password_styles)
        self.main_table.setStyleSheet(Styles.main_table_styles)
        MainWindow.setStyleSheet(Styles.main_window_styles)
        self.right_side_menu.setStyleSheet(Styles.right_side_menu_styles)
        self.show_data_btn.setStyleSheet(Styles.show_data_btn_styles)
        self.add_book_btn.setStyleSheet(Styles.add_book_btn_styles)
        self.update_book_btn.setStyleSheet(Styles.update_book_btn_styles)
        self.delete_book_btn.setStyleSheet(Styles.delete_book_btn_styles)
        self.show_favorites_btn.setStyleSheet(Styles.show_favorites_btn_styles)
        self.add_favorites_btn.setStyleSheet(Styles.add_favorites_btn_styles)
        self.main_footer.setStyleSheet(Styles.main_footer_styles)
        self.dialog_styles = Styles.dialog_styles_styles

    #################################################################################
    # Functions
    #################################################################################
    ########################################################################
    # Functions for select data from db
    ########################################################################
    def select_data(self):
        try:
            mycursor = db.cursor()
            mycursor.execute("SELECT section_name FROM Sections;")
            section_names = mycursor.fetchall()
            section_names_lst = []
            for i in section_names:
                section_names_lst.append(i[0])
        except:
            QMessageBox.critical(
                self,
                "Error!",
                f"CONNECTION ERROR",
            )

        try:
            tablename = str(self.combo_box.currentText())

            if tablename == "Sections":
                sql = f"SELECT * FROM Sections"
                mycursor.execute(sql)
                result = mycursor.fetchall()
                self.main_table.setRowCount(0)

                self.headers = ("ID", "Name")
                self.main_table.setColumnCount(len(self.headers))
                self.main_table.setHorizontalHeaderLabels(self.headers)

            elif tablename == "Genres":
                join = "section_name FROM Genres INNER JOIN Sections ON Genres.section_id = Sections.section_id"
                sql = f"SELECT genre_id, genre_name, {join};"
                mycursor.execute(sql)
                result = mycursor.fetchall()
                self.main_table.setRowCount(0)

                self.headers = ("ID", "Name", "Section")
                self.main_table.setColumnCount(len(self.headers))
                self.main_table.setHorizontalHeaderLabels(self.headers)

            elif tablename == "Books":
                join = "genre_name FROM Books INNER JOIN Genres ON Books.genre_id = Genres.genre_id"
                sql = f"SELECT book_id, book_name, author, description, publication_date, language, pages_count, photo, ISBN13, ratting, {join}"
                mycursor.execute(sql)

                result = mycursor.fetchall()
                self.main_table.setRowCount(0)

                self.headers = (
                    "ID",
                    "Name",
                    "Author",
                    "Description",
                    "Publication Date",
                    "Language",
                    "Pages Count",
                    "Photo",
                    "ISBN13",
                    "Ratting",
                    "Genre",
                )
                self.main_table.setColumnCount(len(self.headers))
                self.main_table.setHorizontalHeaderLabels(self.headers)

            elif tablename == "Comments":
                join = "Users.user_name, Books.book_name FROM ((Comments INNER JOIN Users  ON Comments.user_id = Users.user_id) INNER JOIN Books ON Comments.book_id = Books.book_id); "
                sql = f"SELECT comment_id, text, date, {join}"
                mycursor.execute(sql)
                result = mycursor.fetchall()
                self.main_table.setRowCount(0)

                self.headers = ("ID", "Text", "Date", "User", "Book")
                self.main_table.setColumnCount(len(self.headers))
                self.main_table.setHorizontalHeaderLabels(self.headers)

            elif tablename == "Download_history":
                join = "Users.user_name, Books.book_name FROM ((Download_history INNER JOIN Users  ON Download_history.user_id = Users.user_id) INNER JOIN Books ON Download_history.book_id = Books.book_id); "
                sql = f"SELECT download_history_id, date, {join}"
                mycursor.execute(sql)
                result = mycursor.fetchall()
                self.main_table.setRowCount(0)

                self.headers = ("ID", "Date", "User", "Book")
                self.main_table.setColumnCount(len(self.headers))
                self.main_table.setHorizontalHeaderLabels(self.headers)

            for row_number, row_data in enumerate(result):
                self.main_table.insertRow(row_number)
                for column_number, data in enumerate(row_data):
                    self.main_table.setItem(
                        row_number, column_number, QTableWidgetItem(str(data))
                    )

        except Exception as e:
            print("Error = ", e)

    ########################################################################
    # Functions for show favorite books
    ########################################################################
    def show_favorites(self, user_id):
        join = "Users.user_name, Books.book_name FROM ((Favorites INNER JOIN Users  ON Favorites.user_id = Users.user_id) INNER JOIN Books ON Favorites.book_id = Books.book_id) "
        sql = f"SELECT favorite_id, date, {join} WHERE Users.user_id = {int(user_id)} ;"

        mycursor.execute(sql)
        result = mycursor.fetchall()
        self.main_table.setRowCount(0)

        self.headers = ("ID", "Date", "User", "Book")
        self.main_table.setColumnCount(len(self.headers))
        self.main_table.setHorizontalHeaderLabels(self.headers)

        for row_number, row_data in enumerate(result):

            self.main_table.insertRow(row_number)
            for column_number, data in enumerate(row_data):

                self.main_table.setItem(
                    row_number, column_number, QTableWidgetItem(str(data))
                )
        return user_id

    ########################################################################
    # Functions for searching
    ########################################################################
    def search_in_table(self):
        name = self.search_input.text().lower()
        for row in range(self.main_table.rowCount()):
            item = self.main_table.item(row, 1)
            item2 = self.main_table.item(row, 2)
            self.main_table.setRowHidden(
                row,
                name not in item.text().lower() and name not in item2.text().lower(),
            )
