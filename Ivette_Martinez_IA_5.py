
def get_average():
    """Ask for three test scores, convert to float, compute and return average."""
    # Input with minimal validation loop: re-prompt if a non-number is entered
    count = 0
    total = 0.0
    while count < 3:  # repetition with while (no for loop per instructions)
        raw = input(f"Enter score #{count + 1}: ")
        try:
            score = float(raw)
            total = total + score
            count = count + 1
        except ValueError:
            print(f"Oops, '{raw}' is not a number. Please try again.")
    # Processing: compute average using the provided formula
    average = total / 3
    return average  # return result to main()

def check_average(avg):
    """Decide which message to display based on avg. Only displays (no return)."""
    # Decision logic with if/elif/else (Week 4: decisions)
    if avg > 95:
        print(f"Average: {avg:.2f} -> Congratulations! You did great!")
    elif avg >= 85 and avg <= 95:
        print(f"Average: {avg:.2f} -> You did great, but did not reach the Top High.")
    elif avg >= 70 and avg <= 84:
        print(f"Average: {avg:.2f} -> Good effort, but you could do better.")
    else:  # below 70
        print(f"Average: {avg:.2f} -> You need to study harder next time.")

def main():
    """Program entry point."""
    print("=== Problem 1: Test Average ===")
    avg = get_average()       # get inputs & compute average
    check_average(avg)        # show message based on average

# Only run main() when this file is executed directly.
if __name__ == "__main__":
    main()
