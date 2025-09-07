<!--
*** Thanks for checking out the Book of Mormon Knowledge Graph project!
*** This project aims to create a comprehensive, interactive visualization
*** of the interconnected people, places, groups, and events from the Book of Mormon.
-->

<!-- PROJECT SHIELDS -->
[![Contributors][contributors-shield]][contributors-url]
[![Activity][activity-shield]][activity-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]
[![MIT License][license-shield]][license-url]
[![LinkedIn][linkedin-shield]][linkedin-url]

<!-- PROJECT LOGO -->
<br />
<p align="center">
  <a href="https://github.com/bnelford/book-of-mormon-knowledge-graph">
    <img src="favicon.ico" alt="Logo" width="80" height="80">
  </a>

  <h3 align="center">Book of Mormon Knowledge Graph</h3>

  <p align="center">
    An interactive visualization of the interconnected people, places, groups, and events from the Book of Mormon. Explore the complex relationships and connections between different entities mentioned in the sacred text.
    <br />
    <a href="https://github.com/bnelford/book-of-mormon-knowledge-graph"><strong>Explore the docs »</strong></a>
    <br />
    <br />
    <a href="https://github.com/bnelford/book-of-mormon-knowledge-graph">View Demo</a>
    ·
    <a href="https://github.com/bnelford/book-of-mormon-knowledge-graph/issues">Report Bug</a>
    ·
    <a href="https://github.com/bnelford/book-of-mormon-knowledge-graph/issues">Request Feature</a>
  </p>
</p>

<!-- TABLE OF CONTENTS -->
<details open="open">
  <summary><h2 style="display: inline-block">Table of Contents</h2></summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
        <li><a href="#features">Features</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#data-structure">Data Structure</a></li>
    <li><a href="#contributing">Contributing</a></li>
    <li><a href="#license">License</a></li>
    <li><a href="#contact">Contact</a></li>
    <li><a href="#acknowledgements">Acknowledgements</a></li>
  </ol>
</details>

<!-- ABOUT THE PROJECT -->
## About The Project

The Book of Mormon Knowledge Graph is an interactive web application that visualizes the complex relationships between people, places, groups, and events mentioned in the Book of Mormon. This project combines modern web technologies with scriptural scholarship to create an engaging exploration tool.

### Key Features

- **Interactive Network Visualization**: Explore entities and their relationships through an intuitive graph interface
- **Advanced Filtering**: Filter relationships by type (family, social, spiritual, geographical)
- **Color-Coded Relationships**: Visual distinction between different types of connections
- **Scriptural References**: Direct links to the Church website for every reference
- **Search Functionality**: Real-time search across all entities
- **Responsive Design**: Works on desktop, tablet, and mobile devices
- **AI-Assisted Contributions**: Tools and templates for easy expansion using AI

### Built With

