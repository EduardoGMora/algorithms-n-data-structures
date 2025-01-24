# make a identity matrix with n elements
matrix = []
n = 5

def make_identity_matrix(n):
    for i in range(n):
        row = []
        for j in range(n):
            if i == j:
                row.append(1)
            else:
                row.append(0)
        matrix.append(row)
    
    return matrix

for row in make_identity_matrix(n):
    print(f'{row}', end='\n')