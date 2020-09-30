# myblog
django project for 221bbakerst.site

### Functions in detail：

1. **url of top navigation bar and bottom footer**

2. **index page**

  - [x] register and login
    - [x] registration email auto check if it is illegal or taken, and username auto check if the name is already taken.
    - [x] send a verification email to user's email once registered, but confirmation isn't a must for successful registration
    - [x] be able to modify user information, including password, email and default avatar after log-in
  - [ ] music player
    - [ ] load the music resources
    - [ ] the play/pause/prev/next buttons
    - [ ] show on the bottom of every page unless closed

3. **blog page**

  - [x] the info of each post, including the creation date, the author, the category and the tags, all of which can be manipulated on admin backend
  - [x] preview picture
  - [x] embeded video
  - [x] post overview
    - [x] Apply ckeditor as RichText Editor on admin backend
  - [x] pagination on blog page, to show post overviews page by page
    - [x] highlight the corresponding page button
    - [x] hide first page button and previous page button when on first page, and hide last page button and next page button when on last page
  - [x] sidebar
    - [x] full-text search, and results shown with pagination
    - [x] tags and categories (including the number of each category, and the sorting by number)
    - [x] useful links, edited from admin backend
  - [x] tags and categories, each with the statistics

4. **article page**

  - [x] write the article content with markdown on admin backend
  - [ ] the like button with the number of likes (can be revoked)
  - [ ] comment
	  - [x] login to comment
	  - [x] comment with rich-text editor (emoticon, code block, hyperlinks, etc. supported)
	  - [x] Google reCAPTCHA authentication before submission
	  - [x] record in database when submitted, and post it on the page simultaneously 
    - [x] redirect to error page with error code if failure, but keep the comment where it was if the user step back
    - [x] delete the comments of the user's own
    - [ ] reply every comment/reply
    - [ ] comment thread and email notification if replied
  - [x] sidebar as mentioned above

5. **album page**

  - [x] slide show
  - [x] urls of the mini navbar and album cover

6. **photo page**

  - [x] picture browse in each album
	- [x] description on preview
  - [x] click to view original high-definition photos
  - [x] pagination on blog page, to show post overviews page by page
    - [x] highlight the corresponding page button
    - [x] hide first page button and previous page button when on first page, and hide last page button and next page button when on last page

7. **about page**

  - [x] message board
    - [x] Google reCAPTCHA authentication before submission;
	  - [x] record in database when submitted, and send an email to the admin;
	  - [x] redirect to error page with error code if failure, but keep the message where it was if the user step back

8. **error pages and log system**

  - [x] 404 & 500 pages
	- [x] log
	- [x] notify the admin if any errors, except 404

9. **admin backend**

  - [x] for uploaded images, when they are updated or deleted by admin, they will also be deleted in static files to save storage.
