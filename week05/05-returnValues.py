def get_username(player_number):
    username = input(f"Please enter the username for player {player_number}: ")
    return username


def get_score(username, round_num):
    return int(input(f"Please give the score of {username} on round {round_num}: "))


def print_score(username, round_1_points, round_2_points):
    total_points = round_1_points + round_2_points
    average_points = total_points / 2
    print(f"{username} scored an average of {average_points} points, resulting in a total of {total_points} points.")


username1 = get_username(1)
username2 = get_username(2)

# Get Scores for Round 1
print()
print("Round 1")
user1_scores = []
user2_scores = []
user1_scores.append(get_score(username1, 1))
user2_scores.append(get_score(username2, 1))

# Get Scores for Round 2
print()
print("Round 2")
user1_scores.append(get_score(username1, 2))
user2_scores.append(get_score(username2, 2))

# Print score statistics
print()
print_score(username1, user1_scores[0], user1_scores[1])
print_score(username2, user2_scores[0], user2_scores[1])