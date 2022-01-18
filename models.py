from PyQt5.QtCore import QCoreApplication, QDateTime, Qt, QRegExp
from PyQt5.QtGui import QRegExpValidator
from PyQt5.QtWidgets import (
    QDialog,
    QDialogButtonBox,
    QFormLayout,
    QLineEdit,
    QMessageBox,
    QVBoxLayout,
    QDateTimeEdit,
    QComboBox,
    QCompleter,
)
from re import match
from mysql_dbconfig import db
from app_rc import languages_lst_lower

# styles for success and errors
successStyle = "border:3px solid  rgb(0, 255, 255);border-radius: 10px;"
errorStyle = "border:3px solid  rgb(255, 0, 0);border-radius: 10px;"

try:
    mycursor = db.cursor()
    mycursor.execute("SELECT section_name FROM Sections;")
    section_names = mycursor.fetchall()
    section_names_lst = []
    for i in section_names:
        section_names_lst.append(i[0])
except:
    print("CONNECTION ERROR")

#################################################################################
# dialog for new user
#################################################################################
class New_user_dialog(QDialog):
    """Add User dialog."""

    def __init__(self, parent=None):
        """Initializer."""
        super().__init__()
        self.setWindowTitle("Add User")
        self.layout = QVBoxLayout()
        self.setLayout(self.layout)
        self.data = None
        self.setup_UI()

    def setup_UI(self):
        """Setup the Add User dialog's GUI."""
        #################################################################################
        # Create line edits for data fields for add
        #################################################################################
        self.name_field = QLineEdit()
        self.name_field.setObjectName("Name")
        self.surname_field = QLineEdit()
        self.surname_field.setObjectName("Surname")
        self.birth_day_field = QDateTimeEdit(self)
        self.birth_day_field.setDateTime(QDateTime.currentDateTime())
        self.birth_day_field.setDisplayFormat("yyyy-MM-dd")
        self.email_field = QLineEdit()
        self.email_field.setObjectName("Email")
        self.password_field = QLineEdit()
        self.password_field.setObjectName("Password")
        self.password_field.setEchoMode(QLineEdit.Password)

        #################################################################################
        # Add standard buttons to the dialog and connect them
        #################################################################################
        self.buttons_box = QDialogButtonBox(self)
        self.buttons_box.setOrientation(Qt.Horizontal)
        self.buttons_box.setStandardButtons(
            QDialogButtonBox.Ok | QDialogButtonBox.Cancel
        )
        self.buttons_box.accepted.connect(self.accept)
        self.buttons_box.rejected.connect(self.reject)

        #################################################################################
        # Lay out the data fields
        #################################################################################
        layout = QFormLayout()
        layout.addRow("Name:                            ", self.name_field)
        layout.addRow("Surname:                      ", self.surname_field)
        layout.addRow("Birth Day:                     ", self.birth_day_field)
        layout.addRow("Email:                             ", self.email_field)
        layout.addRow("Password:                      ", self.password_field)
        self.layout.addLayout(layout)
        self.layout.addWidget(self.buttons_box)

    #################################################################################
    # Accept the data provided through the dialog
    #################################################################################
    def accept(self):
        """Accept the data provided through the dialog."""

        self.data = []
        for field in (
            self.name_field,
            self.surname_field,
            self.birth_day_field,
            self.email_field,
            self.password_field,
        ):
            self.name_field.setStyleSheet(successStyle)
            self.surname_field.setStyleSheet(successStyle)
            self.email_field.setStyleSheet(successStyle)
            self.password_field.setStyleSheet(successStyle)

            # validation for name
            if not self.name_field.text() or not match(
                r"[A-Za-z]{2,25}( [A-Za-z]{2,25})?", self.name_field.text()
            ):
                self.name_field.setStyleSheet(errorStyle)
                QMessageBox.critical(
                    self,
                    "Error!",
                    f"Incorrect User {self.name_field.objectName()}",
                )
                self.data = None  # Reset .data
                return

            # validation for surname
            elif not self.surname_field.text() or not match(
                r"[A-Za-z]{2,25}( [A-Za-z]{2,25})?", self.surname_field.text()
            ):
                self.surname_field.setStyleSheet(errorStyle)
                QMessageBox.critical(
                    self,
                    "Error!",
                    f"Incorrect User {self.surname_field.objectName()}",
                )
                self.data = None  # Reset .data
                return

            # validation for email
            elif not self.email_field.text() or not match(
                r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b",
                self.email_field.text(),
            ):
                self.email_field.setStyleSheet(errorStyle)
                QMessageBox.critical(
                    self,
                    "Error!",
                    f"Incorrect User {self.email_field.objectName()}",
                )
                self.data = None  # Reset .data
                return

            # validation for password
            elif not self.password_field.text() or not match(
                r"[A-Za-z0-9@#$%^&+=]{6,}", self.password_field.text()
            ):
                self.password_field.setStyleSheet(errorStyle)
                QMessageBox.critical(
                    self,
                    "Error!",
                    f"Incorrect User {self.password_field.objectName()}",
                )
                self.data = None  # Reset .data
                return
            # append inputs data
            self.data.append(field.text())

        if not self.data:
            return
        super().accept()


