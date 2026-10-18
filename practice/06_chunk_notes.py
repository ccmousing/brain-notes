from pathlib import Path

note_dir = Path(r"D:\doubaoziliao\xuexijihua")
md_files = list(note_dir.glob("**/*.md"))

for file_path in md_files:
    text = file_path.read_text(encoding="utf-8")
    chunks = [c.strip() for c in text.split("\n\n") if c.strip()]
    print(f"{file_path.name} 文件被切分为 {len(chunks)} 个 chunk")
    if chunks:
        print(f"第一个 chunk 的内容:\n{chunks[0]}\n")
