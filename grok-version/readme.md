# Book of Mormon Knowledge Graph

An interactive visualization of the interconnected people, places, groups, and events from the Book of Mormon. This knowledge graph allows you to explore the complex relationships and connections between different entities mentioned in the sacred text.

## 🚀 Getting Started

### Option 1: Using Python (Recommended)
If you have Python installed:
```bash
cd grok-version
python3 server.py
```

### Option 2: Using Node.js
If you have Node.js installed:
```bash
cd grok-version
node server.js
```

### Option 3: Using a Simple HTTP Server
If you have Python 2:
```bash
cd grok-version
python -m SimpleHTTPServer 8000
```

### Option 4: Using PHP
If you have PHP installed:
```bash
cd grok-version
php -S localhost:8000
```

After starting the server, open your browser and navigate to:
**http://localhost:8000/knowledge-graph.html**

> **Important**: You cannot simply open the HTML file directly in your browser due to CORS restrictions. You must use a local server to serve the files.

## 🎯 How to Use the Knowledge Graph

### Navigation
- **Pan**: Click and drag anywhere on the graph to move around
- **Zoom**: Use your mouse wheel or trackpad to zoom in and out
- **Reset View**: Double-click on empty space to reset the view

### Exploring Nodes
- **Hover**: Hover over any node to see detailed information in the sidebar
- **Click**: Click on a node to highlight it and see its connections
- **Node Types**: Different colored nodes represent different entity types:
  - 🔴 **Red**: People (individuals like Nephi, Lehi, etc.)
  - 🟢 **Green**: Groups (families, tribes, nations)
  - 🔵 **Blue**: Places (cities, lands, geographical locations)
  - 🟡 **Yellow**: Events (significant occurrences and happenings)

### Understanding Connections
- **Edges**: Lines connecting nodes show relationships between entities
- **Hover on Edges**: Hover over connection lines to see relationship details
- **Relationship Types**: Common relationships include:
  - `parent_of` - Family relationships
  - `member_of` - Group membership
  - `involved_in` - Participation in events
  - `occurred_at` - Location of events
  - `founded` - Creation of groups or places

### Search Functionality
1. **Search Bar**: Use the search box in the top-right sidebar
2. **Real-time Results**: Results appear as you type
3. **Click to Navigate**: Click on any search result to:
   - Highlight the node on the graph
   - Display detailed information in the sidebar
   - Center the view on that node

### Details Panel
The details panel shows comprehensive information about selected entities:
- **Entity Name**: The primary label
- **Type**: Person, Group, Place, or Event
- **ID**: Unique identifier in the knowledge graph
- **References**: Scriptural references where this entity is mentioned

## 🔍 Search Tips

### Effective Searching
- **Partial Matches**: You don't need to type the full name
- **Case Insensitive**: Search works regardless of capitalization
- **Examples**:
  - Type "nep" to find "Nephi"
  - Type "jared" to find "Jared" and "Jaredites"
  - Type "event" to find all events
  - Type "babel" to find "Tower of Babel"

### Common Searches
- **People**: Try searching for "Lehi", "Nephi", "Alma", "Mosiah"
- **Places**: Search for "Jerusalem", "Zarahemla", "Bountiful"
- **Groups**: Look for "Nephites", "Lamanites", "Jaredites"
- **Events**: Find "Tower of Babel", "Tree of Life", "Christ appears"

## 📊 Data Structure

The knowledge graph contains:
- **97 Nodes**: Individual entities from the Book of Mormon
- **107 Edges**: Relationships between entities
- **4 Entity Types**: People, Groups, Places, Events
- **Scriptural References**: Each entity includes specific verse references

### Entity Categories
- **People**: 47 individuals mentioned in the text
- **Groups**: 12 families, tribes, and nations
- **Places**: 12 geographical locations
- **Events**: 17 significant occurrences

## 🎨 Visual Features

### Modern Design
- **Responsive Layout**: Works on desktop, tablet, and mobile
- **Glassmorphism Effects**: Modern translucent design elements
- **Smooth Animations**: Fluid transitions and hover effects
- **Color-coded Legend**: Easy identification of entity types

### Interactive Elements
- **Hover Effects**: Smooth highlighting of nodes and edges
- **Search Results**: Animated search result list
- **Details Panel**: Clean, organized information display
- **Legend**: Always-visible reference for node types

## 🛠️ Technical Details

### Built With
- **HTML5**: Modern semantic markup
- **CSS3**: Advanced styling with flexbox and grid
- **JavaScript**: Vanilla JS for interactivity
- **Vis.js**: Network visualization library
- **Inter Font**: Modern typography

### Browser Compatibility
- Chrome 60+
- Firefox 55+
- Safari 12+
- Edge 79+

### File Structure
```
grok-version/
├── knowledge-graph.html    # Main application file
├── knowledge-graph.json    # Data file with nodes and edges
├── server.py              # Python server script
├── server.js              # Node.js server script
└── readme.md              # This documentation
```

## 🔧 Troubleshooting

### Common Issues

**404 Error when loading the page**
- Make sure you're using a local server (not opening the file directly)
- Check that the server is running on the correct port
- Verify that `knowledge-graph.json` exists in the same directory

**Graph not displaying**
- Check browser console for JavaScript errors
- Ensure you have a stable internet connection (for loading the Vis.js library)
- Try refreshing the page

**Search not working**
- Make sure the JSON data loaded successfully
- Check that the search input field is focused
- Try typing at least 2-3 characters

### Performance Tips
- **Large Graphs**: If the graph becomes slow, try zooming out to see fewer nodes
- **Mobile Devices**: Use landscape orientation for better viewing
- **Slow Connections**: The initial load may take a moment to fetch the visualization library

## 📚 About the Data

This knowledge graph is based on the Book of Mormon text and includes:
- Major characters and their relationships
- Significant geographical locations
- Important events and their participants
- Family trees and genealogical connections
- Group memberships and affiliations

The data is structured to show both direct relationships (like parent-child) and contextual relationships (like participation in events).

## 🤝 Contributing

To add more entities or relationships:
1. Edit the `knowledge-graph.json` file
2. Add new nodes to the "nodes" array
3. Add new relationships to the "edges" array
4. Restart your local server
5. Refresh the browser

### Data Format
```json
{
  "nodes": [
    {
      "id": "unique_id",
      "label": "Display Name",
      "type": "person|group|place|event",
      "references": ["Scripture 1:1", "Scripture 2:2"]
    }
  ],
  "edges": [
    {
      "from": "source_node_id",
      "to": "target_node_id",
      "label": "relationship_type"
    }
  ]
}
```

---

**Enjoy exploring the rich interconnected world of the Book of Mormon!** 📖✨
