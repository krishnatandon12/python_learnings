# Check the data type of given values.

print(type("Hello world"))

# Int
print(type(12))
# Float
print(type(12.8))
# Complex
print(type(complex(12, 8)))


# Print a string sequence, lists sequence and tuple sequence
strings_sequence = ["K", "R", "I", "S", "H", "N", "A"]
print(strings_sequence, type(strings_sequence))

lists_sequence = [12, "Krishna", 12.8, "Tandon"]
print(lists_sequence, type(lists_sequence))

tuple_sequence = (29, "Saloni", 29.10, "Tandon")
print(tuple_sequence, type(tuple_sequence))

# Dictionary
dictionary_type = {
    "a": 12,
    "b": 12.8,
    "c": "Krishna"
}
print(dictionary_type, type(dictionary_type))
print(dictionary_type["a"])

# Set
set_type = {12, "Krishna", 12.8, "Tandon"}
print(set_type, type(set_type))
