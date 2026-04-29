// netlify\functions\submit-survey.js
const axios = require('axios');

exports.handler = async (event, context) => {
  // 1. Only allow POST requests
  if (event.httpMethod !== "POST") {
    return { statusCode: 405, body: "Method Not Allowed" };
  }

  try {
    // 2. Get the data sent from your HTML form
    const formData = new URLSearchParams(event.body);
    
    // 3. Add your secret key and other "invisible" metadata
    // These values are pulled from Netlify Environment Variables
    const GOOGLE_SCRIPT_URL = process.env.GOOGLE_SCRIPT_URL;
    const APP_SECRET = process.env.APP_SECRET;
    
    formData.append("app_secret", APP_SECRET);

    // 4. Forward the data to Google Apps Script
    const response = await axios.post(GOOGLE_SCRIPT_URL, formData.toString(), {
      headers: {
        "Content-Type": "application/x-www-form-urlencoded"
      }
    });

    return {
      statusCode: 200,
      body: JSON.stringify({ message: "Success", data: response.data })
    };

  } catch (error) {
    console.error("Proxy Error:", error);
    return {
      statusCode: 500,
      body: JSON.stringify({ error: "Failed to send data to storage." })
    };
  }
};
