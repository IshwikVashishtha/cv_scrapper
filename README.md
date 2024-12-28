# CV Scrapper

A Python-based tool for extracting and processing information from PDF resumes/CVs.

## Overview

CV Scrapper is designed to automatically extract relevant information from PDF resumes and CVs, making it easier to process and analyze candidate information. The tool uses various NLP techniques and pattern matching to identify and categorize different sections of a CV.

## Features

- PDF text extraction
- Section identification (Education, Experience, Skills, etc.)
- Contact information extraction
- Skills identification and categorization
- Work experience parsing
- Education history extraction
- Multi-language support

## Prerequisites

Before running the CV Scrapper, ensure you have the following installed:
bash
Python 3.7+
pip

## Installation

1. Clone the repository: https://github.com/IshwikVashishtha/cv_scrapper.git

2. Install required dependencies:
   pip install -r requirements.txt

### Required NLTK Data
Uncomment and run these lines in `app.py` the first time:


nltk.download('averaged_perceptron_tagger_eng')
nltk.download('maxent_ne_chunker_tab')
nltk.download('words')
nltk.download('punkt')


### Required spaCy Model
Install the English language model: 
python -m spacy download en_core_web_sm


## Project Structure

cv_scrapper/
│
├── input/ # Place individual PDF files here
├── pdf/ # Contains merged PDF output
├── doc/ # Place Word documents here
├── output/ # Excel output directory
│
├── app.py # Main application file
├── merger.py # PDF merger utility
├── requirements.txt # Project dependencies
└── README.md # This file


## Usage

### 1. Preparing Your Documents

#### For PDF Files:
1. Place individual PDF files in the `input/` directory
2. Run the merger utility to combine them:
python merger.py

This will create a merged PDF in `pdf/merged_output.pdf`

#### For Word Documents:
- Place .doc or .docx files directly in the `doc/` directory
- Default filename: `input.docx`

### 2. Running the Extractor
python app.py


The script will:
1. Process all documents in the specified directories
2. Extract contact information
3. Generate an Excel file in the `output/` directory

### 3. Output Format

The generated Excel file contains:
- Name
- Name_Found_On_Page
- Email
- Email_Found_On_Page
- Phone
- Phone_Found_On_Page

## Configuration

### Supported Name Formats
The tool recognizes various name formats including:
- Standard formats (e.g., "John Smith")
- Names with titles (Mr., Mrs., Dr., etc.)
- Complex names with prefixes (van, de, von, etc.)
- Hyphenated names
- Names with apostrophes

### Invalid Name Filtering
The tool filters out invalid names containing:
- Common resume keywords
- Numbers
- Special characters
- Improper capitalization

## Error Handling

The tool includes comprehensive error handling:
- File access errors
- PDF/Word processing errors
- Text extraction issues
- Data processing errors

All errors are logged with detailed information for troubleshooting.

## Limitations

- PDF text extraction quality depends on the PDF format (scanned documents may not work well)
- Name extraction accuracy depends on standard formatting
- Phone numbers must be in common formats
- Email addresses must follow standard patterns

## Troubleshooting

### Common Issues

1. **PDF Extraction Fails**
   - Ensure PDF is not password protected
   - Check if PDF is properly formatted (not scanned)
   - Verify file permissions

2. **Name Not Detected**
   - Check if name follows standard formatting
   - Verify text extraction is working (check logs)
   - Ensure name appears in first few pages

3. **Output Directory Issues**
   - Verify write permissions
   - Ensure Excel file is not open
   - Check disk space

## Contributing

1. Fork the repository
2. Create your feature branch
3. Commit your changes
4. Push to the branch
5. Create a new Pull Request

## Acknowledgments

- Uses spaCy for NLP processing
- Uses NLTK for name entity recognition
- Uses pdfplumber for PDF text extraction
- Uses python-docx for Word document processing

---

For additional support or questions, please open an issue in the repository.
