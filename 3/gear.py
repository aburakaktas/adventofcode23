
def data_to_list(filename):
    matrix = []
    with open(filename) as file:
        for line in file:
            matrix.append(list(line.strip()))
    return matrix

def main():
    matrix = data_to_list('data.txt')

    lines = len(matrix)
    rows = len(matrix[0])

    # print(lines, rows)
    total = 0
    for i in range(len(matrix)):
        
        is_recording = 0
        j_start = 0
        j_end = 0
        passed_check = 'yes'
        
        for j in range(len(matrix[0])):
            # if the cell is a number, start recording the number until it stops
            if matrix[i][j].isnumeric():
                if is_recording == 0:
                    j_start = j
                    is_recording = 1
                if j == lines:
                    is_recording = 0
                    j_end = j
                    print("aq")
                    
                        

            else:
                
                if is_recording == 1:
                    # print(number, end="")
                    is_recording = 0
                    j_end = j - 1
                    # print("j start:", j_start, "j end:", j_end, end=";")
                
                    rows_to_check = list(range(i-1, i+2))
                    columns_to_check = list(range(j_start-1, j_end +2))

                    rows_to_check = [x for x in rows_to_check if x >= 0 and x < lines]
                    columns_to_check = [x for x in columns_to_check if x >= 0 and x < rows]
                    # print(" rows to check:", rows_to_check, "columns to check:", columns_to_check)
                    # print("---")
                    for row in rows_to_check:
                        for column in columns_to_check:
                            if not (matrix[row][column].isalnum() or matrix[row][column] == "."):
                                passed_check = 'no'
                    #         print(matrix[row][column], end="")
                    #     print("")
                    # print("passed", passed_check)
                    # print("---")

                    passed_number = ""
                    if passed_check == 'no':
                        for k in range(j_start, j_end + 1):
                            passed_number += matrix[i][k]
                    if passed_number:
                        
                        total += int(passed_number)





                    passed_check = 'yes'
                    j_start = 0
                    j_end = 0
                    number = 0
                    # print(".", end="")

                    
                    # return




                
        print(total)

    
if __name__ == "__main__":
    main()