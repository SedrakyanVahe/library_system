import datetime
from models import (
    QDialog,
    mycursor,
    db,
    New_user_dialog,
    Add_book_dialog,
    Update_book_dialog,
    Delete_book_dialog,
    Add_favorite_dialog,
)
from styles import *

########################################################################
# Abstarct class for app functions
########################################################################
class Functions:
    def __init__(self):
        pass

    ########################################################################
    # Functions for add new users
    ########################################################################
    def add_new_user(self):
        """Add new user into database."""
        new_user_dialog = New_user_dialog(self)
        new_user_dialog.setStyleSheet(Styles.dialog_styles_styles)
        if new_user_dialog.exec() == QDialog.Accepted:

            sql = f"INSERT INTO Users (user_name, surname, birth_day, email, password ) \
                    VALUES ( '{new_user_dialog.data[0]}', '{new_user_dialog.data[1]}', '{new_user_dialog.data[2]}','{new_user_dialog.data[3]}', '{new_user_dialog.data[4]}' )"

            mycursor.execute(sql)
            db.commit()
            print(mycursor.rowcount, "record inserted.")

    ########################################################################
    # Functions for add new books
    ########################################################################
    def add_book(self):
        """Add a book into database."""
        add_book_dialog = Add_book_dialog(self)
        add_book_dialog.setStyleSheet(Styles.dialog_styles_styles)
        if add_book_dialog.exec() == QDialog.Accepted:

            # get id
            genre_id = "".join(x for x in add_book_dialog.data[9] if x.isdigit())
            sql = f"INSERT INTO Books (book_name, author, description, publication_date, language, pages_count, photo, ISBN13, ratting, genre_id) \
                    VALUES ( '{add_book_dialog.data[0]}', '{add_book_dialog.data[1]}', '{add_book_dialog.data[2]}','{add_book_dialog.data[3]}', '{add_book_dialog.data[4]}', \
                    {int(add_book_dialog.data[5])}, '{add_book_dialog.data[6]}', '{add_book_dialog.data[7]}',{int(add_book_dialog.data[8])}, {int(genre_id)})"

            mycursor.execute(sql)
            db.commit()
            print(mycursor.rowcount, "record inserted.")

    ########################################################################
    # Functions for update books
    ########################################################################
    def update_book(self):
        """Update a book into database."""
        update_book_dialog = Update_book_dialog(self)
        update_book_dialog.setStyleSheet(Styles.dialog_styles_styles)
        if update_book_dialog.exec() == QDialog.Accepted:

            sql = f"UPDATE Books SET {update_book_dialog.data[0]} = '{update_book_dialog.data[1]}' WHERE book_id = {int(update_book_dialog.data[2])}"
            mycursor.execute(sql)
            db.commit()
            print(mycursor.rowcount, "record updated.")

    ########################################################################
    # Functions for delete books
    ########################################################################
    def delete_book(self):
        """Remove a book from the database."""
        delete_book_dialog = Delete_book_dialog(self)
        delete_book_dialog.setStyleSheet(Styles.dialog_styles_styles)

        if delete_book_dialog.exec() == QDialog.Accepted:
            sql = f"DELETE FROM Books WHERE book_id = {int(delete_book_dialog.data[0])}"
            mycursor.execute(sql)
            db.commit()
            print(mycursor.rowcount, "record(s) deleted")

    ########################################################################
    # Functions for add favorite books
    ########################################################################
    def add_favorite(self):
        """Add a favorite book into database."""

        add_favorite_dialog = Add_favorite_dialog(self)
        add_favorite_dialog.setStyleSheet(Styles.dialog_styles_styles)
        if add_favorite_dialog.exec() == QDialog.Accepted:

            # get idis
            user_id = "".join(x for x in add_favorite_dialog.data[0] if x.isdigit())
            favorite_book_id = "".join(
                x for x in add_favorite_dialog.data[1] if x.isdigit()
            )

            # get current date
            current_day = str(datetime.datetime.today().strftime("%Y-%m-%d"))

            sql = f"INSERT INTO Favorites (date, user_id, book_id ) \
                        VALUES ('{current_day}', {int(user_id)} ,'{favorite_book_id}' )"

            mycursor.execute(sql)
            db.commit()
            print(mycursor.rowcount, "record inserted.")
