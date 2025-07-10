📖 Book Recommendation Assistant using IBM Watson :

This project is a smart conversational assistant built with IBM Watson Assistant, designed to help users discover books by their favorite authors, explore new genres, and read summaries before diving into a new read. It integrates natural conversation flow with structured data, enabling personalized recommendations.
________________________________________
✨ Features -


•	📖 Get book recommendations by author or genre
•	📅 Book summaries provided directly in the chat
•	✨ Entity-based conversation using @book, @author, @genre
•	🤖 Pre-trained intents like #greeting, #thank_you, #recommend_book, etc.
•	⚖️ CSV-based entity import for easy scaling
•	🤝 Seamless backend integration (optional) for dynamic responses
________________________________________
📚 Authors Included :


•	Agatha Christie
•	J.K. Rowling
•	George Orwell
•	Haruki Murakami
•	Jane Austen
•	Neil Gaiman
•	Stephen King
•	Dan Brown
•	Colleen Hoover
Each author has 4-5 books with summarized descriptions.
________________________________________
📄 File Structure
watson-book-assistant/

├── watson_assistant/

│   ├── workspace_export.json
│   └── entities/

│       ├── books.csv
│       ├── authors.csv
│       └── genres.csv
├── backend/

│   ├── app.py
│   ├── summaries.json
├── data/

│   └── author_book_list.csv
├── requirements.txt
└── README.md
________________________________________
🚪 Example Conversation :


User: can you recommend something by agatha.
Shelfie: 
Classic whodunits and twist endings await! Do you want something iconic like Murder on the Orient Express or a lesser-known gem?
 The Murder of Roger Ackroyd
________________________________________
🌐 Deployment Options


•	IBM Cloud Watson Assistant only (no backend)
•	Flask API + Watson (for dynamic data)
•	Render or Heroku (for backend hosting)
________________________________________
🚀 Future Enhancements


•	User profile memory (Watson context variables)
•	Feedback-based recommendations
•	Genre-based filtering and exploration
•	Book rating and popularity scores
________________________________________
👤 Author
Sakshi singh

