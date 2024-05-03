def total_salary(path):
    
    try:
        with open(path, "r", encoding="utf-8") as file:
            total_salary = 0
            num_developers = 0

            for line in file:
                name, salary = line.strip().split(",")
                total_salary += int(salary)
                num_developers += 1

            if num_developers == 0:
                return 0, 0

            average_salary = total_salary / num_developers
            return total_salary, average_salary    
    except FileNotFoundError:
        print("File not found!")
        return 0, 0
    except Exception as e:
        print(f"An error occurred: {e}")
        return 0, 0
              

total, average = total_salary("task_01/salary_file.txt")
print(f"Загальна сума заробітної плати: {total}, Середня заробітна плата: {average}")              