# 🚀 Deployment Guide

This guide explains how to deploy the Book of Mormon Knowledge Graph to GitHub Pages.

## 📋 Prerequisites

- GitHub repository with the knowledge graph code
- GitHub Pages enabled in repository settings
- Push access to the main/master branch

## 🔧 Setup Instructions

### 1. Enable GitHub Pages

1. Go to your repository on GitHub
2. Click on **Settings** tab
3. Scroll down to **Pages** section
4. Under **Source**, select **GitHub Actions**
5. Save the settings

### 2. Configure Repository Settings

1. In **Settings** → **Actions** → **General**
2. Ensure **Actions permissions** is set to "Allow all actions and reusable workflows"
3. Under **Workflow permissions**, select "Read and write permissions"
4. Check "Allow GitHub Actions to create and approve pull requests"

### 3. Deploy

The deployment happens automatically when you push to the main branch. The workflow will:

1. **Validate** the knowledge graph data
2. **Test** both Python and Node.js servers
3. **Build** the deployment artifact
4. **Deploy** to GitHub Pages

## 🌐 Access Your Deployment

Once deployed, your knowledge graph will be available at:
```
https://[your-username].github.io/book-of-mormon-knowledge-graph/
```

## 🔄 Deployment Process

### Automatic Deployment

Every push to the main branch triggers:
- Data validation
- Server testing
- GitHub Pages deployment

### Manual Deployment

You can manually trigger a deployment:

1. Go to **Actions** tab
2. Select **Deploy to GitHub Pages** workflow
3. Click **Run workflow**
4. Choose branch and click **Run workflow**

## 📊 Deployment Status

Check deployment status:
- **Actions** tab shows workflow runs
- **Pages** tab shows deployment history
- **Settings** → **Pages** shows current deployment

## 🛠️ Troubleshooting

### Common Issues

**Deployment Fails**
- Check Actions tab for error messages
- Ensure all validation checks pass
- Verify repository permissions

**Page Not Loading**
- Wait 5-10 minutes for DNS propagation
- Check if GitHub Pages is enabled
- Verify the deployment was successful

**Custom Domain Issues**
- Add CNAME file to repository root
- Configure DNS settings with your domain provider
- Wait for SSL certificate generation

### Validation Errors

If deployment fails due to validation:
1. Run `python3 validate.py` locally
2. Fix any JSON structure issues
3. Ensure all references are valid
4. Test servers locally before pushing

## 🔒 Security

GitHub Pages provides:
- **HTTPS** by default
- **SSL certificates** automatically managed
- **DDoS protection** through GitHub's infrastructure
- **Global CDN** for fast loading

## 📈 Performance

GitHub Pages offers:
- **Global CDN** for fast worldwide access
- **Automatic compression** for smaller file sizes
- **HTTP/2** support for better performance
- **Caching** for improved load times

## 🔄 Updates

To update your deployment:
1. Make changes to your code
2. Commit and push to main branch
3. Deployment happens automatically
4. Changes are live within minutes

## 📱 Mobile Support

GitHub Pages automatically provides:
- **Responsive design** support
- **Mobile-optimized** loading
- **Touch-friendly** interactions
- **Cross-browser** compatibility

## 🎯 Best Practices

1. **Test locally** before pushing
2. **Validate data** using the validation script
3. **Monitor deployments** in the Actions tab
4. **Keep dependencies** up to date
5. **Use semantic versioning** for releases

## 📞 Support

If you encounter issues:
1. Check the [GitHub Pages documentation](https://docs.github.com/en/pages)
2. Review the [Actions logs](https://docs.github.com/en/actions/monitoring-and-troubleshooting-workflows)
3. Create an [issue](https://github.com/bnelford/book-of-mormon-knowledge-graph/issues) for help

---

**Happy deploying!** 🚀
