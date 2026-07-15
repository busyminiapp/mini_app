# === Stage 23: Добавь форматированный вывод таблицей в консоль ===
# Project: DailySprint
def print_table(headers, rows):
    col_widths = [len(str(h)) for h in headers] + \
                 max([max(len(str(r[i])) for r in rows), len(str(headers[i]))] for i in range(len(headers)))
    fmt = ' | '.join(f'{{:<{w}}}' for w in col_widths)
    print(fmt.format(*headers))
    print('-+-'.join('-' * w for w in col_widths))
    for row in rows:
        print(fmt.format(*[str(c) for c in row]))
