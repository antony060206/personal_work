import re

def validate_email(email):
    Emaillist = email.split(" ")
    EmailValiditylist = []

    cond1 = ["com", "ca","org", "net", "gov", "edu"]
    cond2 = ["scam", "spam", "fakeemail", "trashmail", "pleasenotspam", "therealtaylorswift", "sendmoney"]
    specialchar = ["!", "#", "$" ,"%" ,"^" ,"&", "*" ,"(", ")", "+" ,"?", "_", "=","<", ">", "/", "@"]

    for i in Emaillist:

        if i.find("@") == -1 or i.find(".") == -1:
            EmailValiditylist.append("Invalid")

        else:
            Refcondchecklist = re.split(r'[.@]', i[::-1], maxsplit=2 )
            condchecklist = [Refcondchecklist[::-1] for Refcondchecklist in Refcondchecklist]
            special_Char = False

            print(condchecklist)

            for x in specialchar:
                if condchecklist[2].find(x) != -1:
                    special_Char = True

            if  special_Char == True or condchecklist[0] not in cond1:
                EmailValiditylist.append("Invalid")
            else:
                if condchecklist[1] in cond2:
                    EmailValiditylist.append("Forbidden")
                else:
                    EmailValiditylist.append("Valid")

        condchecklist.clear()

    return EmailValiditylist


Email = input("please enter the email: ")
print(*validate_email(Email), sep = "\n")