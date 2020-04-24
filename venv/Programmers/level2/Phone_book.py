## 전화번호목록은 리스트로 들어옴
## 전화번호목록의 길이는 1이상 100만 이하
## 각 전화번호의 길이 (원소) 는 1이상 20 이하
## 원소의 길이가 작은 값만이 접두어가 될 수 있음
## 그렇다면 원소의 길이를 비교하여 작은 것이 앞에 있는 문자열과 일치하는지 비교

## 하나라도 존재하면 fals전화번호목록은 리스트로 들어옴
## 전화번호목록의 길이는 1이상 100만 이하
## 각 전화번호의 길이 (원소) 는 1이상 20 이하
## 원소의 길이가 작은 값만이 접두어가 될 수 있음
## 그렇다면 원소의 길이를 비교하여 작은 것이 앞에 있는 문자열과 일치하는지 비교

## 하나라도 존재하면 false이기 때문에 바로 return
## sorted(phone_book)
## 문자열의 길이가 같거나 크면 비교해라
## count++ 를 통해서 Ture를 검증할때, 시간복잡도 최소화
## e이기 때문에 바로 return
## sorted(phone_book)
## 문자열의 길이가 같거나 크면 비교해라
## count++ 를 통해서 Ture를 검증할때, 시간복잡도 최소화

def solution(phone_book):
    phone_book.sort()
    print(phone_book)

    for e in range(len(phone_book)-1):
        if phone_book[e] == phone_book[e+1][0:len(phone_book[e])] :
            return False

    answer = True

    return answer

print(solution(["12","123","1235","567","88"]))