# Belief-Divergence 
October 2018 - Present

## Table of Contents 
1. Intro and Summary
2. Current Version
3. User Guide




## 1. Intro and Summary
This project was created for Silvio Ravaioli's (Columbia Ph.D. Student in Economics) project on Belief Divergence. The repository, when run on oTree, contains two tasks:

Task 1 gives the user urn probabilities and ball probabilities per urn. Then, the participant attempts to report the conditional probabilities of the urn given the result of the ball pulled.

Task 2 gives the user, again, urn probabilities and ball probabilities. However, this time they are also given the option to select a gray urn.

Following both tasks is a feedback screen that returns the participants choices along side the correct answers for feedback. Task 2 additionally has a follow up feedback screen that returns the urn selected and feedback.



## 2. Current Version
December 13, 2018
Current version has a working task pages and feedback pages. Below are current notes that still need to be updated (from last meeting)
- [ ] **Overall code needs to be cleaned up once finalized. There are many comments, etc.
- [x] Asthetics of the probability bars
- [x] "given ball" should return the word "white" or "black"
- [ ] Accuracy function should be checked
- [ ] Payout function should be checked
- [x] Decimals should all show as percentages
- [x] Redo task 2 into 2 pages: first page with just the gray urn, and a second with all the info.



## 3. User Guide
Download the repository from GitHub. 
If using your own settings.py, ensure that there is a code block as so:

```
    {
        'name': 'BeliefDivergence',
        'num_demo_participants': 1,
        'app_sequence': ['BeliefDivergence', 'BeliefDivergence2'], 
    },
```

This will ensure that the BeliefDivergence app will play through both tasks.


To customize **Task 1:**

Enter the folder for BeliefDivergence and open models.py
Notice the following current code block:
```
data = [[ 0.25, 0.5, 0.25, 0.8, 0.5, 0.2, 0],
    [ 0.4, 0.5, 0.1, 0.6, 0.5, 0.4, 1]]
```
The entry of data is a list of lists. The indices is as so:
- 0-2 = prior (ex ante urn probability) (Values should be floats between 0.0 and 1.0, and all three must add up to 1.0. The order is Red, Yellow, and Green)
- 3-5 = signal structure (black/white ball probability for each urn) (Values should be floats between 0.0 and 1.0. The number is the probability of the black ball).
- 6 = ball color (An integer 0/1 based on black/white ball color)
    




To customize **Task 2:**

Enter the folder for BeliefDivergence2 and open models.py
Notice the following current code block:
```
data = [[0.25, 0.50,  0.25, 0.8, 0.5, 0.2, 0, 30, 55, 90, 65],
			[0.25, 0.50,  0.25, 0.9, 0.8, 0.7, 1, 30, 60, 90, 60],
			[0.25, 0.50,  0.25, 0.6, 0.5, 0.4, 1, 30, 65, 90, 55]]
```
The entry of data is a list of lists. The indices is as so:
- 0-2 = prior (ex ante urn probability) (Values should be floats between 0.0 and 1.0, and all three must add up to 1.0. The order is Red, Yellow, and Green)
- 3-5 = signal structure (black/white ball probability for each urn) (Values should be floats between 0.0 and 1.0. The number is the probability of the black ball).
- 6 = ball color (An integer 0/1 based on black/white ball color)
- 7-9 = points for the color urn (risky option. Input should be an integer. The order is Red, Yellow, Green)
- 10 = points for the grey urn (status quo option. Input should be an integer.)
