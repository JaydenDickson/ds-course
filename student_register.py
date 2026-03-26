def main():
        number_of_students = input("Enter the number of students: ")
        with open("./reg_form", "a") as file:
            for i in range(int(number_of_students)):
                id = input("Enter the student ID: ")
                file.write(id + "....." + "\n")

if __name__ == "__main__":
    main()