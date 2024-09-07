class BatoResult:
    def __init__(self, title: str, author: str, artist: str, genres: list, status: str, description: str, thumbnail: str, chapter_links: list):
        self.__title = title
        self.__author = author
        self.__artist = artist
        self.__genres = genres
        self.__status = status
        self.__description = description
        self.__thumbnail = thumbnail
        self.__chapter_links = chapter_links

    def get_images_from_chapter(self, chapter_idx: int) -> list:
        '''Returns a list of image links from a chapter'''
        imgs_links = list()
        # Logic to get the images from the chapter
        return imgs_links


    def get_chapter_count(self) -> int:
        '''Returns the number of chapters'''
        return len(self.chapter_links)

    def get_author(self) -> str:
        '''Returns the author of the manga'''
        return self.author

    def get_artist(self) -> str:
        '''Returns the artist of the manga'''
        return self.artist
    
    def get_genres(self) -> list:
        '''Returns the genres of the manga'''
        return self.genres
    
    def get_status(self) -> str:
        '''Returns the status of the manga'''
        return self.status
    
    def get_description(self) -> str:
        '''Returns the description of the manga'''
        return self.description
    
    def get_thumbnail(self) -> str:
        '''Returns the thumbnail of the manga'''
        return self.thumbnail
    
    def get_chapter_links(self) -> list:
        '''Returns the chapter links of the manga'''
        return self.chapter_links

    def __str__(self) -> str:
        '''Returns a string representation of the object'''
        return f"Title: {self.title}\nAuthor: {self.author}\nArtist: {self.artist}\nGenres: {self.genres}\nStatus: {self.status}\nDescription: {self.description}\nThumbnail: {self.thumbnail}\nChapter Links: {self.chapter_links}"


class BatoSemiResult:
    def __init__(self, title: str, alias: list, genre: list, last_vol_ch: str, thumbnail: str) -> None:
        self.__title = title
        self.__alias = alias
        self.__genre = genre
        self.__last_vol_ch = last_vol_ch
        self.__thumbnail = thumbnail
    
    def get_title(self) -> str:
        '''Returns the title of the manga'''
        return self.__title
    
    def get_alias(self) -> list:
        '''Returns the alias of the manga'''
        return self.__alias
    
    def get_genre(self) -> list:
        '''Returns the genre of the manga'''
        return self.__genre
    
    def get_last_vol_ch(self) -> str:
        '''Returns the last volume and chapter of the manga'''
        return self.__last_vol_ch
    
    def get_thumbnail(self) -> str:
        '''Returns the thumbnail of the manga'''
        return self.__thumbnail