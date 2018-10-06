americano=2000
caffelatte=3000
cappucino=3500

americano_sold=int(input("아메리카노 판매 개수 : "))
caffelatte_sold=int(input("카페라떼 판매 개수 : "))
cappucino_sold=int(input("카푸치노 판매 개수 : "))
print("총 매출은 ", americano_sold*americano + caffelatte_sold*caffelatte + cappucino_sold*cappucino, "입니다.")
