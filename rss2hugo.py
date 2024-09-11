import feedparser
import os
from datetime import datetime

# 配置 RSS 源 URL 和 Hugo 文章目录
RSS_FEED_URL = "https://rss-worker.haiyang-una.workers.dev/rss/xiaohongshu/user/5cff9acc0000000025018949"
HUGO_CONTENT_DIR = "./content/posts/"


# 获取 RSS feed 数据
def fetch_rss():
    feed = feedparser.parse(RSS_FEED_URL)
    return feed.entries


# 将 RSS 项目转换为 Markdown 文件
def create_markdown_file(entry):
    # 从 RSS 提取所需数据
    title = entry.title
    link = entry.link
    # published = datetime(*entry.published_parsed[:6])
    content = entry.summary

    # 创建 Markdown 文件内容
    markdown_content = f"""---
    title: "{title}"
    link: "{link}"
    ---
    
    {content}
    """
    # 定义 Markdown 文件的文件名
    filename = os.path.join(
        HUGO_CONTENT_DIR,
        f"{title.replace(' ', '-').lower()}.md",
    )

    # 将内容写入 Markdown 文件
    with open(filename, "w", encoding="utf-8") as f:
        f.write(markdown_content)


# 主程序：抓取 RSS 并生成 Hugo 文章
def main():
    entries = fetch_rss()
    for entry in entries:
        create_markdown_file(entry)
    print(f"Successfully created {len(entries)} new posts!")


if __name__ == "__main__":
    main()
