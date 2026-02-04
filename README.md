# NLP Analysis of Stand-Up Comedy Transcripts  
### Style, Topics, and the Limits of Language Models on Humor

---

##  Project Overview

This project explores the application of Natural Language Processing (NLP) techniques to **stand-up comedy transcripts**. Comedy is a challenging domain for NLP due to sarcasm, exaggeration, informal language, profanity, and inconsistent annotations across transcripts.

The goal of this project is **not to “solve” humor**, but to:
- analyze linguistic style,
- uncover recurring themes,
- and critically evaluate the limitations of common NLP methods when applied to comedic text.

The project emphasizes **honest analysis, reproducibility, and interpretability** over aggressive optimization.

---

##  Objectives

- Analyze **linguistic and stylistic patterns** in stand-up comedy
- Compare comedians using **robust language features**
- Identify recurring themes using **topic modeling**
- Demonstrate why **traditional sentiment analysis fails** on humor
- Explore **text generation** to highlight the gap between surface-level language modeling and actual humor
- Build a complete **end-to-end NLP pipeline** from data ingestion to interpretation

---

##  Dataset Description

The dataset consists of stand-up comedy transcripts collected from publicly available sources.

Key characteristics:
- Long-form spoken language
- Informal grammar and repetition
- Profanity and exaggerated expressions
- Inconsistent use of stage directions (e.g., laughter, applause)
- Mixed transcript conventions depending on source and transcriber

Rather than enforcing strict normalization, this project treats **annotation inconsistency as an inherent property of real-world language data**.

---

##  Methodology

### 1. Data Collection
- Programmatic discovery of transcript URLs
- Web scraping using HTML parsing
- Raw transcripts stored immutably to preserve provenance

### 2. Preprocessing
- Normalized whitespace and formatting
- Preserved paralinguistic signals (e.g., laughter) when present
- Created multiple text representations for different analysis tasks
- Avoided aggressive cleaning to prevent information loss

### 3. Exploratory Data Analysis (EDA)
- Analyzed transcript length and vocabulary distribution
- Identified strong heterogeneity in document structure
- Observed high repetition and limited lexical range typical of spoken comedy

### 4. Comedian Style Analysis
- Extracted robust linguistic features such as:
  - average sentence length
  - lexical diversity
  - profanity usage
  - question frequency
- Compared stylistic patterns across transcripts
- Focused on **how comedians speak**, not whether jokes are successful

### 5. Topic Modeling
- Applied TF-IDF vectorization and Non-Negative Matrix Factorization (NMF)
- Identified recurring themes.
- Interpreted topics cautiously as statistical patterns rather than semantic truths

### 6. Sentiment Analysis (Failure Study)
- Applied VADER sentiment analysis
- Demonstrated how sarcasm, profanity, and exaggeration break lexicon-based models

### 7. Text Generation
- Built a simple n-gram language model
- Generated text that mimics surface-level comedic style
- Highlighted the inability of statistical models to capture timing, surprise, and humor

---

##  Key Findings & Limitations

- Linguistic style can be measured reliably even in noisy transcripts
- Topic modeling reveals broad thematic structure but not comedic intent
- Sentiment analysis performs poorly on humorous text
- Text generation captures form but not function — humor remains elusive

These limitations are **not flaws**, but insights into the challenges of applying NLP to creative and non-literal language.

---

##  What This Project Demonstrates

- End-to-end NLP pipeline design
- Real-world data handling and ambiguity
- Critical evaluation of model assumptions
- Honest interpretation of results
- Strong engineering and documentation practices

---

##  Possible Extensions

- Speaker-aware or comedian-specific modeling
- Neural text generation using transformer models
- Supervised humor or sarcasm detection
- Clustering comedians by linguistic style
- Temporal analysis across years or specials

---

##  Final Note

This project prioritizes **understanding over optimization**.  
Rather than forcing clean labels or overfitting models, it embraces the complexity of real-world language and treats model failure as a source of insight.
