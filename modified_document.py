# 读取文档内容
with open("2026.md", "r") as file:
    document_content = file.read()

# 将文档内容按月份分割成块
months_blocks = document_content.split("#### ")

# 删除开头的空块
# months_blocks = months_blocks[1:]

# 对每个月份的块进行处理
new_document_content = ""
for month_block in months_blocks:
    # 将块内容按行拆分
    lines = month_block.strip().split("\n")
    
    # 获取月份标题
    month_title = lines[0]
    
    # 将每一行的单元格内容拆分成列表
    table_rows = [line.split("|") for line in lines[2:]]
    
    # 移动每一行的最后一列到第一列
    for row in table_rows:
        last_cell = row.pop(-2)  # 移除最后一列，并保存其内容
        row.insert(1, last_cell)  # 将最后一列的内容插入到第一列的后面
    
    # 重新构建处理后的块内容
    new_month_block = f"#### {month_title}\n" + "\n".join("|".join(row) for row in table_rows)
    
    # 将处理后的块添加到新文档内容，并加上一个换行
    new_document_content += new_month_block + "\n\n"

# 将处理后的文档内容写回文件
with open("2026.md", "w") as file:
    file.write(new_document_content)

print("Table columns moved successfully!")
