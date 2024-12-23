from linkedin_api import Linkedin

api=Linkedin("tgj0464@gmail.com","Nikhil#393")
profile = input("Enter username: ")
print(api.get_profile(profile))