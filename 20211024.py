def main():
    num = int(input())
    s = str(input())

    ans = "yes" if s[num - 1] == "o" else "no"
    print(ans)


if __name__ == "__main__":
    main()
