notes = [10, 20, 50, 100, 200, 500]
notes.sort()
notes = notes[::-1]


def get_notes(amount,notes):
    pay = {}
    i = 0
    while True:
        note = notes[i]
        count = 0
        if amount<=0:
            break
        elif amount>=note:
            while amount>=note:
                count += 1
                amount -= note
            pay[note] = count
        i += 1
    
    return pay

pay = get_notes(1750,notes)

print(notes)
print(pay)