#################################################################################
# dialog for adding books
#################################################################################
class Add_book_dialog(QDialog):
    """Add Book dialog."""

    def __init__(self, parent=None):
        """Initializer."""
        super().__init__()
        self.setWindowTitle("Add Book")
        self.layout = QVBoxLayout()
        self.setLayout(self.layout)
        self.data = None
        self.setup_UI()

    def setup_UI(self):
        """Setup the Add Book dialog's GUI."""
        #################################################################################
        # Create line edits for data fields for add
        #################################################################################
        self.name_field = QLineEdit()
        self.name_field.setObjectName("Name")
        self.author_field = QLineEdit()
        self.author_field.setObjectName("Author")
        self.description_field = QLineEdit()
        self.description_field.setObjectName("Description")
        self.publication_date_field = QDateTimeEdit(self)
        self.publication_date_field.setDateTime(QDateTime.currentDateTime())
        self.publication_date_field.setDisplayFormat("yyyy-MM-dd")
        self.language_field = QLineEdit()
        self.language_field.setObjectName("Language")
        language_rx = QRegExp("^[a-zA-Z]{3}$")
        self.language_field.setValidator(QRegExpValidator(language_rx))

        # for language autocomplete

        completer2 = QCompleter(languages_lst_lower)
        self.language_field.setCompleter(completer2)

        self.pages_count_field = QLineEdit()
        self.pages_count_field.setObjectName("Pages Count")
        pages_count_rx = QRegExp("\d+")
        self.pages_count_field.setValidator(QRegExpValidator(pages_count_rx))

        self.photo_field = QLineEdit()
        self.photo_field.setObjectName("Photo")
        self.ISBN13_field = QLineEdit()
        self.ISBN13_field.setObjectName("ISBN13")

        ISBN13_rx = QRegExp("[0-9]+[-\ ]?[0-9]+[-\ ]+[0-9]+[-\ ]?[0-9]+[-\ ]?")
        self.ISBN13_field.setValidator(QRegExpValidator(ISBN13_rx))

        #################################################################################
        # Combo box for genres
        #################################################################################
        self.genre_field = QComboBox()
        self.genre_field.setObjectName("genre_field")
        self.genre_field.setStyleSheet(
            "QComboBox { combobox-popup: 0; }"
        )  # for combo box scroll bar

        mycursor.execute(
            "SELECT CONCAT(genre_name, genre_id) AS WHOLENAME  FROM Genres;"
        )
        genre_names = mycursor.fetchall()
        genre_names_lst = []
        for i in genre_names:
            genre_names_lst.append(i[0])

        for index, name in enumerate(genre_names_lst):
            self.genre_field.addItem("")
            self.genre_field.setItemText(
                index, QCoreApplication.translate("MainWindow", name)
            )

        #################################################################################
        # Combo box for ratting
        #################################################################################
        self.ratting_field = QComboBox()
        self.ratting_field.setObjectName("Ratting")
        self.ratting_field.setStyleSheet(
            "QComboBox { combobox-popup: 0; }"
        )  # for combo box scroll bar
        self.ratting_field.addItems(["1", "2", "3", "4", "5"])

        #################################################################################
        # Add standard buttons to the dialog and connect them
        #################################################################################
        self.buttons_box = QDialogButtonBox(self)
        self.buttons_box.setOrientation(Qt.Horizontal)
        self.buttons_box.setStandardButtons(
            QDialogButtonBox.Ok | QDialogButtonBox.Cancel
        )

        self.buttons_box.accepted.connect(self.accept)
        self.buttons_box.rejected.connect(self.reject)

        #################################################################################
        # Lay out the data fields
        #################################################################################
        layout = QFormLayout()
        layout.addRow("Name:                       ", self.name_field)
        layout.addRow("Author:                     ", self.author_field)
        layout.addRow("Description:            ", self.description_field)
        layout.addRow("Publication Date:  ", self.publication_date_field)
        layout.addRow("Language:                ", self.language_field)
        layout.addRow("Pages Count:           ", self.pages_count_field)
        layout.addRow("Photo:                       ", self.photo_field)
        layout.addRow("ISBN13:                     ", self.ISBN13_field)
        layout.addRow("Ratting:                    ", self.ratting_field)
        layout.addRow("Genre:                       ", self.genre_field)

        self.layout.addLayout(layout)
        self.layout.addWidget(self.buttons_box)

    #################################################################################
    # Accept the data provided through the dialog
    #################################################################################
    def accept(self):
        """Accept the data provided through the dialog."""

        self.data = []
        for field in (
            self.name_field,
            self.author_field,
            self.description_field,
            self.publication_date_field,
            self.language_field,
            self.pages_count_field,
            self.photo_field,
            self.ISBN13_field,
        ):

            self.name_field.setStyleSheet(successStyle)
            self.author_field.setStyleSheet(successStyle)
            self.description_field.setStyleSheet(successStyle)
            self.language_field.setStyleSheet(successStyle)
            self.pages_count_field.setStyleSheet(successStyle)
            self.photo_field.setStyleSheet(successStyle)
            self.ISBN13_field.setStyleSheet(successStyle)
            #################################################################################
            # Add Book validations
            #################################################################################
            if not self.name_field.text() or not match(
                r"[A-Za-z]{2,25}( [A-Za-z]{2,25})?", self.name_field.text()
            ):
                self.name_field.setStyleSheet(errorStyle)
                QMessageBox.critical(
                    self,
                    "Error!",
                    f"Incorrect  Book {self.name_field.objectName()}",
                )
                self.data = None  # Reset .data
                return

            elif not self.author_field.text() or not match(
                r"[A-Za-z]{2,25}( [A-Za-z]{2,25})?", self.name_field.text()
            ):
                self.author_field.setStyleSheet(errorStyle)
                QMessageBox.critical(
                    self,
                    "Error!",
                    f"Incorrect  Book {self.author_field.objectName()}",
                )
                self.data = None  # Reset .data
                return

            elif not self.description_field.text():
                self.description_field.setStyleSheet(errorStyle)
                QMessageBox.critical(
                    self,
                    "Error!",
                    f"Incorrect  Book {self.description_field.objectName()}",
                )
                self.data = None  # Reset .data
                return

            elif not self.language_field.text():
                self.language_field.setStyleSheet(errorStyle)
                QMessageBox.critical(
                    self,
                    "Error!",
                    f"Incorrect  Book {self.language_field.objectName()}",
                )
                self.data = None  # Reset .data
                return

            elif not self.photo_field.text() or not match(
                "(https?:\/\/(?:www\.|(?!www))[a-zA-Z0-9][a-zA-Z0-9-]+[a-zA-Z0-9]\.[^\s]{2,}|www\.[a-zA-Z0-9][a-zA-Z0-9-]+[a-zA-Z0-9]\.[^\s]{2,}|https?:\/\/(?:www\.|(?!www))[a-zA-Z0-9]+\.[^\s]{2,}|www\.[a-zA-Z0-9]+\.[^\s]{2,})",
                self.photo_field.text(),
            ):
                self.photo_field.setStyleSheet(errorStyle)
                QMessageBox.critical(
                    self,
                    "Error!",
                    f"Incorrect  Book {self.photo_field.objectName()}",
                )
                self.data = None  # Reset .data
                return

            elif not self.ISBN13_field.text() or not match(
                "[0-9]+[-\ ]?[0-9]+[-\ ]+[0-9]+[-\ ]?[0-9]+[-\ ]?",
                self.ISBN13_field.text(),
            ):
                self.ISBN13_field.setStyleSheet(errorStyle)
                QMessageBox.critical(
                    self,
                    "Error!",
                    f"Incorrect  Book {self.ISBN13_field.objectName()}",
                )
                self.data = None  # Reset .data
                return

            # append inputs data
            self.data.append(field.text())

        # append ratting and genre input data from combo box
        self.data.append(self.ratting_field.currentText())
        self.data.append(self.genre_field.currentText())
        if not self.data:
            return
        super().accept()


