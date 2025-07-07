# from random import randint, random
from numpy.random import randint, seed
import pandas as pd
from random import random
from math import ceil

seed(100)

def get_weight(percentage: int | float) -> float:
    if percentage >= 75:
        return 4.00
    if percentage >= 70:
        return 3.50
    if percentage >= 65:
        return 3.25
    if percentage >= 60:
        return 3.00
    if percentage >= 55:
        return 2.75
    if percentage >= 50:
        return 2.50
    if percentage >= 45:
        return 2.25
    if percentage >= 40:
        return 2.00
    return 0.00

def randomScore(numberOfScores: int = 10, amountOfScore: int = 10):
    scores = []
    all_weight = []
    all_course_unit = []
    all_gpa = []
    for _ in range(numberOfScores):
        # Generate random scores between 50 and 100 (inclusive)
        score: list[int] = list(randint(50, 101, size=amountOfScore))
        course_unit: list[int] = [round(random() * 3) for _ in range(amountOfScore)]
        # print("Score", score, "Course Unit", course_unit)
        
        weight = [get_weight(score[i]) for i in range(len(score))]
        
        # print(
        #     {
        #     "weight": sum(weight),
        #     "course_unit": sum(course_unit),
        #     "gpa": round(sum(weight)/sum(course_unit), 2) if sum(course_unit) else 0.0
        #     }
        # )

        all_weight.append(sum(weight))
        all_course_unit.append(sum(course_unit))
        all_gpa.append(round(sum(weight)/sum(course_unit), 2) if sum(course_unit) else 0.0)
    
    df = pd.DataFrame({
        "weight": all_weight,
        "course_unit": all_course_unit,
        "gpa": all_gpa
    })
    df.to_csv("../ml/results.csv", index=False)
    # return df

if __name__ == "__main__":
    randomScore(5000)