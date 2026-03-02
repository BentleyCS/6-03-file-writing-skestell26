import random

#You need to create your own test file for this assignment.
#Because we are dealing with both reading and writing to files. Your test file will be more complicated than it has been.


def writeFile(inputList, fileName):
    # Creates a file of the given name and adds each value
    # from the list to said file with each line being an index from the list.

    with open(fileName, "w") as f:
        for item in inputList:
            f.write(str(item) + "\n")


def sortNames(fileName, targetFile):
    # Read names from the source file
    with open(fileName, "r") as f:
        names = f.readlines()

    # Remove newline characters
    names = [name.strip() for name in names]

    # Sort the list
    names.sort()

    # Write sorted names to the target file
    with open(targetFile, "w") as f:
        for name in names:
            f.write(name + "\n")


def highScore(newScore: int):
    # Add the new score to scores.txt
    with open("scores.txt", "a") as f:
        f.write(str(newScore) + "\n")

    # Read all scores from the file
    with open("scores.txt", "r") as f:
        scores = f.readlines()

    # Convert scores to integers
    scores = [int(score.strip()) for score in scores]

    # Calculate and return the average
    return sum(scores) / len(scores)