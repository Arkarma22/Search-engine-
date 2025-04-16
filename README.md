# 🔍 Google Custom Search Node App

A lightweight Node.js web app that allows users to search the internet using the **Google Programmable Search Engine (CSE)** API. You can filter which websites the search results come from by configuring your CSE settings.

---

## 📦 Technologies Used

- **Node.js** – lightweight runtime environment
- **Axios** – HTTP requests to Google Search API
- **dotenv** – secure environment variable handling
- **Google Programmable Search Engine** – restricts searches to specific sites

---

## 🛠 Setup & Installation

### 1. Clone the Repository

```bash
git https://github.com/Arkarma22/Search-engine-
cd Search-engine
```
2. Install Dependencies
bash
Copy
Edit
npm install
This installs:

axios

dotenv

3. Get Your Google API Key & CSE ID
Step 1: Go to Google Cloud Console

Create a project

Enable Custom Search API

Create an API key

Step 2: Go to Programmable Search Engine

Create a search engine

Add sites you want to include in the search

Copy your Search Engine ID (CX)

4. Create a .env File
In the root folder, create a .env file and add the following:

env
Copy
Edit
GOOGLE_API_KEY=your-google-api-key
GOOGLE_CSE_ID=your-custom-search-engine-id
✅ You can also check .env.example as a reference.

5. Run the App
bash
Copy
Edit
node index.js
Then open your browser and go to:

arduino
Copy
Edit
http://localhost:3000
Type a search query and hit enter to see filtered search results using your configured CSE.

🌐 How It Works
When the app receives a search query, it sends a request to the Google Custom Search API.

The API returns results limited to the domains you configured.

Results are displayed with titles and clickable links.

📁 File Structure
perl
Copy
Edit
.
├── index.js            # Main server code
├── .env.example        # Example environment variables
├── .gitignore          # Ignores node_modules and .env
├── package.json        # Project config and dependencies
├── package-lock.json   # Dependency lockfile
🔒 Security Notes
Keep your .env file private.

Never commit API keys to a public repository.

Add .env to .gitignore (already included).


👨‍💻 Author
Built by ARK

✅ Happy Coding!
vbnet
Copy
Edit

Let me know if you'd like me to write this directly to a file or customize it further (like adding screenshots, instructions for deploying online, or converting it into an Electron app).
