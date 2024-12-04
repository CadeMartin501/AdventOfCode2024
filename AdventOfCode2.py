with open("nums.rb") as file:
    lines = file.readlines()
safeReports = 0
report = []
for line in lines:
    isSafe = True
    line = line.strip()
    report = (line.split(' '))
    int_array = list(map(int, report))
    if ((int_array[0])-(int_array[1]))<0:
        ascending = True
        for i in range(0,len(int_array)-1):
            if (int_array[i])>=(int_array[i+1]) or abs((int_array[i])-(int_array[i+1]))>3:
                isSafe = False
    elif ((int_array[0])-(int_array[1]))>0:
        ascending = False
        for i in range(0,len(int_array)-1):
            if (int_array[i])<=(int_array[i+1]) or abs((int_array[i])-(int_array[i+1]))>3:
                isSafe = False
    else:
        isSafe = False
    if isSafe:
        safeReports+= 1
print(safeReports)