import fs from 'fs';
import path from 'path';
import { fileURLToPath } from 'url';

// Get current directory in ES modules
const __filename = fileURLToPath(import.meta.url);
const __dirname = path.dirname(__filename);

// Path to newsItems.json
const filePath = path.resolve(__dirname, '../src/data/newsItems.json');

try {
  // Read existing file
  const fileContent = fs.readFileSync(filePath, 'utf8');
  const newsItems = JSON.parse(fileContent);

  // Format today's date (e.g., "13 September 2026")
  const today = new Date();
  const months = [
    "January", "February", "March", "April", "May", "June",
    "July", "August", "September", "October", "November", "December"
  ];
  const day = today.getDate();
  const month = months[today.getMonth()];
  const year = today.getFullYear();
  const dateStr = `${day} ${month} ${year}`;

  // Unique temporary id
  const tempId = `new-item-${Date.now()}`;

  const newItem = {
    id: tempId,
    title: "New News Item Title",
    date: dateStr,
    tags: [],
    content: "<p>Write your content here...</p>"
  };

  // Prepend to array
  newsItems.unshift(newItem);

  // Write back to file
  fs.writeFileSync(filePath, JSON.stringify(newsItems, null, 2) + '\n', 'utf8');

  console.log(`Successfully prepared new empty news item template in 'src/data/newsItems.json'.`);
  console.log(`Item ID: ${tempId}`);
} catch (error) {
  console.error("Error updating newsItems.json:", error);
  process.exit(1);
}
