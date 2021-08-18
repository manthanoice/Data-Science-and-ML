def perse_header(header):
    return header.strip().split(',')
def perse_lines(lines):
    value = []
    for i in lines.strip().split(','):
        if i == '':
            value.append('0.00')
        else:
            value.append(float(i))
    return value
def create_dict_item(headers, values):
    result = {}
    for value,header in zip(headers,values):
        result[header]=value
    return result
def read_csv(path):
    result = []
    with open(path,'r') as file:
        line = file.readlines()
        headers = parse_headers(line[0])
        for data_line in line[1:]:
            value = parse_values(data_line)
            item_dic = create_dict_item(value,header)
            result.append(item_dic)
    return result
