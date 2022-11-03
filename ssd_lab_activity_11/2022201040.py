import csv

def read_csv(path, header=True):
    with open(path) as f:
        file = csv.reader(f)
        file = [*file]
        return file

def remove_last_6_columns(file):
    new_file = []
    for line in file:
        new_file.append(line[:-6])
    return new_file

def drop_negative_change(file):
    new_file = [*filter(lambda x: float(x[6]) >= -3.0,file[1:])]
    columns = file[0]
    # print(columns)
    new_file.insert(0,columns)
    return new_file

def write_average(file):
    columns = file[0]
    file = file[1:]
    open_ = [*map(lambda x: float(x[1].replace(',','')),file)]
    high_ = [*map(lambda x: float(x[2].replace(',','')),file)]
    low_ = [*map(lambda x: float(x[3].replace(',','')),file)]
    open_avg = round(sum(open_) / len(open_), 2)
    high_avg = round(sum(high_) / len(high_), 2)
    low_avg = round(sum(low_) / len(low_), 2)
    
    with open('avg_output.txt','w') as f:
        f.write(str(open_avg)+'\n')
        f.write(str(high_avg)+'\n')
        f.write(str(low_avg)+'\n')

def show_data(file):
    char = input("Enter the first character(in capital) to show stocks: ")
    rows = [*filter(lambda x: x[0][0] == char,file[1:])]
    with open('stock_data.txt','w') as f:
        for row in rows:
            line = " ".join(row)
            f.write(line+'\n')

def main():
    file = read_csv('lab_11_data.csv')
    file = remove_last_6_columns(file)
    file = drop_negative_change(file)
    write_average(file)
    show_data(file)

if __name__ == '__main__':
    main()