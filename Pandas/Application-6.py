import os
import fnmatch
from sys import *
import xlsxwriter

def ExcelCreate(filename):
       workbook = xlsxwriter.Workbook(filename)

       worksheet = workbook.add_worksheet()

       worksheet.write("A1","Name")
       worksheet.write("B1","Collage")
       worksheet.write("C1","Mail ID")
       worksheet.write("D1","Mobile")

       workbook.close()

def main():
       print("___Welcome to our Script")

       print("Application name is : ",argv[0])

       if (len(argv) !=2):
              print("ERROR : Invalid number of Arguments")
              exist()

       if argv[1]=="h" or argv[1]=="H":
              print("HELP : This script is used to create excel file and write data into it")
              exit()

       if argv[1]=="u" or argv[1]=="U":
              print("USAGE : Application Name  Name_of_file")
              exit()
       try:
              ExcelCreate(argv[1])
       except Exception:
              print("ERROR : Invalid Input")
if __name__ == "__main__":
       main()