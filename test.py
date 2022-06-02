import random

def random_choice()->int:
    outcome_list = list()

    for i in range(0, 1000):
        random_num = random.randint(1, 8)
        outcome_list.append(random_num)
    
    return outcome_list[500]

outcomes_of_outcomes = list()
for i in range(100):
    outcomes_of_outcomes.append(random_choice())

print(outcomes_of_outcomes[50])