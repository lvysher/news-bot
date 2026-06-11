import requests
import feedparser
from datetime import date
import smtplib
import os
from email.mime.text import MIMEText


# -----------------------------
# FUNCTION : Fetch News
# -----------------------------

def get_news():

    feeds = {
        "BBC": "https://feeds.bbci.co.uk/news/rss.xml",
        "Reuters": "https://feeds.reuters.com/reuters/topNews",
        "NYTimes": "https://rss.nytimes.com/services/xml/rss/nyt/HomePage.xml"
    }

    headlines = []

    for source, url in feeds.items():

        try:

            feed = feedparser.parse(url)

            for item in feed.entries[:3]:

                headlines.append({
                    "source": source,
                    "title": item.title,
                    "link": item.link,
                    "published": item.get(
                        "published",
                        "Publication time unavailable"
                    )
                })

        except Exception as e:

            headlines.append({
                "source": source,
                "title": f"Failed to fetch news ({e})",
                "link": "",
                "published": ""
            })

    return headlines


# -----------------------------
# FUNCTION : Build HTML Email
# -----------------------------

def build_html():

    today = date.today().strftime(
        "%A, %d %B %Y"
    )

    news = get_news()

    html = f"""
    <html>
    <body>

    <h1>📰 Morning News Digest</h1>

    <p>{today}</p>

    <hr>
    """

    for article in news:

        html += f"""
        <div style="margin-bottom:20px;">

            <h3>{article['title']}</h3>

            <p>
                <strong>Source:</strong>
                {article['source']}
            </p>

            <p>
                <strong>Published:</strong>
                {article['published']}
            </p>

            <a href="{article['link']}">
                Read Article
            </a>

        </div>
        """

    html += """
    <hr>
    <p>Generated automatically by NewsBot</p>
    </body>
    </html>
    """

    return html


# -----------------------------
# EMAIL
# -----------------------------

def send_email(html_content):

    sender = os.environ.get("EMAIL_SENDER")
    password = os.environ.get("EMAIL_PASSWORD")
    receiver = os.environ.get("EMAIL_RECEIVER")

    msg = MIMEText(
        html_content,
        "html"
    )

    msg["Subject"] = "Morning News Digest"
    msg["From"] = sender
    msg["To"] = receiver

    with smtplib.SMTP_SSL(
        "smtp.gmail.com",
        465
    ) as server:

        server.login(
            sender,
            password
        )

        server.send_message(msg)

    print("Email sent.")


# -----------------------------
# RUN
# -----------------------------

def run():

    html = build_html()

    with open(
        "news_digest.html",
        "w",
        encoding="utf-8"
    ) as f:

        f.write(html)

    send_email(html)

    print(
        "News Bot ran successfully."
    )


if __name__ == "__main__":
    run()