#################################################################################
# dialog for updating books
#################################################################################
class Update_book_dialog(QDialog):
    """Add Book dialog."""

    def __init__(self, parent=None):
        """Initializer."""
        super().__init__()
        self.setWindowTitle("Update Book")
        self.layout = QVBoxLayout()
        self.setLayout(self.layout)
        self.data = None
        self.setup_UI()

    def setup_UI(self):
        """Setup the Update Book dialog's GUI."""
        #################################################################################
        # Create line edits for data fields for add
        #################################################################################

        self.book_id_field = QLineEdit()
        self.book_id_field.setObjectName("book_id")
        self.book_id_field.setPlaceholderText("BOOK ID")
        book_id_rx = QRegExp("\d+")
        self.book_id_field.setValidator(QRegExpValidator(book_id_rx))

        self.update_to_field = QLineEdit()
        self.update_to_field.setObjectName("update_to_field")
        self.update_to_field.setPlaceholderText("UPDATE TO")

        #################################################################################
        # Combo box for book fields
        #################################################################################
        self.selected_column_field = QComboBox()
        self.selected_column_field.setStyleSheet(
            "QComboBox { combobox-popup: 0; }"
        )  # for combo box scroll bar
        self.selected_column_field.setObjectName("selected_column_field")
        column_names_lst = [
            "book_name",
            "author",
            "description",
            "publication_date",
            "language",
            "pages_count",
            "photo",
            "ISBN13",
            "ratting",
        ]
        for index, name in enumerate(column_names_lst):
            self.selected_column_field.addItem("")
            self.selected_column_field.setItemText(
                index, QCoreApplication.translate("MainWindow", name)
            )

        #################################################################################
        # Add standard buttons to the dialog and connect them
        #################################################################################
        self.buttons_box = QDialogButtonBox(self)
        self.buttons_box.setOrientation(Qt.Horizontal)
        self.buttons_box.setStandardButtons(
            QDialogButtonBox.Ok | QDialogButtonBox.Cancel
        )

        self.buttons_box.accepted.connect(self.accept)
        self.buttons_box.rejected.connect(self.reject)

        #################################################################################
        # Lay out the data fields
        #################################################################################
        layout = QFormLayout()
        layout.addRow("BOOK ID:          ", self.book_id_field)
        layout.addRow("WHICH FIELD: ", self.selected_column_field)
        layout.addRow("UPDATE TO:     ", self.update_to_field)

        self.layout.addLayout(layout)
        self.layout.addWidget(self.buttons_box)

    #################################################################################
    # Accept the data provided through the dialog
    #################################################################################
    def accept(self):
        """Accept the data provided through the dialog."""
        self.data = []

        if not self.update_to_field.text() or not self.book_id_field.text():
            QMessageBox.critical(
                self,
                "Error!",
                f"You must provide a all fields ",
            )
            self.data = None
            return
        for field in (
            self.selected_column_field,
            self.update_to_field,
            self.book_id_field,
        ):

            if isinstance(field, QLineEdit):
                self.data.append(field.text())

            elif isinstance(field, QComboBox):
                self.data.append(field.currentText())

        if not self.data:
            return

        super().accept()


