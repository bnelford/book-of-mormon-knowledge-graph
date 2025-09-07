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
├── validate.py            # Validation script for contributors
├── contribution-template.json # Template for new contributions
└── readme.md              # This documentation
```

### 🛠️ Contributor Tools

**Validation Script (`validate.py`)**
```bash
python3 validate.py
```
This script checks:
- JSON structure validity
- Required fields for nodes and edges
- Duplicate IDs
- Reference format validation
- Relationship type statistics
- Node type distribution

**Contribution Template (`contribution-template.json`)**
Use this file as a reference for:
- Proper JSON structure
- Example entities and relationships
- Available relationship types
- AI prompt templates

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

We welcome contributions to expand and improve the Book of Mormon Knowledge Graph! This section provides comprehensive guidance for contributors, including how to use AI tools to enhance the graph.

### 🚀 Quick Start for Contributors

1. **Fork the Repository**
   ```bash
   git clone https://github.com/your-username/book-of-mormon-knowledge-graph.git
   cd book-of-mormon-knowledge-graph
   ```

2. **Set Up Local Development**
   ```bash
   cd grok-version
   python3 server.py  # or node server.js
   ```

3. **Make Your Changes**
   - Edit `knowledge-graph.json` to add nodes and relationships
   - Test your changes locally
   - Ensure the graph loads without errors

4. **Submit a Pull Request**
   - Create a new branch for your changes
   - Commit your changes with descriptive messages
   - Submit a pull request with details about your additions

### 🤖 Using AI to Enhance the Graph

AI tools like ChatGPT, Claude, or GitHub Copilot can be incredibly helpful for expanding the knowledge graph. Here's how to use them effectively:

#### **Prompt Templates for AI Assistance**

**1. Adding New Entities**
```
I'm working on a Book of Mormon knowledge graph. I need to add [entity type] entities from [specific book/chapter]. 

Current entities include: [list a few examples from the JSON]

Please help me identify:
- Key [people/places/groups/events] from [book/chapter]
- Their scriptural references
- Their relationships to existing entities

Format the response as JSON following this structure:
{
  "nodes": [
    {
      "id": "unique_id",
      "label": "Display Name", 
      "type": "person|group|place|event",
      "references": ["Book Chapter:Verse"]
    }
  ],
  "edges": [
    {
      "from": "source_id",
      "to": "target_id", 
      "label": "relationship_type",
      "references": ["Book Chapter:Verse"]
    }
  ]
}
```

**2. Finding Relationships**
```
Analyze these Book of Mormon entities and identify relationships between them:

[Paste your entity list]

Focus on these relationship types:
- family relationships (parent_of, sibling_of, ancestor_of)
- social relationships (allied_with, opposed_by, taught_by)
- spiritual relationships (prophesied_by, converted)
- geographical relationships (occurred_at, resided_in)
- group relationships (member_of, founded)

For each relationship, provide the specific scriptural reference that supports it.
```

**3. Verifying References**
```
I have this relationship in my Book of Mormon knowledge graph:
[Paste the relationship]

Please verify:
1. Is this relationship accurate according to the text?
2. Are the scriptural references correct?
3. Are there additional references I should include?
4. Is the relationship type appropriate?

If there are issues, please suggest corrections.
```

**4. Expanding Existing Entities**
```
I have this entity in my knowledge graph:
[Paste entity]

