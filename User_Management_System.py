import tkinter as tk
from tkinter import messagebox
from PIL import ImageTk, Image
import openpyxl

def on_submit():   
    if entry1.get() and entry2.get() and entry3.get():
        values = [entry1.get(), entry2.get(), entry3.get()]
        result = "-".join(values)
        print("제출된 값으로 문자열 생성:", result)

        # 엑셀 파일 읽기
        try:
            # 워크북 로드
            wb = openpyxl.load_workbook('kr_user.xlsx', data_only=True)
            sheet = wb.active

            # 첫 번째 열 (A)의 모든 값을 리스트로 가져오기
            column_a_values = [cell.value for cell in sheet['A']]

            if result in column_a_values:
                # 결과가 첫 번째 열 (A)에서 발견된 경우 해당 행의 번호 찾기
                row_num = column_a_values.index(result) + 1

                # 해당 행에서 열 A, B, C의 값을 가져오기
                values_a_b_c = [sheet.cell(row=row_num, column=col_num).value for col_num in range(1, 4)]
                values_a_b_c_str = "           ".join(str(val) for val in values_a_b_c)
                label_result2.config(text=values_a_b_c_str)
                label_result1.config(text="          전화번호                고객명      주문횟수")
            else:
                label_result1.config(text="")
                label_result2.config(text=result + " 는 최초 주문자입니다.")
                
                user_response = messagebox.askyesno("새로운 주문자 추가", "새로운 주문자를 추가하시겠습니까?")
                
                # USER 추가 로직 (코드 생략 합니다 ^^7)

        except Exception as e:
            print("Error occurred while reading the Excel file:", e)
    else:
        label_result2.config(text="번호를 정상적으로 입력하였는지 확인해주세요")


# 창 생성
window = tk.Tk()
window.title("규림 최초 주문자 확인")

# 아이콘 파일 경로
icon_path = "kr.ico"

# 아이콘 설정
window.iconbitmap(default=icon_path)

# 창의 크기 설정
window.geometry("300x500")
window.resizable(width=False, height=False)

# 회사 로고
image_path = "kr_rogo.jpg"  # 이미지 파일 경로
image = Image.open(image_path)
image = image.resize((100, 60))  # 이미지 크기 조정
photo = ImageTk.PhotoImage(image)

# 이미지를 표시할 라벨 생성
label_image = tk.Label(window, image=photo)
label_image.place(relx=0.5, rely=0.1, anchor=tk.CENTER)

# 안내 문구를 표시할 라벨 생성
label = tk.Label(window, text="최초 주문자 확인")
label.place(relx=0.5, rely=0.2, anchor=tk.CENTER)  # 가운데 정렬

label = tk.Label(window, text="입력 예시 : 010 1234 5678")
label.place(relx=0.5, rely=0.3, anchor=tk.CENTER)

label = tk.Label(window, text="made by Min")
label.place(relx=0.15, rely=0.02, anchor=tk.CENTER)

def validate_input(new_text, max_length):
    if new_text == "" or new_text.isdigit() and len(new_text) <= max_length:
        return True
    return False

# 입력 상자 생성 (최대 3글자 숫자 입력 가능)
entry1 = tk.Entry(window, width=6, validate="key", validatecommand=(window.register(lambda text: validate_input(text, 3)), "%P"))
entry1.place(relx=0.3, rely=0.35, anchor=tk.CENTER)  # 가운데 정렬

# 입력 상자 생성 (최대 4글자 숫자 입력 가능)
entry2 = tk.Entry(window, width=6, validate="key", validatecommand=(window.register(lambda text: validate_input(text, 4)), "%P"))
entry2.place(relx=0.5, rely=0.35, anchor=tk.CENTER)  # 가운데 정렬

# 입력 상자 생성 (최대 3글자 숫자 입력 가능)
entry3 = tk.Entry(window, width=6, validate="key", validatecommand=(window.register(lambda text: validate_input(text, 4)), "%P"))
entry3.place(relx=0.7, rely=0.35, anchor=tk.CENTER)  # 가운데 정렬

# 버튼 생성
button = tk.Button(window, text="검색", command=on_submit)
button.place(relx=0.5, rely=0.45, anchor=tk.CENTER)  # 가운데 정렬

# 입력 상자의 포커스를 변경할 때 다음 입력 상자로 포커스 이동
entry1.bind("<KeyRelease>", lambda event: entry2.focus() if len(entry1.get()) >= 3 else None)
entry2.bind("<KeyRelease>", lambda event: entry3.focus() if len(entry2.get()) >= 4 else None)

# 결과 출력 라벨 생성
label_result1 = tk.Label(window, text="")
label_result1.place(relx=0.5, rely=0.6, anchor=tk.CENTER)

# 결과 출력 라벨 생성
label_result2 = tk.Label(window, text="")
label_result2.place(relx=0.5, rely=0.65, anchor=tk.CENTER)


# 이벤트 루프 시작
window.mainloop()
