import requests
from bs4 import BeautifulSoup
import ast
from BATO_RESULT import BatoResult
from BATO_RESULT import BatoSearchResult

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
    

    
    ''' All Static Methods will be defined below'''

    @staticmethod
    def get_genre_list_S() -> list:
        '''Returns a list of genres available on Batoto (A Static Method)'''
        
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
    
    @staticmethod
    def get_search_manga_names_by_title_S(title: str) -> list:
        '''Returns a list of manga titles that match the title (A Static Method)'''
        
        url = "https://bato.to/search"
        params = {
            "word": title,
            'langs': 'en',
        }
        response = requests.get(url, params=params)
        soup = BeautifulSoup(response.text, 'html.parser')
        result = soup.find('div', class_='series-list')
        results = result.find_all('div', class_='line-b')
        titles_search_result = list()
        for res in results:
            j = res.find('div', class_='item-text')
            titles_search_result.append(j.find('a').text)

        return titles_search_result
    
    def __get_max_page_number(self, html: str) -> list:
        '''Returns an integer of the last page link'''
        
        page_links = list()
        max_page_num = 0
        soup = BeautifulSoup(html, 'html.parser')
        pages = soup.find_all('ul', class_='pagination')[-1]
        pages_link = pages.find_all('li', class_='page-item')

        for page in pages_link:
            link = page.find('a')['href']
            link = self.__base_url + link

            page_links.append(link)

        for link in page_links:
            try:
                page_num = int(link.split('=')[-1])
                if page_num > max_page_num:
                    max_page_num = page_num
            except:
                pass
        return max_page_num

    def get_page_links(self, html: str) -> list:
        '''Returns a list of page links'''
        page_links = list()
        max_num_pages = self.__get_max_page_number(html)
        soup = BeautifulSoup(html, 'html.parser')
        pages = soup.find_all('ul', class_='pagination')[-1]
        pages_link = pages.find_all('li', class_='page-item')
        link_template = pages_link[0].find('a')['href']
        link_template = link_template.split('page=')
        base_link = link_template[0] + 'page='

        for i in range(1, max_num_pages + 1):
            page_links.append(f"{self.__base_url}{base_link}{i}")

        return page_links

    def get_manga_list_by_title(self, title: str, limit=20) -> list:
        '''Returns a list of manga links that match the title'''
        
        titles = list()
        params = {
            "word": title,
            'langs': 'en',
        }

        response = requests.get(self.__search_url, params=params)
        page_links = self.get_page_links(response.text)

        for link in page_links:
        # make a request for each page
        # Then get titles from each page
            if len(titles) >= limit:
                break
            response = requests.get(link)
            soup = BeautifulSoup(response.text, 'html.parser')
            result = soup.find('div', class_='series-list')
            results = result.find_all('div', class_='line-b')
        
            for res in results:
                if len(titles) >= limit:
                    break
                img_link = res.find('a', class_='item-cover').find('img')['src'].strip()
        

                text_result = res.find('div', class_='item-text')

                title = text_result.find('a', class_='item-title').text
                link = self.__base_url + text_result.find('a')['href']
                aliasStr = text_result.find('div', class_='item-alias')
                alias = list()
                if aliasStr:
                    alias += aliasStr.text.split('/')
                    alias += aliasStr.text.split(',')
                    for i in range(len(alias)):
                        alias[i] = alias[i].strip()
                else:
                    alias = None
    
                genre = text_result.find('div', class_='item-genre').text.split(',')
                for i in range(len(genre)):
                    genre[i] = genre[i].strip()
    
                volch = text_result.find('div', class_='item-volch')
                if volch:
                    volch = volch.find('a').text.strip()
                else:
                    volch = None
    
                titles.append(BatoSearchResult(title, link, alias, genre, volch, img_link))

        return titles