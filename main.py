import instaloader
loader = instaloader.Instaloader()
login_user = input("Enter username: ")
login_pwd = input("Enter password: ")
loader.login(login_user, login_pwd)
user = input("Enter username of profile you'd like to search up: ")
profile = instaloader.Profile.from_username(loader.context, user)
profile_followers = []
profile_following = []


def not_following_back():
    global profile_following, profile_followers

    if len(profile_followers) == 0:
        profile_followers = list(profile.get_followers())
        print(f"...retrieved {len(profile_followers)} followers")

    if len(profile_following) == 0:
        profile_following = list(profile.get_followees())
        print(f"...retrieved {len(profile_following)} following")

    set_followers = {f.username for f in profile_followers}
    print("Created set of followers. Looking through following...")

    for f in profile_following:
        if f.username not in set_followers:
            print(f.username)

cmd = ""
while cmd != "q":
    cmd = input("Enter u to change searched user\n"
                "Enter n for followers who don't follow back\n"
                "Enter f1 for number of followers\n"
                "Enter f2 for number of following\n"
                "Enter q to quit\n")

    if cmd == "q":
        print("Shutting down, bye!")
        quit(0)
    if cmd == "u":
        user = input("Enter username of profile you'd like to search up: ")
        profile = instaloader.Profile.from_username(loader.context, user)
        profile_followers = []
        profile_following = []
    if cmd == "n":
        not_following_back()
    if cmd == "f1":
        print(f"{len(profile_followers)} followers")
        if len(profile_followers) == 0:
            print("You may want to run \"n\" first.")
    if cmd == "f2":
        print(f"{len(profile_following)} following")
        if len(profile_following) == 0:
            print("You may want to run \"n\" first.")

    print("\n")

