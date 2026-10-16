from pathlib import Path

# create a path object
note_path = Path(r"D:\doubaoziliao\xuexijihua\学习计划\学习计划.md")
# read the content of the file
content = note_path.read_text(encoding="utf-8")
# print the content of the file
print(f"读了 {len(content)} 个字符")
