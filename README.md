# graham-scan
CS 3353 Midterm Project - Graham Scan

This Python program implements and analyzes the Graham Scan algorithm on data sets with varying distribution and size.
The program implements pyplot from the matplotlib library to display the set of points, along with the set's
**convex hull**.

Points are defined as an ordered tuple (x,y) and are plotted accordingly.
A "gift" is a set of such Points.
The "wrapper" is the gift's Convex Hull.

Two independent variables are presented:

(1). Data Distribution types ~ n = size of the data
- Random distribution (Each (x,y) are both random values 0-n)
- Concentric circles (Each (x,y) form two concentric circles centered at n/2, with radii n/2 and n/4 respectively)

(2). Data set sizes
- 10 elements
- 100 elements
- 1,000 elements
- 10,000 elements

## Build/Run Instructions

###Prerequisites:

This project requires Python to run. Learn more about how to download Python [here](https://www.python.org/downloads/).

###Running the project - Quickstart

1. Clone the repository using `git clone https://github.com/mplennon617/graham-scan`
2. Navigate to the source code folder `cd [...]/21s-pa02-mplennon617/src`
3. Enter your IDE of choice (Example: `code .` for Visual Studio Code)
4. Run GiftPlot.py in your Python terminal.
5. A plot window will be displayed. Exit out of each plot to advance to the next plot generated.
6. You are done!

- NOTE: The following external libraries are used: numpy matplotlib.pyplot, random, math

# Report

You may view a comprehensive report of this midterm project [here -- TO BE EDITED LATER](https://medium.com/p/e6ecc25c30da).

The report describes and analyzes the Algorithm used (Graham Scan) in full detail.

### Sources

[https://www.algorithm-archive.org/contents/jarvis_march/jarvis_march.html](https://www.algorithm-archive.org/contents/jarvis_march/jarvis_march.html)
[https://www.math.ucsd.edu/~ronspubs/72_10_convex_hull.pdf](https://www.math.ucsd.edu/~ronspubs/72_10_convex_hull.pdf)
[https://www.ams.org/journals/notices/201903/rnoti-p330.pdf](https://www.ams.org/journals/notices/201903/rnoti-p330.pdf)
[https://www.geeksforgeeks.org/convex-hull-set-1-jarviss-algorithm-or-wrapping/](https://www.geeksforgeeks.org/convex-hull-set-1-jarviss-algorithm-or-wrapping/)
[https://en.wikipedia.org/wiki/Convex_hull#History](https://en.wikipedia.org/wiki/Convex_hull#History)