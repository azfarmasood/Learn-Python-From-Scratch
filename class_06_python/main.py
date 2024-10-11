# x: int = 10
# if x > 5:
#     print("x is greater than 5")
# else:
#     print("x is not greater than 5")
    

# x: int = 4
# if x > 5:
#     print("x is greater than 5")
# elif x == 5:
#     print("x is equal to 5")
# else:
#     print("x is less than 5")

# x: int = 5
# y: int = 6
# if x > 5:
#     if y > 5:
#         print("x and y are both greater than 5")
#     else:
#         print("x is greater than 5 but y is not")
# elif x == 5:
#     if y == 5:
#         print("x and y are both equal to 5")
#     else:
#         print("x is equal to 5 but y is not")
# else:
#     print("x is less than 5")
    
    
# x: int = 10
# y: str = "Hello"
# z: float = 3.14

# print(x, y, z)

# from typing import Union

# def greet(name:Union[str, None] = None) -> str:
#     if name is None:
#         return "Name not Found!"
#     else:
#         return f"Hello {name}"
# print(greet())
# print(greet("Azfar"))

# def greet(name:Union[str, None] = None) -> str:
#     if name:
#         return f"Name: {name}"
#     else:
#         return "Name not Found!"

# # print(greet())
# print(greet("Azfar"))

# from typing import Union

# # db: list[str] = ["Azfar", "Masood", "Ali", "Ahmed"]
# percentages: list[float] = [84.4, 85, 99.4, 55]
# roll_no: list[Union[int, float]] = [1, 2, 3, 4]
# grades: list[str] = ["A+", "A+", "B", "C"]

# # print(list(zip(db, roll_no, grades)))

# data_base = list(zip(roll_no,percentages, grades))

# print(data_base)
