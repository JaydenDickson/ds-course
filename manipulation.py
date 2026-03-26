import sys

def main():
   str_manip = input("enter a sentence: ")
   length = len(str_manip)
   print(length)
   last = str_manip[length-1]
   replace = str_manip.replace(last, "@")
   print(replace)
   print(str_manip[:length-4:-1])
   print(str_manip[0:3]+str_manip[length-2:length])
if __name__ == "__main__":
    main()