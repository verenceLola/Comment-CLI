"""App selection inputs"""

choice1 = input("To use this app please follow th11e guide bellow: \n Press: \n 1.To signup \n 2.To login \n")

from src.users import User

userAO = User()

# def comment_choices():
#     comment_choice=input("To create comment: \n Press:\n 1.To add comment \n 2.To edit comment")

if int(choice) == 1:
    userAO.save()
    #comment_choices()

elif int(choice) == 2:
    userAO.login()


    