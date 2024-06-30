# Class representing a reward account
class RewardAccount:
    def __init__(self, reward_points=0):
        self.reward_points = reward_points  # Initial reward points

    def earn_rewards(self, amount):
        # Method to earn reward points
        points = int(amount / 10)  # 1 reward point for every 10 units of currency
        self.reward_points += points
        print(f"Earned {points} reward points. Total reward points: {self.reward_points}.")

    def redeem_rewards(self, points):
        # Method to redeem reward points
        if points > self.reward_points:
            print("Insufficient reward points.")
        else:
            self.reward_points -= points
            print(f"Redeemed {points} reward points. Remaining reward points: {self.reward_points}.")
