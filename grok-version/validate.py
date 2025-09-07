#!/usr/bin/env python3
"""
Validation script for Book of Mormon Knowledge Graph data.
Use this to check your JSON additions before submitting a pull request.
"""

import json
import sys
from collections import defaultdict

def validate_knowledge_graph(filename='knowledge-graph.json'):
    """Validate the knowledge graph JSON file."""
    print(f"🔍 Validating {filename}...")
    
    try:
        with open(filename, 'r', encoding='utf-8') as f:
            data = json.load(f)
    except FileNotFoundError:
        print(f"❌ Error: {filename} not found")
        return False
    except json.JSONDecodeError as e:
        print(f"❌ JSON Error: {e}")
        return False
    
    print("✅ JSON is valid")
    
    # Check required structure
    if 'nodes' not in data or 'edges' not in data:
        print("❌ Error: Missing 'nodes' or 'edges' arrays")
        return False
    
    nodes = data['nodes']
    edges = data['edges']
    
    print(f"📊 Found {len(nodes)} nodes and {len(edges)} edges")
    
    # Validate nodes
    node_ids = set()
    node_issues = []
    
    for i, node in enumerate(nodes):
        # Check required fields
        if 'id' not in node:
            node_issues.append(f"Node {i}: Missing 'id' field")
            continue
            
        node_id = node['id']
        
        # Check for duplicate IDs
        if node_id in node_ids:
            node_issues.append(f"Node {i}: Duplicate ID '{node_id}'")
        else:
            node_ids.add(node_id)
        
        # Check required fields
        required_fields = ['label', 'type', 'references']
        for field in required_fields:
            if field not in node:
                node_issues.append(f"Node '{node_id}': Missing '{field}' field")
        
        # Check type values
        if 'type' in node and node['type'] not in ['person', 'group', 'place', 'event']:
            node_issues.append(f"Node '{node_id}': Invalid type '{node['type']}'")
        
        # Check references format
        if 'references' in node:
            if not isinstance(node['references'], list):
                node_issues.append(f"Node '{node_id}': References must be a list")
            else:
                for ref in node['references']:
                    if not isinstance(ref, str) or ':' not in ref:
                        node_issues.append(f"Node '{node_id}': Invalid reference format '{ref}'")
    
    # Validate edges
    edge_issues = []
    relationship_types = defaultdict(int)
    
    for i, edge in enumerate(edges):
        # Check required fields
        required_fields = ['from', 'to', 'label', 'references']
        for field in required_fields:
            if field not in edge:
                edge_issues.append(f"Edge {i}: Missing '{field}' field")
        
        if 'from' in edge and 'to' in edge:
            from_id = edge['from']
            to_id = edge['to']
            
            # Check if referenced nodes exist
            if from_id not in node_ids:
                edge_issues.append(f"Edge {i}: Source node '{from_id}' not found")
            if to_id not in node_ids:
                edge_issues.append(f"Edge {i}: Target node '{to_id}' not found")
        
        # Track relationship types
        if 'label' in edge:
            relationship_types[edge['label']] += 1
        
        # Check references format
        if 'references' in edge:
            if not isinstance(edge['references'], list):
                edge_issues.append(f"Edge {i}: References must be a list")
            else:
                for ref in edge['references']:
                    if not isinstance(ref, str) or ':' not in ref:
                        edge_issues.append(f"Edge {i}: Invalid reference format '{ref}'")
    
    # Report issues
    all_issues = node_issues + edge_issues
    
    if all_issues:
        print(f"\n❌ Found {len(all_issues)} issues:")
        for issue in all_issues:
            print(f"  • {issue}")
        return False
    else:
        print("✅ All nodes and edges are valid")
    
    # Show statistics
    print(f"\n📈 Relationship Types:")
    for rel_type, count in sorted(relationship_types.items()):
        print(f"  • {rel_type}: {count}")
    
    # Show node type distribution
    node_types = defaultdict(int)
    for node in nodes:
        if 'type' in node:
            node_types[node['type']] += 1
    
    print(f"\n👥 Node Types:")
    for node_type, count in sorted(node_types.items()):
        print(f"  • {node_type}: {count}")
    
    print(f"\n✅ Validation complete! Your knowledge graph is ready for submission.")
    return True

def check_references(filename='knowledge-graph.json'):
    """Check for common reference issues."""
    print(f"\n🔍 Checking scriptural references...")
    
    try:
        with open(filename, 'r', encoding='utf-8') as f:
            data = json.load(f)
    except:
        return
    
    all_references = set()
    
    # Collect all references
    for node in data.get('nodes', []):
        for ref in node.get('references', []):
            all_references.add(ref)
    
    for edge in data.get('edges', []):
        for ref in edge.get('references', []):
            all_references.add(ref)
    
    # Check for common issues
    issues = []
    for ref in all_references:
        # Check format
        if not ':' in ref:
            issues.append(f"Invalid format: '{ref}'")
            continue
        
        parts = ref.split(':')
        if len(parts) != 2:
            issues.append(f"Invalid format: '{ref}'")
            continue
        
        book_chapter, verse = parts
        
        # Check for common book names
        valid_books = [
            '1 Nephi', '2 Nephi', 'Jacob', 'Enos', 'Jarom', 'Omni', 'Words of Mormon',
            'Mosiah', 'Alma', 'Helaman', '3 Nephi', '4 Nephi', 'Mormon', 'Ether', 'Moroni'
        ]
        
        book_found = False
        for valid_book in valid_books:
            if book_chapter.startswith(valid_book):
                book_found = True
                break
        
        if not book_found:
            issues.append(f"Unknown book: '{ref}'")
    
    if issues:
        print(f"⚠️  Found {len(issues)} reference issues:")
        for issue in issues[:10]:  # Show first 10
            print(f"  • {issue}")
        if len(issues) > 10:
            print(f"  ... and {len(issues) - 10} more")
    else:
        print("✅ All references look good!")

if __name__ == '__main__':
    if len(sys.argv) > 1:
        filename = sys.argv[1]
    else:
        filename = 'knowledge-graph.json'
    
    success = validate_knowledge_graph(filename)
    check_references(filename)
    
    if not success:
        sys.exit(1)
