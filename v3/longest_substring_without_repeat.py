#https://www.geeksforgeeks.org/length-of-the-longest-substring-without-repeating-characters/

x = "geeksforgeeks"


start_pointer = 0
end_pointer = 0
pos_data = {
}

max_length_sofar = 0
length = 0


end_pointer = 0
while end_pointer < len(x):
    current_char = x[end_pointer]
    if current_char not in pos_data:
        end_pointer += 1
        pos_data[current_char] = end_pointer
        length += 1

        max_length_sofar = max(max_length_sofar, length - start_pointer)

    else:
        conflict_pos = pos_data[current_char]
        for d in x[start_pointer: conflict_pos]:
            del pos_data[d]
        start_pointer = conflict_pos

print(max_length_sofar)
print(pos_data.keys())
