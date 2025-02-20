# Lesson 6
userInput = [int(x) for x in input().split()]
w1, h1, w2, h2 = userInput

perimeter1 = 2*(w1+w2) + 2*max(h1,h2)
perimeter2 = 2*max(w1,w2) + 2*(h1+h2)

print(f"Minimum perimeter: {min(perimeter1,perimeter2)}")