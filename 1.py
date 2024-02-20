n = [int(x) for x in input("Enter no with spaces:").split()]
setlen = len(set(n))
if len(n) == setlen:
    print("All elements unique...")
else:
    print("Recursive elements present...")
