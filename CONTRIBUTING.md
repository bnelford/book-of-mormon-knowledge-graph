# Contributing to Book of Mormon Knowledge Graph

Thank you for your interest in contributing to the Book of Mormon Knowledge Graph! This project aims to create a comprehensive, interactive visualization of the interconnected people, places, groups, and events from the Book of Mormon.

## 🤖 AI-Assisted Contributions

This project is designed to be enhanced using AI tools like ChatGPT, Claude, or GitHub Copilot. We encourage contributors to leverage AI to help identify entities, relationships, and scriptural references.

### Quick AI Contribution Workflow

1. **Fork and Clone**
   ```bash
   git clone https://github.com/your-username/book-of-mormon-knowledge-graph.git
   cd book-of-mormon-knowledge-graph
   ```

2. **Set Up Local Environment**
   ```bash
   python3 server.py  # Start local server
   # Open http://localhost:8000/knowledge-graph.html
   ```

3. **Use AI to Generate Data**
   - Use the prompt templates in the README
   - Ask AI to identify entities and relationships
   - Request JSON-formatted output
   - Verify AI suggestions against scripture

4. **Test and Submit**
   - Validate your JSON additions
   - Test the visualization locally
   - Submit a pull request

## 📋 Contribution Types

### High-Priority Contributions

- **Missing Key Figures**: Add important people not yet included
- **Geographical Expansion**: Add more places and locations
- **Event Documentation**: Add significant events with dates
- **Relationship Discovery**: Find new connections between entities
- **Reference Verification**: Ensure accuracy of existing data

### Technical Contributions

- **UI/UX Improvements**: Enhance the visualization interface
- **Performance Optimization**: Improve loading and interaction speed
- **New Features**: Add filtering, search, or analysis capabilities
- **Documentation**: Improve guides and instructions

## 🎯 Getting Started

### 1. Choose Your Focus Area

Pick a specific book or theme to work on:
- **1 Nephi**: Lehi's family journey
- **Alma**: Missionary work and wars
- **3 Nephi**: Christ's visit to the Americas
- **Ether**: Jaredite history
- **Geographic**: Focus on places and locations
- **Genealogical**: Family relationships and lineages

### 2. Use AI Effectively

**Example AI Prompt:**
```
I'm expanding a Book of Mormon knowledge graph. I want to add entities from Alma chapters 17-26 (the sons of Mosiah's mission to the Lamanites).

Current entities include: Ammon, Aaron, Omner, Himni, Lamoni, Abish

Please help me identify:
1. Key people mentioned in these chapters
2. Important places and locations
3. Significant events
4. Relationships between these entities

Format as JSON with nodes and edges arrays, including scriptural references for each.
```

### 3. Follow Data Standards

**Node Format:**
```json
{
  "id": "unique_identifier",
  "label": "Display Name",
  "type": "person|group|place|event",
  "references": ["Book Chapter:Verse"],
  "date": "B.C. 600" // Optional for events
}
```

**Edge Format:**
```json
{
  "from": "source_node_id",
  "to": "target_node_id",
  "label": "relationship_type",
  "references": ["Book Chapter:Verse"]
}
```

## 🔍 Quality Guidelines

### Scriptural Accuracy
- All references must be accurate
- Relationships must be supported by the text
- Use the Church website for verification: https://www.churchofjesuschrist.org/study/scriptures/bofm

### Data Consistency
- Use consistent naming conventions
- Follow existing ID patterns
- Maintain proper JSON formatting
- Include comprehensive references

### Testing Requirements
- Test all changes locally
- Verify JSON validity
- Check visualization rendering
- Ensure no broken references

## 📝 Pull Request Process

### Before Submitting
1. **Fork** the repository
2. **Create** a feature branch
3. **Make** your changes
4. **Test** thoroughly
5. **Validate** JSON structure

### Pull Request Template
```markdown
## Description
Brief description of what you're adding

## Changes Made
- Added X new entities
- Added Y new relationships
- Updated Z references

## AI Tools Used
- ChatGPT/Claude for entity identification
- GitHub Copilot for JSON formatting
- [Other tools]

## Testing
- [ ] Tested locally with Python server
- [ ] Validated JSON structure
- [ ] Verified scriptural references
- [ ] Checked visualization rendering

## References
List key scriptural references used:
- Book Chapter:Verse - Description
- Book Chapter:Verse - Description
```

## 🛠️ Development Setup

### Prerequisites
- Python 3.x or Node.js
- Git
- Text editor (VS Code recommended)
- AI tool access (ChatGPT, Claude, etc.)

### Local Development
```bash
# Clone your fork
git clone https://github.com/your-username/book-of-mormon-knowledge-graph.git
cd book-of-mormon-knowledge-graph/grok-version

# Start development server
python3 server.py
# OR
node server.js

# Open browser to http://localhost:8000/knowledge-graph.html
```

### File Structure
```
book-of-mormon-knowledge-graph/
├── knowledge-graph.html          # Main application
├── knowledge-graph.json          # Data file (edit this)
├── server.py                     # Python server
├── server.js                     # Node.js server
├── validate.py                   # Validation script
├── contribution-template.json    # Template for contributions
├── CONTRIBUTING.md               # This file
├── README.md                     # Main documentation
└── .github/                      # GitHub templates
    ├── ISSUE_TEMPLATE/
    └── pull_request_template.md
```

## 🎉 Recognition

Contributors will be recognized in:
- Project README
- Release notes
- GitHub contributors list
- Special acknowledgments

## 📞 Getting Help

- **Issues**: Create a GitHub issue for questions
- **Discussions**: Use GitHub Discussions for ideas
- **Documentation**: Check the detailed README in grok-version/
- **Community**: Join project discussions

## 📜 Code of Conduct

- Be respectful and inclusive
- Focus on scriptural accuracy
- Help others learn and contribute
- Maintain the project's educational purpose

---

**Ready to contribute? Start by exploring the existing data and choosing a focus area. Every addition helps build a more comprehensive understanding of the Book of Mormon!** 📖✨
