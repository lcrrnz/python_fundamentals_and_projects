def scores_average(students_info):
    try:
        averages = {} 
        if not students_info:
            print("No student data available. Please enter students first")
        else:
            print("Calculating students' averages. Please wait...")
            for student in students_info:  
                name = student.get("name", "Unknown")  
                scores = [int (value) for key, value in student.items() if key.endswith("score")]
                if not scores: 
                    print(f"Unable to calculate average for {name} (No scores provided)")
                else:
                    averages[name] = sum(scores) / len(scores)
            print(averages)
            
    except Exception as error:
        print(f"Unable to complete due to {error}")
    return averages
