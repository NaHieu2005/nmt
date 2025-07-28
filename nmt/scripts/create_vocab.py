import sys
from collections import Counter


def create_vocab(input_file_path, output_file_path, min_freq=1):
    """
    Tạo từ vựng từ một file văn bản đầu vào và ghi kết quả ra một file đầu ra.
    """
    word_counts = Counter()
    try:
        # Mở file đầu vào với mã hóa UTF-8 để đọc
        with open(input_file_path, 'r', encoding='utf-8') as f_in:
            for line in f_in:
                word_counts.update(line.strip().split())
    except FileNotFoundError:
        print(f"Lỗi: Không tìm thấy file đầu vào '{input_file_path}'")
        sys.exit(1)

    # Lấy danh sách các từ, sắp xếp theo tần suất từ cao đến thấp
    vocab = [word for word, count in word_counts.most_common() if count >= min_freq]

    try:
        # Mở file đầu ra với mã hóa UTF-8 để ghi. Đây là điểm mấu chốt!
        with open(output_file_path, 'w', encoding='utf-8') as f_out:
            # Ghi các token đặc biệt vào file
            f_out.write("<unk>\n")
            f_out.write("<s>\n")
            f_out.write("</s>\n")

            # Ghi các từ trong từ vựng vào file
            for word in vocab:
                f_out.write(word + "\n")

        print(f"Đã tạo thành công file từ vựng tại: {output_file_path}")

    except IOError:
        print(f"Lỗi: Không thể ghi vào file đầu ra '{output_file_path}'")
        sys.exit(1)


if __name__ == "__main__":
    # Script bây giờ sẽ nhận 2 tham số: file_input và file_output
    if len(sys.argv) != 3:
        print("Lỗi: Cần cung cấp đúng 2 tham số.")
        print("Cách dùng: python create_vocab.py <đường_dẫn_file_input> <đường_dẫn_file_output>")
        sys.exit(1)

    input_file = sys.argv[1]
    output_file = sys.argv[2]
    create_vocab(input_file, output_file)