# 🔍 Google Custom Search Node App

A lightweight Node.js app that lets you search the web using the **Google Programmable Search Engine (CSE)**. You control which websites are included in the search results.

---

## ⚙️ Setup Instructions

### 📦 Install Dependencies  
Run the following command in your terminal:

👉 `npm install`  

This installs:  
✅ axios  
✅ dotenv  

---

### 🔑 Get Your Google API Key & CSE ID

**Step 1: Google Cloud Console**  
1. 🌐 Go to [Google Cloud Console](https://console.cloud.google.com/)  
2. 📁 Create a new project  
3. ✅ Enable the **Custom Search API**  
4. 🔐 Generate an **API key**

**Step 2: Programmable Search Engine**  
1. 🔎 Visit the [Programmable Search Engine](https://programmablesearchengine.google.com/controlpanel)  
2. 🛠️ Create a new custom search engine  
3. 🌍 Add the websites you want to include in the search  
4. 📋 Copy your **Search Engine ID (CX)**

---

### 🗂️ Create a .env File

In the root directory of your project, create a file named `.env` and add:

```
GOOGLE_API_KEY=your-google-api-key  
GOOGLE_CSE_ID=your-custom-search-engine-id
```

📌 Use the `.env.example` file as a guide.

---

### 🚀 Run the App

Start the app by running:

👉 `node index.js`  

Then open your browser and go to:  
🌐 `http://localhost:3000`  

Type a search query and hit **Enter** — your app will return results based on the websites you configured in your CSE settings.

---

## 🌐 How It Works

🔹 The app receives your search query  
🔹 Sends it to the Google Custom Search API  
🔹 Returns results based on your selected websites  
🔹 Displays clickable titles and descriptions in your browser  

---

## 🗃️ Project Structure

- `index.js` – Main app/server file  
- `.env.example` – Sample file for environment variables  
- `.gitignore` – Ignores `node_modules/` and `.env`  
- `package.json` – Contains project info and dependencies  
- `package-lock.json` – Locks dependency versions  

---

## 🔐 Security Tips

🚫 Never commit your actual `.env` file to GitHub  
✅ `.gitignore` already includes `.env` and `node_modules/`  
📁 Use `.env.example` to help others set up their own version safely  

---

## 👨‍💻 Author

Built with ❤️ by **ARK**  
GitHub: [@your-username](https://github.com/your-username)

---

✅ Happy Coding & Exploring the Web Smarter!
