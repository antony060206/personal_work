# Name: Antony Feng
# ccid: zfeng8
# studentId: 1802829
# operating system: window 10
# python version: 3.12

import re
def validate_email(Emaillist, EmailValiditylist, cond1, cond2, specialchar ):
    for i in Emaillist:

        if i.find("@") == -1 or i.find(".") == -1:
            EmailValiditylist.append("Invalid")

        else:
            Refcondchecklist = re.split(r'[.@]', i[::-1], maxsplit=2)
            condchecklist = [Refcondchecklist[::-1] for Refcondchecklist in Refcondchecklist]
            special_Char = False

            for x in specialchar:
                if condchecklist[2].find(x) != -1:
                    special_Char = True

            if special_Char == True or condchecklist[0] not in cond1:
                EmailValiditylist.append("Invalid")
            else:
                if condchecklist[1] in cond2:
                    EmailValiditylist.append("Forbidden")
                else:
                    EmailValiditylist.append("Valid")

        condchecklist.clear()

    return EmailValiditylist

def main():
    # Takes in the input and stores the email addresses in a list
    Emaillist = list(input().split())
    EmailValiditylist = []

    cond1 = ["com", "ca", "org", "net", "gov", "edu"]
    cond2 = ["scam", "spam", "fakeemail", "trashmail", "pleasenotspam", "therealtaylorswift", "sendmoney"]
    specialchar = ["!", "#", "$", "%", "^", "&", "*", "(", ")", "+", "?", "_", "=", "<", ">", "/", "@"]

    # Validate each email here
    print(*validate_email(Emaillist, EmailValiditylist, cond1, cond2, specialchar), sep="\n")

if __name__ == "__main__":
    main()
