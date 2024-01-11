import time

import scrapy
from scrapy import Spider
from scrapy.http import Response, TextResponse
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

from config import HEADERS
from scrapping.helpers import (
    convert_month_name_to_month_num,
    find_technologies
)


class VacanciesSpider(scrapy.Spider):
    name = "vacancies"
    allowed_domains = ["jobs.dou.ua"]
    start_urls = ["https://jobs.dou.ua/vacancies/?category=Python"]

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.driver = webdriver.Chrome()

    def close(self, spider: Spider, reason: str):
        super().close(self, reason)
        self.driver.close()

    def start_requests(self):

        for url in self.start_urls:
            yield scrapy.Request(url, headers=HEADERS, callback=self.parse)

    def parse(self, response: Response, **kwargs):
        response = self._click_more_vacancies_button(response)

        for vacancy_url in response.css("#vacancyListId .vt::attr(href)").getall():
            yield scrapy.Request(
                url=vacancy_url,
                headers=HEADERS,
                callback=self._parse_vacancy_details
            )

    @staticmethod
    def _parse_vacancy_details(response: Response) -> dict:
        yield {
            "date": convert_month_name_to_month_num(response.css(".date::text").get().strip()),
            "vacancy": response.css(".l-vacancy h1::text").get().replace(u"\xa0", u" ").strip(),
            "salary": (
                response.css(".salary::text").get().replace(u"\xa0", u" ").strip()
                if response.css(".salary::text").get() else None
            ),
            "place": response.css(".place::text").get().replace(u"\xa0", u"").strip(),
            "description": [
                text.replace(u"\xa0", u" ").strip()
                for text in response.xpath(
                    "//div[@class='text b-typo vacancy-section']//text()"
                ).getall()
            ],
            "company": response.css(".b-compinfo .info a::text").get().strip(),
            "required_technologies": find_technologies(
                "".join(
                    [
                        text.replace(u"\xa0", u" ").strip()
                        for text in response.xpath(
                            "//div[@class='text b-typo vacancy-section']//text()"
                        ).getall()
                    ]
                )
            )
        }

    def _click_more_vacancies_button(self, response: Response) -> Response:
        self.driver.get(response.url)

        while True:
            button = self.driver.find_element(
                By.CSS_SELECTOR,
                value="#vacancyListId .more-btn a"
            )

            if button.is_displayed():
                ActionChains(self.driver).click(button).perform()
            else:
                response = TextResponse(
                    url=response.url,
                    headers=response.headers,
                    body=self.driver.page_source,
                    encoding="utf-8",
                )
                return response

            time.sleep(1)
