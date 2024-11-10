def calculate_grade():
    # Get the number of subjects
    num_subjects = int(input("Enter the number of subjects: "))
    
    total_score = 0
    
    # Get the scores for each subject
    for i in range(num_subjects):
        score = float(input(f"Enter the score for subject {i + 1}: "))
        total_score += score

    # Calculate the total percentage
    percentage = (total_score / (num_subjects * 100)) * 100

    # Print the percentage
    print(f"Total Percentage: {percentage:.2f}%")

    # Determine the letter grade based 
