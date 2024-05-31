# config.py

SUBMISSION_DATA_FIELDS = [
    "author",
    "author_flair_text",
    "clicked",
    "comments",
    "created_utc",
    "distinguished",
    "edited",
    "id",
    "is_original_content",
    "is_self",
    "link_flair_template_id",
    "link_flair_text",
    "locked",
    "name",
    "num_comments",
    "over_18",
    "permalink",
    "poll_data",
    "saved",
    "score",
    "selftext",
    "spoiler",
    "stickied",
    "subreddit",
    "title",
    "upvote_ratio",
    "url"
]

LLAMA_PROMPT = """
<task>
You will be given a rap feud context and a user comment from an online forum. 
Your task is to classify the comment based on the given context.
The context of the rap feud is provided within <context></context>.
Based on the context and the comment, choose one of the following responses:
<output>Drake, Kendrick Lamar, Neutral</output>
Choose the rapper who is positively mentioned or the one not being criticized in a negative comment about the other rapper.

Examples:
1. Comment: "Drake's new song is fire! Kendrick can't compete with that."
   Output: Drake

2. Comment: "Kendrick's lyrics are way deeper than Drake's."
   Output: Kendrick Lamar

3. Comment: "Drake's accusations are totally false and just a low blow."
   Output: Kendrick Lamar

4. Comment: "Both of them are talented in their own ways."
   Output: Neutral
</task>
<context>
Canadian rapper Drake (also known as Champagne Papi, Drizzy, OVO, 6 God) and American rapper Kendrick Lamar (also known as K.Dot, Kendrick Lamar Duckworth) have been in a rap feud since the early 2010s. 
The feud escalated in March 2024 after the release of "Like That" by Future, Metro Boomin, and Lamar.
Their relationship began with collaborations in 2011 on Drake's album *Take Care* and in 2012 on Lamar's album *Good Kid, M.A.A.D City*. 
In 2013, Lamar dissed Drake on Big Sean's song "Control", which he called "friendly competition".
In March 2024, Lamar dissed J. Cole and Drake on "Like That" after J. Cole suggested on "First Person Shooter" that he, Drake, and Lamar were the "Big Three" of hip hop. 
Cole responded with "7 Minute Drill", which he later apologized for and removed.
In April, Drake released "Push Ups" and "Taylor Made Freestyle", the latter being deleted due to legal threats from Tupac Shakur's estate over AI-generated vocals. 
Lamar replied with "Euphoria" on April 30 and "6:16 in LA" on May 3. 
Drake then released "Family Matters" on May 3, accusing Lamar of domestic abuse and alleging that one of Lamar's children was fathered by Dave Free. 
Lamar countered with "Meet the Grahams", accusing Drake of sex trafficking, being a sexual predator, and fathering a secret child. 
Lamar followed up with "Not Like Us" on May 4, further accusing Drake of pedophilia and lying about Lamar's family. 
Drake responded with "The Heart Part 6" on May 5, denying Lamar's accusations and claiming Lamar had false information about the secret child. 
On May 24, Drake released "U My Everything" with Sexyy Red, rapping over the "BBL Drizzy" beat, produced by Metro Boomin, which claimed Drake received a Brazilian butt lift.
Critics generally view Lamar as leading the feud, with Pitchfork, The Ringer, and Rolling Stone, and social media users favoring Lamar.
</context>"""

