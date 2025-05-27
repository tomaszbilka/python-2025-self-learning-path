import requests

def main():
    r = requests.get("https://www.selleo.com")
    print("Hello from week-01!")
    print(r.status_code)


if __name__ == "__main__":
    main()
