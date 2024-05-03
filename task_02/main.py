def get_cats_info(path):
    cats_info =[]
    try:
        with open(path, 'r', encoding='utf-8') as file:
            for line in file:
                cat_data = line.strip().split(',')
                if len(cat_data) == 3:
                    cat = {
                        "id": cat_data[0],
                        "name": cat_data[1],
                        "age": cat_data[2]
                    }
                    cats_info.append(cat)    
                else:
                    print(f"Incorrect data format '{line.strip()}'")    
    except FileNotFoundError:
        print("File not found!") 
    except Exception as e:
        print(f"An error occurred: {e}")   

    return cats_info    

cats_info = get_cats_info("task_02/cats_file.txt")
print(cats_info)