from models import Authors,Quotes
from connect import connection

def get_quote_by_name(name):
    author_name = name.split(":")[1].strip()
    author = Authors.objects.get(fullname=author_name)
    quotes = Quotes.objects.filter(author=author)
    for quote in quotes:
        print("Quote:", quote.quote)

def get_quote_by_tag(tag):
    tag = tag.split(":")[1].strip()
    quotes = Quotes.objects.filter(tags=tag)
    for quote in quotes:
        print("Quote:", quote.quote)

def get_quote_by_tags(tags):
    tags = tags.split(":")[1].strip().split(",")
    quotes = Quotes.objects.filter(tags__in=tags)
    for quote in quotes:
        print("Quote:", quote.quote)

def main():
    while True:
        connection()

        print('Enter author name,tag or tags to find quotes!')
        print('---------------------------------------------')
        
        value = input()

        if value.startswith('name:'):
            get_quote_by_name(value)
        elif value.startswith('tag:'):
            get_quote_by_tag(value)
        elif value.startswith('tags:'):
            get_quote_by_tags(value)
        elif value == 'exit':
            break
        else:
            print('No results with your query!')
    
if __name__ == '__main__':
    main()