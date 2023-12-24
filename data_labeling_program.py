import pandas as pd
import os

pd.options.mode.chained_assignment = None

def check_file_exists(directory, filename):
    file_path = os.path.join(directory, filename)
    return os.path.isfile(file_path)
def start_label(df):
    for i in range(len(df)):
        if pd.isnull(df['Sentiment'][i]) == True:
            print("Câu",i+1,":",df['Sentences'][i])
            label = int(input())
            if label != 0 and label != 1 and label != -1:
                print("Chỉ chấp nhận input 1, -1, 0 thôi bạn :(")
                break
            df['Sentiment'][i] = label
            df.to_csv(labeled_fname, encoding='utf8', index=False)
            print("\n")

dir = os.getcwd()
for i in range(1,4):
    print("unlabeled_data_{num}.csv".format(num = i))
file_number = int(input("Có 3 file, bạn đang gán nhãn file số mấy zị ???:"))

fname = "unlabeled_data_{num}.csv".format(num = file_number)
labeled_fname = "labeled_sentences_{num}.csv".format(num = file_number)
print("="*50)
print("Quy tắc:")
print("1: Câu tích cực.")
print("-1: Câu tiêu cực.")
print("0: Câu trung tính hoặc không có ý nghĩa.")
print("="*50)

if not check_file_exists(dir, fname): print(f"File {fname} không tồn tại. Kiểm tra lại bạn ơi!")
else:
    if not check_file_exists(dir, labeled_fname):
        print(f"Giữ file {labeled_fname} cùng thư mục để có thể tiếp tục quá trình gán nhãn.")
        print("Bắt đầu gán nhãn...")
        print("="*50)
        df = pd.read_csv(dir + "\\" + fname, encoding='utf8')
    else:
        print(f"Đã tìm thấy file {labeled_fname}.")
        print("Tiếp tục gán nhãn...")
        print("="*50)
        df = pd.read_csv(dir + "\\" + labeled_fname, encoding='utf8')
    while True:
        start_label(df)