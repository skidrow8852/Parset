# Parset
![DALL·E 2024-12-21 10 55 51 - A modern and sleek logo for 'Parset', a programming interpreter  The logo features a stylized representation of a parser, incorporating minimalistic b](https://github.com/user-attachments/assets/70d2d1a1-6928-4e34-bfb6-5967124ffceb)


Parset is a simple yet versatile programming language designed and implemented to practice and enhance my Python programming skills. It serves as a learning project and an exploration into how programming languages are built, parsed, and executed.

# Why Parset?

Parset was born out of curiosity and a desire to dive deeper into the inner workings of interpreters, compilers, and language design. It’s an experimental project aimed at understanding:

- **Lexical analysis:** Breaking down raw code into tokens.
- **Syntax parsing:** Understanding the structure of code.
- **Evaluation:** Executing instructions based on their semantics.


# Syntax

---

## Comments

Line comments start with `#` and end at the end of the line:

```parset
# This is a comment
```

---

## Reserved Words

A reserved word (also known as a reserved identifier) is a word that cannot be used as an identifier, such as the name of a variable, function, or label. Here are parset's reserved words:

```
if
then
else
true
false
and
or
while
do
for
func
end
print
println
ret
```

---

## Identifiers

Naming rules are similar to other programming languages. Identifiers start with a letter or an underscore and may contain letters, digits, and underscores.

Examples of valid identifiers:

```parset
x
id
flatcase
snake_case
camelCase
PascalCase
_acc
MAX_SPEED
```

parset is **case-sensitive**.

---

## Whitespace

Whitespace characters are ignored by the language, including spaces and tabs. Unlike Python, parset does not consider indentation as syntax:

```parset
if x == 0 then print(x + 1) end
```

---

## Variables

parset is a dynamically typed language, meaning the type of a variable is assigned at runtime based on its value. The core language offers just three primitive types: `number`, `string`, and `bool`.

Examples:

```parset
score := 5
name := 'parset'
isrunning := true
```

Numbers in parset are stored as 64-bit floating-point numbers, even if the literal read by the tokenizer is an integer:

```parset
pi := 3.141592   -- Stored as a double-precision float
numlives := 0    -- Also stored as a double-precision float
```

---

## Strings

String literals can be enclosed in single or double quotes:

```parset
text := 'This is a valid string'
name := "This is also a valid string"
```

Strings can be concatenated using the `+` operator. Numbers and booleans are automatically converted to strings when concatenated:

```parset
speed := 76.68
text := 'The current speed is: ' + speed
```

---

## Expressions

Expressions in parset always result in a value:

```parset
2 + 13      -- [ans: 15] A single expression is a valid statement
2 + 4*3     -- [ans: 14] Operator precedence in action
4 ^ 2       -- [ans: 16] Special exponent operator
3 * (2+4)   -- [ans: 18] Grouping using parentheses
17 - -3     -- [ans: 20] Both unary and binary minus
1 > 2       -- [ans: false] A simple boolean expression
```

---

## Operators

### Arithmetic Operators

```parset
x + y   -- Addition
x - y   -- Subtraction
x * y   -- Multiplication
x / y   -- Division
x % y   -- Modulo
x ^ y   -- Exponentiation
-x      -- Unary minus
```

### Comparison Operators

Comparison operators in parset can compare numbers and strings:

```parset
x > y     -- Greater than
x < y     -- Less than
x >= y    -- Greater or equal
x <= y    -- Less or equal
x == y    -- Equal
x ~= y    -- Not equal
```

### Logical Operators

Logical operators in parset use short-circuit evaluation:

```parset
x and y   -- Logical AND
x or y    -- Logical OR
~x        -- Logical negation
```

Short-circuit behavior:
- If the first operand of `and` evaluates to `false`, the result is `false`.
- If the first operand of `or` evaluates to `true`, the result is `true`.

---

## Print

You can print a value to the standard output using the `print` or `println` keywords:

```parset
print "Hello, world!"  -- Outputs the value of an expression
println x              -- Prints a value and adds a newline
```

---

## Conditionals

Control the flow of your program using `if` statements. The syntax is straightforward:

```parset
if x > 10 then
  println "Consequence block"
else
  println "Alternative block"
end
```

The test condition is always a boolean. Unlike C-like languages, it is not mandatory to wrap the test condition in parentheses.

---

## Loops

parset supports `while` and `for` loops.

### While Loops

```parset
i := 1
while i <= 10 do
  println i
  i := i + 1
end
```

### For Loops

For loops require a start and an end expression:

```parset
for i := 1, 10 do
  println i
end
```

Optionally, you can provide a step value:

```parset
for i := 1, 10, 2 do
  println i
end
```

---

## Functions

Functions in parset are declared using the `func` keyword. Use `ret` to return values:

```parset
func say(msg)
  print msg
end

func pow(base, exponent)
  ret base^exponent
end
```

Functions can also be recursive:

```parset
func factorial(n)
  if n == 1 then
    ret 1
  end
  ret n * factorial(n - 1)
end

print factorial(5)  -- Outputs: 120
```

---

## Local Variables

Local variables can be declared using the `local` keyword, which shadows any global variables of the same name until the block ends:

```parset
x := 0
i := 1
while i <= 10 do
  local x := 999  -- Shadows the previous x
  print x
  i := i + 1
end
```

---

## Numbers

All numbers are stored as 64-bit floating-point numbers unless the architecture does not support floats. In that case, only integers are used.

```parset
pi := 3.141592
numlives := 0
```

---