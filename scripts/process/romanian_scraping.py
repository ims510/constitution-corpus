"""
This script scrapes news articles from the Romanian news website www.mediafax.ro. 
It first cleans up the text of the articles by replacing named entities with a placeholder, then it writes the raw and cleaned articles to CSV files.
Each row of the CSV corresponds to an article, and the columns represent a unique id for each article, the category of the article and the text of the article.

Author: Ioana-Madalina SILAI
Date: 17/05/2024

Modules:
    requests: For making HTTP requests.
    lxml.html: For parsing HTML.
    csv: For reading and writing CSV files.
    collections.namedtuple: For creating a simple data structure to hold the scraped data.
    spacy: For natural language processing (finding the named entities in the scraped data).

Functions:
    get_urls(): Fetches and returns a list of URLs from the Romanian news website www.mediafax.ro.
    get_items(url_list): Fetches and returns a list of items from the given list of URLs. Each item is a namedtuple with fields 'id', 'category', and 'text'.
    write_items_to_csv(items, csv_path): Writes the given list of items to a CSV file at the given path.
    clean_items(items): Cleans up the text of the given list of items by replacing named entities with a placeholder, and returns a new list of cleaned items.

Variables:
    raw_csv_path (str): The path to the CSV file where the raw scraped data will be written.
    clean_csv_path (str): The path to the CSV file where the cleaned scraped data will be written.
    Item (namedtuple): A simple data structure to hold the scraped data. Each item has fields 'id', 'category', and 'text'.
"""

import requests
import lxml.html
import csv
from collections import namedtuple
import spacy

# Define the paths to the CSV files
raw_csv_path = "../../data/raw/romanian_news.csv"
clean_csv_path = "../../data/clean/romanian_news.csv"

# Define the namedtuple for items
Item = namedtuple("Item", ["id", "category", "text"])


def get_urls():
    """
    Fetches and returns a list of URLs from the Romanian news website www.mediafax.ro.

    Returns:
        list: A list of URLs.
    """
    r = requests.get("https://www.mediafax.ro")
    root = lxml.html.fromstring(r.content)
    a_tags = root.xpath('//*[@id="content"]/div[3]/ul/li/p/a')
    url_list = []
    for element in a_tags:
        href = element.attrib["href"]
        if href.startswith("http://") or href.startswith(
            "https://"
        ):  # if it's from a different website
            pass
        elif href.startswith("/"):
            url_list.append("https://www.mediafax.ro" + href)
        else:
            url_list.append("https://www.mediafax.ro/" + href)
    return url_list


def get_items(url_list):
    """
    Fetches and returns a list of items from the given list of URLs. Each item is a namedtuple with fields 'id', 'category', and 'text'.

    Parameters:
        url_list (list): A list of URLs.

    Returns:
        list: A list of items, where each item is a namedtuple with fields 'id', 'category', and 'text'.
    """
    list_items = []
    for url in url_list:
        article_id = url.split("-")[-1]
        category = url.split("/")[3]
        r = requests.get(url)
        url_root = lxml.html.fromstring(r.content)
        paragraphs = url_root.xpath('//*[@id="article_text_content"]/div[1]/p')
        text = ""
        for paragraph in paragraphs:
            text += paragraph.text_content().strip() + " "
        item = Item(article_id, category, text)
        list_items.append(item)
    return list_items


def write_items_to_csv(items, csv_path):
    """
    Writes the given list of items to a CSV file at the given path.

    Parameters:
        items (list): A list of items to write to the CSV file.
        csv_path (str): The path to the CSV file.
    """
    with open(csv_path, "a") as f:
        writer = csv.writer(f)
        writer.writerow(Item._fields)
        for item in items:
            writer.writerow(item)


def clean_items(items):
    """
    Cleans up the text of the given list of items by replacing named entities with a placeholder, and returns a new list of cleaned items.

    Parameters:
        items (list): A list of items to clean.

    Returns:
        list: A new list of cleaned items.
    """
    nlp = spacy.load("ro_core_news_sm")
    list_clean_items = []
    for item in items:
        doc = nlp(item.text)
        ne = [ent.text for ent in doc.ents]
        clean_text = ["$NE$" if token.text in ne else token.text for token in doc]
        item = Item(item.id, item.category, " ".join(clean_text))
        list_clean_items.append(item)
    return list_clean_items


def main():
    url_list = get_urls()
    items = get_items(url_list)
    write_items_to_csv(items, raw_csv_path)
    clean_items = clean_items(items)
    write_items_to_csv(clean_items, clean_csv_path)


if __name__ == "__main__":
    main()
