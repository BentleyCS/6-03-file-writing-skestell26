from CSP_6_03_Writing_to_files import writeFile, sortNames, highScore
import random


def test_writeFile():
    test_list = ["Apple", "Banana", "Cherry"]
    writeFile(test_list, "test_output.txt")

    with open("test_output.txt", "r") as f:
        content = f.read().strip().split("\n")

    assert content == test_list, "writeFile failed: contents do not match input list"


def test_sortNames():
    # Create unsorted file
    writeFile(["Zoe", "Alice", "Mark"], "names.txt")
    sortNames("names.txt", "namesNew.txt")

    with open("namesNew.txt", "r") as f:
        result = f.read().strip().split("\n")

    assert result == ["Alice", "Mark", "Zoe"], "sortNames failed: names not sorted correctly"


def test_highScore():
    # Reset scores file
    writeFile([50, 100], "scores.txt")

    # Add new score
    avg = highScore(50)

    # Scores are now [50, 100, 50], average = 200/3
    expected_avg = 200 / 3
    assert abs(avg - expected_avg) < 1e-6, f"highScore failed: expected {expected_avg}, got {avg}"
