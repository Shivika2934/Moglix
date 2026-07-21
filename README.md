# Moglix Online Shortlisting Round – Coding Assignment

## Problem Statement

Given a string containing only the characters `'('` and `')'`, determine the length of the **longest valid (well-formed) parentheses substring**.

### Examples

**Example 1**

```text
Input: "(()"
Output: 2
```

**Example 2**

```text
Input: ")()())"
Output: 4
```

**Example 3**

```text
Input: ""
Output: 0
```

---

## Solution

This solution is implemented in **Python** using a **stack-based approach**.

### Approach

* Initialize a stack with `-1` as a sentinel value.
* Traverse the string character by character.
* For every `'('`, push its index onto the stack.
* For every `')'`, pop from the stack.

  * If the stack becomes empty, push the current index as the new base.
  * Otherwise, calculate the current valid substring length using the difference between the current index and the top of the stack.
* Keep track of the maximum valid length encountered.

---

## Language

* Python

---

## Submission

This repository was created as part of the **Moglix Online Shortlisting Round** coding assignment.
