# Write your solution here

def histogram(word: str):
    freq = {}
    
    for w in word:
        if w not in freq:
            freq[w] = 0
        freq[w] += 1
        
    for key, value in freq.items():
        print(f"{key} {'*' * value}")
        

if __name__ == "__main__":
    histogram("abba")
    histogram("statistically")