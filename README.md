# Hacker News Scraper

## Introduction

This Python script scrapes the [Hacker News](https://news.ycombinator.com/) front page to extract and display the top articles with more than 99 upvotes. It uses the `requests` library for HTTP requests and `BeautifulSoup` for HTML parsing, then sorts the results by vote count.

## Table of Contents

* [Introduction](#introduction)
* [Installation](#installation)
* [Usage](#usage)
* [Features](#features)
* [Dependencies](#dependencies)
* [Configuration](#configuration)
* [Documentation](#documentation)
* [Examples](#examples)
* [Troubleshooting](#troubleshooting)
* [Contributors](#contributors)
* [License](#license)

## Installation

1. Install the required dependencies.

```bash
pip install requests beautifulsoup4
```

## Usage

Run the script using Python:

```bash
python hackernews_scraper.py
```

The script will print a sorted list of articles with more than 99 points.

## Features

* Scrapes Hacker News front page.
* Extracts article title, link, and vote count.
* Filters articles with more than 99 points.
* Sorts articles by vote count in descending order.
* Pretty-prints the results.

## Dependencies

* [requests](https://pypi.org/project/requests/)
* [beautifulsoup4](https://pypi.org/project/beautifulsoup4/)

## Configuration

No configuration is required. The script runs with default settings targeting the Hacker News front page.

## Documentation

### Functions

* `sorted_hn(hnlist)`: Sorts the article list by vote count.
* `create_custom_hn(links, subtext)`: Extracts article data and filters articles with >99 votes.

## Examples

Example output:

```python
[{'title': 'Example Article',
  'links': 'https://example.com/article',
  'votes': 150},
 {'title': 'Another Article',
  'links': 'https://example.com/another',
  'votes': 120}]
```

## Troubleshooting

* **Issue:** No articles are printed.

  * **Solution:** Ensure you have internet connectivity and the Hacker News page structure hasn’t changed.
* **Issue:** `ModuleNotFoundError`

  * **Solution:** Run `pip install requests beautifulsoup4` to install dependencies.

## Contributors

* Jose Reyes — creator and maintainer

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

Would you like me to draft a `LICENSE` file or a `requirements.txt` as well? Let me know!
