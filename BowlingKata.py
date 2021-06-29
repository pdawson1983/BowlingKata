class Game():
    def __init__(self):
        self.rolls = []
        self.currentRoll = 0
        self.tenPins = 10

    def roll(self, pins):
        self.rolls.append(pins)

    def score(self):
        score = 0
        frameIndex = 0
        for _ in range(10):
            if self.isStrike(frameIndex): 
                score += self.tenPins + self.strikeBonus(frameIndex)
                frameIndex += 1
            elif self.isSpare(frameIndex):
                score += self.tenPins + self.spareBonus(frameIndex)
                frameIndex += 2
            else:
                score += self.normalFrameScore(frameIndex)
                frameIndex += 2
        return score

    def isStrike(self, frameIndex):
        return self.rolls[frameIndex] == self.tenPins

    def isSpare(self, frameIndex):
        return self.rolls[frameIndex] + self.rolls[frameIndex + 1] == self.tenPins

    def strikeBonus(self, frameIndex):
        return self.rolls[frameIndex+1] + self.rolls[frameIndex+2]
    
    def spareBonus(self, frameIndex):
        return self.rolls[frameIndex+2]
    
    def normalFrameScore(self, frameIndex):
        return self.rolls[frameIndex] + self.rolls[frameIndex+1]