#################################################################################
# dialog for deleting books
#################################################################################
class Delete_book_dialog(QDialog):
    """Delete Books dialog."""

    def __init__(self, parent=None):
        """Initializer."""
        super().__init__()
        self.setWindowTitle("Delete Book")
        self.layout = QVBoxLayout()
        self.setLayout(self.layout)
        self.data = None
        self.setup_UI()

    def setup_UI(self):
        """Setup the Delete Books dialog's GUI."""

        #################################################################################
        # Create line edits for data fields for add
        #################################################################################
        self.id_field = QLineEdit()
        self.id_field.setObjectName("Id")
        id_rx = QRegExp("\d+")
        self.id_field.setValidator(QRegExpValidator(id_rx))

        #################################################################################
        # Add standard buttons to the dialog and connect them
        #################################################################################
        self.buttons_box = QDialogButtonBox(self)
        self.buttons_box.setOrientation(Qt.Horizontal)
        self.buttons_box.setStandardButtons(
            QDialogButtonBox.Ok | QDialogButtonBox.Cancel
        )

        self.buttons_box.accepted.connect(self.accept)
        self.buttons_box.rejected.connect(self.reject)

        #################################################################################
        # Lay out the data fields
        #################################################################################
        layout = QFormLayout()
        layout.addRow("ID:", self.id_field)

        self.layout.addLayout(layout)
        self.layout.addWidget(self.buttons_box)

    #################################################################################
    # Accept the data provided through the dialog
    #################################################################################
    def accept(self):
        """Accept the data provided through the dialog."""
        self.data = []
        # for field in (self.id_field):
        if not self.id_field.text():
            QMessageBox.critical(
                self,
                "Error!",
                f"You must provide a book {self.id_field.objectName()}",
            )
            self.data = None  # Reset .data
            return

        self.data.append(self.id_field.text())

        if not self.data:
            return
        super().accept()


