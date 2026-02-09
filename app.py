def main():
    task = str(input("Task : "))
    planned_time = int(input("Planned Time : "))
    actual_time = int(input('Actual Time : '))
    distraction = str(input("Distraction : "))
    root_causes = ["In the Zone.", "Estimation Error", "Minor Distraction", "Major Context Leakage"]
    rules = ["Great Work! Keep up the behaviour.", "Add 10% Buffer. Do not change behaviour.", "Single-task with a visible timer. No App Switching.", "Remove the primary distraction physically before starting."]

    overrun_time = actual_time - planned_time

    overrun_percent = round((overrun_time/actual_time)*100, 2)

    if overrun_percent >= 0:
        print(f"Overrun : {overrun_time} min ({overrun_percent}%)\nLikely Cause : {root_causes[0]}\nRule for Tomorrow : {rules[0]}")   
    elif overrun_percent <= -10:
        print(f"Overrun : {overrun_time} min ({overrun_percent}%)\nLikely Cause : {root_causes[1]}\nRule for Tomorrow : {rules[1]}")
    elif overrun_percent <= -30:
        print(f"Overrun : {overrun_time} min ({overrun_percent}%)\nLikely Cause : {root_causes[2]}\nRule for Tomorrow : {rules[2]}")
    else:
        print(f"Overrun : {overrun_time} min ({overrun_percent}%)\nLikely Cause : {root_causes[3]}\nRule for Tomorrow : {rules[3]}")


if __name__ == "__main__":
    main()