def get_number_participants():
    n_participants = -1
    while True:
        try:
            n_participants = int(input("Please enter a number: "))
            if(n_participants < 3):
                print("3 participants are require")
            else:
                break
        except ValueError:
            print("That was no valid number. Try again...")
    return n_participants

def get_participants():
    participants_list = []
    n_participants = get_number_participants()
    print("Getting participants...")
    counter = 0
    while True:
        if counter == n_participants:
            break
        try:
            participant = input("Please enter a participant, name and email sepparated by comas\nExample: name,name@email.com:\n")
            #verify correct imput
            participants_list.append(creat_tuple_info(participant))
            counter +=1
        except ValueError:
            print("That was no valid number. Try again...")

    print(participants_list)

def creat_tuple_info(participant_info):
    try:
        x = participant_info.split(", ")
        print(x)
        participant = ("","")

        if(len(x) == 2):
            participant = (x[0], x[1])
            # TODO: check regular expresions name and email
            return participant
    except ValueError:
        print("Invalid participant info. Try again...")

def generate_friend():
    # we make the random friend per user
    print("Getting participnts...")
def send_mails():
    print("sending mails...")

if __name__ == "__main__":
    get_participants()
    get_participants()