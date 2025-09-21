# AI Chat Companion 🤖 👇 

A modern, empathetic AI chat companion built with Flask and Google's Gemini Pro API. This web application provides users with a supportive and understanding conversational partner, featuring a beautiful UI with dark mode support and seamless animations.



# ✨ Features of our webapp are as follows 👇

- 🎯 Empathetic AI responses using Gemini API 
- 🌓 Dark/Light toggle mode
- 💾 Local conversation history(History of last chat)
- 🔄 Smooth animations and transitions 
- 📱 Fully responsive design 
- 🔒 Rate limiting for API protection
- 🗑️ Clear chat history with ease
- 🏠 Easy navigation between landing and chat pages

## 🚀 Live Demo of our empathy bot is given below 👇 

[View Live Demo](https://empathy-bot.onrender.com) 
It may take time in loading so wait (deployed on render)
....
## 🛠️ Technologies Used in this project are as follows below  👇

- Flask (Python web framework)
- Google Generative AI (Gemini Pro)
- HTML,CSS
- JavaScript (Vanilla)
- Animate.css
- Python

## 📋 Prerequisites required 

- Python 3.8 or higher version
- Google API key for Gemini Pro or gemini flash 
- Modern web browser

## ⚙️ Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/Empathy_Bot.git
   cd Empathy_Bot
   ```

2. Create a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Create a `.env` file in the root directory:
   ```env
   GOOGLE_API_KEY=your_api_key_here
   SECRET_KEY=your_secret_key_here
   ```

5. Run the application:
   ```bash
   python app.py
   ```

6. Open your browser and navigate to:
   ```
   http://localhost:5000
   ```

## 🔧 Configuration 👇

The application can be configured through environment variables:

- `GOOGLE_API_KEY`: Your Google Gemini Pro API key
- `SECRET_KEY`: Flask session secret key
- `REQUESTS_PER_MINUTE`: Rate limit for API requests (default: 60)
- `REQUESTS_PER_DAY`: Daily limit for API requests (default: 1000)

## 🎨 Customization 👇

You can customize the appearance by modifying:
- `static/style.css` for styling
- `templates/index.html` for layout
- System prompt in `app.py` for AI personality

## 📱 Mobile Support 👇

The application is fully responsive and works on:
- Desktop browsers
- Mobile devices
- Tablets
- Different screen sizes and orientations

## 🔒 Security Features 👇

- Rate limiting
- Input sanitization
- API key protection
- Session management
- Safety settings for AI responses

## 🤝 For Contributing follow the steps  as 👇

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📝 License 👇

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for the details.

## 👏 Acknowledgments 👇


- Google for the Gemini Pro API
- Animate.css for animations
- Flask community for the excellent framework
Made by Aditya Chaudhary

## 📧 For Contact 👇
drop me a mail at:
adityachaudhary834@gmail.com
Project Link: [https://github.com/Empathy_Bot/ai-chat-companion](https://github.com/Empathy_Bot/ai-chat-companion)


---
Made with ❤️ by Empathy_Bot
