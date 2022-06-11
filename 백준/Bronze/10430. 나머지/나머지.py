#첫째 줄에 (A+B)%C, 둘째 줄에 ((A%C) + (B%C))%C, 셋째 줄에 (A×B)%C, 넷째 줄에 ((A%C) × (B%C))%C
A,B,C = map(int, input().split())
print(f"{(A+B)%C}")
print( f"{((A%C) + (B%C)) %C}")
print(f"{(A*B)%C}")
print(f"{((A%C) * (B%C))%C}")