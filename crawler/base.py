class BaseCrawler:

    def headers(self):
        return {
            'Host':
            'www.uber.com',
            'Referer':
            'https://www.uber.com/pt-BR/fare-estimate/',
            'User-Agent':
            'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36'
        }
