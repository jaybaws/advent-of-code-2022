datastream_input = open('input.txt', 'r')
datastream = datastream_input.readlines()[0].strip()

def findMarker(size: int) -> int:
    i = 0
    while i < len(datastream) - (size - 1):
        if len(set(datastream[i:i + size])) == size:
            break
        else:
            i += 1
    return i + size

print(f"""
    Answer one: {findMarker(4)}
    Answer two: {findMarker(14)}
""")

"""
Right after completion:
- Felt pretty good. Didn't need a lot of lines
- Still too 'procedural'
- Happy I could quickly move the 4/14 to a param and keep the method generic
Right after seeing other people's solutions:
- Dang it, too procedural.
Learned:
- 
"""