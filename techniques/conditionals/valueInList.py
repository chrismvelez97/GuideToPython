#                           How to check if a value is in a list
banned_users = ["Joe", "Alex", "Chris"]
user = "Chris"

if user in banned_users:
    print ("The user {0} is on the blacklist".format(user))

#                        How to check if a value is NOT in a list
new_user = "Don"
if new_user not in banned_users:
    print ("Congratulations {0} you are not on the blacklist".format(new_user))
