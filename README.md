
# AI-Listener

A modern, empathetic AI chat companion built with Flask and Google's Gemini Pro API. This web application provides users with a supportive and understanding conversational partner, featuring a clean UI with dark mode support and smooth animations.

## Features

* Empathetic AI responses using Gemini API
* Dark/Light mode toggle
* Local conversation history (last chat stored)
* Smooth animations and transitions
* Fully responsive design
* Rate limiting for API protection
* Clear chat history option
* Easy navigation between landing and chat pages

## Live Demo

[View Live Demo](https://empathy-bot.onrender.com)

*(Deployed on Render, may take time to load)*

## Technologies Used

* Flask (Python web framework)
* Google Generative AI (Gemini Pro)
* HTML, CSS
* JavaScript (Vanilla)
* Animate.css
* Python

## Prerequisites

* Python 3.8 or higher
* Google API key for Gemini Pro or Gemini Flash
* Modern web browser

## Installation

1. Clone the repository:
   <pre class="overflow-visible!" data-start="1223" data-end="1320"><div class="contain-inline-size rounded-2xl relative bg-token-sidebar-surface-primary"><div class="sticky top-9"><div class="absolute end-0 bottom-0 flex h-9 items-center pe-2"><div class="bg-token-bg-elevated-secondary text-token-text-secondary flex items-center gap-4 rounded-sm px-2 font-sans text-xs"></div></div></div><div class="overflow-y-auto p-4" dir="ltr"><code class="whitespace-pre! language-bash"><span><span>git </span><span>clone</span><span> https://github.com/adityachaudharycode/AI-Listener
   </span><span>cd</span><span> AI-Listener
   </span></span></code></div></div></pre>
2. gitCreate a virtual environment:
   <pre class="overflow-visible!" data-start="1358" data-end="1460"><div class="contain-inline-size rounded-2xl relative bg-token-sidebar-surface-primary"><div class="sticky top-9"><div class="absolute end-0 bottom-0 flex h-9 items-center pe-2"><div class="bg-token-bg-elevated-secondary text-token-text-secondary flex items-center gap-4 rounded-sm px-2 font-sans text-xs"></div></div></div><div class="overflow-y-auto p-4" dir="ltr"><code class="whitespace-pre! language-bash"><span><span>python -m venv venv
   </span><span>source</span><span> venv/bin/activate  </span><span># On Windows: venv\Scripts\activate</span><span>
   </span></span></code></div></div></pre>
3. Install dependencies:
   <pre class="overflow-visible!" data-start="1490" data-end="1539"><div class="contain-inline-size rounded-2xl relative bg-token-sidebar-surface-primary"><div class="sticky top-9"><div class="absolute end-0 bottom-0 flex h-9 items-center pe-2"><div class="bg-token-bg-elevated-secondary text-token-text-secondary flex items-center gap-4 rounded-sm px-2 font-sans text-xs"></div></div></div><div class="overflow-y-auto p-4" dir="ltr"><code class="whitespace-pre! language-bash"><span><span>pip install -r requirements.txt
   </span></span></code></div></div></pre>
4. Create a `.env` file in the root directory:
   <pre class="overflow-visible!" data-start="1591" data-end="1675"><div class="contain-inline-size rounded-2xl relative bg-token-sidebar-surface-primary"><div class="sticky top-9"><div class="absolute end-0 bottom-0 flex h-9 items-center pe-2"><div class="bg-token-bg-elevated-secondary text-token-text-secondary flex items-center gap-4 rounded-sm px-2 font-sans text-xs"></div></div></div><div class="overflow-y-auto p-4" dir="ltr"><code class="whitespace-pre! language-env"><span>GOOGLE_API_KEY=your_api_key_here
   SECRET_KEY=your_secret_key_here
   </span></code></div></div></pre>
5. Run the application:
   <pre class="overflow-visible!" data-start="1704" data-end="1735"><div class="contain-inline-size rounded-2xl relative bg-token-sidebar-surface-primary"><div class="sticky top-9"><div class="absolute end-0 bottom-0 flex h-9 items-center pe-2"><div class="bg-token-bg-elevated-secondary text-token-text-secondary flex items-center gap-4 rounded-sm px-2 font-sans text-xs"></div></div></div><div class="overflow-y-auto p-4" dir="ltr"><code class="whitespace-pre! language-bash"><span><span>python app.py
   </span></span></code></div></div></pre>
6. Open your browser at:
   <pre class="overflow-visible!" data-start="1765" data-end="1800"><div class="contain-inline-size rounded-2xl relative bg-token-sidebar-surface-primary"><div class="sticky top-9"><div class="absolute end-0 bottom-0 flex h-9 items-center pe-2"><div class="bg-token-bg-elevated-secondary text-token-text-secondary flex items-center gap-4 rounded-sm px-2 font-sans text-xs"></div></div></div><div class="overflow-y-auto p-4" dir="ltr"><code class="whitespace-pre!"><span><span>http:</span><span>//localhost:5000</span><span>
   </span></span></code></div></div></pre>

## Configuration

Environment variables:

* `GOOGLE_API_KEY`: Your Google Gemini Pro API key
* `SECRET_KEY`: Flask session secret key
* `REQUESTS_PER_MINUTE`: API requests per minute (default: 60)
* `REQUESTS_PER_DAY`: API requests per day (default: 1000)

## Customization

* `static/style.css` → Styling
* `templates/index.html` → Layout
* System prompt in `app.py` → AI personality

## Mobile Support

* Desktop browsers
* Mobile devices
* Tablets
* Different screen sizes and orientations

## Security Features

* Rate limiting
* Input sanitization
* API key protection
* Session management
* Safety settings for AI responses

## Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

* Google for Gemini Pro API
* Animate.css for animations
* Flask community for the framework

---

**Made with dedication by Aditya Chaudhary**

📧 Contact: [adityachaudhary834@gmail.com]()

🔗 Project Link: https://empathy-bot.onrender.com/
