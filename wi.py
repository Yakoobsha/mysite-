import random  
import string
import pyautogui

'''Hello guys in this we are going to make a password cracker using Python.'''

chars = ' a b c d e f g h i j k l m n o p q r s t u v w x y z '

chars_list = list(chars)

password = pyautogui.password("Enter your password : ")

guess_password = ""

while (guess_password != password):
     guess_password = random.choices(chars_list, k=len(password))
     print("==========" + str(guess_password) + "===========")
     if (guess_password==password):

          print("Your password is : " +"" .join(guess_password))
          break