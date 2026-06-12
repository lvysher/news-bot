# Morning News Digest Bot

## Problem

Staying informed requires visiting multiple news websites and manually browsing through headlines every morning. This process can be time-consuming and often leads to information overload.

The goal of this project was to automate news collection and deliver a concise, easy-to-read summary of the most important headlines directly to the user's inbox every morning.

## Approach

The Morning News Digest Bot is a Python-based automation tool that collects the latest headlines from multiple trusted news sources, compiles them into a formatted email, and delivers the digest automatically.

The bot retrieves:

* Top headlines from BBC News
* Top headlines from Reuters
* Top headlines from The New York Times
* Publication timestamps
* Direct article links

The application runs automatically every morning using GitHub Actions and requires no manual intervention after deployment.

## Tech Stack

* Python
* Requests
* Feedparser
* SMTP (Email Automation)
* GitHub Actions
* RSS Feeds
* Environment Variables
* GitHub Secrets

## Key Features

* Automated daily execution
* Aggregates headlines from multiple news sources
* Includes article publication times
* Includes direct article links
* HTML email generation
* Email delivery directly to the user's inbox
* Secure credential management using GitHub Secrets
* Cloud-based scheduling using GitHub Actions

## Data Sources

The bot retrieves news from publicly available RSS feeds:

* BBC News
* Reuters
* The New York Times

Using RSS feeds ensures reliable access to current headlines without requiring complex web scraping logic.

## Craft

The project was designed with reliability and maintainability in mind.

* Each news source is fetched independently.
* Failed requests do not stop the entire digest generation process.
* API and network errors are handled gracefully.
* Sensitive credentials are stored securely using GitHub Secrets.
* HTML email formatting improves readability across devices.
* Automated workflows ensure consistent daily execution.

This approach allows the bot to continue functioning even if one news source becomes temporarily unavailable.

## Outcome

The Morning News Digest Bot automatically generates and delivers a curated news summary every morning.

The project demonstrates practical skills in:

* Python Automation
* RSS Feed Processing
* Email Automation
* Data Aggregation
* GitHub Actions
* Cloud Scheduling
* Error Handling
* Secure Credential Management

## Sample Output

### Email Subject

```text
Morning News Digest
```

### Example Digest

```text
Morning News Digest
Friday, 12 June 2026

BBC
• Global markets react to economic data
Published: Fri, 12 Jun 2026 05:00 GMT

Reuters
• Technology companies announce new AI initiatives
Published: Fri, 12 Jun 2026 04:45 GMT

The New York Times
• Scientists report breakthrough climate findings
Published: Fri, 12 Jun 2026 03:30 GMT

Read the full articles using the links provided.
```

## Future Improvements

* Category-based filtering (Technology, Sports, Business)
* Personalized news preferences
* AI-generated article summaries
* Telegram notifications
* WhatsApp integration
* Daily PDF digest generation
* News sentiment analysis
* Multi-language support
* Trending topic detection
* Web dashboard for managing subscriptions
