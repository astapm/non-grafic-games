# Simple non-grafic games on Python

**Minimum grafic, maximum replayability**  
Entertainment is not the main thing in the game


* [Dice-racing](#Simple-dice-racing)


## Simple dice-racing

* The two cars move through the cells with numbers from 0 to 100
* The car moves as many cells as there are points on the rolled dice
* The dice is rolled and the cars move automatically
* The winner is the car that first reaches the cell number 100
* Minimal graphics -- only cell numbers are displayed
* There is a pause between moves for the player to assess the situation


### Launching the game

The game files: f1.py - English version, f1-rus.py - Russian version

Requires **Python 3** interpreter installed. Launch:

     $ python3 f1.py


### How to enjoy it

Cars move automatically. For example, you can place bets with a friend on the victory of one of them.

You can just watch the races. Especially for this, a pause is made between moves. They are unpredictable and dramatic. Below is an example of such a race.


```
START
N1 N2
5 3     Car 1 breaks away
9 4
15 9
21 11
23 14
26 16
29 18
34 24
38 26
39 27
42 29
47 34   The gap reaches 13 points
51 39   Car 2 starts to close the gap
52 45
57 46
60 52
61 56
64 57
66 59
67 65
69 68
70 70   Car 2 catches up with the opponent
71 74   Car 2 comes forward
72 78
76 80
81 82
87 87   Cars are level again
92 88   Victory finish of car 1
98 91
100 94
FINISH
```

### Modification

You can easily modify the game code for more cars


## License

GPLv3 2020 Astapchyk Mikhail
