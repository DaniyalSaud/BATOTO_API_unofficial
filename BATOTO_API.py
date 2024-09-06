import requests
from bs4 import BeautifulSoup
import ast
import fake_useragent


class Batoto_API:
    
    def __init__(self) -> None:
        self.__base_url = "https://bato.to"
        self.__search_url = "https://bato.to/search"
        self.__browse_url = "https://bato.to/browse"
        self.__latest_releases_url = "https://bato.to/latest"
        self.__base_html = None
        self.__genre_list = ['artbook', 'cartoon', 'comic', 'doujinshi', 'imageset', 'manga', 'manhua', 'manhwa', 'webtoon', 'western', '_4_koma', 'oneshot', 'shoujo', 'shounen', 'josei', 'seinen', 'yuri', 'yaoi', 'bara', 'kodomo', 'old_people', 'non_human', 'gore', 'bloody', 'violence', 'ecchi', 'adult', 'mature', 'smut', 'hentai', 'action', 'adaptation', 'adventure', 'age_gap', 'aliens', 'animals', 'anthology', 'beasts', 'bodyswap', 'boys', 'cars', 'cheating_infidelity', 'childhood_friends', 'college_life', 'comedy', 'contest_winning', 'cooking', 'crime', 'crossdressing', 'delinquents', 'dementia', 'demons', 'drama', 'dungeons', 'emperor_daughte', 'fantasy', 'fan_colored', 'fetish', 'full_color', 'game', 'gender_bender', 'genderswap', 'ghosts', 'girls', 'gyaru', 'harem', 'harlequin', 'historical', 'horror', 'incest', 'isekai', 'kids', 'magic', 'magical_girls', 'martial_arts', 'mecha', 'medical', 'military', 'monster_girls', 'monsters', 'music', 'mystery', 'netorare', 'ninja', 'office_workers', 'omegaverse', 'parody', 'philosophical', 'police', 'post_apocalyptic', 'psychological', 'regression', 'reincarnation', 'reverse_harem', 'revenge', 'reverse_isekai', 'romance', 'royal_family', 'royalty', 'samurai', 'school_life', 'sci_fi', 'shoujo_ai', 'shounen_ai', 'showbiz', 'slice_of_life', 'sm_bdsm', 'space', 'sports', 'super_power', 'superhero', 'supernatural', 'survival', 'thriller', 'time_travel', 'tower_climbing', 'traditional_games', 'tragedy', 'transmigration', 'vampires', 'villainess', 'video_games', 'virtual_reality', 'wuxia', 'xianxia', 'xuanhuan', 'yakuzas', 'zombies']

    
    def __set_homepage_html(self) -> str:
        if self.__base_html == None:
            r = requests.get(self.__base_url)
            self.__base_html = r.text
    
    def get_homepage(self) -> str:
        '''Returns the HTML of the homepage of Batoto'''
        
        if (self.__base_html == None):
            self.__set_homepage_html()
        return self.__base_html
    
    def __set_genre_list(self) -> None:
        '''Sets the genre list of Batoto'''
        if self.__genre_list == None:
            genre_list = list()
            params = {
                'langs': 'en'
            }
            r = requests.get(self.__browse_url, params=params)

            soup = BeautifulSoup(r.text, 'html.parser') 
            # Find all script tags
            scripts = soup.find_all('script')
    
    
            useful_script= None
            # Find the script tag that contains the data we need
            for script in scripts:
                if 'const _genres' in script.text:
                    useful_script = script.text
                    break  
            # remove whitespace
            useful_script = useful_script.strip()
            useful_script = useful_script[16:]

            half_genres = useful_script[: 8454]
            genres_dict = ast.literal_eval(half_genres)
            # remaining_genres = useful_script[8454 + 21: -785]
            # rem = ast.literal_eval(remaining_genres)['genres']
            genre_list = genres_dict.keys()

            self.__genre_list = genre_list
    
    def get_genre_list(self) -> list:
        '''Returns a list of genres available on Batoto'''
        if self.__genre_list == None:
            self.__set_genre_list()

        return self.__genre_list
    
    @staticmethod
    def get_genre_list_S() -> list:
        genre_list = list()
        params = {
            'langs': 'en'
        }
        r = requests.get("https://bato.to/browse", params=params)
        soup = BeautifulSoup(r.text, 'html.parser') 
        # Find all script tags
        scripts = soup.find_all('script')


        useful_script= None
        # Find the script tag that contains the data we need
        for script in scripts:
            if 'const _genres' in script.text:
                useful_script = script.text
                break  
        # remove whitespace
        useful_script = useful_script.strip()
        useful_script = useful_script[16:]
        half_genres = useful_script[: 8454]
        genres_dict = ast.literal_eval(half_genres)
        # remaining_genres = useful_script[8454 + 21: -785]
        # rem = ast.literal_eval(remaining_genres)['genres']
        genre_list = genres_dict.keys()
        return genre_list