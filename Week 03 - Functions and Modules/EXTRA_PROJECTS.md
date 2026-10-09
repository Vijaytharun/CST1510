# Week 3 — Extra Practice Projects

Optional. Beyond the lab — classic beginner projects, adapted from Angela
Yu's *100 Days of Code*, trimmed to use this week's new tools: functions,
parameters, defaults, scope, and the `import` keyword (`random`, `math`,
and friends). Still no lists or dicts — that's Week 4; use separate
variables instead of a collection, even where it feels repetitive.

---

## Rock, Paper, Scissors

**Uses:** functions, `return`, `random.randint()`

1. Write a function `get_computer_choice()` that returns `"rock"`,
   `"paper"`, or `"scissors"` — use `random.randint(0, 2)` and an
   `if`/`elif`/`else` to map the number to a name.
2. Ask the user for their choice with `input()`.
3. Write a function `decide_winner(user_choice, computer_choice)` that
   returns `"user"`, `"computer"`, or `"draw"`.
4. Print who won.

*Adapted from: 100 Days of Code, Day 4.*

---

## Calculator

**Uses:** functions, parameters, `return`, calling one function from another

1. Write four functions: `add(n1, n2)`, `subtract(n1, n2)`,
   `multiply(n1, n2)`, `divide(n1, n2)` — each returns the result.
2. Ask the user for a first number, an operator (`+ - * /`), and a second
   number.
3. Use `if`/`elif` to call the matching function and print the result.
4. Ask if they want to keep calculating with the result as the new first
   number, or start over. Use a `while` loop.

**Extension, once you've done Week 4:** replace the `if`/`elif` dispatch
with a dictionary of `{"+"  : add, "-": subtract, ...}` and call
`operations[chosen_operator](n1, n2)` instead.

*Adapted from: 100 Days of Code, Day 10.*

---

## Number Guessing Game, upgraded

**Uses:** `random.randint()`

Already built the Week 2 version? Swap the hard-coded secret number for
`random.randint(1, 100)`. Same loop, same comparisons — now every
playthrough is different.

*Adapted from: 100 Days of Code, Day 12.*

---

Stuck on why a function returning nothing gives you `None`? That's
`01 - Defining and Calling Functions`, section 4, in this folder.
