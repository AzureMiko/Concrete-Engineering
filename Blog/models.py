
class PostUI:
    def __init__(self):
        self.__author_name = ''
        self.__author_id = -10000
        self.__body = ''
        self.__post_title = ''
    def save(self):
        pass
    def get(self):
        pass
    @property
    def author_name(self):
        return self.__author_name
    @author_name.setter
    def author_name(self, author_name):
        if (author_name == '') or (author_name is None):
            raise ValueError('The author name can not be  null or blank!')
        else:
            self.__author_name = author_name
    @property
    def author_id(self):
        return self.__author_id
    @author_id.setter
    def author_id(self, author_id):
        if (author_id is None) or (author_id <= 0):
            raise ValueError('The author is is not null or <= 0')
        else:
            self.__author_id = author_id
    @property
    def post_body(self):
        return self.__body
    @post_body.setter
    def post_body(self, body):
        if not  isinstance(body, str):
            raise ValueError('The post must be a string!')
        else:
            self.__body = body
    @property
    def post_title(self):
        return self.__post_title
    @post_title.setter
    def post_title(self, title):
        if title == '' or title is None:
            raise ValueError('The title can not be null or blank!')
        else:
            self.__post_title = title
