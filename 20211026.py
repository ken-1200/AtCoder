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
    xy = str(input("「1≤X≤15」の整数と「0≤Y≤9」の整数を「X.Y」の形式で入力して下さい"))
    idx = str(xy).find(".")
    x = xy[:idx]
    y = xy[idx + 1 :]
    if int(x) < 1 or int(x) > 15:
        return print("正しい文字列を入力してください")
    if int(y) < 0 or int(y) > 9:
        return print("正しい文字列を入力してください")

    if int(y) >= 7:
        print(f"{x}+")
    elif int(y) >= 3:
        print(f"{x}")
    else:
        print(f"{x}-")


if __name__ == "__main__":
    main()
