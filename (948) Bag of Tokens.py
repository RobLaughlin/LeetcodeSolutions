"""
(948) Bag of Tokens
https://leetcode.com/problems/bag-of-tokens/

You have an initial power of power, 
an initial score of 0, and a bag of tokens where tokens[i] is the value of the ith token (0-indexed).

Your goal is to maximize your total score by potentially playing each token in one of two ways:

If your current power is at least tokens[i], you may play the ith token face up, losing tokens[i] power and gaining 1 score.
If your current score is at least 1, you may play the ith token face down, gaining tokens[i] power and losing 1 score.
"""

def maxScore(power, tokens):
    # Employ a greedy strategy of playing the most valuable tokens face up,
    # then only gaining power when we can't play a token face up.
    # We're able to pick and choose the tokens we can play, so we ultimately choose the best ones.
    # The best tokens to play face up are the ones with the least power,
    # and the best tokens to play face down are the ones with the most power.
    score = 0

    # Sort the list of tokens in ascending order.
    tokens = list(sorted(tokens))

    # i points to the next token we want to play face up,
    # j points to the next token we want to play face down.
    i = 0
    j = len(tokens)-1

    while (i <= j):
        if power >= tokens[i]:
            power -= tokens[i]
            score += 1
            i += 1
        
        # Case where we can play a token face down and still get a score at least as big as the current score by next move.
        elif (tokens[j] + power >= tokens[i]) and i != j and score >= 1:
            power += tokens[j]
            score -= 1
            j -= 1
        
        # In this case, playing a token face down will only hurt us in the future.
        else:
            break
    
    return score

if __name__ == '__main__':
    power = 54
    tokens = [71,55,82]
    score = maxScore(power, tokens)
    print(score)