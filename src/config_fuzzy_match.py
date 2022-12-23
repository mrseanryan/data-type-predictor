# Allow the Fuzzy Match to be reconfigured without passing around parameters
class FuzzyMatchConfig:
    MAX_DISTANCE = 2
    MIN_LENGTH = 5
    def CalculateMinLength():
        return max(FuzzyMatchConfig.MIN_LENGTH, FuzzyMatchConfig.MAX_DISTANCE)
