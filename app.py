from summarizer import summarize

def main():
    with open("sample_paper.txt", "r", encoding="utf-8") as file:
        paper_text = file.read()

    result = summarize(paper_text)
    print(result)

if __name__ == "__main__":
    main()
