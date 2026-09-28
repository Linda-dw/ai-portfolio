# vocab_tool.py
# 第3周课后作业最终版：包含填空题生成功能
import csv
import collections

# 【语法点①：变量】定义输入输出路径
DATA_FILE = "data/生词表.csv"
OUTPUT_FILE = "练习.txt"

def load_data(path):
    """读取 CSV 数据"""
    with open(path, 'r', encoding='utf-8') as f:
        return list(csv.DictReader(f))

def process_words(words, level="4"):
    """【语法点④：函数】筛选和统计"""
    # 差异点4：使用列表推导式（来自官方教程）代替普通for循环，代码更简洁
    filtered = [w for w in words if str(w["HSK等级"]) == str(level)]
    
    # 统计词性
    pos_counts = collections.Counter(w["词性"] for w in filtered)
    return filtered, pos_counts

def generate_output(words, counts, out_path):
    """【语法点③：循环 for】生成练习题和填空题"""
    with open(out_path, 'w', encoding='utf-8') as f:
        f.write("--- 词汇练习 ---\n")
        for w in words:
            # 差异点2：改变输出格式
            f.write(f"词语：{w['词汇']} | 等级：HSK{w['HSK等级']} | 词性：{w['词性']} | 释义：{w['释义']}\n")
            
            # 作业2功能扩展：生成填空题
            f.write(f"【填空练习】他凭借_____最终取得了成功。（答案：{w['词汇']}）\n\n")
        
        f.write("--- 词性统计 ---\n")
        for pos, count in counts.items():
            f.write(f"{pos}: {count}个\n")

def main():
    try:
        words = load_data(DATA_FILE)
        # 筛选 HSK 4 级的词
        filtered_words, counts = process_words(words, level="4")
        generate_output(filtered_words, counts, OUTPUT_FILE)
        
        print(f"处理完成！共处理 {len(words)} 个词，筛选出 HSK4 词汇 {len(filtered_words)} 个。")
        print(f"已生成结果文件：{OUTPUT_FILE}")
        
    except FileNotFoundError:
        print(f"错误：找不到 {DATA_FILE}，请检查路径是否正确。")
    except KeyError as e:
        print(f"错误：CSV表头缺少必要的列，报错的列名是：{e}")

if __name__ == "__main__":
    main()