#################################################################################
# dialog for Aadding favorite books
#################################################################################
class Add_favorite_dialog(QDialog):
    """Add Favorite dialog."""

    def __init__(self, parent=None):
        """Initializer."""
        super().__init__()
        self.setWindowTitle("Add Favprite Book")
        self.layout = QVBoxLayout()
        self.setLayout(self.layout)
        self.data = None
        self.setup_UI()

    def setup_UI(self):
        """Setup the Add Favorite Book dialog's GUI."""
        #################################################################################
        # Create combo boxes for adding data
        #################################################################################
        # combo  box for books
        mycursor.execute("SELECT CONCAT(user_name, user_id) AS WHOLENAME FROM Users;")
        user_names = mycursor.fetchall()
        user_names_lst = []
        for i in user_names:
            user_names_lst.append(i[0])
        self.user_name_field = QComboBox()
        self.user_name_field.setStyleSheet(
            "QComboBox { combobox-popup: 0; }"
        )  # for com box scroll bar
        self.user_name_field.setObjectName("user_name_field")
        for index, name in enumerate(user_names_lst):
            self.user_name_field.addItem("")
            self.user_name_field.setItemText(
                index, QCoreApplication.translate("MainWindow", name)
            )

        # combo  box for books
        mycursor.execute("SELECT CONCAT(book_name, book_id) AS WHOLENAME  FROM Books;")
        book_names = mycursor.fetchall()
        book_names_lst = []
        for i in book_names:
            book_names_lst.append(i[0])
        self.book_name_field = QComboBox()
        self.book_name_field.setStyleSheet(
            "QComboBox { combobox-popup: 0; }"
        )  # for com box scroll bar
        self.book_name_field.setObjectName("book_name_field")
        for index, name in enumerate(book_names_lst):
            self.book_name_field.addItem("")
            self.book_name_field.setItemText(
                index, QCoreApplication.translate("MainWindow", name)
            )

        #################################################################################
        # Add standard buttons to the dialog and connect them
        #################################################################################
        self.buttons_box = QDialogButtonBox(self)
        self.buttons_box.setOrientation(Qt.Horizontal)
        self.buttons_box.setStandardButtons(
            QDialogButtonBox.Ok | QDialogButtonBox.Cancel
        )

        self.buttons_box.accepted.connect(self.accept)
        self.buttons_box.rejected.connect(self.reject)

        #################################################################################
        # Lay out the data fields
        #################################################################################
        layout = QFormLayout()
        layout.addRow("User Name:                 ", self.user_name_field)
        layout.addRow("Book Name:                 ", self.book_name_field)

        self.layout.addLayout(layout)
        self.layout.addWidget(self.buttons_box)

    #################################################################################
    # Accept the data provided through the dialog
    #################################################################################
    def accept(self):
        """Accept the data provided through the dialog."""

        self.data = []
        for field in (self.user_name_field, self.book_name_field):
            if not self.book_name_field.currentText():
                QMessageBox.critical(
                    self,
                    "Error!",
                    f"You must provide a book {self.book_name_field.objectName()}",
                )
                self.data = None  # Reset .data
                return

            self.data.append(field.currentText())

        # append book name
        self.data.append(self.book_name_field.currentText())

        if not self.data:
            return
        super().accept()
