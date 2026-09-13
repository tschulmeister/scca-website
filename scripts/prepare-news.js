import fs from 'fs';
import path from 'path';
import { fileURLToPath } from 'url';

// Get current directory in ES modules
const __filename = fileURLToPath(import.meta.url);
const __dirname = path.dirname(__filename);

// Paths
const jsonPath = path.resolve(__dirname, '../src/data/newsItems.json');
const newsBaseDir = path.resolve(__dirname, '../src/components/news');

try {
  // Read existing index file
  const fileContent = fs.readFileSync(jsonPath, 'utf8');
  const newsItems = JSON.parse(fileContent);

  // Dynamic Date Formatting
  const today = new Date();
  const months = [
    "January", "February", "March", "April", "May", "June",
    "July", "August", "September", "October", "November", "December"
  ];
  
  const numericYear = today.getFullYear().toString();
  const numericMonth = (today.getMonth() + 1).toString().padStart(2, '0');
  const numericDay = today.getDate().toString().padStart(2, '0');
  
  const textDay = today.getDate();
  const textMonth = months[today.getMonth()];
  const textYear = today.getFullYear();
  const dateStr = `${textDay} ${textMonth} ${textYear}`;

  // Unique Identifier
  const tempId = `new-item-${Date.now()}`;

  // Folder & File Resolution
  const relativePath = `${numericYear}/${numericMonth}/${numericDay}/${tempId}.htm`;
  const fullHtmDir = path.join(newsBaseDir, numericYear, numericMonth, numericDay);
  const fullHtmPath = path.join(fullHtmDir, `${tempId}.htm`);

  // Ensure directories exist
  fs.mkdirSync(fullHtmDir, { recursive: true });

  // Write default empty template to htm file
  const defaultTemplate = `<p>Write your content here...</p>\n`;
  fs.writeFileSync(fullHtmPath, defaultTemplate, 'utf8');

  // Construct index metadata (no 'content' key, uses 'contentPath')
  const newItem = {
    id: tempId,
    title: "New News Item Title",
    date: dateStr,
    tags: [],
    contentPath: relativePath
  };

  // Prepend to array
  newsItems.unshift(newItem);

  // Write back to newsItems.json
  fs.writeFileSync(jsonPath, JSON.stringify(newsItems, null, 2) + '\n', 'utf8');

  console.log(`\n=============================================================`);
  console.log(`Successfully prepared new news item!`);
  console.log(`=============================================================`);
  console.log(`1. Registered in index: 'src/data/newsItems.json'`);
  console.log(`2. Created HTM template: 'src/components/news/${relativePath}'`);
  console.log(`=============================================================\n`);
} catch (error) {
  console.error("Error preparing new news item:", error);
  process.exit(1);
}
