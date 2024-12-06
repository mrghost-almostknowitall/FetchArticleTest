# Part 1: Website Sharing

**Objective**:
Whenever a new article is published on a given website an image or video with a caption is published
on your website. If you need to use API’s or external tools, make it cost efficient.

Steps:
1. Trigger: The automation recognizes when a new post is published on a website. (Choose
cnn.com, variety.com, or any other credible news website of your choice).

Solution : Using selenium to scrape the latest article'


2. The automation fetches and reads the new article to write a 2-3 sentence caption using
an API or similar. The caption must also include a shortened URL to the article.

**Sol**: Concatenating the article text and shortened url (using ulvis.net free url shortnere api)


3. Based on the retrieved text contents of the article an image or video is generated (you may
use an API).

**Sol**:Using unsplash api for random image based on a keyword picked on random to generate a image url


4. Publish: The picture/video and caption with shortened link is uploaded on your own
website.

**Sol**: Using streamlit to make a temporary website to host content. Not yet fully implemented.


5. Automation: Ensures every time the trigger is activated (new post on website) it goes
through this process for uploading the thumbnail/video alongside a short caption with

**Sol**: ~~Not implemented~~


# Part 2: Instagram Sharing
**Objective:**
Testing your skills with social media instead of a website.

### NOT ATTEMPTED YET