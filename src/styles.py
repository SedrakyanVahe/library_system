########################################################################
# Abstract class for app styles
########################################################################
class Styles:
  def __init__(self):
    pass

  main_window_styles = (
      "QWidget{\n"
      "    font-size: 14px;\n"
      "    text-decoration:none;\n"
      "}\n"
      "QListWidget:item {\n"
      "  padding-top: 5px;\n"
      "  padding-bottom: 5px;\n"
      "}\n"
      "\n"
      "QTableView {\n"
      "color: #FFFFFF;\n"
      "}\n"
      "\n"
      "QTableView QTableCornerButton::section {\n"
      "background: qlineargradient(x1: 0, y1: 0, x2: 0.5, y2: 0.5, stop: 0 rgb(0, 136, 255), stop: 1 rgb(0, 136, 255));\n"
      "}\n"
      "\n"
      "QHeaderView {\n"
      "qproperty-defaultAlignment: AlignLeft;\n"
      "}\n"
      "\n"
      "QHeaderView:section {\n"
      "background: qlineargradient(x1: 0, y1: 0, x2: 0.5, y2: 0.5, stop: 0 rgb(0, 136, 255), stop: 1 rgb(0, 136, 255));\n"
      "border: 1px white;\n"
      "padding-left: 5px;\n"
      "padding-top: 5px;\n"
      "color: #000000;\n"
      "}"
  )

  main_header_styles = (
      u"QFrame{\n"
      "	border-bottom: 1px solid #000;\n"
      "	\n"
      "	background-color: rgb(0, 0, 0);\n"
      "}"
  )

  left_menu_toggle_styles = (
      u"QFrame{\n"
      "	background-color: #000;\n"
      "}\n"
      "QPushButton{\n"
      "	padding: 5px 10px;\n"
      "	border: none;\n"
      "	border-radius: 5px;\n"
      "	background-color: #000;\n"
      "	color: #fff;\n"
      "}\n"
      "QPushButton:hover{\n"
      "	background-color: rgb(0, 92, 157);\n"
      "}"
  )

  tittle_bar_styles = u"QLabel{color: #fff;\n" "}"

  top_right_btns_styles = (
      u"QPushButton{\n"
      "	border-radius: 5px;\n"
      "}\n"
      "QPushButton:hover{\n"
      "	background-color: rgb(0, 92, 157);\n"
      "}"
  )

  left_side_menu_styles = (
      u"QFrame{\n"
      "	background-color: #000;\n"
      "}\n"
      "QPushButton{\n"
      "	padding: 20px 10px;\n"
      "	border: none;\n"
      "	border-left: 2px solid transparent;\n"
      "	border-bottom: 2px solid transparent;\n"
      "	border-radius: 5px;\n"
      "	background-color: #000;\n"
      "	color: #fff;\n"
      "	font-size: 20px;\n"
      "}\n"
      "QPushButton:hover{\n"
      "	background-color: rgb(0, 92, 157);\n"
      "}\n"
      "QPushButton:pressed {\n"
      "	background-color:  rgb(0, 92, 157);\n"
      "	border-bottom: 2px solid rgb(255, 165, 24);\n"
      "}"
  )

  accounts_button_styles = (
      u"background-image: url(src/icons/cil-user.png);\n"
      "background-repeat: none;\n"
      "padding-left: 50px;\n"
      "background-position: center left;"
  )

  home_button_styles = (
      u"background-image: url(src/icons/cil-home.png);\n"
      "background-repeat: none;\n"
      "padding-left: 50px;\n"
      "background-position: center left;\n"
      "/*This is the default selected button style*/\n"
      "border-left: 2px solid  rgb(0, 136, 255);\n"
      "border-bottom: 2px solid  rgb(0, 136, 255);"
  )

  about_button_styles = (
      u"background-image: url(src/icons/cil-people.png);\n"
      "background-repeat: none;\n"
      "padding-left: 50px;\n"
      "background-position: center left;"
  )

  sign_in_response_frame_styles = (
      u"QFrame{\n"
      "	color: rgb(255, 255, 255);\n"
      "	background-color: rgb(0, 0, 0);\n"
      "	border: 2px solid rgb(0, 69, 116);\n"
      "	border-radius: 20px;\n"
      "}\n"
      "QPushButton{	\n"
      "	color: rgb(255, 255, 255);\n"
      "	background-color: rgb(0, 69, 116);\n"
      "	border: none;\n"
      "	border-radius: 10px;\n"
      "}\n"
      "QLabel{\n"
      "	padding: 10px;\n"
      "	border: none;\n"
      "}"
  )

  input_fileds_frame_styles = (
      u"QFrame{\n"
      "	background-color: rgb(34, 34, 34);\n"
      "	color: rgb(255, 255, 255);\n"
      "	border: 2px solid rgb(1, 90, 153);\n"
      "}\n"
      "QLineEdit {\n"
      "	border: 2px solid rgb(0, 93, 159);\n"
      "	border-radius: 10px;\n"
      "	padding: 15px;\n"
      "	background-color: rgb(0, 69, 116);\n"
      "	color: rgb(255, 255, 255);\n"
      "}\n"
      "QLineEdit:hover {\n"
      "	border: 2px solid rgb(0, 66, 124);\n"
      "}\n"
      "QLineEdit:focus {\n"
      "	border: 2px solid rgb(206, 206, 206);\n"
      "	color: rgb(200, 200, 200);\n"
      "}\n"
      "QPushButton {\n"
      "	border: 2px solid rgb(45, 45, 245);\n"
      "	border-radius: 10px;\n"
      "	padding: 15px;\n"
      "	background-color:rgb(14, 13, 24);\n"
      "	color: rgb(255, 255, 255);\n"
      "}\n"
      "QPushButton:hover {\n"
      "	border: 2px solid rgb(0, 66, 124);\n"
      "}\n"
      "QLabel{\n"
      "	border:3px solid  rgb(45, 45, 45);\n"
      "	border-radius: 10px;\n"
      "	\n"
      "	background-color: rgb(6, 63, 104);\n"
      "}\n"
      "QCheckBox{\n"
      "	color: rgb(255, 255, 255);\n"
      "	padding: 10px;\n"
      "}\n"
      "QCheckBox::indicator {\n"
      "   border: 3px solid rgb(0, 93, 159);\n"
      "	width: 20px;\n"
      "	height: 20px;\n"
      "	border-radius: 10px;\n"
      "   background:rgb(0, 0, 0);\n"
      "}\n"
      "QCheckBox::indicator:hover {\n"
      "    border: 3px solid rgb(255, 255, 255);\n"
      "}\n"
      "QCheckBox::indicator:checked {\n"
      "    background: 3px solid rgb(34, 34, 34);\n"
      "	background-image: url(src/icons/cil-check.png);\n"
      "}"
  )

  username_and_password_styles = (
      u"border:3px solid  rgb(43, 31, 91);\n" "border-radius: 10px;"
  )

  profile_icon_frame_styles = (
      u"image: url(src/icons/cil-user-follow.png);\n"
      "background-color: rgb(34, 34, 34);\n"
      "border-radius: 25px;\n"
      "border: 3px solid rgb(0, 93, 159);"
  )

  main_table_styles = " color: white; font-size: 16px;"

  right_side_menu_styles = (
      u"QFrame{\n"
      "	background-color: #000;\n"
      "}\n"
      "QPushButton, QLineEdit{\n"
      "	padding: 20px 10px;\n"
      "	border: none;\n"
      "	border-left: 2px solid transparent;\n"
      "	border-bottom: 2px solid transparent;\n"
      "	border-radius: 5px;\n"
      "	background-color: #000;\n"
      "	color: #fff;\n"
      "	font-size: 20px;\n"
      "}\n"
      "QPushButton:hover{\n"
      "	background-color: rgb(0, 92, 157);\n"
      "}\n"
      "QPushButton:pressed {\n"
      "	background-color:  rgb(0, 92, 157);\n"
      "	border-bottom: 2px solid rgb(255, 165, 24);\n"
      "}\n"
      "QComboBox{\n"
      "	padding: 15px 10px;\n"
      "	border: none;\n"
      "	border-left: 2px solid transparent;\n"
      "	border-bottom: 2px solid transparent;\n"
      "	border-radius: 5px;\n"
      "	background-color: #000;\n"
      "	color: #fff;\n"
      "	font-size: 20px;\n"
      "}\n"
      "QLineEdit{\n"
      "	padding: 10px 10px;\n"
      "	background-color: #fff;\n"
      "	color: #000;\n"
      "}\n"
  )

  show_data_btn_styles = (
      u"background-image: url(src/icons/cil-view-module.png);\n"
      "background-repeat: none;\n"
      "padding-left: 50px;\n"
      "background-position: center left;"
  )

  add_book_btn_styles = (
      u"background-image: url(src/icons/cil-plus.png);\n"
      "background-repeat: none;\n"
      "padding-left: 50px;\n"
      "background-position: center left;"
  )

  update_book_btn_styles = (
      u"background-image: url(src/icons/cil-pencil.png);\n"
      "background-repeat: none;\n"
      "padding-left: 50px;\n"
      "background-position: center left;"
  )

  delete_book_btn_styles = (
      u"background-image: url(src/icons/cil-trash.png);\n"
      "background-repeat: none;\n"
      "padding-left: 50px;\n"
      "background-position: center left;"
  )

  show_favorites_btn_styles = (
      u"background-image: url(src/icons/cil-heart.png);\n"
      "background-repeat: none;\n"
      "padding-left: 50px;\n"
      "background-position: center left;"
  )

  add_favorites_btn_styles = (
      u"background-image: url(src/icons/cil-star.png);\n"
      "background-repeat: none;\n"
      "padding-left: 50px;\n"
      "background-position: center left;"
  )

  main_footer_styles = (
      u"QFrame{\n"
      "	background-color: rgb(0, 0, 0);\n"
      "	border-top-color: solid 1px  rgb(0, 0, 0);\n"
      "}\n"
      "QLabel{\n"
      "	color: #fff;\n"
      "}"
  )

  dialog_styles_styles = (
      "QDialog{\n"
      "background:rgb(34, 34, 34);}\n"
      "QFrame{\n"
      "	background-color: rgb(34, 34, 34);\n"
      "	border: 2px solid rgb(1, 90, 153);\n"
      "	color: rgb(255, 255, 255);\n"
      "	font-size: 16px;\n"
      "	font-weight: bold;\n"
      "}\n"
      " QLineEdit, QComboBox, QDateTimeEdit {\n"
      "	border: 2px solid rgb(0, 93, 159);\n"
      "	border-radius: 10px;\n"
      "	padding: 15px;\n"
      "	background-color: rgb(0, 69, 116);\n"
      "	color: rgb(255, 255, 255);\n"
      "	font-size: 16px;\n"
      "	font-weight: bold;\n"
      "}\n"
      "QLineEdit:hover {\n"
      "	border: 2px solid rgb(0, 66, 124);\n"
      "}\n"
      "QLineEdit:focus {\n"
      "	border: 2px solid rgb(206, 206, 206);\n"
      "	color: rgb(200, 200, 200);\n"
      "}\n"
      "QPushButton {\n"
      "	border: 2px solid rgb(45, 45, 45);\n"
      "	border-radius: 10px;\n"
      "	padding: 15px;\n"
      "	background-color:rgb(14, 13, 24);\n"
      "	color: rgb(255, 255, 255);\n"
      "}\n"
      "QPushButton:hover {\n"
      "	border: 2px solid rgb(0, 66, 124);\n"
      "}\n"
      "QLabel{\n"
      "	border:3px solid  rgb(45, 45, 45);\n"
      "	border-radius: 10px;\n"
      "	\n"
      "	background-color: rgb(6, 63, 104);\n"
      "	padding: 15px;\n"
      "}\n"
  )
