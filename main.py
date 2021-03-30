import re
import random

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

def creat_structure_info(participant_info):
    try:
        if(len(participant_info) == 2):
            participant = [participant_info[0], participant_info[1], -1]
            return participant
    except ValueError:
        print("Invalid participant info. Try again...")

def regex_user(participant_info):
    # cheeck if correct name and email wit re
    if (bool(re.fullmatch('[A-Za-z]{2,25}( [A-Za-z]{2,25})?', participant_info[0])) and (bool(re.fullmatch('^[a-z0-9]+[\._]?[ a-z0-9]+[@]\w+[. ]\w{2,3}$', participant_info[1])))):
        return True
    else:
        return False

def get_participants():
    participants_list = []
    n_participants = get_number_participants()
    print("Getting participants...")
    counter = 0
    while True:
        if counter == n_participants:
            break
        try:
            participant_info = []
            participant_name = input("Please enter the name of a participant: ")
            participant_email = input("Please enter the email of a participant: ")
            participant_info.append(participant_name)
            participant_info.append(participant_email)

            if(regex_user(participant_info)):
                participants_list.append(creat_structure_info(participant_info))
                counter +=1
            else:
                print("Invalid user...")
        except ValueError:
            print("Invalid user...")

    return participants_list

def generate_friend(participants_list):
    # we make the random friend per user
    print("Getting participnts...")
    randomized_list = participants_list[:]
    while True:
        random.shuffle(randomized_list)
        for a, b in zip(participants_list, randomized_list):
            if a == b:
                break
        else:
            return randomized_list
            
def assign_friend(participants, listfriends):
    friends = generate_friend(participants)
    for index, s in enumerate(participants):
        s[2] = listfriends[index][0]
    return participants

def send_mails():
    print("sending mails...")

if __name__ == "__main__":
    participants = get_participants()
    friends = generate_friend(participants)
    
    a = assign_friend(participants, friends)
    print(a)