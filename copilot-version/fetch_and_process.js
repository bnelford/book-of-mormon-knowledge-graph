const https = require('https');
const fs = require('fs');
const path = require('path');

const DATA_URL = 'https://raw.githubusercontent.com/bcbooks/scriptures-json/master/book-of-mormon.json'; // Corrected URL
const OUTPUT_FILE = path.join(__dirname, 'data.json');

// Fetch JSON data from the URL
function fetchData(url) {
  return new Promise((resolve, reject) => {
    https.get(url, (res) => {
      let data = '';

      res.on('data', (chunk) => {
        data += chunk;
      });

      res.on('end', () => {
        resolve(JSON.parse(data));
      });

      res.on('error', (err) => {
        reject(err);
      });
    });
  });
}

// Process the data to extract entities and relationships
function processScriptures(scriptures) {
  const entities = [];
  const relationships = [];

  // Add predefined people and places
  const people = [
    { id: 'person-1', name: 'Nephi', description: 'A prophet and the son of Lehi.' },
    { id: 'person-2', name: 'Lehi', description: 'A prophet who led his family from Jerusalem to the Americas.' }
  ];

  const places = [
    { id: 'place-1', name: 'Jerusalem', description: 'The city where Lehi and his family lived before their journey.' },
    { id: 'place-2', name: 'Bountiful', description: 'A place where Nephi built a ship.' }
  ];

  entities.push(...people, ...places);

  // Link people and places to books or chapters
  relationships.push(
    { source: 'person-1', target: 'book-1', type: 'MentionedIn', description: 'Nephi is mentioned in the first book.' },
    { source: 'person-2', target: 'place-1', type: 'LivedIn', description: 'Lehi lived in Jerusalem.' }
  );

  // Process books, chapters, and verses
  if (typeof scriptures === 'object' && scriptures.books) {
    scriptures.books.forEach((book, bookIndex) => {
      const bookId = `book-${bookIndex + 1}`;
      entities.push({
        id: bookId,
        name: book.book,
        type: 'Book',
        description: `Book of ${book.book}`
      });

      book.chapters.forEach((chapter, chapterIndex) => {
        const chapterId = `${bookId}-chapter-${chapterIndex + 1}`;
        entities.push({
          id: chapterId,
          name: `Chapter ${chapterIndex + 1}`,
          type: 'Chapter',
          description: `Chapter ${chapterIndex + 1} of ${book.book}`
        });

        relationships.push({
          source: bookId,
          target: chapterId,
          type: 'Contains',
          description: `${book.book} contains Chapter ${chapterIndex + 1}`
        });

        chapter.verses.forEach((verse, verseIndex) => {
          const verseId = `${chapterId}-verse-${verseIndex + 1}`;
          entities.push({
            id: verseId,
            name: `Verse ${verseIndex + 1}`,
            type: 'Verse',
            description: verse.text
          });

          relationships.push({
            source: chapterId,
            target: verseId,
            type: 'Contains',
            description: `Chapter ${chapterIndex + 1} contains Verse ${verseIndex + 1}`
          });
        });
      });
    });
  } else {
    throw new Error('Unexpected data structure: scriptures does not contain books.');
  }

  return { entities, relationships };
}

// Save the processed data to a file
function saveData(data, filePath) {
  fs.writeFileSync(filePath, JSON.stringify(data, null, 2), 'utf8');
}

// Main function
(async function main() {
  try {
    console.log('Fetching data...');
    const scriptures = await fetchData(DATA_URL);

    console.log('Fetched data structure:', JSON.stringify(scriptures, null, 2)); // Log the data structure

    console.log('Processing data...');
    const processedData = processScriptures(scriptures);

    console.log('Saving data...');
    saveData(processedData, OUTPUT_FILE);

    console.log('Data successfully fetched and saved to data.json');
  } catch (error) {
    console.error('Error:', error);
  }
})();