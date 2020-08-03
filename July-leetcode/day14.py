'''
Angle Between Hands of a Clock

Given two numbers, hour and minutes. Return the smaller angle (in degrees) formed between the hour and the minute hand
'''
class Solution:
    def angleClock(self, hour: int, minutes: int) -> float:
        diff = abs(30 * hour - 5.5 * minutes)
        return diff if diff <= 180 else 360 - diff

#Runtime: 72 ms
#Memory Usage: 13.9 MB