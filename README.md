#KNOWN BUGS
- Images for new stories are not loading correctly

## Stories by Author feature
### Plan:
1. Create stories with different authors in db using shell or SQL
2. Figure out the query to retrieve the stories for a particular author

SELECT * from news_newsstory
    WHERE author_id = 1;
    
2. figure out the query to make the author's name on a story / storycard, a dynamic link to all stories by that author
3. template for that view  