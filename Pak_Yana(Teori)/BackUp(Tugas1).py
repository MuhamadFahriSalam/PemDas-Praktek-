# define the base salary for each grade
GRADE_SALARY = {'A': 1000000, 'B': 1500000, 'C': 2000000}

# define the allowance percentage for each grade
GRADE_ALLOWANCE = {'A': [0.05, 0.15, 0.25], 'B': [0.15, 0.30, 0.45], 'C': [0.25, 0.35, 0.45]}

# define the overtime pay per hour
OVERTIME_PAY = {'A': 20000, 'B': 25000, 'C':30000}

# get the input from the user
name = input("Nama: ")
work_experience = int(input("Masa Kerja: "))
grade = input("Golongan: ").upper()
total_work_hours = int(input("Total Jam Kerja: "))

# calculate the base salary based on the grade
salary = GRADE_SALARY[grade]

# calculate the allowance based on the grade and work experience
if work_experience > 5:
    allowance = GRADE_ALLOWANCE[grade][2] * salary
else:
    allowance = GRADE_ALLOWANCE[grade][work_experience // 5 - 1] * salary

# calculate the overtime pay if applicable
if total_work_hours > 40 * 7:
    overtime_hours = total_work_hours - 40 * 7
    overtime_pay = OVERTIME_PAY * overtime_hours
else:
    overtime_pay = 0

# calculate the total salary
total_salary = salary + allowance + overtime_pay

# print the results
print("\nDATA PEGAWAI")
print("Nama: ", name)
print("Masa Kerja: ", work_experience, "tahun")
print("Golongan: ", grade)
print("Total Jam Kerja: ", total_work_hours, "jam")
print("\nPERHITUNGAN GAJI")
print("Gaji Pokok: ", salary)
print("Tunjangan: ", allowance)
print("Lembur: ", overtime_pay)
print("Total: ", total_salary)                                                           
