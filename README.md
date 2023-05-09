#### Old Pad Phone Algorithm

To implement the Old Pad Phone algorithm, we first define a function with one parameter named "old_phone_pad". In the function, we create a dictionary that maps numbers to characters. We also initialize a list named "result" that will store the function's output.

Next, we use a while loop because in Python, it is the only way to skip incremental steps. Inside the loop, we initialize two variables: "inc" and "consec". "inc" is used to dynamically control the while loop steps, while "consec" tracks how many consecutive characters are in the user input.

The loop breaks when the current value matches with '#'. The loop continues with an increment value when two conditions happen: the current value matches with '*' and the output 'result' is not empty, or the current value matches with space ' '.

When the current value matches with '*', we remove the last character in the "result" list.

***Main Part***

To handle three or four consecutive characters, there are four nested "if" statements. The outermost block checks if the current value is equal to the next value. If so, we increment both "consec" and "inc".

The next block checks if the next value is equal to the next next value. This condition handles three consecutive characters.

The next block is a filter for '7' and '9' because only these numbers have four consecutive characters. This step helps avoid index out of error when indexing the fourth character from the current position.

Finally, we append the mapped character to the "result" list using the following code:

```
result.append(mapNumToChar[stri[i]][consec])
```

Then we add "inc" to "i" to continue iterating over the user input.

After finishing the while loop, we convert the "result" list to a string and return it as the function's output. That's all!