import pandas as pd
import sqlite3 as sql
import matplotlib.pyplot as plt

# reading and displaying database with pandas
with sql.connect("student.db") as conn:
    df = pd.read_sql('select * from tbl_stud', conn)
    print("All student records:")
    print(df)
    print()

    # Display basic statistics
    print("Database Statistics:")
    print(f"Total students: {len(df)}")

    # Count by gender
    gender_counts = df['sex'].value_counts()
    print("Gender distribution:")
    print(gender_counts)
    print()

    # Count by course
    course_counts = df['course'].value_counts()

    if course == 'BSIT':
        bsitcount+1
    elif course == 'BSCS':
        bscscount+1
    else: bsiscount+1

    print("Course distribution:")
    print(course_counts)
    print()

    # Create visualizations based on actual data

    # 1. Gender Distribution Pie Chart
    plt.figure(figsize=(12, 8))

    plt.subplot(2, 2, 1)
    colors = ['lightblue', 'lightpink']
    plt.pie(gender_counts.values, labels=gender_counts.index, colors=colors,
            startangle=90, shadow=True, autopct='%1.1f%%')
    plt.title('Gender Distribution')

    # 2. Course Distribution Bar Chart
    plt.subplot(2, 2, 2)
    course_counts.plot(kind='bar', color='skyblue')
    plt.title('Students by Course')
    plt.xlabel('Course')
    plt.ylabel('Number of Students')
    plt.xticks(rotation=45)

    # 3. Student Numbers (if they are numeric)
    plt.subplot(2, 2, 3)
    try:
        # Try to convert student numbers to numeric for plotting
        numeric_stud_no = pd.to_numeric(df['stud_no'], errors='coerce')
        if not numeric_stud_no.isna().all():
            plt.scatter(range(len(numeric_stud_no)), numeric_stud_no,
                        color='green', marker='o', s=50)
            plt.title('Student Numbers')
            plt.xlabel('Record Index')
            plt.ylabel('Student Number')
        else:
            plt.text(0.5, 0.5, 'Student numbers are not numeric',
                     ha='center', va='center', transform=plt.gca().transAxes)
            plt.title('Student Numbers Distribution')
    except:
        plt.text(0.5, 0.5, 'Cannot plot student numbers',
                 ha='center', va='center', transform=plt.gca().transAxes)
        plt.title('Student Numbers Distribution')

    # 4. Course and Gender Cross-tabulation
    plt.subplot(2, 2, 4)
    if len(df) > 0:
        crosstab = pd.crosstab(df['course'], df['sex'])
        crosstab.plot(kind='bar', stacked=True, color=['lightblue', 'lightpink'])
        plt.title('Course Distribution by Gender')
        plt.xlabel('Course')
        plt.ylabel('Number of Students')
        plt.xticks(rotation=45)
        plt.legend(title='Gender')

    plt.tight_layout()
    plt.show()

    # Additional analysis
    print("Detailed Course and Gender Analysis:")
    if len(df) > 0:
        crosstab = pd.crosstab(df['course'], df['sex'], margins=True)
        print(crosstab)
    else:
        print("No data available for analysis")

print("\nAnalysis complete!")