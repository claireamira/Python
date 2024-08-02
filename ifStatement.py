english_mark = float(input("Enter the mark for English: "))
maths_mark = float(input("Enter the mark for Maths: "))
kiswahili_mark = float(input("Enter the mark for Kiswahili: "))
science_mark = float(input("Enter the mark for Science: "))
history_mark = float(input("Enter the mark for History: "))

average = (english_mark + maths_mark + kiswahili_mark + science_mark + history_mark) / 5

if average >= 81:
    grade = 'A'
elif 71 <= average < 81:
    grade = 'B'
elif 61 <= average < 71:
    grade = 'C'
elif 51 <= average < 61:
    grade = 'D'
else:
    grade = 'E'

print(f"Average: {average:.2f}")
print(f"Grade: {grade}")
