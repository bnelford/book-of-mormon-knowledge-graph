#!/usr/bin/env node
/**
 * Loopback static server for the knowledge graph.
 * The page and JSON are same-origin, so wildcard CORS is not sent.
 * Hidden files (including .git) and paths outside this directory are refused.
 */

const http = require('http');
const fs = require('fs');
const path = require('path');

const ROOT = path.resolve(__dirname);

function parsePort(argv, fallback) {
  for (let i = 0; i < argv.length; i += 1) {
    const arg = argv[i];
    if (arg.startsWith('--port=')) {
      return Number(arg.slice('--port='.length));
    }
    if (arg === '--port') {
      return Number(argv[i + 1]);
    }
  }
  return fallback;
}

const PORT = parsePort(process.argv.slice(2), 8000);
if (!Number.isInteger(PORT) || PORT < 1 || PORT > 65535) {
  console.error('Invalid port');
  process.exit(1);
}

const mimeTypes = {
  '.html': 'text/html',
  '.js': 'text/javascript',
  '.css': 'text/css',
  '.json': 'application/json',
  '.png': 'image/png',
  '.jpg': 'image/jpeg',
  '.gif': 'image/gif',
  '.svg': 'image/svg+xml',
  '.ico': 'image/x-icon'
};

function resolveFromRoot(rawPathname) {
  let decoded;
  try {
    decoded = decodeURIComponent(rawPathname);
  } catch {
    return null;
  }
  if (decoded.includes('\0')) {
    return null;
  }

  const parts = [];
  for (const part of decoded.split(/[/\\]/)) {
    if (part === '' || part === '.') {
      continue;
    }
    // Reject parent traversal and dotfiles such as .git/config.
    if (part === '..' || part.startsWith('.')) {
      return null;
    }
    parts.push(part);
  }

  const filePath = path.resolve(ROOT, ...parts);
  const relative = path.relative(ROOT, filePath);
  if (relative.startsWith('..') || path.isAbsolute(relative)) {
    return null;
  }
  return filePath;
}

function send(res, status, body, headers) {
  res.writeHead(status, headers);
  res.end(body);
}

const handler = (req, res) => {
  if (req.method !== 'GET' && req.method !== 'HEAD') {
    send(res, 405, 'Method not allowed', {
      'Content-Type': 'text/plain',
      Allow: 'GET, HEAD'
    });
    return;
  }

  const rawUrl = req.url || '/';
  let pathname = rawUrl.split('?')[0].split('#')[0];
  if (pathname === '/') {
    pathname = '/knowledge-graph.html';
  }

  const filePath = resolveFromRoot(pathname);
  if (!filePath) {
    send(res, 403, 'Forbidden', { 'Content-Type': 'text/plain' });
    return;
  }

  fs.realpath(filePath, (realErr, realPath) => {
    if (realErr) {
      send(res, 404, 'File not found', { 'Content-Type': 'text/plain' });
      return;
    }

    const relative = path.relative(ROOT, realPath);
    const escaped = relative.startsWith('..')
      || path.isAbsolute(relative)
      || relative.split(path.sep).some((part) => part.startsWith('.'));
    if (escaped) {
      send(res, 403, 'Forbidden', { 'Content-Type': 'text/plain' });
      return;
    }

    const ext = path.extname(realPath).toLowerCase();
    const contentType = mimeTypes[ext] || 'application/octet-stream';
    fs.readFile(realPath, (readErr, data) => {
      if (readErr) {
        send(res, 500, 'Internal server error', { 'Content-Type': 'text/plain' });
        return;
      }
      res.writeHead(200, { 'Content-Type': contentType });
      if (req.method === 'HEAD') {
        res.end();
        return;
      }
      res.end(data);
    });
  });
};

function announce(port) {
  console.log(`Server running at http://localhost:${port}/`);
  console.log(`Open http://localhost:${port}/knowledge-graph.html in your browser`);
  console.log('Press Ctrl+C to stop the server');
}

function listen(port) {
  const v4 = http.createServer(handler);
  v4.on('error', (err) => {
    if (err.code === 'EADDRINUSE') {
      console.log(`Port ${port} is already in use. Trying port ${port + 1}...`);
      listen(port + 1);
      return;
    }
    console.error('Server error:', err);
  });

  v4.listen(port, '127.0.0.1', () => {
    let announced = false;
    const sayReady = () => {
      if (!announced) {
        announced = true;
        announce(port);
      }
    };

    const v6 = http.createServer(handler);
    v6.on('error', () => {
      sayReady();
    });
    v6.listen(port, '::1', () => {
      sayReady();
    });
  });
}

listen(PORT);
