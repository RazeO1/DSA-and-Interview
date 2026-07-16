def reverse_word(s):
    words = s.split()
    words.reverse()
    return ' '.join(words)

def solve():
    s = input()
    print(reverse_word(s))

if __name__ == "__main__":  
    solve()