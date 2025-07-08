from flask import Flask, request, jsonify

api = Flask(__name__)

# Your book data
book_data = {
    [
  {
    "author": "Dan Brown",
    "books": [
      {
        "title": "The Da Vinci Code",
        "summary": "Symbologist Robert Langdon uncovers a secret that could shake the foundations of Christianity while solving a murder mystery in the Louvre."
      },
      {
        "title": "Angels & Demons",
        "summary": "Langdon investigates a deadly vendetta against the Vatican by a secret society known as the Illuminati."
      },
      {
        "title": "Inferno",
        "summary": "Langdon races against time in Florence to decode symbols linked to Dante's Inferno to stop a global catastrophe."
      }
    ]
  },
  {
    "author": "Colleen Hoover",
    "books": [
      {
        "title": "It Ends With Us",
        "summary": "A young woman must choose between a new love and an old flame while confronting a cycle of abuse and resilience."
      },
      {
        "title": "Ugly Love",
        "summary": "A tale of intense passion and pain, where love doesn’t come with promises, only heartbreak and healing."
      },
      {
        "title": "Verity",
        "summary": "A struggling writer uncovers dark secrets while ghostwriting for an injured bestselling author."
      }
    ]
  },
  {
    "author": "George Orwell",
    "books": [
      {
        "title": "1984",
        "summary": "In a dystopian future ruled by total surveillance, Winston Smith rebels against a society that punishes independent thought."
      },
      {
        "title": "Animal Farm",
        "summary": "A political allegory where farm animals overthrow humans to create a society of equals — until tyranny returns."
      }
    ]
  },
  {
    "author": "J.K. Rowling",
    "books": [
      {
        "title": "Harry Potter and the Philosopher's Stone",
        "summary": "Orphan Harry discovers he’s a wizard and enters a magical world at Hogwarts School of Witchcraft and Wizardry."
      },
      {
        "title": "Harry Potter and the Chamber of Secrets",
        "summary": "Students are being petrified at Hogwarts, and Harry uncovers the secrets of a hidden chamber within the school."
      }
    ]
  },
  {
    "author": "Jane Austen",
    "books": [
      {
        "title": "Pride and Prejudice",
        "summary": "Elizabeth Bennet navigates love, class, and social expectations in 19th-century England, challenging the proud Mr. Darcy."
      },
      {
        "title": "Sense and Sensibility",
        "summary": "Two sisters — one sensible, one emotional — struggle with love and hardship after their father’s death."
      }
    ]
  },
  {
    "author": "Haruki Murakami",
    "books": [
      {
        "title": "Norwegian Wood",
        "summary": "A nostalgic tale of love and loss as a college student reflects on his relationships in 1960s Tokyo."
      },
      {
        "title": "Kafka on the Shore",
        "summary": "A surreal journey of a runaway teen and an elderly man who talk to cats, blending dreams and reality."
      }
    ]
  },
  {
    "author": "Paulo Coelho",
    "books": [
      {
        "title": "The Alchemist",
        "summary": "A young shepherd named Santiago travels from Spain to Egypt in search of treasure and self-discovery."
      },
      {
        "title": "Brida",
        "summary": "A spiritual journey of a young Irish girl in search of knowledge, love, and her true self."
      }
    ]
  },
  {
    "author": "Stephen King",
    "books": [
      {
        "title": "The Shining",
        "summary": "A family heads to an isolated hotel for the winter, where the father descends into madness and supernatural forces emerge."
      },
      {
        "title": "It",
        "summary": "A group of children confronts a shape-shifting evil entity that haunts their small town every 27 years."
      }
    ]
  },
  {
    "author": "Agatha Christie",
    "books": [
      {
        "title": "Murder on the Orient Express",
        "summary": "Detective Hercule Poirot solves a murder mystery on a snowbound luxury train filled with suspects."
      },
      {
        "title": "And Then There Were None",
        "summary": "Ten strangers are invited to an island, only to be killed off one by one as dark secrets surface."
      }
    ]
  }
]

}

@app.route('/books', methods=['GET'])
def get_books():
    author = request.args.get('author')
    if author in book_data:
        return jsonify({
            "author": author,
            "books": book_data[author]
        })
    else:
        return jsonify({"error": "Author not found"}), 404

if __name__ == '__main__':
    app.run(debug=True)
