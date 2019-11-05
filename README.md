# random_walk - Simulate a basic random walk through a given graph
************************************************

The core functionality of this project is contained in RandomWalk.py. All the different parts of the process were separated out into different functions to make it clear what steps are necessary in this process.

It should be self explanatory how each function depends on the others. To see the process in action simply run the main.py file and change the parameters as necessary. You can also add your own graph files as required, but they need to abide by the given format. The output will be stored in a file named after outputname which can also be changed.


## Edge Cases - Walk reaches a Dead End

One particular case I considered is what happens if the random walk reaches a node that has no outgoing nodes. In this case, the random walk is simply attempted again.

In the first graph graph1.txt , there is always a valid output, no matter where the walk starts. However, walks in other graphs could reach a dead end where this might be necessary.

A more extreme case is given in graph2.txt. Here only one node is connected to another going one way. clearly if L is greater than 2, no valid walk can be reached. To take this into account I abort the process if no valid path can be found after five tries and raise an exception.

This is not a perfect solution because there are setups where a walk of the given length is possible, but the algorithm simply doesn't reach this case after five attempts and aborts. There are other ways to handle this problem than what was presented in this algorithm but for this application I assumed that my solution is fine.
