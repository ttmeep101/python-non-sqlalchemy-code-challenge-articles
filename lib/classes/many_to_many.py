class Article:
    all = []

    def __init__(self, author, magazine, title):
        if isinstance(author, Author):
            self.author = author
        else:
            raise ValueError('author must be an Author object')
        if isinstance(magazine, Magazine):
            self.magazine = magazine
        else:
            raise ValueError('magazine must be an Magazine object')
        if isinstance(title, str):
            if len(title) >= 5 and len(title) <= 50:
                self.title = title
            else:
                raise ValueError('title must be between 5 and 50 characters')
        else:
            raise ValueError('title must be a string')
        Article.all_articles(self)

    @property
    def title(self):
        return self.title
    
    @property
    def author(self):
        return self.author
    
    @author.setter
    def author(self, new_author):
        if isinstance(new_author, Author):
            self.author = new_author
        else:
            raise ValueError('author must be an Author object')
        
    @property
    def magazine(self):
        return self.magazine
    
    @magazine.setter
    def magazine(self, new_magazine):
        if isinstance(new_magazine, Magazine):
            self.magazine = new_magazine
        else:
            raise ValueError('magazine must be an Magazine object')
        
    @classmethod
    def all_articles(cls, new_article):
        cls.all.append(new_article)
        
class Author:
    def __init__(self, name):
        if isinstance(name, str):
            if len(name) > 0:
                self.name = name
            else:
                raise ValueError('name must be longer than 0 characters')
        else:
            raise ValueError('name must be a string')

    def articles(self):
        return [article for article in Article.all if article.author == self]

    def magazines(self):
        return list(set([article.magazine for article in Article.all if article.author == self]))

    def add_article(self, magazine, title):
        return Article(self, magazine, title)

    def topic_areas(self):
        topics =  list(set([magazine.category for magazine in Magazine.all if magazine.author == self]))
        return topics if topics else None
    
    @property
    def name(self):
        return self.name

class Magazine:
    all = []

    def __init__(self, name, category):
        if isinstance(name, str):
            if len(name) >= 2 and len(name) <= 16:
                self.name = name
            else:
                raise ValueError('name must be between 2 and 16 characters')
        else:
            raise ValueError('name must be a string')
        if isinstance(category, str):
            if len(category) > 0:
                self.category = category
            else:
                raise ValueError('cateogry must be longer than 0 characters')
        else:
            raise ValueError('category must be a string')
        Magazine.all_magazines(self)

    def articles(self):
        return [article for article in Article.all if article.magazine == self]

    def contributors(self):
        return list(set([article.author for article in Article.all if article.magazine == self]))

    def article_titles(self):
        titles = [article.title for article in Article.all if article.magazine == self]
        return titles if titles else None

    def contributing_authors(self):
        articles = [article for article in Article.all if article.magazine == self]
        author_counts = {}
        for article in articles:
            if article.author in author_counts:
                author_counts[article.author] += 1
            else:
                author_counts[article.author] = 1
        return [author for author, count in author_counts.items() if count >= 2]

    @property
    def name(self):
        return self.name
    
    @name.setter
    def name(self, new_name):
        if isinstance(new_name, str):
            if len(new_name) >= 2 and len(new_name) <= 16:
                self.name = new_name
            else:
                raise ValueError('name must be between 2 and 16 characters')
        else:
            raise ValueError('name must be a string')
    
    @property
    def category(self):
        return self.category
    
    @category.setter
    def category(self, new_category):
        if isinstance(new_category, str):
            if len(new_category) > 0:
                self.category = new_category
            else:
                raise ValueError('cateogry must be longer than 0 characters')
        else:
            raise ValueError('category must be a string')
    
    @classmethod
    def all_magazines(cls, new_magazine):
        cls.all.append(new_magazine)