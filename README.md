# AirBnB clone
The AirBnB clone is simple copy of the AirBnB website with minimal features.
## Features
- A command interpreter to manipulate data without a visual interface, like in a Shell (perfect for development and debugging).
- A website (the front-end) that shows the final product to everybody: static and dynamic
- A database or files that store data (data = objects)
- An API that provides a communication interface between the front-end and your data (retrieve, create, delete, update them).
## Technologies
- Scripts are written in Bash 5.0.17(1)
- Tested on Ubuntu 20.04.1 LTS
- All python scripts wre written in python3.8
## Steps
1. #### The console
- Create your data model
- Manage (create, update, destroy, etc) objects via a console / command interpreter.
The first piece is to manipulate a powerful storage system. This storage engine will give us an abstraction between “My object” and “How they are stored and persisted”. This means: from your console code (the command interpreter itself) and from the front-end and RestAPI you will build later, you won’t have to pay attention (take care) of how your objects are stored.

This abstraction will also allow you to change the type of storage easily without updating all of your codebase.

The console will be a tool to validate this storage engine.
![The console](https://res.cloudinary.com/christo/image/upload/v1689093140/console_tk6bbz.png)
2. #### Web static
Now that you have a command interpreter for managing your AirBnB objects, it’s time to make them alive!
Before developing a big and complex web application, we will build the front end step-by-step.
The first step is to “design” / “sketch” / “prototype” each element:
- Create simple HTML static pages
- Style guide
- Fake contents
- No Javascript
- No data loaded from anything
During this project, you will learn how to manipulate HTML and CSS languages. HTML is the structure of your page, it should be the first thing to write. CSS is the styling of your page, the design. I really encourage you to fix your HTML part before starting the styling. Indeed, without any structure, you can’t apply any design.
![Web static](https://res.cloudinary.com/christo/image/upload/v1690073513/webstatic_hfpqy9.png)
