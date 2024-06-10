# Sprachen Karte
This project, titled "Sprachen Karte", generates a website featuring an interactive map complete with pointers. You can zoom in, move around, and toggle various features on the map. It encompasses every known language, including those that are extinct or endangered, along with outlines of their family origins and numerous other captivating features. My objective was Language Diversity Visualization I want to build an interactive visualization tool that displays the geographical distribution of languages, their relationships, and linguistic diversity metrics like language families, dialect continua, and endangered languages. I plan to implement graphs, interactive elements to engage users, and smears of colors representing families.

I created all python and JSON code, and you can freely use them for reference! I didn't personally develop the HTML, CSS, or JS code, although I did edit some of them. Credit for that goes to [@ajlkn](https://twitter.com/ajlkn), whose work I utilized. You can find all the files associated with his work in the "solid temp" folder. The result is stunning, and I'm grateful for his contribution. Moreover, the JS code for the map, 'map.js', is from [Amcharts](https://www.amcharts.com/demos/rotate-globe-to-a-selected-country/). Don't forget to explore [html5up](https://html5up.net/) for their fantastic templates!

My motivations were:
+ Develope an understanding of HTML, CSS, and JS code by experimenting and seeing what changes. Moreover, learning their syntax at a depper level.
+ Develope experience parsing larger websites with more sophisticated HTML and multiple variables (including dealing with coordinate variables).
+ Learn frontend and backend development at a basic level.
+ Creating datasets and uutilizing them in the JS code (taking data from Ethnologue and displaying them on the map).

Improvements I still ned to make:
1. **Batch Requests**: Instead of sending individual HTTP requests for each language page, you can utilize batch processing or asynchronous requests to scrape multiple pages simultaneously, which can significantly reduce the overall execution time.
2. **Caching Mechanism**: Implement a caching mechanism to store previously scraped data, reducing the need to re-scrape pages that haven't changed. This can be especially useful if you anticipate running the script multiple times.
3. **Optimized XPath Queries**: Review the XPath queries used in your code and ensure they are as efficient as possible. Avoid overly broad queries that may unnecessarily traverse large portions of the HTML tree.
4. **Minimize External Requests**: Minimize the number of external requests by fetching only the necessary data from each page. For example, if you only need language status, extract only that information instead of parsing the entire page.
5. **Error Handling**: Implement robust error handling to gracefully handle exceptions, such as network errors or unexpected HTML structures. This ensures your script continues to run smoothly even in adverse conditions.
6. **Parallel Processing**: Utilize parallel processing techniques, such as multi-threading or multiprocessing, to perform tasks concurrently and make better use of available system resources.
7. **Code Refactoring**: Refactor your code to eliminate redundancy and improve readability. Look for opportunities to modularize repetitive tasks into functions or classes.

Overall, this is to enhance efficiency, you can make some optimizations and improvements to your code. Here are some suggestions:

Thanks to [Rafee Adnan](https://www.linkedin.com/in/radnaan/) for helping with the JS code!
