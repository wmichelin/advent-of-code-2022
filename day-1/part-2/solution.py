with open("../input.txt", "r") as f:
    total_calories_by_elf = []
    curr_elf_calories = []
    for line in f.readlines():
        if line == "\n":
            total_calories_by_elf.append(curr_elf_calories[:])
            curr_elf_calories = []
            continue
        
        curr_elf_calories.append(int(line))
    print(f"solution: {sum(sum(curr) for curr in sorted(total_calories_by_elf, key=lambda curr_elf_totals: sum(curr_elf_totals), reverse=True)[:3])}")