* [HTML5](https://developer.mozilla.org/en-US/docs/Web/HTML) - Modern semantic markup
* [CSS3](https://developer.mozilla.org/en-US/docs/Web/CSS) - Advanced styling with flexbox and grid
* [JavaScript](https://developer.mozilla.org/en-US/docs/Web/JavaScript) - Vanilla JS for interactivity
* [Vis.js](https://visjs.org/) - Network visualization library
* [Inter Font](https://rsms.me/inter/) - Modern typography
* [Python](https://python.org/) - Local development server
* [Node.js](https://nodejs.org/) - Alternative development server

<!-- GETTING STARTED -->
## Getting Started

To get a local copy up and running, follow these simple steps:

### Prerequisites

You need one of the following to run the local server:
* Python 3.x (recommended)
* Node.js
* PHP
* Any other local HTTP server

### Installation

1. Clone the repository
   ```bash
   git clone https://github.com/bnelford/book-of-mormon-knowledge-graph.git
   cd book-of-mormon-knowledge-graph
   ```

2. Start a local server (choose one option):

   **Option 1: Python (Recommended)**
   ```bash
   python3 server.py
   ```

   **Option 2: Node.js**
   ```bash
   node server.js
   ```

   **Option 3: PHP**
   ```bash
   php -S localhost:8000
   ```

   **Option 4: Python 2**
   ```bash
   python -m SimpleHTTPServer 8000
   ```

3. Open your browser and navigate to:
   ```
   http://localhost:8000/knowledge-graph.html
   ```

> **Important**: You cannot simply open the HTML file directly in your browser due to CORS restrictions. You must use a local server to serve the files.

<!-- USAGE -->
## Usage

### Navigation
- **Pan**: Click and drag anywhere on the graph to move around
- **Zoom**: Use your mouse wheel or trackpad to zoom in and out
- **Reset View**: Double-click on empty space to reset the view

### Exploring Nodes
- **Hover**: Hover over any node to see detailed information in the sidebar
- **Click**: Click on a node to select it and see its connections
- **Node Types**: Different colored nodes represent different entity types:
  - 🔴 **Red**: People (individuals like Nephi, Lehi, etc.)
  - 🟢 **Green**: Groups (families, tribes, nations)
  - 🔵 **Blue**: Places (cities, lands, geographical locations)
  - 🟡 **Yellow**: Events (significant occurrences and happenings)

### Understanding Connections
- **Edges**: Lines connecting nodes show relationships between entities
- **Hover on Edges**: Hover over connection lines to see relationship details with clickable references
- **Color-Coded Relationships**: Different relationship types have distinct colors:
  - 🔴 **Red**: "opposed_by" - Conflict and opposition relationships
  - 🔵 **Blue**: "prophesied_by" - Prophetic relationships
  - 🟢 **Green**: "taught_by" - Teaching and mentorship relationships
  - 🟣 **Purple**: "allied_with" - Alliance and partnership relationships
  - And many more...

### Search and Filter
1. **Search Bar**: Use the search box in the sidebar to find entities
2. **Relationship Filter**: Use the dropdown to filter by relationship type
3. **Click References**: All scriptural references are clickable links to the Church website

### Search Tips
- **Partial Matches**: You don't need to type the full name
- **Case Insensitive**: Search works regardless of capitalization
- **Examples**:
  - Type "nep" to find "Nephi"
  - Type "jared" to find "Jared" and "Jaredites"
  - Type "event" to find all events
  - Type "babel" to find "Tower of Babel"

<!-- DATA STRUCTURE -->
## Data Structure

The knowledge graph contains:
- **100+ Nodes**: Individual entities from the Book of Mormon
- **120+ Edges**: Relationships between entities
- **4 Entity Types**: People, Groups, Places, Events
- **Scriptural References**: Each entity includes specific verse references

### Entity Categories
- **People**: Individuals mentioned in the text
- **Groups**: Families, tribes, and nations
- **Places**: Geographical locations
- **Events**: Significant occurrences

### Relationship Types
- **Family**: `parent_of`, `sibling_of`, `ancestor_of`
- **Social**: `allied_with`, `opposed_by`, `taught_by`
- **Spiritual**: `prophesied_by`, `converted`
- **Geographical**: `occurred_at`, `resided_in`
- **Group**: `member_of`, `founded`
- **Event**: `involved_in`

### File Structure
```
book-of-mormon-knowledge-graph/
├── knowledge-graph.html          # Main application file
├── knowledge-graph.json          # Data file with nodes and edges
├── server.py                     # Python server script
├── server.js                     # Node.js server script
├── validate.py                   # Validation script for contributors
├── contribution-template.json    # Template for new contributions
├── CONTRIBUTING.md               # Detailed contribution guidelines
├── .github/                      # GitHub templates and workflows
│   ├── ISSUE_TEMPLATE/
│   └── pull_request_template.md
└── README.md                     # This documentation
```

### Contributor Tools

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

<!-- CONTRIBUTING -->
## Contributing

We welcome contributions to expand and improve the Book of Mormon Knowledge Graph! This project is designed to be enhanced using AI tools like ChatGPT, Claude, or GitHub Copilot.

### Quick Start for Contributors

1. **Fork the Repository**
   ```bash
   git clone https://github.com/your-username/book-of-mormon-knowledge-graph.git
   cd book-of-mormon-knowledge-graph
   ```

2. **Set Up Local Development**
   ```bash
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

### Using AI to Enhance the Graph

AI tools can be incredibly helpful for expanding the knowledge graph. Here are some prompt templates:

**Adding New Entities**
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

**Finding Relationships**
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

### Quality Assurance

Before submitting your contribution:

1. **Test Locally**
   ```bash
   python3 server.py
   # Open http://localhost:8000/knowledge-graph.html
   # Verify your changes display correctly
   ```

2. **Validate JSON**
   ```bash
   python3 validate.py
   ```

3. **Check References**
   - Verify all scriptural references are accurate
   - Use the Church website to verify: https://www.churchofjesuschrist.org/study/scriptures/bofm

For detailed contribution guidelines, see [CONTRIBUTING.md](CONTRIBUTING.md).

<!-- LICENSE -->
## License

Distributed under the MIT License. See `LICENSE` for more information.

<!-- CONTACT -->
## Contact

Beau Nelford - [@beaunelford](https://twitter.com/@beaunelford) - nelfordbc@gmail.com

Project Link: [https://github.com/bnelford/book-of-mormon-knowledge-graph](https://github.com/bnelford/book-of-mormon-knowledge-graph)

<!-- ACKNOWLEDGEMENTS -->
## Acknowledgements

* [The Church of Jesus Christ of Latter-day Saints](https://www.churchofjesuschrist.org/?lang=eng) - For the sacred text and online resources
* [Vis.js](https://visjs.org/) - For the network visualization library
* [Inter Font](https://rsms.me/inter/) - For the beautiful typography
* [othneildrew](https://github.com/othneildrew) - For [The Best Readme Template](https://github.com/othneildrew/Best-README-Template)

<!-- MARKDOWN LINKS & IMAGES -->
[contributors-shield]: https://img.shields.io/github/contributors/bnelford/book-of-mormon-knowledge-graph?style=for-the-badge
[contributors-url]: https://github.com/bnelford/book-of-mormon-knowledge-graph/graphs/contributors
[activity-shield]: https://img.shields.io/github/commit-activity/y/bnelford/book-of-mormon-knowledge-graph?style=for-the-badge
[activity-url]: https://github.com/bnelford/book-of-mormon-knowledge-graph/graphs/commit-activity
[forks-shield]: https://img.shields.io/github/forks/bnelford/book-of-mormon-knowledge-graph?style=for-the-badge
[forks-url]: https://github.com/bnelford/book-of-mormon-knowledge-graph/network/members
[stars-shield]: https://img.shields.io/github/stars/bnelford/book-of-mormon-knowledge-graph?style=for-the-badge
[stars-url]: https://github.com/bnelford/book-of-mormon-knowledge-graph/stargazers
[issues-shield]: https://img.shields.io/github/issues/bnelford/book-of-mormon-knowledge-graph?style=for-the-badge
[issues-url]: https://github.com/bnelford/book-of-mormon-knowledge-graph/issues
[license-shield]: https://img.shields.io/github/license/bnelford/book-of-mormon-knowledge-graph?style=for-the-badge
[license-url]: https://github.com/bnelford/book-of-mormon-knowledge-graph/blob/main/LICENSE
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555
[linkedin-url]: https://www.linkedin.com/in/beaunelford/