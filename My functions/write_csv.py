def write_csv(items, path):
    with open(path, 'w') as f:
        if len(items)==0:
            return
        else:
            headers = list(items[0].keys())
            f.write(','.join(headers)+'\n')
            for item in items:
                values = []
                for header in headers:
                    values.append(str(item.get(header, "")))
                f.write(', '.join(values)+'\n')
