# Indonesian Parliament Member Data Scraper

This Python script is a web scraper designed to extract and collect information about members of the Indonesian Parliament (DPR) from their official website. It utilizes the requests library to fetch web pages, BeautifulSoup for parsing HTML, and writes the collected data to a CSV file.

## Prerequisites

Before running this script, ensure you have the following:

- Python installed on your system.
- The required Python libraries installed, which can be installed using pip:
  ```bash
  pip install requests beautifulsoup4
  ```

## Usage

1. Clone this repository or download the script.

2. Open the script in a text editor or IDE.

3. Customize the script as needed, such as changing the output filename, headers, or other settings.

4. Run the script using Python:
   ```bash
   python script_name.py
   ```

## Description

- The script starts by sending an HTTP GET request to the Indonesian Parliament's official member listing page for each province.

- It uses a session for better performance when making multiple requests.

- The `fetch_details` function is used to extract the details of each parliament member from their individual page. It extracts information such as name, email, birthplace, religion, membership number, fraction, electoral district, and various biographical data.

- The script iterates through the pages for each province and scrapes data for all parliament members.

- The collected data is written to a CSV file named 'data_anggota_dpr.csv' with predefined field names.

## Customization

Customize the script by adjusting the following variables:

- `BASE_URL`: The base URL of the Indonesian Parliament's member listing page.
- `TIMEOUT`: The timeout value for HTTP requests.
- `HEADERS`: The user-agent header for HTTP requests.
- The structure of the CSV output, including the field names, can be adjusted in the `fieldnames` list.

## License

This code is provided under the MIT License. You can find the full license details in the `LICENSE` file.

## Disclaimer

This web scraping script is intended for educational and personal use. Ensure that you respect the website's terms of service and privacy policy. Unauthorized scraping may be against the website's terms of use. Always comply with copyright, privacy, and website usage regulations.

Feel free to check out, use, and provide feedback on this scraper. Happy scraping! 🚀 #Python #WebScraping #DataCollection #Parliament #Indonesia #GitHub
