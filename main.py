printf("계산할 첫번째 정수를 입력해주세요.")
num1 = int(input())

printf("계산할 두번째 정수를 입력해주세요.")
num2 = int(input())

printf("1 = 더하기")
printf("2 = 빼기")
printf("3 = 곱하기")
printf("4 = 나누기")
printf("계산할 사칙연산을 선택해주세요.")
symbol = int(input())

if symbol == 1:
    print(str(num1) + " + " + str(num2) + " = " + str(num1 + num2))
if symbol == 2:
    print(str(num1) + " - " + str(num2) + " = " + str(num1 - num2))
if symbol == 3:
    print(str(num1) + " * " + str(num2) + " = " + str(num1 * num2))
if symbol == 4:
    print(str(num1) + " / " + str(num2) + " = " + str(num1 / num2))
else:
    print("정확한 사칙연산 선택이 아닙니다. 프로그램을 종료합니다.")