# CMPSC 100: Computatonal Expression Activity Repository

![](https://github.com/user-attachments/assets/716f979e-d003-48d7-82ef-9483f33d3ff2)

|Activity |Completion Status |
|:--------|:-----------------|
|Activity 1|[![Activity 1](../../actions/workflows/activity_one.yml/badge.svg?branch=main)](../../actions/workflows/activity_one.yml)|
|Activity 2|[![Activity 2](../../actions/workflows/activity_two.yml/badge.svg?branch=main)](../../actions/workflows/activity_two.yml)|
|Activity 2|[![Activity 2](../../actions/workflows/activity_three.yml/badge.svg?branch=main)](../../actions/workflows/activity_three.yml)|

This repository will contain the various activities we will complete during our time together in class. This `README` will regularly update with new content about those activities, to provide context and additional information for what we're doing on a given day. This document may link to additional information, contain diagrams, or provide important details.

We will keep this repository updated on a regular basis.

## Activity 1

### Summary

This activity is a short profile about you and a beginning exposure to the language that we will use to write documents: Markdown. In addition to getting used to VSCode (our code editor), you'll provide some more detail so that we can get to know you better.

### Part 1: Installing Supporting Tools

1. Head to our [course wiki](https://github.com/allegheny-college-cmpsc-100-spring-2026/course-materials/wiki).
2. Locate the link to the page titled `Installing Supporting Tools`

This page will guide you through the tools that we should set up during our time together today. Don't worry if it takes you the entire class; this stuff is important, so we should take our time. When you finish and a TL or the instructor has verified that you've done so, we'll move forward together as a class.

### Part 2: What's Your Story?

For this part of the activity, refer to the ["Basic writing and formatting syntax"](https://docs.github.com/en/get-started/writing-on-github/getting-started-with-writing-and-formatting-on-github/basic-writing-and-formatting-syntax) article on Github. This will provide you with enough information to complete our profile!

You'll get a basic demonstration of how to do some of this, and a brief tour of some of the software that you've downloaded.

### Part 3: Showing Your Work

In addition, this activity will _grade itself_ on Github once we've practiced `push`ing content to it. This humble profile really does a lot more than just report answers to questions!

This will be part of our course presentation, so you should be able to refer back to that if you need any refreshers! In addition, there's a page on our [course wiki](https://github.com/allegheny-college-cmpsc-100-spring-2026/course-materials/wiki) that summarizes these steps.

## Activity 2

During `Activity 2`, we start into learning Python fundamentals. To do so,
we'll re-approach the algorithm we crowd-sourced during our first class:

$$\frac{(n_{1} - n_{0} + 1)}{2}\times({n_{1} + n_{0}}) $$

Reviewing our discussion of computational thinking and implement the last 
part of the our thinking:

1. Decomposition
2. Recognition
3. Abstraction
4. _Programming_

Here, we learn a few key things:

* variables
* types
* functions
* user inputs

## Activity 3

For `Activity 3`, we'll be exploring `functions` and `conditional statements`: ways that your program can use types to do _more stuff_. In this activity, we'll build a guessing game that has a few parts:

1. Generates a random number
2. Accepts user guesses
3. Judges if those guess are right, too low, or too high
4. Invites winners to play another round

This task is deceptively simple, but with our new tools, it should also read _deceptively easy_.

> [!NOTE]
> As a stretch goal, we _could_ implement a function to introduce some progressive difficulty.
> * For each incorrect guess, regenerate a random number between the guess and the correct answer, uninclusive of the guessed number
> * How would we go about implementing this?