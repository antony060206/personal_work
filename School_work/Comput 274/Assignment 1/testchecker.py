import AntonysolutionQuestion1
from AntonysolutionQuestion1 import Email
import testfiles

f = open("testfiles/test_case10.txt", "r")
testcase = (f.read()).split("\n")
testcase.pop()

print(testcase)
print(AntonysolutionQuestion1.validate_email(Email))
if(testcase == AntonysolutionQuestion1.validate_email(Email)):
    print("Same")
else:
    print("not same")