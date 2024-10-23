import os
import traceback
import sys
import subprocess
import platform

# Get the folder paths
inputFolder = os.path.join(os.getcwd(), "Input")
expectedFolder = os.path.join(os.getcwd(), "Expected")
outputFolder = os.path.join(os.getcwd(), "Output")
errorsFolder = os.path.join(os.getcwd(), "Error")
solutionPath = os.path.join(os.getcwd(), "solutionQuestion2.py")

if not os.path.exists(outputFolder):
    os.mkdir(outputFolder)

if not os.path.exists(errorsFolder):
    os.mkdir(errorsFolder)
failedCases = []

# This loop will go through each file in the input folder and run the solution with
# that file as input. It will then check if the solution failed with an error,
# if not, it will check the output against the expected output
for file in os.listdir(inputFolder):
    inputFile = os.path.join(inputFolder, file)
    expectedFile = os.path.join(expectedFolder, file)
    outputFile = os.path.join(outputFolder, file)
    errorsFile = os.path.join(errorsFolder, file)
    
    inputFd = open(inputFile, "r")
    outputFd = open(outputFile, "w")
    errorFd = open(errorsFile, "w")

    python = "python3"
    if platform.system() == "Windows":
        python = "python"
    
    proc = subprocess.Popen([python, solutionPath], stdin=inputFd,
                            stdout=outputFd, stderr=errorFd)

    # Arbitrary timeout of 5 minutes, the solution shouldn't time out
    timeout = 300
    try:
        proc.wait(timeout=timeout)

        if proc.returncode == 0:
            # Compare the output if it ran sucessfully
            outputFd.close()
            
            outLines = []
            with open(outputFile, "r") as f:
                for line in f.readlines():
                    outLines.append(line.rstrip())
            
            expectedLines = []
            with open(expectedFile, "r") as f:
                for line in f.readlines():
                    expectedLines.append(line.rstrip())

            for idx in range(len(expectedLines)):
                try:
                    if outLines[idx] != expectedLines[idx]:
                        failedCases.append(file)
                        print(f"\nOutput mismatch for {file}")
                        print(f"Please check your output in Output/{file}")
                        break
                except IndexError:
                        failedCases.append(file)
                        print(f"\nOutput mismatch for {file}")
                        print(f"Please check your output in Output/{file}")
                        break
        else:
            # Failed with error, print error info
            print(f"\nSolution failed with error on {file}")
            print("Please check the corresponding Output and Error files")
            failedCases.append(file)

    except subprocess.TimeoutExpired:
        # Timed out, print info in case there is some output
        print(f"\nSolution timed out on {file}, in {timeout} seconds")
        proc.kill()
        print("Please check the corresponding Output and Error files")
        failedCases.append(file)

if len(failedCases) > 0:
    print("Failed test cases:")
    for file in failedCases:
        print(file)
else:
    print("All tests passed!")

