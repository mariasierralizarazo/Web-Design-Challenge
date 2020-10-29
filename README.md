# Web-Design-Challenge
HTML site creation based on provided data and images
<br></br>
Used tools:
<li><strong>Bootstrap:</strong> as Front end Framework </li>
<li><strong>Pandas:</strong> for generating HTML code of a large dataset as a table </li>
<br>
Nowadays, reading data is better with all the available visualization tools. Graphical visualizations allow people to have a better understanding of what datasets are representing or the goal of analyzing them; also, as it is well known: " A picture is worth a thousand words."
In this project, the main goal was to build a website where the results of analyzing a weather dataset were posted with the corresponding explanations. All the data and images were given for focusing the project on the construction of the website. <br>
The initial graphs from the analysis are in the <a href="https://github.com/mariasierralizarazo/Web-Design-Challenge/tree/master/WebVisualizations/assets/images">[assets/images]</a> folder, and the original data is in the <a href="https://github.com/mariasierralizarazo/Web-Design-Challenge/blob/master/WebVisualizations/Resources/cities.csv">[Resources/cities.csv]</a> file.   
<br></br>
In general, the website has 3 important elements:
<p align="center">
  <img width="560" height="250" src="https://github.com/mariasierralizarazo/Web-Design-Challenge/blob/master/WebVisualizations/assets/images/figures/page_explanation.png?raw=true">
</p>
<li><strong> Navbar</strong>: located at the top, allows the navigation through all the pages. On the left side, it has the "logo" of the website with the highlight word Latitude, and on the right side, it has the link to the data and comparison pages and a drop-down menu with the links to the temperature, humidity, cloudiness, and wind speed analysis.</li>
<li><strong>Visualization menu</strong>: located at the right side of the visualization and index pages, it allows the user to navigate on the visualization pages. This menu eases access. </li>
<li><strong>Content</strong>: Where the principal information on each page is posted.</li> 
<br>
<strong>Note:</strong>It is important to point out that all the pages on this website are responsible, which means that they change the structure with the size of the screen. The latter allows the user to have better visualization. 
<p align="center">
  <img width="560" height="250" src="https://github.com/mariasierralizarazo/Web-Design-Challenge/blob/master/WebVisualizations/assets/images/figures/responsive_small.png?raw=true">
</p>
<h3> Pages on the website: </h3>
<li> Landing page <a href="https://github.com/mariasierralizarazo/Web-Design-Challenge/blob/master/WebVisualizations/index.html">[index.html]</a>: It contains the general project's explanation.</li>
<li> Comparison page <a href="https://github.com/mariasierralizarazo/Web-Design-Challenge/blob/master/WebVisualizations/comparison.html">[comparison.html]</a>: It allows the user to see all the graphs in a better size for comparison between them. It does also allow the navigation clicking the images. </li>
<li> Data page <a href="https://github.com/mariasierralizarazo/Web-Design-Challenge/blob/master/WebVisualizations/comparison.html">[data.html]</a>: It displays the data used for all the analyses. For the production of this view, it was necessary to use the Pandas module that helped to generate the table HTML code after reading the CSV file. [Used code here] </li>
<li>  Visualization pages: </li>
<ul>
  <li>  Maximum temperature <a href="https://github.com/mariasierralizarazo/Web-Design-Challenge/blob/master/WebVisualizations/temp.html">[temp.html]</a></li>
  <li>  Humidity <a href="https://github.com/mariasierralizarazo/Web-Design-Challenge/blob/master/WebVisualizations/humidity.html">[humidity.html]</a></li>
  <li>  Cloudiness <a href="https://github.com/mariasierralizarazo/Web-Design-Challenge/blob/master/WebVisualizations/cloudiness.html">[cloudiness.html]</a></li>
  <li>  Wind speed <a href="https://github.com/mariasierralizarazo/Web-Design-Challenge/blob/master/WebVisualizations/windspeed.html">[windspeed.html]</a></li>
</ul>
<br></br>
Finally, this website was host on the Github server <a href="https://mariasierralizarazo.github.io/"> [Latitude Website] </a>, and all the pages were deployed in GitHub too. 

