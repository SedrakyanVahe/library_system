"""
ABSTARCT:
Online Library Management System is a system which maintains the information 
about the books present in the library, their authors, the members of library to 
whom books are issued, library staff and all. 
Owing to the advancement of technology, organization of an Online Library 
becomes much simple. The Online Library Management has been designed to 
computerize and automate the operations performed over the information about the 
members, book issues and returns and all other operations. This computerization of 
library helps in many instances of its maintenances. It reduces the workload of 
management as most of the manual work done is reduced

PRODUCT DESCRIPTION:  
Library Management System is a computerized system which helps  
user to manage the library daily activity in electronic format. It reduces  
the risk of paper work such as file lost, file damaged and time consuming.  
It can help user to manage the transaction or record more effectively and time-  
saving
"""
import sys
from PyQt5.QtWidgets import QApplication
from main_window import MainWindow

if __name__ == "__main__":
  app = QApplication(sys.argv)
  window = MainWindow()
  sys.exit(app.exec_())
else:
  print(__name__, " ")
