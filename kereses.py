import random

def srch(sorted_arr: list[int], target: int) -> int:
    low = 0
    high = len(sorted_arr) - 1

    while low <= high:
        mid = (low + high) // 2
        if sorted_arr[mid] == target:
            return mid
        elif sorted_arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1

    return -1

rand_list = [random.randint(1, 100) for _ in range(10)]
rand_list.sort()

print(f"A listád: {rand_list}. Ebben kereshetsz egy elemet")
trg = int(input("Add meg a keresett számod: "))

index = srch(rand_list, trg)
if index != -1:
    print(f"{rand_list} listában az általad keresett {trg} elem indexe {index}")
else:
    print(f"Az általad keresett {trg} elem nem található meg {rand_list} listában. (returned {index})")






