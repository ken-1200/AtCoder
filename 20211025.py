def main():
    s = str(input("1-10文字の文字列を入力してください"))
    if len(s) < 1 or len(s) > 10:
        return print("正しい文字列を入力してください")

    t = str(input("1-10文字の文字列を入力してください"))
    if len(t) < 1 or len(t) > 10:
        return print("正しい文字列を入力してください")

    list = [word.lower() for word in [s, t]]
    list.sort()
    print("Yes") if list[0] == s else print("No")

    # if list[0] == s:
    #     print("Yes")
    # else:
    #     print("No")


if __name__ == "__main__":
    main()
