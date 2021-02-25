scores = [2, 3, 6, 6, 5]
def second_place(scores):
    scores.sort(reverse=True)

    first_scores = scores[0]

    for elem in scores:
        if elem < first_scores:
            result = "You have won with a score of: " elem
            return result

print(second_place(scores))