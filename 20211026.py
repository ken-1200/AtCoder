def main():
    """
    問題文
    実数 X.Y が与えられます。ただし Y はちょうど 1 桁です。
    0≤Y≤2 ならば、X-
    3≤Y≤6 ならば、X
    7≤Y≤9 ならば、X+
    と出力してください。

    制約
    1≤X≤15
    0≤Y≤9
    X と Y は整数
    """
    x = str(input("1≤X≤15の整数を入力して下さい"))
    # if x < 1 or x > 15:
    #     return print("正しい文字列を入力してください")

    idx = str(x).find(".")
    s = x[:idx]
    print(idx)

    y = int(input("0≤Y≤9の整数を入力して下さい"))
    if y < 0 or y > 9:
        return print("正しい文字列を入力してください")

    if int(y) >= 7:
        print(f"{x}+")
    elif int(y) >= 3:
        print(f"{x}")
    else:
        print(f"{x}-")


if __name__ == "__main__":
    main()
