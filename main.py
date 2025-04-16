import sys
import requests
from PyQt5.QtWidgets import (QApplication, QWidget, QVBoxLayout, 
                             QPushButton, QTextBrowser, QLineEdit, QLabel)
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont

class SearchApp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        # Set window properties
        self.setWindowTitle('Search App')
        self.setGeometry(100, 100, 600, 400)
        self.setStyleSheet("background-color: #f5f5f5; border-radius: 10px;")  # Light background with rounded corners
        
        # Create layout
        layout = QVBoxLayout()
        layout.setContentsMargins(20, 20, 20, 20)  # Margins for the layout

        # Title label
        title = QLabel("Welcome to the Search App")
        title.setFont(QFont('Helvetica', 24))
        title.setAlignment(Qt.AlignCenter)
        layout.addWidget(title)

        # Search input
        self.search_input = QLineEdit(self)
        self.search_input.setPlaceholderText("Enter your search query here...")
        self.search_input.setStyleSheet("padding: 10px; border: 1px solid #007BFF; border-radius: 5px;")
        layout.addWidget(self.search_input)

        # Search button
        self.search_button = QPushButton('Search', self)
        self.search_button.setStyleSheet("background-color: #007BFF; color: white; padding: 10px; border-radius: 5px;")
        self.search_button.clicked.connect(self.perform_search)
        layout.addWidget(self.search_button)

        # Result browser
        self.result_browser = QTextBrowser(self)
        self.result_browser.setOpenExternalLinks(True)  # Make links clickable
        self.result_browser.setStyleSheet("background-color: #ffffff; padding: 10px; border-radius: 5px;")
        layout.addWidget(self.result_browser)

        # Set layout for the main widget
        self.setLayout(layout)

    def perform_search(self):
        query = self.search_input.text().strip()
        if query:
            self.fetch_results(query)
        else:
            self.result_browser.setPlainText("Please enter a valid query.")

    def fetch_results(self, query):
        # Replace with your Google API key and custom search engine ID
        API_KEY = "AIzaSyDNMeM1xBNjL6Ej3IBUGhPhGjvLBiF5oMI"
        CX = "90001fd4025f94539"
        
        url = f"https://www.googleapis.com/customsearch/v1?key={API_KEY}&cx={CX}&q={query}"
        response = requests.get(url)
        data = response.json()

        if 'items' in data:
            results = ""
            for item in data['items']:
                title = item['title']
                link = item['link']
                results += f"<a href='{link}' style='text-decoration: none; color: #007BFF;'>{title}</a><br>{link}<br><br>"  # Use HTML links
            self.result_browser.setHtml(results)  # Show results in HTML format
        else:
            self.result_browser.setPlainText("No results found.")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = SearchApp()
    ex.show()
    sys.exit(app.exec_())
