# Outline of `SimpleCompiler`

In case you forgot your high school arithmetic rules, here's a basic outline:

> **Brackets first, exponentials next, followed by multiplication and division, and lastly addition and subtraction.**

The goal of `SimpleCompiler` is to parse barebones mathematical expressions, and will be the foundations of future improvement projects such as the future `AlgebraCompiler` or `CalculusCompiler`.

# Pseudocode

Let the input string be `1+(12 - 3)*4+2^{4/2 + 1}*3`. This string covers all the basic corner cases.

```
inn[0]: s = '1+(12 - 3)*4+2^{4/2 + 1}*3'
```

## Step 1: Parse

We parse the string input into an array, while *consistently formatting* it. This will also help to purge any malicious code or invalid expressions. Brackets will be formatted into a subarray.

```
inn[1]: arr = parse(s)
inn[2]: arr
[1,'+',[12,'-',3],'*',4,'+',2,'^',[4,'/',2,'+',1],'*',3]
```

This can be done with `.replace()` function in python, a stack to ensure consistent bracketting, and iterating through the string to ensure no 2 operations are side by side *(except +- or -+ which will be evaluated to -)*, and that expressions start and end with numbers, not operators. `float()` and `.isnumeric()` are helpful functions to detect and convert integers *(though we will need some modification for decimals)*.

## Step 2: Recusively compile

Apply this algorithm recursively onto subarrays (bracket . expressions), since they have to be evaluated first. For now, we will assume the algorithm works and magically spits out the right solution.

```
inn[3]: for i in range(len(arr)):
			if type(arr[i]) == list:
				arr[i] = compile(arr[i])
inn[4]: arr
[1,'+',9,'*',4,'+',2,'^',3,'*',3]
```

This can be easily done by iterating through the list, detecting for subarrays, and recursively feeding them with `arr[i] = compile(arr[i])`.

*Note: Since we are recursively feeding them into `compile`, sub-sub-subarrays will be eventually evaluated as well.*

## Step 3: Ignoring addition & subtraction operators

Find all occurences of `[<number>, '+', <number>]` and `[<number>, '-', <number>]`, and split the array into subarrays.

It might seem counter-intuitive to deal with addition and subtraction first, but here we just want to split the array where addition & subtraction operations exist, to evaluate other operations first

```
inn[5]: arr = split_as(arr)
inn[6]: arr
[[1],'+',[9,'*',4],'+',[2,'^',3,'*',3]]
```

This can be easily done by splitting the arrays where '+' or '-' appears, and creating a new array with the split segments as sub-arrays.

## Step 4: Recursively compile (again)

Now that we have subarrays (again), we recursively compile them. These sub-expressions contain multiplication & exponential operations, thus are to be evaluated before addition & subtraction.

```
inn[7]: for i in range(len(arr)):
			if type(arr[i]) == list:
				arr[i] = compile(arr[i])
inn[8]: arr
[1,'+',36,'+',24]
```

## Step 5: Done?

**Not so fast!** It might seem we can finally compute left to right the simple addition and subtraction operations, but we forgot about our recursive steps -- which contains multiplication and exponential operators...**how do we evaluate those?**

Remember that we have also fed into `compile()` arrays such as `[2,'^',3,'*',3]`. How do we deal with them?

## Step 5: Repeating Steps 3 & 4

We carry out steps 3 & 4, but for multiplication and division operators. Afterwards, we carry out steps 3 & 4 yet again, but for the exponential operator.

```
inn[9]: arr = split_md(arr)
inn[10]: # [2,'^',3,'*',3] -> [[2,'^',3],'*',[3]]
...

inn[12]: arr = split_e(arr)
inn[13]: # [2,'^',3] -> [[2],'^',[3]]
...
```

## Step 6: Computing operations

Finally, since the string is split by the operators, we can start evaluating operations. If we have done everything correctly, the expressions reaching here should either:

- contain only addition & subtraction
- contain only multiplication & division
- contain only exponentials

As such, we can simply evaluate left-to-right, and return the output.

# Summary

![Summary](https://github.com/EthanKuai/calculator/blob/main/SimpleCompiler_Outline.png)
