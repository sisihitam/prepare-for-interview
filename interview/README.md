# Prolog
Hi there! This folder is containing 2 separated folder for each question. I will give you a brief explanation how to run the script. The scripts are tested and running well on `MacOS` or `Linux` environment (I'm not tested on Windows since I'm not familiar and I'm not using Windows)

## Solutions location
I have separated the solutions into two folders, each folder contains the scripts needed to solve each problem. Folder `royal_rumble` contains solution for `Royal Rumble Problem (Question 1)` and folder `defender_arcade` contains solution for `Defender Arcade Problem (Question 2)`

## Directory structures
Inside each solution folder, there are several folders:
- `input` : this contains the input file(s), you have to put your input file here.
- `process` : this contains the core script file(s) that process the input
- `log` : this contains the log of process (file format `log_{timestamps}.log`)
- `output`: this containse the output file

## How to give the input set to the script?
The main script is listening to the `STDIN`, so you have to pass the input into the `STDIN` by piping the input and the script. In linux/MacOS I suggest you to use this `|` (pipe). 

Here is a sample command I use to run the script for Defender Arcade problem.

```bash
cat input/input1.txt | python main_defender_arcade.py
```

 and here is a sample command I use to run the script for Royal Rumble problem.
 
```bash
cat input/input1.txt | python main_royal_rumble.py
```
 > Note: **DO NOT** forget to go to each solution folder (`royal_rumble` folder or `defender_arcade` folder from the `interview` folder) first (change directory `cd`) before you run the two commands above.

By using this statement you pass the data by using cat and transfer them into `STDIN` and then the script will consume them at all. You can pass argument `-o` to write the result to the `output` folder (your new output file will available in `output_{timstamps}`.txt format). If you dont pass the `-o` argument, the output will only be printed to the screen not written to the file. Sample command with `-o` statement:

- Royal Rumble
```bash
cat input/input1.txt | python main_royal_rumble.py -o
```

- Defender Arcade
```bash
cat input/input1.txt | python main_defender_arcade.py -o
```

## Unit Testing
I also attached a unit testing script in each solution folder. This testing will assure you to get same true output after you modify or edit the scripts. This is how you run the unit testing.

> Note: The script is located inside `process` folder for each solution directory, so you have to change your directory before your run the script.

- Defender Arcade
```bash
python unittest_defender_arcade.py
```

- Royal Rumble 
```bash
python unittest_royal_rumble.py
```

There is a `log` folder inside folder `process`, this folder is aiming to store unittest log. 


# Techniques in use

## Royal Rumble
Inside `process` folder, and under `royal_rumble.py` script, there are 2 (two) functions, first is called `string_to_roman_number` that takes one parameter (string). This function will parse every parsable and valid Roman number into our well-known number such (1,2,3,4,4,10,50, and so on). For example: `V` will be translated into `5`. The second function is `transform_name`. This function will transform every roman-numbered name into normal-numbered name, for example: `William IV` -> `William 4`. Then I sort them easily (I employ a python dictionary to get the origin format of `William 4` as `William IV`)

## Defender Arcade
Inside `process` folder, and under `defender_arcade.py` script, there is only one and only `overlap` function. I assume every playtime is given in a sorted format: for example:
```
900 910
940 1200
950 1120
```
and there won't be any unsorted like this

```
900 910
950 1120
940 1200
```
I use this formula:
```
(C < B)  and  (A < D)
```

Proof:
Let the condition mean that TimeRange A is completely before TimeRange B
```
|---- TimeRange A -----|                       _ 
(A)                   (B)    
        |--- TimeRange B ----|
       (C)                  (D)
```
Overlap = `If NOT(B < C or A > D)`

Now one of `De Morgan's` laws says that:

`Not (A Or B) <=> Not A And Not B`

Which translates to: `(C < B)  and  (A < D)`

After that I track every group of consecutive overlap time into a list, and I count which group has max count.

Here is the sample list of overlap:

```
[None, None, ('940', '1200'), ('950', '1120'), ('1100', '1130'), None, ('1300', '1400'), ('1350', '1420')]
```

There are two group of consecutive overlap 

```
('940', '1200'), ('950', '1120'), ('1100', '1130') = Size 3
```

and 

```
('1300', '1400'), ('1350', '1420') = Size 2
```

Since 3 > 2 then I choose 3 as result