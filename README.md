# ECOBIZ
 
To deploy changes, use:
```
gcloud builds submit --tag gcr.io/ecobiz-com/ecobiz
gcloud beta run deploy ecobiz --image gcr.io/ecobiz-com/ecobiz

firebase deploy
```
## Inspiration
In the ideation of our product, we wanted to create a community-driven platform inspired by the 17 United Nations Sustainable Development Goals in order to ensure both social and sustainable impact for the world at large. These were adopted by all member states of the United Nations in 2015 as a universal call to action and are generally recognized as a symbol of our goals for a bright future by 2030. With this in mind, we decided to create a spin on freelancing platforms such as Fiverr and Upwork by developing ECOBIZ, which redefines the future of freelancing and protects the world at large, one sustainable service at a time.

## What it does
ECOBIZ is a web app that creates a global network of sustainable businesses and freelancers. The platform matches freelancers with businesses who are seeking to outsource creative services remotely, ranging from product design to social media marketing. In doing so, ECOBIZ raises awareness and visibility of people who create sustainable products, businesses with sustainable practices, and other advocates of eco-friendly entrepreneurship. ECOBIZ also provides a variety of resources to keep “eco-entrepreneurs” up to date with the latest sustainable practices, project management tools, and guides for business owners.

Freelancers can promote their services through ECOBIZ by joining The Sustainable Directory, or they can apply to a job directly through the links embedded on a company's listing on The Eco-Job Board. Businesses can explore The Sustainable Directory to find freelancers with specific skills they are looking to outsource, or post a listing directly on The Eco-Job Board.

## How we built it
In order to lay out the overall vision of our web application and construct an intuitive user experience, we first created high-fidelity mockups using Figma, then used HTML and CSS to build the static frontend.

To integrate the HTML and CSS with the Python backend, we used the Flask framework and Jinja2 for templating. For dynamic pages, such as registering, logging in, and posting listings or profiles, the website triggers a POST request and the server-side Python code retrieves data from the client-side HTML form. This data is then formatted and passed to Firebase API calls.

We use Firebase to let users register and log in, as well as for its Realtime Database, where we store information about jobs and freelancers’ profiles. We also use Firebase Hosting and Google Cloud Run in conjunction to serve our website (Cloud Run is needed because Firebase only hosts static sites by itself).


## Accomplishments that we're proud of
Skyler - While building the high-fidelity wireframes, I dove deeper into the product design thinking process and learned so much more about how to keep users in mind when designing the UI. It was rewarding to help bring the prototype to life with HTML and CSS. I had such a blast working with Rachelle to help create a sustainable product that could make a greater difference for the world.

Rachelle - This was my first time using Firebase and Cloud Run to deploy a full-fledged dynamic web application. It was a difficult process with many bugs and refactorings, but it was worth it in the end to see the result and be able to share it with other people. I’m proud that Skyler and I were able to work together in our respective areas to bring this project to fruition with the goal of increasing sustainable business practices.


## What's next for ECOBIZ
In the future, we plan to integrate more educational resources into the “resources” tab of ECOBIZ, along with developing a form that allows users to manually contribute sustainable resources to the database. Moreover, we plan to create an online, self-paced curriculum with multiple learning modules which educate entrepreneurs about sustainable practices to incorporate when scaling their business. We also want to launch a new feature in the job board that enables freelancers to apply for gigs directly within the ECOBIZ website, rather than through a third party platform.
