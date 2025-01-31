'''
Write a function (run_timing) that asks how long it took for you to run 10 km.
The function continues to ask how long (in minutes) it took for additional runs,
until the user presses Enter. At that point, the function exits--but only after
calculating and displaying the average time that the 10 km runs took.
'''

def run_timing():
    iteration = 0
    total_run = 0

    while True:
        run = input("Enter 10 km run time: ")
        if not run:
            break
        total_run += float(run)
        iteration += 1

    return f"Average of {total_run / iteration}, over {iteration} runs"

if __name__ == "__main__":
    print(run_timing())