Please help me:
1. Find additional scriptural references for this entity
2. Identify relationships I might have missed
3. Suggest related entities that should be included
4. Verify the accuracy of existing information
```

#### **AI Tools and Their Strengths**

**ChatGPT/Claude:**
- Excellent for analyzing text and identifying relationships
- Good at generating structured JSON data
- Can help verify scriptural accuracy
- Useful for brainstorming new entities

**GitHub Copilot:**
- Great for code completion and JSON formatting
- Helps with consistent data structure
- Good for repetitive tasks like adding multiple entities

**Specialized Bible/Book of Mormon AI:**
- More accurate with scriptural references
- Better understanding of theological relationships
- Can provide historical context

### 📊 Data Structure Guidelines

#### **Node Format**
```json
{
  "id": "unique_identifier",
  "label": "Display Name",
  "type": "person|group|place|event",
  "references": ["Book Chapter:Verse", "Book Chapter:Verse"],
  "date": "B.C. 600" // Optional, for events
}
```

#### **Edge Format**
```json
{
  "from": "source_node_id",
  "to": "target_node_id", 
  "label": "relationship_type",
  "references": ["Book Chapter:Verse", "Book Chapter:Verse"]
}
```

#### **Relationship Types**
- **Family**: `parent_of`, `sibling_of`, `ancestor_of`
- **Social**: `allied_with`, `opposed_by`, `taught_by`
- **Spiritual**: `prophesied_by`, `converted`
- **Geographical**: `occurred_at`, `resided_in`
- **Group**: `member_of`, `founded`
- **Event**: `involved_in`

### 🎯 Contribution Ideas

#### **High-Value Additions**
1. **Missing Key Figures**: Add important people not yet included
2. **Geographical Locations**: Expand place entities with coordinates
3. **Temporal Relationships**: Add more event entities with dates
4. **Spiritual Connections**: Focus on prophetic and teaching relationships
5. **Family Trees**: Complete genealogical connections

#### **Data Quality Improvements**
1. **Reference Verification**: Ensure all references are accurate
2. **Relationship Validation**: Verify relationship types are appropriate
3. **Consistency**: Maintain consistent naming and formatting
4. **Completeness**: Add missing references for existing entities

#### **Technical Enhancements**
1. **New Relationship Types**: Propose new relationship categories
2. **Enhanced Metadata**: Add dates, descriptions, or other attributes
3. **Visual Improvements**: Suggest UI/UX enhancements
4. **Performance**: Optimize data structure for better performance

### 🔍 Quality Assurance

Before submitting your contribution:

1. **Test Locally**
   ```bash
   cd grok-version
   python3 server.py
   # Open http://localhost:8000/knowledge-graph.html
   # Verify your changes display correctly
   ```

2. **Validate JSON**
   ```bash
   # Use the provided validation script
   python3 validate.py
   
   # Or use basic JSON validation
   python3 -m json.tool knowledge-graph.json > /dev/null
   # Should return no errors
   ```

3. **Check References**
   - Verify all scriptural references are accurate
   - Ensure references support the claimed relationships
   - Use the Church website to verify: https://www.churchofjesuschrist.org/study/scriptures/bofm

4. **Review Relationships**
   - Ensure relationship types are appropriate
   - Check that both nodes exist in the graph
   - Verify the relationship makes logical sense

### 📝 Pull Request Guidelines

When submitting a pull request:

1. **Clear Title**: Describe what you're adding (e.g., "Add Alma the Younger and his relationships")

2. **Detailed Description**: Include:
   - What entities/relationships you added
   - Why they're important
   - How you verified the information
   - Any AI tools you used

3. **Testing Notes**: Mention:
   - How you tested the changes
   - Any issues you encountered
   - Screenshots if relevant

4. **Reference Sources**: List the specific verses you used for verification

### 🛠️ Development Tips

#### **Using AI Effectively**
- **Be Specific**: Provide context about existing entities
- **Ask for Verification**: Always ask AI to verify its suggestions
- **Iterate**: Use AI to refine and improve your additions
- **Cross-Reference**: Verify AI suggestions against the actual text

#### **Common Pitfalls to Avoid**
- Don't add entities without scriptural references
- Don't create relationships that aren't supported by the text
- Don't use inconsistent naming conventions
- Don't add duplicate entities with different IDs

#### **Best Practices**
- Start with well-known, clearly referenced entities
- Focus on one book or section at a time
- Test frequently as you add data
- Keep relationships simple and clear
- Use the existing data as a template

### 🎉 Recognition

Contributors will be recognized in:
- The project README
- Release notes
- Special thanks in the application

### 📞 Getting Help

If you need assistance:
1. Check existing issues on GitHub
2. Create a new issue with your question
3. Join discussions in the project's community space
4. Reach out to maintainers directly

---

**Ready to contribute? Start by forking the repository and exploring the existing data structure. Every addition helps build a more comprehensive understanding of the Book of Mormon's interconnected world!** 📖✨
