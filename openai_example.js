// Load environment variables from .env file
import dotenv from 'dotenv';
import OpenAI from 'openai';

// Initialize dotenv to load .env variables
dotenv.config();

// Initialize the OpenAI client
const openai = new OpenAI({
  apiKey: process.env.OPENAI_API_KEY, // Use your API key from .env
});

// Function to generate a haiku
async function generateHaiku() {
  try {
    const completion = await openai.chat.completions.create({
      model: "gpt-3.5-turbo", // Use "gpt-4" if you have access and want to use that model
      messages: [
        { "role": "user", "content": "Write a haiku about AI" }
      ],
    });

    // Output the AI response
    console.log('AI Response:', completion.choices[0].message.content);
  } catch (error) {
    console.error('Error fetching AI response:', error);
  }
}

// Call the function to generate a haiku
generateHaiku();
