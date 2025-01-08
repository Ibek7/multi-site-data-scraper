Multi-Site Data Scraper

A Python-based framework for scraping data from 50+ websites, tailored for research and analysis across diverse domains including academia, news, policy, and statistical platforms.

📜 Overview

This repository is a comprehensive and modular web scraping framework designed to streamline data collection from a wide array of sources. Whether you’re conducting research, monitoring news trends, or analyzing policies, this tool provides a robust foundation for automating your workflows.

Key Features:
	•	📰 Multi-Site Coverage: Support for over 50 websites, with easy extension for more.
	•	🎯 Modular Design: Each scraper is independently configured, making maintenance and updates efficient.
	•	🧪 Unit Testing: Includes tests to ensure reliability and minimize disruptions from website changes.
	•	🛠️ Customizable Configurations: YAML-based configuration for selectors, headers, and site-specific settings.
	•	📊 Focus on Research Needs: Optimized for data analysts, policy researchers, and academics.

🚀 Getting Started

Prerequisites

Ensure the following dependencies are installed on your system:
	•	Python 3.9+
	•	pip (Python package manager)

Installation

Clone the repository and set up your environment:

git clone https://github.com/<username>/multi-site-data-scraper.git
cd multi-site-data-scraper
python -m venv env
source env/bin/activate  # On Windows: env\Scripts\activate
pip install -r requirements.txt

Configuration

Configure the scraper by editing the YAML files in the configs/ directory:
	•	Example:
           africanews:
                      url: "https://www.africanews.com"
                      selectors:
                      article_link: ".teaser_title a"

Running the Scraper

Use the main script to scrape data:
                                  python main.py --config configs/news.yaml


🧪 Testing

Run the unit tests to validate functionality:

                                             python -m unittest discover tests/

📂 Repository Structure

multi-site-data-scraper/
├── configs/
│   ├── settings.yaml        # General scraper settings (e.g., headers, delays)
│   ├── academic.yaml        # Configurations for academic scrapers
│   ├── news.yaml            # Configurations for news scrapers
│
├── data/
│   ├── raw/                 # Raw scraped data
│   ├── processed/           # Cleaned and structured data
│   ├── logs/                # Logs for debugging and monitoring scraper runs
│
├── docs/
│   ├── README.md            # Project overview and setup instructions
│   ├── CONTRIBUTING.md      # Guidelines for collaboration
│   ├── scraper_guidelines.md # Instructions for creating new scrapers
│
├── notebooks/
│   ├── data_cleaning.ipynb  # Jupyter notebook for preprocessing data
│   ├── analysis.ipynb       # Jupyter notebook for data visualization and exploration
│
├── scrapers/
│   ├── academic/            # Academic scraper scripts
│   │   ├── pubmed_scraper.py
│   │   ├── __init__.py
│   ├── news/                # News scraper scripts
│   ├── ngo_policy/          # NGO and policy organization scrapers
│   ├── data_sources/        # Data and statistical sources scrapers
│   ├── regional/            # Regional and specialized platform scrapers
│   ├── aggregators/         # Aggregators and open-access site scrapers
│
├── tests/
│   ├── test_scrapers.py     # Test scripts for individual scrapers
│   ├── test_utils.py        # Test scripts for utilities
│
├── utils/
│   ├── downloader.py        # Utility functions for downloading data
│   ├── parser.py            # Utility functions for parsing data
│   ├── logger.py            # Centralized logging utilities
│   ├── database.py          # Data storage and database utilities (e.g., SQLite, MongoDB)
│
├── .gitignore               # Files and folders to ignore in Git
├── requirements.txt         # Python dependencies for consistent environments
├── Dockerfile               # Docker configuration for containerized environments
├── main.py                  # Entry point for running all or selected scrapers

📚 Documentation

Detailed documentation is available in the docs/ folder, including:
	•	Guidelines for adding new scrapers.
	•	Examples of advanced use cases.
	•	Common troubleshooting steps.

🛠️ Built With
	•	BeautifulSoup - HTML parsing library
	•	Requests - HTTP library for making web requests
	•	PyYAML - For handling YAML configurations
	•	Docker - For containerized deployments

🌟 Contributing

Contributions are welcome! If you’d like to add new features, improve the existing ones, or fix bugs:
	1.	Fork the repository.
	2.	Create a feature branch (git checkout -b feature-name).
	3.	Commit your changes (git commit -m "Add feature-name").
	4.	Push to the branch (git push origin feature-name).
	5.	Open a pull request.


🤝 Acknowledgments

Special thanks to Professor Henry Dambanemuya for their mentorship and guidance in making this project. Your insights into data analysis and web technologies have greatly influenced the design and functionality of this framework.

📄 License

This project is licensed under the MIT License - see the LICENSE file for details.

📧 Contact

For any inquiries or support, please feel free to reach out:
	•	Name: Bekam Guta
	•	Email: bekamdawit551@gmail.com
	•	LinkedIn: http://linkedin.com/in/bekam-guta/
