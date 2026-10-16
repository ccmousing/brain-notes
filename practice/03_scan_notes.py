from pathlib import Path

note_dir = Path(r"D:\doubaoziliao\xuexijihua")

md_files = list(note_dir.glob("**/*.md"))

print(f"找到了 {len(md_files)} 个 md 文件")

for f in md_files[:10]:  # 先打印前10个看看
    print(f.name, f.stat().st_size, "字节")
