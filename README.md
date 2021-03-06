# Proof of work
## A simple Proof Of Work module made with python

## **POW ALGORITHM**
The algorythm used in this module is very simple:
The inputs are an **initial SHA-256 hash** (that could be the last proof of work hash, like in bitcoin system) and a **difficult in number of zeroes**. That means the number of zeroes that the resulting hash must have at it's begining.

Starting with those two arguments, the script now makes a new random hash. That's the proof of work.
This new hash has to meet a condition:
1. The new hash is attached to the **initial hash**
2. The script now converts those two joint hashes (initial + new) into another hash. (Resulting hash)
3. If the resulting hash begins with the specified **number of zeroes**, the proof of work is valid.
4. The information returned is: (proof_of_work_hash, resulting_hash, number_of_attempts)
> Notice that the resulting hash may have more zeroes than the specified. The difficult is a **minimum**.

For curious people: [What is a proof of work?](https://en.wikipedia.org/wiki/Proof-of-work_system)

## **Other methods**
proof_of_work() is not the only method contained in this module. Here's an explanation of some others:
* **random_hash()**: Returns a random SHA-256 hash.
* **make_hash(string)**: Converts a string into a SHA-256 hash.

## **How to use it**
**From pip:** ```pip install powpy```
**From github repository:** Download and run setup.py