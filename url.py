import string
import random

class URLShortener:
    def __init__(self):
        self.url_map = {}
        self.characters = string.ascii_letters + string.digits
        self.short_url_length = 6

    def generate_short_url(self):
        return ''.join(random.choice(self.characters) for _ in range(self.short_url_length))

    def shorten_url(self, original_url):
        if original_url in self.url_map:
            return self.url_map[original_url]
        
        short_url = self.generate_short_url()
        while short_url in self.url_map.values():
            short_url = self.generate_short_url()

        self.url_map[original_url] = short_url
        return short_url

    def original_url(self, short_url):
        for original, short in self.url_map.items():
            if short == short_url:
                return original
        return None

def main():
    shortener = URLShortener()

    while True:
        print("URL Shortener")
        print("1. Shorten a URL")
        print("2. Expand a Shortened URL")
        print("3. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            original_url = input("Enter the URL to shorten: ")
            short_url = shortener.shorten_url(original_url)
            print(f"Shortened URL: {short_url}")

        elif choice == '2':
            short_url = input("Enter the short URL: ")
            original_url = shortener.original_url(short_url)
            if original_url:
                print(f"Expanded URL: {original_url}")
            else:
                print("Short URL not found.")

        elif choice == '3':
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()