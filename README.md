# User_Management_System
-------

## 설명
이사님의 요청사항으로 주문자가 첫주문 고객인지 관리할 수 있는 프로그램을 만들었다.

## 환경
import tkinter, PIL, openpyxl, pyinstaller
```
pip install tk
```
```
pip install Pillow
```
```
pip install openpyxl
```
```
pip install pyinstaller
```
Making EXE file
```
pyinstaller --add-binary "path\\PIL;PIL" --add-binary "path\\openpyxl;openpyxl" -F -w --icon=아이콘명.ico ppap.py
```
## 구현 사진
![1111](https://github.com/AF797/User_Management_System/assets/86837707/97aefc26-83f8-4020-9a06-8f9253893aff)

![2222](https://github.com/AF797/User_Management_System/assets/86837707/9a85f1fc-f325-4238-a869-78836d183347)

## 구현 영상
![ppap](https://github.com/AF797/User_Management_System/assets/86837707/97f04e4c-589e-42ba-be1e-7ff9c853878f)

## Update
(2023-08-02)
- 엑셀에 데이터를 추가하는 로직에 치명적 결함이 있었다. 이를 해결하였다.
- 고객이 주문한 날짜도 원하셔서 추가해드렸다. 코드 업데이트는 하지 않을 예정이다.

- 업데이트 구현 영상
  ![user](https://github.com/AF797/User_Management_System/assets/86837707/f0aea90f-cc90-4de6-b82d-d570474a56ed)
