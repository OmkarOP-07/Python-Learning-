class Classroom:
    classroom_list = ["Room A101", "Room A102", "Room A103", "Room A104", "Room A105"]

    @staticmethod
    def search_classroom(class_room):
        for classroom in Classroom.classroom_list:
            if classroom.lower() == class_room.lower():
                return "Found"
        return -1

if __name__ == "__main__":
    class_room = input("Enter the classroom name to search: ")
    result = Classroom.search_classroom(class_room)

    if result == "Found":
        print(f"The classroom {class_room} is in the left wing.")
    else:
        print(f"The classroom {class_room} was not found in the left wing.")
