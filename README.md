# HackerRank
## What is HackerRank?
HackerRank is a developer platform in which developers from all over the world come together to solve problems in a wide range of Computer Science domains such as algorithms, machine learning, or artificial intelligence, as well as to practice different programming paradigms like functional programming.

## How do I start to prepare for a HackerRank assessment?
Start by taking a 30-minute sample test so you can get familiar with the assessment process. There is also a HackerRank Interview Preparation Kit that is available. We carefully curated challenges to help you prepare in the most comprehensive way possible so try to solve as many challenges as possible and if you get stuck, use the discussion and editorial sections for hints and solutions. If you have any additional questions, check out the HackerRank test FAQ page.

## How can I practice and solve challenges?
Sign up on www.hackerrank.com/signup to join our HackerRank community and start solving challenges. As you solve challenges you will gain points and go up on the HackerRank leaderboard. Our strong community of developers likes to discuss problems, learn, compete and collaborate together. The HackerRank community is the largest learning and competition community for programmers.

## Which programming languages are supported by HackerRank?
HackerRank currently supports 35 programming languages. If you are a LinkedIn candidate you have the flexibility to choose the languages that are allowed for answering a particular question or test, however, only those languages will be available to you. You can refer this page to view the supported languages with their versions. This page will be also available to you while attempting the test.


# Complexity
## Asymptotic Notation
The **asymptotic behavior** of a function `f(n)` (such as `f(n)=c*n` or `f(n)=c*n2`, etc.)refers to the growth of `f(n)` as n gets large. We typically ignore small values of n, since we are usually interested in estimating how slow the program will be on large inputs. A good rule of thumb is: the slower the asymptotic growth rate, the better the algorithm (although this is often not the whole story).

By this measure, a linear algorithm (i.e., `f(n)=d*n+k`) **is always asymptotically better** than a quadratic one (e.g., `f(n)=c*n^2+q`). That is because for any given (positive) c,k,d, and q there is always some n at which the magnitude of `c*n^2+q` overtakes `d*n+k`.

`0.6n^2 vs 1000n+3000`?

![The comparison](https://cdn.kastatic.org/ka-perseus-images/d2d40c938c1bab9f413c83164fec8ae9945e402b.png)

## Big O Notation
Let's look at a simple implementation of linear search:
```golang
var doLinearSearch = function(array, targetValue) {
  for (var guess = 0; guess < array.length; guess++) {
    if (array[guess] === targetValue) { 
        return guess;  // found it!
    }
  }
  return -1;  // didn't find it
};
```
Let's denote the size of the array (array.length) by *n*. The maximum number of times that the for-loop can run is **n**, and this worst case occurs when the value being searched for is not present in the array.

## Enriching
### O: Asymptotic Upper Bound
‘O’ (Big Oh) is the most commonly used notation. 

A function 𝐟(𝐧) can be represented is the order of `𝒈(𝒏)` that is `𝑶(𝒈(𝒏))`, if there exists a value of positive integer n as n0 and a positive
constant c such that:
`𝒇(𝒏) ≤ 𝒄.𝒈(𝒏) for 𝒏 > 𝒏𝟎` in all case.

Hence, function `𝒈(𝒏)` is an upper bound for function `𝒇(𝒏)`, as `𝒈(𝒏)` grows faster than `𝒇(𝒏)`.

#### Example
Let us consider a given function, `𝒇(𝒏) = 𝟒.𝒏^𝟑 + 𝟏𝟎.𝒏^𝟐 + 𝟓.𝒏+ 𝟏`.
Considering `𝒈(𝒏) = 𝒏^𝟑`

`𝒇(𝒏) ≤ 𝟓.𝒈(𝒏)` for all the values of `𝒏 > 𝟐`.
Hence, the complexity of `𝒇(𝒏)` can be represented as `𝑶(𝒈(𝒏))`, i.e. `𝑶(𝒏^𝟑)`.

### Ω: Asymptotic Lower Bound
We say that `𝒇(𝒏) = 𝛀(𝐠(𝒏))` when there exists constant c that 
`𝒇(𝒏) ≥ 𝒄.𝒈(𝒏)` for all sufficiently large value of `n`. 

Here n is a positive integer. It means function g is a **lower bound** for function f; after a certain value of n, f will never go below g.

#### Example
Let us consider a given function, `𝒇(𝒏) = 𝟒.𝒏^𝟑 + 𝟏𝟎.𝒏^𝟐 + 𝟓.𝒏+ 𝟏`.
Considering `𝒈(𝒏) = 𝒏^𝟑`, `𝒇(𝒏) ≥ 𝟒.𝒈(𝒏)` for all the values of `𝒏 > 𝟎`.
Hence, the complexity of `𝒇(𝒏)` can be represented as `𝛀(𝒈(𝒏))`, 
i.e. `𝛀(𝒏^3)`.

### Ɵ: Asymptotic Tight Bound
We say that `𝑓(𝑛) = Ɵ(g(𝑛))` when there exist constants `c1` and `c2` that `𝑐1.𝑔(𝑛) ≤ 𝑓(𝑛) ≤ 𝑐2 𝑔(𝑛)` for all sufficiently large value of n. Here `n` is a positive integer. This means function g is a tight bound for function f.

#### Example
Let us consider a given function, `𝒇(𝒏) = 𝟒.𝒏^𝟑 + 𝟏𝟎.𝒏^𝟐 + 𝟓.𝒏+ 𝟏`.
Considering `𝒈(𝒏) = 𝒏^𝟑`, `𝟒.𝒈(𝒏) ≤ 𝒇(𝒏) ≤ 𝟓.𝒈(𝒏)` for all the large values of `n`.

# Documentation
I suggest you to read more about `Markdown` since it is easy to be used and more community supports. 

# Unit Testing
This things is mandatory, everytime you change your code this will be your checkpoint whether your code is working well or not.

# Github
Practice how to use github/gitlab properly, learn how to add, commit, and push your code to repo.

> Practice and learn more about **Design and Analysis of Algorithm (DAA)** alongside your **Discrete Mathemathics** skill 

- book in use: [https://www2.cs.duke.edu/courses/fall08/cps230/Book.pdf](download here) 

Curated by <yoshuajoe@gmail.com>