Customer Feedback Intelligence System

An AI-powered customer feedback analysis system that processes raw customer feedback, identifies sentiment and categories, discovers recurring themes using semantic embeddings and clustering, and generates actionable business insights using a local Large Language Model.

Features

- Text preprocessing and cleaning using NLP techniques
- Sentiment analysis using NLTK VADER
- Rule-based feedback categorization
- Semantic embeddings using Sentence Transformers
- Customer feedback clustering using K-Means
- Structured cluster-level insights and summaries
- AI-generated business recommendations using a local Mistral LLM through Ollama

Project Pipeline


  Customer Feedback
        ↓
  Text Preprocessing
        ↓
  Sentiment Analysis
        ↓
  Feedback Categorization
        ↓
  Semantic Embeddings
        ↓
  K-Means Clustering
        ↓
  Structured Cluster Insights
        ↓
  Local LLM Analysis
        ↓
  Actionable Business Recommendations

Tech Stack

- Language: Python
- NLP: NLTK
- Embeddings: Sentence Transformers
- Machine Learning: Scikit-learn, K-Means
- Data Processing: Pandas
- LLM: Mistral via Ollama
- Development: VS Code, Git, GitHub

Project Structure

```text
CFIS/
│
├── data/
│   └── feedback.csv
│
├── src/
│   ├── categorize.py
│   ├── clustering.py
│   ├── embeddings.py
│   ├── insights.py
│   ├── llm_insights.py
│   ├── preprocess.py
│   ├── run_phase2.py
│   └── sentiment.py
│
├── .gitignore
├── requirements.txt
└── README.md


How It Works

1. Text Preprocessing

Customer feedback is cleaned by:

- Converting text to lowercase
- Removing non-alphabetic characters
- Removing stopwords
- Applying lemmatization

2. Sentiment Analysis

The system uses NLTK VADER to classify feedback into:

- Positive
- Negative
- Neutral

3. Feedback Categorization

Feedback is classified into categories such as:

- Feature Request
- Complaint
- Praise
- Other

4. Semantic Embeddings

The cleaned feedback is converted into numerical vector representations using the all-MiniLM-L6-v2 Sentence Transformer model.

5. Clustering

K-Means clustering groups semantically similar feedback together, helping identify recurring customer themes.

6. Structured Insights

Each cluster is summarized using:

- Number of feedback items
- Sentiment distribution
- Representative feedback examples

7. LLM-Based Insights

The structured cluster information is passed to a local Mistral model through Ollama to identify:

- Key customer pain points
- Priority issues
- Potential product improvements
- Actionable recommendations

Installation

Clone the repository:

git clone https://github.com/AtharvaBilloreIndore/CFIS.git
cd CFIS

Create a virtual environment:

python -m venv senv

Activate it on Windows PowerShell:

.\senv\Scripts\Activate.ps1

Install dependencies:

pip install -r requirements.txt


NLTK Resources

The project automatically downloads the required NLTK resources when the relevant modules are executed:

stopwords
wordnet
vader_lexicon

Running the Project

From the project root:

python src/run_phase2.py


The pipeline will process the feedback dataset and display:

1. Feedback with sentiment and cluster assignments
2. Structured cluster insights
3. LLM-generated business insights


LLM Requirement

The project uses Ollama to run the Mistral model locally.

Make sure Ollama is installed and the Mistral model is available before running the complete pipeline.


ollama pull mistral

Then run:

python src/run_phase2.py

Example Dataset

The project currently uses sample customer feedback such as:


Delivery was late again
App crashes frequently
Please add dark mode
Customer support was very helpful
Checkout process is confusing
Love the new UI update
Notifications are delayed
Add UPI payment option


Future Improvements

Planned extensions include:

- Retrieval-Augmented Generation (RAG)
- Vector database integration
- Semantic search
- Interactive feedback dashboard
- Automated evaluation of AI-generated insights
- API integration using FastAPI
- Cloud deployment and MLOps pipeline

Author

Atharva Billore

GitHub: [AtharvaBilloreIndore]