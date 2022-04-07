[techxplore.com](https://techxplore.com/news/2022-02-scientist-network-witcher.html)

# Data scientist builds a detailed network map of 'The Witcher'

Ingrid Fadelli

---

"The Witcher," a fantasy novel series by Andrzej Sapkowski, has become increasingly popular, following the release of several videogames and a spin-off series by Netflix. The latest season of the show, uploaded on Netflix in December 2021, was watched by users worldwide for 2.2 billion minutes in its debut week alone.

Milán Janosov, lead scientist at Datopolis with a Ph.D. in Network Science from Central European University recently tried to summarize the plot and character relationships in "The Witcher" using network science. In a paper published on Nightingale, arXiv and ResearchGate, he introduced the first visual network map outlining the hidden patterns, storylines and character relationships in the fantasy series.

"I started reading "'The Witcher' early last year, shortly after I got hooked to the Netflix show, and the storyline just sucked me in," Janosov told TechXplore. "It was a somewhat similar experience to watching 'Game of Thrones' a few years ago, which had also inspired one of my research articles. When I was about to finish watching the new season of Witcher, I started to wonder how I could get more out of this."

Although "The Witcher" videogames are also highly popular and iconic, Janosov was more drawn to the storylines and relationships outlined in the books and Netflix series. On a quest to understand the iconic series' world more in depth, he thus set out to create a social map of 'The Witcher.'"

The first step for his research was to collect data that he could then use to create the network map. He started by looking at the Netflix show's subtitles, but soon realized that he would need more than that and decided to analyze the whole text of the book series, too.

"To build a network, I also needed a complete list of the characters who appeared in the series," Janosov said. "After collecting these initial pieces of information, my job was fairly simple. I wrote a computer program that screened through every single sentence of all the books and took a note every time it matched a character's name into a sentence."

Using his computer program, Janosov derived the mentions for every character in sentences. This allowed him to determine how close or far two characters were, in terms of how often they were mentioned in similar parts of the texts (e.g., whether two characters were mentioned in the same sentence, two sentences apart, and so on).

"As it turns out, these proximities are pretty good indicators of whether two characters have actually met or were featured in the same plots," Janosov said.
The social map of The Witcher. Characters are represented by nodes, their size corresponding to their degree centrality, and their colors encode the network communities to which they belong. The network links are proportional to the number of times two characters were mentioned within a five-sentence distance from each other in the novel. The most significant 50 individuals are labeled. Credit: Milán Janosov.

After looking at the proximity between character mentions, Janosov defined the elements in his network. More specifically, he decided to represent every character with a node, linking nodes when characters were mentioned in the same "context" or part of the text.

"While context is relatively easy to interpret for humans, for a computer, it is not that simple," Janosov explained. "So to capture the context of the characters mentioned, I assumed that two characters were mentioned in the same context as they were not mentioned further than five sentences from each other. While the number five is somewhat arbitrary, it was chosen for the sake of simplicty (and OCD-friendliness), because three, four or even six sentence-distances lead to very similar results too, also staying consistent for example with the typical paragraph lengths in written text."

Janosov's paper is a valuable example of how network science can be used to reveal hidden patterns in large amounts of unstructured data, such as texts, novels, or movie scripts. After reading books or other texts that are thousands of pages long, humans can get a general idea of how a story is structured. However, they will generally be unable to memorize all the characters and remember all details of the plot.

If they were to draw a map of the story, therefore, this map would most likely be biased. In contrast, network science tools can help to summarize a saga or book series in a quantitive and objective way.

"I was surprised and excited to see the different plots clustered into network communities," Janosov said. "You know that kind of Eureka moment when suddenly everything starts to make sense—who met whom, who is together, where the main conflicts and smaller spin-off plots fold out, etc., almost like in a detective movie. At this point,the skeptic may ask—why would we care so much about a fantasy novel? While the example of 'The Witcher' is certainly fun, it indeed does not seem to bear that crucial practical importance at first."

While the network map of "The Witcher" resulting from this study and other maps that Janosov created in the past are unique and interesting, his work is merely an example of how network science could be implemented in the real-world. In fact, similar data analysis tools could also be used to summarize other networks in the real world.

"In our daily lives, we are surrounded by social networks: our friends on social media, our colleagues at work, friends from school, family, sports and hobbies, and many more," Janosov said. "All these social systems are intertwined by networks of which we almost always only have a partial and subjective understanding. To overcome this lack of knowledge and sparsity of information, network science comes really handy as it provides a set of tools and a framework of thinking that can help us better understand these social networks we participate in daily, just as it helped to clear the fog around 'The Witcher.'"

Network science tools like the ones employed by Janosov could also be applied (or are already in use) in a series of real-world settings. For instance, they could be used by HR specialists to design better work environments or enhance collaboration between co-workers, by scientific organizations to optimize the sharing of research funding across different research groups, or even to analyze and improve international trade and telecommunications.

"As the Academy Awards are coming next month, I am now thinking to revisit my previous research capturing the role of luck in the success of films and music, to see how much luck counts this year," Janosov added. 
