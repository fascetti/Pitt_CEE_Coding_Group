# def get_largest_string(s, n):

def unique_list(l):
    unique = []
    for i in l:
        if i not in unique:
            unique.append(i)
    return unique


s = "ccabc"
n = 2

letters = len(s)
s_list = []
for i in range(letters):
    s_list.append(s[i])

s_list.sort(reverse=True)
s_list_unique = unique_list(s_list)
unique_count = []

for i in range(len(s_list_unique)):
    unique_count.append(s_list.count(s_list_unique[i]))

string = []
while len(s_list) > 0:
    string.append(s_list[0])

    if len(string) > n and len(unique_list(string[-n:])) == 1:
        del string[-1]
        if len(unique_list(s_list)) > 1:
            string.append(unique_list(s_list)[1])
        else:
            break
    s_list.remove(string[-1])

print(string)
