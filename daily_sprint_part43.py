# === Stage 43: Добавь пагинацию длинных списков ===
# Project: DailySprint
def paginate(items, page_size):
    for i in range(0, len(items), page_size):
        yield items[i:i + page_size]
