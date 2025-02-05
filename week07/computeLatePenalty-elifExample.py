print("The assignment is due on the Sunday")
print("On what day was the assignment turned in? Give the day of the week, or 'Early' if before Sunday")
submission_day = input()

if submission_day == 'Sunday' or submission_day == 'Early':
    print("The assignment was submitted on time, so there is no penalty")
elif submission_day == 'Monday':
    print("The assignment was a day late, 10% penalty")
elif submission_day == 'Tuesday':
    print("The assignment was 2 days late, 20% penalty")
elif submission_day == 'Wednesday':
    print("The assignment was 3 days late, 30% penalty")
elif submission_day == 'Thursday':
    print("The assignment was 4 days late, 40% penalty")
else:
    print("The submission was more than 4 days late, no points will be awarded")

