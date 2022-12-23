# Allow the Fuzzy Match to be reconfigured without passing around parameters
class FuzzyMatchConfig:
    MAX_DISTANCE = 1
    MIN_LENGTH = 6
    def CalculateMinLength():
        return max(FuzzyMatchConfig.MIN_LENGTH, FuzzyMatchConfig.MAX_DISTANCE)
