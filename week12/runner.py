class MarathonRunner:
    race_distance = 42.195  # Marathon distance in kilometers

    def get_speed(self):
        return self.speed

runner1 = MarathonRunner()
runner1.speed = 7.5

runner2 = MarathonRunner()
runner2.speed = 8.0

print(MarathonRunner.race_distance)  # Look in class namespace
print(runner1.race_distance)  # Look in instance namespace
print(f'Runner 1 speed: {runner1.speed}')
print(runner2.race_distance)
print(f'Runner 2 speed: {runner2.speed}')

MarathonRunner.race_distance = 42
print(runner2.race_distance)
