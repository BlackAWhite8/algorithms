from collections import deque
def find_correct_people(name):
    return len(name) == 4
circle = {}

circle["i"] = ["Alice","Bob", "Eva"]
circle["Bob"] = ["Stuart","Mike"]
circle["Alice"] = ["Ann","John"]
circle["Eva"] = ["Jack"]
circle["Stuart"] = []
circle["Mike"] = []
circle["Ann"] = []
circle["John"] =[]
circle["Jack"] = []

search_que = deque()
search_que += circle["i"]
already_checked = []
while search_que:
    person = search_que.popleft()
    if not person in already_checked:
        if find_correct_people(person):
            print(person)
            break;
        else:
            search_que += circle[person]
            already_checked.append(person)

