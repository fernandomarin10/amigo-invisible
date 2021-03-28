def get_participants():
    print("Getting participants...")

    while True:
        try:
            n_participants = int(input("Please enter a number: "))
            if(n_participants < 3):
                print("Only integers > 3 are allowed")
            else:
                break
        except ValueError:
            print("Oops!  That was no valid number.  Try again...")

    print(n_participants) 
       
    print("Number of participants = {}".format(str(n_participants)))
def generate_friend():
    # we make the random friend per user
    print("Getting participnts...")
def send_mails():
    print("sending mails...")

if __name__ == "__main__":
    get_participants()