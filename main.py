print("첫번째 숫자 입력 : ")
num1 = int(input())

print("두번째 숫자 입력 : ")
num2 = int(input())

print("1 = 더하기")
print("2 = 빼기")
print("3 = 곱하기")
print("4 = 나누기")
print("계산 입력 ( +, -, *, / ) : ")
symbol = int(input())

if symbol == 1:
    print(" ## 계산기 : ")
    print(str(num1) + " + " + str(num2) + " = " + str(num1 + num2))
if symbol == 2:
    print(" ## 계산기 : ")
    print(str(num1) + " - " + str(num2) + " = " + str(num1 - num2))
if symbol == 3:
    print(" ## 계산기 : ")
    print(str(num1) + " * " + str(num2) + " = " + str(num1 * num2))
if symbol == 4:
    print(" ## 계산기 : ")
    print(str(num1) + " / " + str(num2) + " = " + str(num1 / num2))
else:
    print("정확한 사칙연산 선택이 아닙니다. 프로그램을 종료합니다.")