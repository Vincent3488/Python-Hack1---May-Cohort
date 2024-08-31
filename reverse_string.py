def reverse_string(s: str) -> str:
    # Use a list to serve as a stack
    stack = list(s)
    
    # Collect characters in reversed order using list comprehension
    reversed_chars = [stack.pop() for _ in range(len(stack))]
    
    # Join the list of characters into a single string
    reversed_str = ''.join(reversed_chars)
    
    return reversed_str

if __name__ == "__main__":
    print(reverse_string("hello"))  # Output: "olleh"
