# CIACR
Cross Referencing 13m pages of CIA declassified reports

## Background
  On January 17th 2017 the CIA declassified and released 13 million pages of documents to the public.
We aim to scrape and analyze these files.  We want to show the public information that may have been hidden. We will link articles useres read to relavant declassified CIA documents.

## Product
  We created a chrome extension that will provide links to pdf of declassified CIA documents to relevant articles as needed by the user.

## Usage
  After cloning, open chrome and enable developer mode for extensions.  Upload our extension from the /chrome_extension/inject-sidebar-master and run it.  Next in terminal, navigate to the /backend folder and run $node app.js
  Now you're good to go.  Go to any wikipedia page and click on our extension to see a list of up to 3 relevant newly declassified CIA documents.

## Development

### 1) Web Crawler
  The documents can be found at https://www.cia.gov/library/readingroom/collection/general-cia-records, CIACrawler.java scrapes relevant pages to compile a list of links to the document PDFs.  This is a total of over 760000 links to documents.  Can be run in java.
  
### 2) Word Extraction
  Because they had no actual word values and were mostly scans of old documents, the pdfs were functionally images.  As such, a script was created to convert each pdf into images.
  Tesseract was then used on each image for Optical Character Recognition (OCR) to generate text files of the pdf documents.
  
### 3) Data Cleaning
   We used python scripts to do a simple cleaning of the data (removing stopwords, running autocorrect on clearly misspelled words, removing other unnecessary words)
    
### 4) Feature Generation
  We used a python script using Rake to identify key phrases for each article.
  Another script then identified common key phrases across multiple documents and the most popular of these were selected as identifying features for the document.
    
### 5) Data Analysis
  Using the identified features a python script generated a .dat file representing a matrix of 1's and 0's where each row represents a CIA document and each column a specific feature (key phrase).  An element of this matrix has a 1 only if its corresponding article has the corresponding key phrase (feature).
  Using this data, we used matlab to cluster the data and identify trends between them.
### 6) REST API (Backend)
  A rest API with a post endpoint was made for the extention to post urls of articles and in return recieve a list of relevant CIA document pdf links.  Written using node.js / express.  It calls a python script to perform the same key phrase extraction on the inputed page and return the keywords.  These are then analyzed with a table of CIA document data that maps popular key features to their associated documents and then all relevant articles are served by the API.  
  To run in terminal navigate to the /backend folder and run "node app.js".
### 7) Chrome Extension
  Our product, a chrome extension will offer readers important information they may be missing in their articles - What the CIA has done behind the scenes related to them!  
