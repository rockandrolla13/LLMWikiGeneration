## O'REILLY 

## | 

is|q to Un derstand, k With Co 


![](markdown_output/hermans-2024-code-reading-in-practice_images/hermans-2024-code-reading-in-practice.pdf-0001-03.png)


**----- Start of picture text -----**<br>
SSPo<br>A& Speevo<br>Bae ieHe ZZa<<br>SSN<br>Sa Chee fetea Se= a<br>ieee EA Seas Leek gyhera .SN<br>ae AE SOROS 7s .a<br>Baas aie Bs Bate ie... fa Ne eae ' ah uy a<br>Sanisiunie TH ip ce aed<br>HeyCNV,<< “a<br>WA — _<br>**----- End of picture text -----**<br>



![](markdown_output/hermans-2024-code-reading-in-practice_images/hermans-2024-code-reading-in-practice.pdf-0001-04.png)


**----- Start of picture text -----**<br>
W &<br>**----- End of picture text -----**<br>


lenncne 

## Code Reading in Practice 

Hands-On Techniques to Understand, Refactor and Improve How You Work With Code 

With Early Release ebooks, you get books in their earliest form—the author’s raw and unedited content as they write—so you can take advantage of these technologies long before the official release of these titles. 

Felienne Hermans 

## Code Reading in Practice 

by Felienne Hermans 

Copyright © 2023 Felienne Hermans. All rights reserved. 

Printed in the United States of America. 

Published by O’Reilly Media, Inc., 1005 Gravenstein Highway North, Sebastopol, CA 95472. 

O’Reilly books may be purchased for educational, business, or sales promotional use. Online editions are also available for most titles (http://oreilly.com). For more information, contact our corporate/institutional sales department: 800-998-9938 or . _corporate@oreilly.com_ 

Acquisitions Editor: Melissa Duffield 

- Development Editor: Sara Hunter 

- Production Editor: Clare Laylock 

- Copyeditor: [TO COME] 

Proofreader: [TO COME] 

Indexer: [TO COME] 

Interior Designer: David Futato 

Cover Designer: Karen Montgomery 

Illustrator: Kate Dullea 

December 2023: First Edition 

Revision History for the Early Release 

2022-09-29: First Release 

= See http://oreilly.com/catalog/errata.csp?isbn 9781098133825 for release details. 

The O’Reilly logo is a registered trademark of O’Reilly Media, Inc. _Code Reading in Practice_ , the cover image, and related trade dress are trademarks of O’Reilly Media, Inc. 

The views expressed in this work are those of the author(s) and do not represent the publisher’s views. While the publisher and the author(s) have used good faith efforts to ensure that the information and instructions contained in this work are accurate, the publisher and the author(s) disclaim all 

responsibility for errors or omissions, including without limitation responsibility for damages resulting from the use of 

or reliance on this work. Use of the information and instructions contained in this work is at your own risk. If any code samples or other technology this work contains or describes is subject to open source licenses or the intellectual property rights of others, it is your responsibility to ensure that your use thereof complies with such licenses and/or rights. 

978-1-098-13376-4 

[TO COME] 

## Chapter 1. Structural examination 

## **A NOTE FOR EARLY RELEASE READERS** 

With Early Release ebooks, you get books in their earliest form —the author’s raw and unedited content as they write—so you can take advantage of these technologies long before the official release of these titles. 

This will be the 2nd chapter of the final book. Please note that the GitHub repo will be made active later on. 

If you have comments about how we might improve the content and/or examples in this book, or if you notice missing material within this chapter, please reach out to the editor at . _shunter@oreilly.com_ 

The following chapters dive into five different dimensions of code reading: structure, domain, concepts, context, and collaboration. 

I have often seen unfamiliar code and got deterred from reading on after seeing a few lines of code that did not make any sense to me, even in programming languages I was quite 

comfortable with. There are different reasons that code can be hard to read. For example the code can contain _code smells_ like long methods, or methods with confusing or contradicting names. In other cases, code can be organized well, but hard to read because you yourself lack knowledge. A code base filled with domain concepts that you are unfamiliar with, or algorithms and data structures that you do not know will be hard to grok, even if it is written and documented perfectly. 

But sometimes the confusion lies in the fact that the code is connected in ways that you do not yet know. When you are new to a code base, you are still learning what methods call which other methods, what parameters play a role in similar parts of the code base and how important domain concepts are represented in the code. This chapter focuses on that part of confusion about code: the lack of knowledge of how the various code elements relate to each other. Stop scrolling around in the code base in the hopes of finding understanding, or reading docs that do not yet have meaning, but instead expand your structural knowledge using focused exercises. 

The exercises and techniques in this chapter help to answer questions like: Is the code organized in methods and classes? What methods and classes depend on each other? What is the 

‘flow’ of the code? Are there clear _entry points_ such as a main method where the code execution will start? 

At the end of the chapter, you will know X techniques to be applied to more deeply understand code structure of a new code base. 

## Background & Running example 

Let’s study this small code snippet from the Hedy code base. When this code is unfamiliar to you, it will be tempting to dive into all the details. What is a syntax tree? What does it mean for it to be complete, and what is a lookup table, and what are its entries? 

However, these small details are likely to overwhelm your _working memory_ . Your working memory acts a bit like the processor of your brain, it processes information when you read it. Research tells us that your working memory is really small, it only has about 2 to 6 “spots” to store information in! When you have only a little bit of prior knowledge, each line of code, or even each individual element might take up one spot, but if you know a lot about the code base, each method might hold a spot, causing you to be able to process a lot more. This . process is called _chunking_ 

As an illustration of the idea of chunking, imagine that you have to remember the numbers 1934 5023 7544 1846 and also 

1918 1945 1990 2003. Most likely the second number set is a lot easier to understand since you can remember it using prior knowledge: First World War, Second World War, First Gulf War, Second Gulf War. Those four chunks make the second example easy to process, but lacking such chunks the first string of numbers will be impossible to remember or reason with. 

This example underlines why it is so important to first gain some deeper understanding of the concepts and their relationships: without solid prior knowledge of the structure of the code, it will be harder than necessary to read unfamiliar code. 

## Structural components 

Now that you understand why it is important to understand the structure of code, you can start examining a number of techniques to gain this understanding. One of the first techniques to apply when reading unfamiliar code is to understand its division into components; this includes classes and methods in an Object-oriented project, or functional components in a more functional style program. It is tempting to start to read individual lines of code when you examine unfamiliar code for the first time, but as explained above, 

focusing on small details can be confusing and also feel overwhelming. Starting your analysis with the structural components instead provides a high level view that will aid in your more detailed line-by-line read later. 

## **Objects and functions** 

Generally, code contains three types of structural components: 

1. Firstly there are **object components** , which are used to create meaningful abstractions. Examples of object components in code are user-created datatypes, structs or classes. 

2. There are also **functional components** in which execution is grouped, like methods or functions. 

3. Finally code can contain **singular components** that are variables or constants not contained in either objects or functional components. 

These three components appear in different forms in different programming languages, and not all languages support all three objects. For example, objects are, of course, commonly present in object-oriented languages, but these languages traditionally do not allow for variables to be defined outside of classes and 

thus do not have variables or constants living outside of object or functional components. 

Functional components on the other hand are, of course, the core component used in functional languages. In objectoriented languages, functional components take the form of methods within classes. 

Singular components are not possible in most pure OO languages like Java or C#, components that are not objects must live within classes and as such there are no singular variables outside classes. Inside classes they take the form of fields. In functional languages variables may always be declared, inside or outside functions. 

Nowadays, many languages allow for multiple paradigms including functional and object-oriented, for example Python or JavaScript. In these languages all three components can (and will often) be present. 

## **IDE support for structural reading** 

Many Interactive Development Environments support a code folding or collapse feature, which helps to manage the complexity in reading by showing only a summarized view of 

functions, methods or loops, rather than their implementations. For a method/function or class, the minimized view will show the definition, including parameters for method/functions, and including inheritance information for classes. For loops, typically the line containing the loop code (for, while, forEach) is shown in full, while the loop’s body is hidden. 

In most cases, code folding will be done with a little minus in the _gutter_ , the side bar typically placed next to code also - 1. containing line numbers, as shown in Figure 1 

Figure 1-1. PyCharm showing a for loop which can be folded with the minus symbol. 

This is a great way to view the components without getting overwhelmed by the details. This view however makes it harder to see how big the individual components are, which can limit your insights into the code base, because size can be a useful indicator of priority. Larger functions tend to play a bigger role in a code base than smaller ones. You can work - around this limitation by looking at the line numbers. Figure 1 2 shows, for example, a constant assignment starting on line 86 

of 12 lines, and a method definition on line 99 containing 52 lines. 

Figure 1-2. : PyCharm showing a folded view on a piece of code. Line numbers can be used to determine size. 

While it might seem surprising, reading code in this folded fashion can already help you to gain initial understanding. For example, the folded view will show you which components are there, what their types are, how many components there are of the different types, and how their sizes compare to each other. 

## **Example 1-1. Exercise** 

Choose a project from GitHub that you do not know. Review only the components. What objects components (classes or structs) does this code snippet contain? What functional components does the code have (methods or functions)? How big are the components? Do they look balanced in size? Are there any large or small ones that catch your attention? And what singular components (variables, constants) does the code contain? 

## Fill out the table below to guide your reading: 

|Object components||
|---|---|
|Component name|Lines of Code<br>Size (small/medium/large)|
|_ParseTree_|_267_<br>_Large_|
|_Variable_|_53_<br>_Small_|
|Functional components||
|Method/function name|Lines of Code<br>Size (small/medium/large)|
|_parse()_|_121_<br>_Large_|
|_execute()_|_53_<br>_Medium_|
|_checht_parse_tree()_||
|Singular components||
|Variable name||
|_base_url_||
|_user_key_||



## Relationships between components 

Now that the core three components of the code have been identified, it is important to understand the relationship between them. Again, it can be tempting to start to read the code to investigate its functionality in detail, but there is a lot 

still to be learned from how the components relate without even looking at the functionality of the code. Chapter X outlines a number of techniques to examine details of the code. 

An important part of the structural dimension of code is not only the components but also the way they are connected to each other. To understand why the relationships in code are important, you need to understand a bit more about how people process new information in general. When understanding new information, your brain always tries to relate new information to things you already know or understand. As such, your brain forms a _mental model_ of the information that you can use to reason about the new information. Explicitly making connections between information visible will support your brain in easier understanding. 

When you read very unfamiliar code, you have no model of the code in your long-term memory. Simply scrolling through the code will give your brain some nuggets of new information, but it will not directly help to form a mental model. Making the relationships explicit and storing them in a table or graphs supports your memory in quickly processing new insights about the code 

When reading unfamiliar code, and sometimes even when reading familiar code, it can be hard to get a good overview of all the dependencies in the code base. Often, when bugs occur in code, an overlooked dependency is the cause, for example when a method is not called which should have been. So, for a deeper level of understanding code, understanding the connections within the code is an important first step. It will help you form a mental model of the code and as such, strengthen your prior knowledge and thus make it easier to reason about the code. 

Let’s dive into the types of relationships that code can contain, since three different types of components can relate to each - other in different ways. Table 1 1 presents an overview of the different relationships. 

Firstly, when object components are classes, two components can relate to other classes with inheritance in object oriented languages. For example, because one class inherits from another class, but also when both classes inherit from a similar base class. Classes can also contain functional components as methods and classes. 

In some languages functional components can use objects as parameters, and functions can call static methods defined on 

classes. Furthermore functional components can call each other creating a dependency between two functional components in both object-oriented and functional languages. In objectoriented languages methods can also be related because one method overrides the other one. Singular components can be used inside the body of functional components. 

Singular components do not depend on the other two object types. 

Table 1-1. Different ways in which components can relate to each other 

||Object Component|Functional Component<br>Singular Component|
|---|---|---|
|**Object**|Inherits from|Contains as<br>Contains as|
|**Component**|(OO)|method (OO)<br>feld (OO)|
|**Functional**|Uses are|Calls (OO, FP)<br>Used in body|
|**Component**|parameter (OO,|Overrides (OO)|
||FP)||
||Calls on static||
||method (OO)||
|**Singular**|-|-<br>-|
|**Component**|||



## **IDE support for dependency analysis** 

The IDE can help you to determine relationships between components in different ways. 

A simple and quick way to understand dependencies in a code base is using **search functionality** . While you will probably use search functionalities all the time when writing and debugging code, you can use the IDE in a slightly different way when specifically looking to find relationships, by searching when the code is **folded** . 

When you search for names of constants, variables or methods when the code is folded, results will be highlighted in the folded code blocks. This gives a quick overview of usage of constants and variables, or the calling of methods. For example, suppose you want to know what methods use the PREFIX_CODE - constant defined in the code snippet above. See Figure 1 3 for the results that appear when searching the code for the string PREFIX_CODE in the search bar. 

Figure 1-3. PyCharm indicates the presence of PREFIX_CODE in the parse method with yellow marking. In contrast, transpile_add_stats() does not contain PREFIX_CODE. 

This view can immediately help you find the specific dependency of object or functional components on singular - objects (in Figure 1 3 on the singular object PREFIX_CODE). 

Of course, string matching is limited. In fact, the full code base - from Figure 1 3 has a second constant called 

TURTLE_PREFIX_CODE that would also be found with a search for PREFIX_CODE in other places in the code (which are not shown in the figure). 

A second, more powerful method to examine structure is to use **dependency features** in the IDE to list dependencies explicitly. In many IDEs, right clicking a constant, variable or method will - 4. reveal the option to list all usages, as shown in Figure 1 

Figure 1-4. Find Usages feature shown in PyCharm. 

The list of usages which the IDE now shows will also be the usages of PREFIX_CODE in functions and objects. 

In most IDEs, find usages-features do not just find dependencies on variables, they can also detect other relationships including class inheritance and function calls. However, often IDEs do not clearly distinguish between different types of relationships. For - example, Figure 1 5 shows the result of finding dependencies for a class called ConvertToPython. You can see an inheritance relationship (line 1186) as well as a call to a static method (lines 1359 and 1479). 

Figure 1-5. Output of the Find Usages-feature shown in PyCharm. Inheritance relationship on line 1186 is interspersed with calls to a static method on lines 1359 and 1479. 

## **Example 1-2. Exercise** 

Write the names of each component you identified in - Example 1 1 in row 1 and column 1 of a new chart and indicate their types with a letter for brevity (O for object, F for function, S for singual) 

Now fill the table with the relationships types between the components. As explained earlier in the chapter, you can do this 

with search or dependency analysis features in the IDE. Note that for some dependencies, you can use but not fully rely on find usages-features and you will have to manually inspect the positions that the IDE returns. 

|Component|_Parser (O)_|_parse (F)_|_execute (F)_<br>_URL (O)_|
|---|---|---|---|
|_Parser (O)_||_contains_|_contains_|
|_parse (F)_||||
|_execute (F)_||_calls_|_uses in body_|
|_URL (O)_||||



## **Manual inspection** 

While IDEs can help illuminate dependencies, doing this analysis manually by reading the entire code snippet from the top to the bottom can also be very useful, because you are then building a more complete model of the code and you might find relationships which the IDE misses. 

For example, sometimes there are informal relationships between code components, like a comment in one class saying something like “this class is similar to class X and we should consider merging them”. This is not a formal relationship between classes like inheritance but does give us more depth in understanding the code. When you are building a mental model 

of the code in a manual way, using a table like the one in - Example 1 2 or a graph is inevitable, because without some external help it will be very hard to keep track of what dependencies you have already analyzed. 

Another more informal type of relationship that can exist between components and requires some manual inspection are the relationships that can occur at the parameter level. Functional components can be connected when they use the same parameters frequently, which Fowler calls a Data Clump. Even if functions are not formally connected by being grouped in a class, they can still be similar because they operate on the same type of objects. For example, when your code base contains a Canvas object that you write information to, multiple classes can have methods that use that Canvas as a parameter without calling each other. While these methods lack a formal connection, they do have a relationship, one that is hard to determine without manual inspection of the method declarations. 

## **Example 1-3. Exercise** 

Examine the parameters of the functions of methods in your - - code base from Example 1 1. If you have done Example 1 2 you can simply copy all function lines. Now list the parameters that 

occur in these functions as column headers and mark cells with an X when a function uses a certain parameter. 

|Component|_program_textskulpt_|_program_textskulpt_|_URL_<br>_…_|
|---|---|---|---|
|_parse (F)_|_X_|||
|_execute (F)_|_X_|_X_|_X_|



This analysis might help you find patterns of methods that are linked because they work on the same parameters, and thus will share a number of Xs in a column. 

You might want to note some of these parameter connections in - the table of Example 1 2, especially if there is a strong overlap in parameters and a similarity between functionality. 

Finally, when you are doing any kind of analysis manually, it can be tempting to dive deep into the code, but it is better in this phase to try to limit yourself to finding the dependencies. Later chapters cover other exercises looking at names, code quality, and other aspects of the code. 

## **Exploring the connections** 

Once you have investigated the dependency table of a piece of code, you might start to notice patterns. Some code bases might have a linear dependency path, starting at a clear starting point, 

like a main method, which in turn calls one other method, which calls another one etc. 

Other codebases might have different patterns, including recursive calls, or methods that branch out into several different methods whose results are combined. Once you have identified the patterns for a new codebase, decide if the patterns match your expectations. Is this pattern what you had expected? Are there methods that are very heavily connected? Or, are there functions or methods that are not connected to others? Investigating those in detail can be very useful to build strong mental models of the code base. 

## Entry points 

Now that you have gained some initial understanding of the different components and their relationships to each other, it is time to make a plan for reading the code. You’ll do that firstly by locating an **entry point.** An entry point is a point where you will start reading. 

There are many different ways in which you can read code, which I discuss later in this book, in Part Z. For now, let’sl focus on reading by following the execution flow of the code. 

## **Finding entry points** 

While it is not always clear where unfamiliar code starts, often, you can guess a few places in the code where you expect the execution to start, like a main() method in a C like language, code guarded by an if __name__ == “__main__”: in Python, or a method related to the /index route in a web application. Finding generic entry points can be done with text search, if you have a good guess that the methods might be called main or if you know what route to look for. 

However, sometimes you will lack a good guess of where the execution starts. In such a case, you can use a table like the one - you constructed in Example 1 2 to help find another entry point. First, ignore the object and singular components and just focus on the rows and columns of functional components. Now look at the functional components that have an empty or almost empty column, and also have a full row. These are functional components that are not, or hardly called but do call a lot of other functions and as such can be interesting places to start an exploration. 

Teresa Busjahn, a researcher at Freie Universität Berlin, led a **1** study involving 14 novice programmers and 6 experts ~~. S~~ he and her colleagues wanted to know whether the two groups read code differently from one another. 

They learned that novices read more linearly and follow the call stack more frequently than expert programmers. Learning to follow the call stack while reading code, apparently, is a practice that comes with experience. 

So when reading code that is entirely unfamiliar to you, you might feel the need to start at the top just to see what the code contains since you are in a sense a beginner in the code base. Forcing yourself to follow the execution of the code by starting at a generic entry point and working from there might be more insightful. 

## **Reading from the entry point** 

Now that you have identified an entry point, you can start to build a mental model of the remainder of the code. You can again use the IDE to help you understand code dependencies by placing a breakpoint on the entry point and stepping into each dependent code block examining the **slice** of code that you are 

interested in. A slice is a part of the code that relates to a certain function or variable and is exactly that part of the code that this variable is used in or that this function leads into. 

If you want to step through a slice of code, in most IDEs you can place a breakpoint such that the code will stop when the execution reaches the breakpoint. You can do so by clicking in the gutter next to the code, which will create a breakpoint indicated by a red dot as shown in Figure 1-6. 

Figure 1-6. Find Usages feature shown in PyCharm. 

Once you have placed the breakpoint, you can follow the execution path using the IDE to step into each of the called functions. Again, your instincts might be to dive into each method in detail and read all the inner workings. But at this level of reading, the concrete goal is to scratch the surface of the code and not go too much deeper, so as not to tax your working memory. Don’t worry, that phase will come later! 

A good strategy at this point is to try to contextualize the relationships that you have, summarizing the why of the 

## relationship in one or two sentences. 

## **Example 1-4. Exercise** 

Follow the call stack of your chosen entry point and read from there. Fill the table with the relationship types between the functions. Describe the role of the dependency in one or two sentences. 

|sentences.|||
|---|---|---|
|Component|_parse (F)_|_execute (F)_<br>_validate_tree(F)_|
|_parse (F)_||_calls the_|
|||_validate_tree()n_|
|||_function to_|
|||_determine if the_|
|||_parse tree can_|
|||_be processed_|
|_execute (F)_|_calls the parse()_||
||_function to obtain_||
||_the transpiled code_||
||_which then can be_||
||_executed_||
|_validate_tree(F)_|||



You can find the dependencies manually or using the IDE. While using the IDE can feel easier, stepping through the code 

can be useful but is also likely to be overwhelming. If the IDE will step into a piece of code that is located far away from the current line, you will have to reorient yourself in the codebase again, and you will easily lose track. This is especially true if there are pieces of code in which multiple execution paths come together, like when a function gathers information from several other methods and combines them. For example, the function print_ask_args below first checks the variables in all arguments (and throws if that is not possible) and then transforms each of the arguments in the next line. 

```
def print_ask_args(self, args):
   args = self.check_var_usage(args)
   transformed_args = [self.process_variable_for_
return ''.join(transformed_args)
```

: 

In such complex cases, manual reading aided by search might be less demanding and thus more effective than “hopping” through the code using the IDE using breakpoints.. 

In addition to making notes in a dependency table (see - Example 1 3), visualizations as Unified Modeling Language - (UML) class diagrams like the one in Figure 1 7 can help 

support this type of code reading as well. In a class diagram we described the classes in a system as boxes containing their - fields and methods. For example in Figure 1 7, Client, Receiver, Invoker, Command and ConcreteCommand are classes and execute() is a method of Command and ConcreteCommand. 

Figure 1-7. [[placeholder]] 

If you are looking for specific information, it is especially important to keep an eye on your reading plan and determine if what you are reading is helping you to answer concrete questions about the code. 

## **VISUALIZATION TOOLS** 

You might be wondering why I ask you to draw a visualization by hand and not use one of the existing tools for that like **2** ~~e .~~ Umbrello or the built-in support in Visual Studio Cod 

There are two reasons for that. Firstly, visualization tools will show you the whole system, even if you are only interested in one slice of the program. Therefore a generated visualization is likely to overwhelm your working memory and discourage you from understanding the system. 

Secondly, researc ~~h~~ **3** has shown that simply viewing a visualization is not so useful. In a study comparing groups of students using visualization tools, the group just looking at the visualizations did not show signifcant learning advantages over students who used other learning materials. Studies however showed that when you are actively engaging with the visualizations, it can be useful! 

Thus, you will first want to sketch your view of the system, formulating your own clear questions and then only look at the output of a tool in order to help you answer your specific questions. 

## **Different kinds of entry points** 

Your prior knowledge of a code base will impact what entry point to use, as well as the activities you are performing. For example, when you are looking at a codebase that is quite unfamiliar to you, starting at a generic entry point like a main method can be helpful because it helps you build a mental model of what happens in the code in the order that it will happen at runtime too. 

But in a more familiar code base, it is more likely that you will start with a context-specific entry point, and which type depends on the activity. For example, while debugging, a failing test will be a natural entry point to start your reading process from. Later in this book, in chapter X we will dive into the process of code reading when debugging is depth. While optimizing, a line flagged by the profiler is a good place to start. Later chapters of this book, particularly in Part 2, will dive into different types of reading scenarios with different types of entry points. 

After the read 

During the structural examination described in this chapter, you have gathered a lot of relevant information about the structure of the code. In many cases, you might want to commit some of the information you gather back into the code base. This information might help you if you decide to explore the code in more depth, for example using exercises later in this book, but it might also help newcomers after you find their way in the code base. In this section we outline some ways in which the gathered information can be useful. 

## **Expand documentation** 

Firstly, some of the information that you have gathered can be useful as documentation for the project. A list of all components in the project can be helpful, maybe not in the full version with the three types and just limited to the core components. The - - results of Example 1 1 and Example 1 2 can serve as good starting points for written documentation. 

## **Improve comments** 

Some information that you have found while reading can also be committed to the source code itself. The brief text snippets - resulting from Example 1 3 could, if this information was not yet present in the code, be placed right before a method call. 

## **Discuss code quality** 

Sometimes while examining the code from a structural perspective, you will find parts of the code that have code smells, specifically structural code smells. Here are some to look out for. 

## **NOTE** 

## **Code smells are generally separated into two categories: structural and linguistic** 

Structural code smells are the code smells that come from Fowler’s original book, and refer to the way code is organized. Examples of such smells are **Message chains** in which methods call other methods, which in turn call other methods etc, **long parameter lists** or **large classes** . 

The other type of code smells are linguistic code smells as defined by Venera Arnaoudova. Linguistic code smells refer to names of variables or classes that do not aptly describe what they do. That can be vague names such as “fetch” or names that omit part of the functionality, such as a conversion method that converts but also stores information about the conversion in the database. 

**Size.** Looking at the sizes of objects alone can already reveal bloated classes, data classes or very small classes. The analysis - of size you performed in Example 1 1 can point you to this particular code smell. 

These findings can serve as a great conversation starter with your team to talk about code history and code quality. Here are some questions to consider based on this analysis: 

- Is there a reason these classes are large, small or only contain data? 

- Is this a historical reason or is there a good justification for the size of the classes? 

**Smells in relationships.** Other code smells pertaining to object components are inappropriate intimacy and feature envy, which both point to two or more classes that have too much interaction to be useful. You can detect these code smells by - looking at the table that you created in Example 1 2 and examining if there exists a number of classes that often work on each other’s fields (inappropriate intimacy) or one that very often class fields or classes of another (feature envy). Again, there might be good reasons for this design, but it is something to discuss, for example: 

- Do we understand why these classes are intimately related? Are there alternative ways in which the classes could be organized? 

**Smells in functional components.** The smells above 

concerned object components, but there are also code smells of functional components that can be found with structural - analysis. For example, the results of Example 1 2 is a message chain. Start at an entry point in the table and follow the functional components it calls, and then the functional components that that component calls, etc. If you have to make a large number of “hops” in the table, that indicates the presence of a message chain. Now, message chains are not necessarily bad, however, if you find one you can discuss whether: 

Some of the methods on the path are so small they could be merged? 

There are specific scenarios in the code that call long chains that could be solved differently, for example with caching or early returns? 

Another smell which can be found with structural analysis is dead code. Are there any methods that are not called at all? These might represent dead code. Be sure to also examine alternative ways in which dead code might be used, such as calls from the test suite for example, or from other parts of the code base. This is especially relevant in multi-lingual code bases 

in which static source code analysis might not always find dependencies. 

## **Refactor** 

When you find code that has code smells using structural analysis, sometimes you will want to improve the code. If you decide to do a refactor, the analysis that you performed so far can also guide the refactorings. 

**Large class** If you find large classes in the size analysis, these classes could be split up. A relationship table like the one you - created in Example 1 2 can help you find groups of methods that call each other. If two or three subgroups exist in these methods, the large class could be split into those subgroups without causing too many dependencies between the new classes. 

**Small class** On the other hand, if you find small classes in your analysis, you might want to merge them into another class. The - 2 can relationship table like the one you created in Example 1 help you decide which class would be a good home for the small number of fields and methods in the small class. Ideally this would be a class with which this small class shares the most fields and methods. 

**Data class** For a data class (a class that has a lot of fields but no or hardly any methods) a similar analysis can be made; this class could be merged with a class that often accessed the fields of the data class. If there is no such class, maybe the code 

**Long parameter list** In some cases, you will find methods or functions with long parameter lists. These can be found in - Example 1 3 as lines with a lot of Xs. In the case of methods on a class, these long parameter lists might be shortened by moving some of the parameters to be fields on the class. In functions or methods, you might group some of the parameters into larger objects. For example, a function that has x, y and z as parameters might be refactored into a function that uses just the point data type, which then contains x, y and z fields. 

- **One call functions** In Example 1 3 you might have identified methods that are only called in one place. This is not necessarily a smell as defined by Fowler, however such 

organization might point to premature generalization where an abstraction is introduced that is not used (yet). While this might be worth it in some cases, it will also cause the editor to “hop” when reading and debugging, causing more cognitive load because your brain has to reorient itself. These methods might be inlined reducing that cognitive load, at the expense of 

making the method in which the method or function is inlined longer. 

**Dead code.** If you found dead code in examining the relationships in the code, you might want to remove that dead code when you have verified it is indeed no longer needed. 

## Summary 

Code can be read in different dimensions: structure, domain, concepts, context, and collaboration. This chapter explored the structural dimension and looked at how variables, functions and objects in code can relate to each other, and how that information can be used while reading code. The following chapter explores domain. 

- **1** See “Eye Movements in Code Reading: Relaxing the Linear Order” by Teresa Busjahn et al. (2015). 

- **2** See for example: https://medium.com/nerd-for-tech/how-to-generate-uml-diagramsfrom-your-existing-code-814d27bd1537. 

**3** 

https://www.sciencedirect.com/science/article/pii/S1045926X02902375&sa=D&source= docs&ust=1658912480042497&usg=AOvVaw3mvAJmKBMgrgVt4HM9Ez13 

## Chapter 2. Domain 

## **A NOTE FOR EARLY RELEASE READERS** 

With Early Release ebooks, you get books in their earliest form —the author’s raw and unedited content as they write—so you can take advantage of these technologies long before the official release of these titles. 

This will be the 3rd chapter of the final book. Please note that the GitHub repo will be made active later on. 

If you have comments about how we might improve the content and/or examples in this book, or if you notice missing material within this chapter, please reach out to the editor at . _shunter@oreilly.com_ 

The previous chapter examined relationships in code, without diving into the content of the code in depth. This chapter will do the reverse and examine the content of the code without looking at the way it is connected. Isolating these different parts of looking at code makes the tasks smaller and thus less scary and less cognitively demanding. 

More specifically, this chapter solely examines the domain concepts present in the code. With domain here we refer to the business domain or problem of the code. The programming domain will be covered in Chapter 4. Examining the domain concepts is useful because if you miss a thorough 

understanding of what words in the code mean precisely, it will be hard to understand the code as a whole. This relates to your long-term memory, as discussed in Chapter 2: if you do not have some prior understanding, remembering and analyzing code will be a lot harder than needed. 

Variable and method or function names can be great sources of information about the domain aspects of code, since they will very often contain words used in the domain. In his book Patterns of Enterprise Application Architecture, Martin Fowler describes a domain model as having two components: behavior **1** and data ~~.~~ Words that occur in variables often point to either data or behavior: verbs will often refer to behaviour, while nouns refer to objects. So in a sense, in this chapter you will be looking at objects and their functionality, but you will gather the information from names rather than from the structure of the code. 

The exercises and techniques in this chapter thus focus only on the domain aspects of code, helping you answer questions like: 

What are the central domain concepts in this code base and how do they relate to each other? 

At the end of the chapter, you will know X techniques to be applied to more deeply understand the domain of a codebase: 

List all variable names Identify different parts of variable names Look at name molds 

## Learning from variable names 

In the previous chapter, you folded all the code so you could focus on just the structural elements of the code. In this first technique to understand the code’s domain, you’ll do the reverse: you’ll just list all domain elements and disregard the remainder of the code including the structural components. Sadly though, IDEs do not typically contain a feature to list all the different identifier names used in a file or project, so you will have to use a bit of manual effort. 

To find all singular components you can still rely on folding the code, so let’s start there. If you fold all code, you can scroll through it and find the variables in the code at the top level with relative ease. Of course, variable names can also be 

contained within classes as fields. If you are working in a code base that has classes you will have to open the and find the names with some effort. 

## **Gathering domain insights from variable names** 

To explore all domain concepts, one method is to list all variables in use in a project or file. You can write the names down in a text file or markdown file, but it can also be a piece of paper. 

In this exercise you will want to fully focus on variable names. It will be very tempting to browse the code a bit more, and of course, there is nothing wrong with reading some code around the variables, but try to keep your eyes on the goal, and especially do not let yourself be discouraged by the code itself. 

Once you have listed all variable names, you can start to dive into the domain. Variable names often contain separate parts such as **quantifiers** , and **programming concepts** but also . **domain concepts** 

**Quantifiers** are parts of names that refer to quantities, like count, number_of, maximum, or filtered. 

**Programming concepts** can also occur within names, for example from a name like m_object, object can refer to a specific concept in a language. Other parts of names that refer to concepts are list, hash, table, string, or number. In this chapter, we will not yet focus on concepts, that is the topic of chapter 4. 

**Domain concepts** refer to the domain, like customer, import, parser, code, or language. Some parts of variable names point to concepts, often in the form of nouns, like customer or code, but they can also represent _domain behavior_ in the form of verbs like import, or parse. 

Using variable names, you can get an introductory sense of what concepts and behavior play a role in the code base. 

**Example 2-1. Exercise: List all variables in the codebase** 

For this exercise, simply list all variables in the codebase. In many cases the variable names will contain abbreviations or acronyms. If there are abbreviations or acronyms that are unfamiliar now, it is best to relieve that confusion at this point before diving into the code further and write down the full meaning in the second column. 

Variable name Extended 

_keywords_requiring_indentation imported_product r_id referred_id_ 

## **Exploring the domain from variable names** 

Once you have gathered all variable names in the file or module that you are currently investigating, it can be very useful to reflect on the concepts within the names, since names can reveal insights about the domain. While the precise formulation might differ from codebase to codebase, it is often the case that nouns reveal concepts within the domain, like parse tree, keyword, or account. Adjectives on the other hand can indicate _behaviour_ that can be executed on concepts, such as transpiled_code, indicating that transpiring is a thing you can do with code. 

**Example 2-2. Exercise: Reflect on terms within the names** 

- From the list of variables from Example 2 1, extract the separate words within the variable names, and divide them into nouns and verbs. For example, a variable name called keywords_requiring_indentation would be split up as shown below. 

||Domain<br>Domain|
|---|---|
|Variable name|noun(s)/concepts<br>verb(s)/behaviour|
|_keywords_requiring_indentationkeyword,_<br>_requiring_||
||_indentation_<br>_indentation_|
|_imported_product_|_product_<br>_importing_|



If you have access to domain experts (which is not always the case if you are reading code from an open source project), this is a good point to discuss the list of concepts. Great questions to ask are: 

- Are there any synonyms in the list of domain concepts that might not be obvious? 

Are there any central domain concepts or behaviours that this list misses? 

## Learning from function or method names 

Once you have formed an initial idea of the central domain concepts and behaviors based on variable names, you can follow the same steps to gather more information from the function or method names. 

## **Gathering domain insights from function names** 

As you will see in the next exercise, function names are often different from variable names. Functions tend to contain more generic words, especially verbs such as execute, read, load or create. However function names often also reveal domainspecific behaviour such as buying, selling, placing an order or favoriting an item. And function names are not limited to behaviour. Function names can also reveal domain concepts; for example, a function name such as check_program_size_is_valid tells us that there is such a thing as a size for programs that may or may not be valid. 

**Example 2-3. Exercise: List all functions/methods in the codebase** 

For this exercise, list all functions or methods in the codebase. Remember that many IDEs allow you to fold the code, allowing you to get an overview of all functions quickly. 

Function or method name 

_process_input_string() check_program_size_is_valid()_ 

_…_ 

As in the list of variables, be sure to explore the meaning of abbreviations or acronyms in the function names before diving deeper in the code. 

## **Mapping the domain from variable names** 

After you have gathered all function names, try to investigate what the parts of the names reveal about the domain in terms of both concepts and behaviour. You can take the information about size that you gathered in the previous chapter into account here also, focusing first on the larger methods and then on the smaller ones. 

**Example 2-4. Exercise: List all functions/methods in the codebase** 

- Similar to Example 2 2, extract the separate words within the variable names, and enter them into the columns for nouns (domain concepts) and verbs (domain behavior). 

||Domain|
|---|---|
|Function name|Domain noun(s)/concepts<br>verb(s)/behaviour|
|_process_input_string()_|_input string_<br>_process_|
|_check_program_size_is_valid()program size,_||



_valid_ 

## Expanding knowledge 

You have now looked at names occurring in both variables and functions or methods and gathered two domain categories from the names: concepts and behaviour. Before you summarize your findings, let’s focus on these two categories separately. The aim of the next step in reading is to try to define the concepts and behaviours as precisely as possible, based on your prior 

knowledge of code and domain, and, if possible, on documentation and knowledge of others. 

## **Gathering more knowledge about concepts** 

Let’s focus firstly on the concepts present in the code. Start with the list of concepts and decide if you can explain in your own words what the domain concepts mean. 

If you can’t, reading more of the code might not be the best next step. Instead, you might want to start by gathering more information about the concepts from other sources by asking teammates or other contributors or reading comments and documentation. 

It can be especially valuable to also investigate whether you suspect that synonyms are used in the code. While writing this exercise, I realized that in the Hedy code base we sometimes say _parse tree_ , but also use _tree_ in other places. While that might be very clear to the code team, using synonyms can be confusing for newcomers. And using synonyms can even impact experienced developers negatively, for example by hampering searchability, since looking for “parse tree” will not reveal locations of “tree” in the code. 

## **Example 2-5. Exercise** 

Examine the concepts that you have gathered from the names. Do you understand enough about the domain to describe the meaning of each concept? 

|Concept|Meaning<br>Potential synonym|
|---|---|
|_parse_tree_|_A tree resulting from the parsing of_<br>_a program_<br>_AST, tree,_<br>_parse_result_|



## **Gathering more knowledge about behaviour** 

Now that you have examined the concepts in detail, let’s look at the behaviour that you gathered in exercise X.X. Is it clear to you what all the behaviours mean and on what type of objects they can and cannot be performed? 

It can be especially valuable to dive into the precise meaning of generic-sounding behaviour like process, start, analyze or prune. Can you deduce a more precise meaning from the comments or the implementation? 

## **Example 2-6. Exercise** 

Examine the concepts that you have gathered from the names. Do you understand enough about the domain to describe the meaning of each operation and to understand what data types or classes the operations can be applied to? 

|Operation<br>Meaning<br>Data type|
|---|
|_check_is_validIs the program valid: meaning_<br>_whether it is smaller than 100 lines_<br>program|



## **Combining domain concepts and behaviour** 

While this chapter has treated domain concepts and domain behaviour as entirely separate things, they are, of course, very related! Concepts like customer are the subject of behaviours, including generic ones like create, delete or update, and domain-specific ones like open account or mark fraudulent. 

Depending on the programming language you are using, these connections can be made explicit in the structure of code, such 

as with a class customer having a method open_account(), but in other cases, these connections rely more on naming. Despite the language of the codebase and its use of OO, there is a lot to be learned about concepts and behaviour from names. 

Now that you have gathered the concepts and behaviour in the code and reflected on their meaning, the final step is combining them. What verbs are used together with concepts, and what nouns are used in function names? 

## **Example 2-7. Exercise** 

Combine the list of concepts with that of behaviour. Which ones belong together? 

> Concept -> _program tree_ Operation _check if validx process x_ 

## **Enrich domain understanding** 

Once you have investigated the code and made an effort to understand the domain concepts from the code itself, it can be very valuable to enrich your knowledge in two ways. 

Firstly, you can direct your attention outside of the codebase. Depending on your context, this might be a deep dive into the documentation trying to obtain more information about the concepts that you have found in an open source project, or a session with an experienced colleague within a company. In both cases, you are looking to gather more depth in your understanding of the concepts that you have just learned about. A great exercise is to double check your findings from - - Example 2 6a and Example 2 6b. Can you verify that the - meaning and synonyms from Example 2 6a are correct, and - that the datatype from Example 2 6b are correct? 

Secondly, after expanding your knowledge of all domain concepts with information outside of the code base, a second way to deepen understanding is to reread the code. Now is a great moment to let go of the small focus on the names in the code, and read the code as a whole again. Because your knowledge is now expanded, you will certainly pick up on new things in the code that did not occur to you before. 

## After the read 

During the domain examination described in this chapter, you have again gathered a lot of relevant information about the code, this time about its domain concepts and domain behaviour. As with the structural information from chapter 2, you have probably gathered some information you might want to commit back to the code base, either to help future 

newcomers understand the code better, or to guide your own reading process when diving deeper with exercises later in this book. Here are some ways in which this information can be useful. 

## **Expand documentation** 

Some of the information about domain concepts and behaviour can serve as excellent documentation to add to a readme file. In particular, you have explored a lot of important concepts in the code, and these might not live somewhere in a documentation file yet. In a sense, you might have been starting to document the Ubiquitous Language of the project. 

## **NOTE** 

## **Ubiquitous Language** 

Eric Evans coined the term **Ubiquitous Language** in his Domain Driven Design book. With the ubiquitous language, Evan denotes a language that developers and users of software systems share. Often this language only partially emerges naturally and parts of it will need to be deliberately designed. Evans states that the Ubiquitous Language should be based on the Domain Model used in the software since natural language concepts tend to be imprecise. 

The information that you have gathered so far could be converted into documentation. The lists of concepts that you - - created in Example 2 6a and Example 2 6b can serve as starting points for a list of domain concepts. From there, you can expand, for example by: 

- Ensuring that all abbreviations or acronyms in variable or function names are either replaced by full words, or if people prefer keeping them, documented 

- Describing domain objects that felt similar to you but turned out to be different. If they are not exactly the same but there are reasons that they look similar, such as similar names or similar behaviour, other people might be confused too. Documenting how these concepts differ subtly can be very useful 

- Discussing these lists with users. Do they recognize and understand all concepts? What concepts are missing and are they maybe missing or represented in other ways? If you work a context where DDD is practiced and a Ubiquitous Language is used, you can check whether the list of your concepts is similar to the documentation of the Ubiquitous Language that already exists. 

Furthermore, you will likely find some names that do not exactly describe the functionality of code, such as analyze(), convert(), or process(). While reading the code, you might have found a deeper understanding of those words, based on examining the call trace of the function, variable names in the function or comments. You might be able to commit to the documentation, specifically the docstrings of these functions to aid future readers. 

## **Discuss code quality** 

While examining the code from the domain perspective, you might find parts of the code that have code smells, specifically linguistic code smells, which are code smells relating to the naming of objects, functions, methods or variables. Your domain findings can serve as a great conversation starter with your team to talk about naming quality. 

**Similar objects.** Your domain analysis might point to objects that seem very similar. Apart from documenting the differences, as explained above, you might also want to dive deeper into the reasons that the code is like it is, for example by discussing: 

- Are these domain concepts truly synonyms or are they different, and if so, how? 

- Are there historical reasons for the similarities? Sometimes when a new product or process is introduced, it comes with its own objects since the author might not be aware of places in the code where it could fit. 

**Linguistic code smells.** Chapter 2 discussed two different code smells.: structural smells as described by Fowler, and linguistic code smells as defined by Arnaoudova. Since this chapter focuses on domain concepts, it makes sense to evaluate the quality of the names in terms of smells. You can focus on specific types of linguistic smells, which Arnaudova 

distinguished between in her work, three for functions/methods and three for identifiers. 

- Methods that do more than they say 

- Methods that say more than they do 

- Methods that do the opposite of what they say 

- Identifiers whose names say that they contain more than what the entity contains 

- Identifiers whose names say that they contain less than 

what the entity contains 

- Identifiers whose names say the opposite of what the entity contains 

Identifying these code smells is most easily done by starting - - with the tables you made for Example 2 1 and Example 2 3 and comparing the two sources where you can learn about types. Firstly, the types you can gather from the names (such as find_id, which indicates an id, maybe a string or integer will be returned) versus the names the function definitions define (such as int find_id()). Of course this will be a lot different in - static languages versus in dynamic ones. Example 2 8 can help you to compare these two sources. 

**Example 2-8. Exercise: Examine types of identifiers and functions/methods** 

For this exercise, examine your lists of identifiers and function/methods in the codebase that you created in - - Example 2 1 and Example 2 3. For each of the identifiers and function/methods identify the type expected based on the name and the type determined by reading the code or gathering 

- information from other sources. If you have done Example 1 3 where you describe dependency between methods, that table might also support your understanding of the role and output value of methods. 

For now, try to focus on the output values of the code, for example by looking at the locations of the return keyword or the final lines. At this stage of code reading, you are specifically interested in the naming dimensions, not yet in deeper reading, to avoid overloading your working memory. 

||Type expected based on<br>Type gathered from|
|---|---|
|Identifier name|name<br>reading code|
|_keywords_requiring_indentation_||
|_imported_product_||



_…_ 

Function or method name 

_process_input_string_ 

_check_program_size_is_valid_ 

_…_ 

## **Check for linguistic smells automatically** 

Are you curious about whether your codebase suffers from linguistic antipatterns? Is your codebase written in Java? In that case you can evaluate smells automatically with the Linguistic 

Anti-Pattern Detector (LAPD) that Arnaoudova created based on her research. LAPD is available as an extension of Eclipse **2** ~~.~~ Checkstyle plugin 

**Name molds** . Name molds are patterns in which elements in a variable name are typically combined (see further breakout box) and form are a great dimension for examining code quality. Using many different name molds in a code base makes the code unnecessarily hard to read. If you want to examine the name molds in your code base, you have already done some - partial work in Example 2 2 where you listed the names and their word/domain parts. You can now expand this table in the next exercise to detect different molds. 

## **Example 2-9. Exercise: Examine name molds** 

Examine the names of the identifiers in the code base and determine the order in which the elements appear, as illustrated by the examples. I distinguish verbs, nouns, adjectives, and quantifiers here, but you might want to add your own categories where that makes sense, such as acronyms (EBIT) or filters (monthly, per customer). 

How many different orders of words can you find? It is also interesting to discuss patterns that arise. Are the orders or 

words similar locally or globally, i.e. does one method have a lot of one mold while another method uses a different one? 

|Variable name|Elements<br>Order|
|---|---|
|_keywords_requiring_indentationkeyword, requiring,_<br>_noun, verb,_||
||_indentation,_<br>_noun_|
|_imported_product_|_imported, product_<br>_adjective,_|
||_noun_|
|_minimum_distance_|_minimum, distance quantifer,_<br>_noun_|



## **NAME MOLDS** 

Name molds **3** are patterns in which elements in a variable name are typically combined. For example, when a name was needed for the maximal benefits someone can 

receive per month, you could choose max_benefit, or max_benefit_per_month, or max_benefit_num. Each of these contains the same domain concepts, but expressed in different ways. Feitelson ran an experiment with 47 developers which showed that the probability that two developers select the same name is low: the median probability in the study was only 7%! And diverse variable names put more strain on your working memory since you will have to search for the relevant parts in different places each time. 

## **Refactor** 

If you want to use the findings of this chapter to improve your code base, there are a number of refactorings that you can consider, partly also based on the quality issues from section 3.4.2. 

**Similar sounding objects.** In some cases, similar sounding objects may warrant a code change. Here are a couple questions to ask: 

- If they are genuinely different, can you rename one to minimize overlap and confusion? 

- If they are the same, can they be merged into one object sharing some of the similarities? 

**Vague-sounding names.** You will likely find some names that do not exactly describe the functionality of code, such as analyze, convert. What could be a more precise name for vague names like process()? 

**Smelly names.** If you identified names which do not fully 

- match their implementation in Example 2 8, you might want to rename the method or identifiers to be more precise. You may also want to discuss their implementation with someone more familiar with the code base, to determine why the name does 

not match the implementation. In some cases a change to the implementation might be better than a change to the name. For example, when you have a method called return name_and_id which only returns an id, which is then used in several places to later fetch a name, it might be better to actually return the name and the id and refactor the code to centralize fetching the name. 

## Summary 

Code can be read in different dimensions: structure, domain, concepts, context, and collaboration. This chapter explored the domain dimension and looked at how variables, functions and objects are named, what you can learn from the names and how names can be used to understand and improve code quality. The following chapter explores programming concepts. 

- **1** https://martinfowler.com/books/eaa.html 

- **2** http://www.veneraarnaoudova.ca/linguistic-anti-pattern-detector-lapd/ 

- **3** Dror G. Fietelson et al., “How Developers Choose Names” 

## About the Author 

**Felienne Hermans** is associate professor at Leiden Institute of Advanced Computer Science at Leiden University, where she heads the PERL research group, focused on programming education. She also works at the Vrije Universiteit Amsterdam, where she teaches prospective computer science teachers. 

Felienne is the creator of the Hedy programming language, and was one of the founders of the Joy of Coding conference. Since 2016, she has been a host at SE radio, one of the most popular software engineering podcasts on the web. Felienne is the author of _The Programmer’s Brain_ (Manning 2021) which helps programmers understand how their brains work and how to use it more effectively. In 2021, Felienne was awarded the Dutch Prize for ICT research. 

Felienne is a member of the board of I&I, the Dutch association of high-school computer science teachers, and of TC39, the committee that designs JavaScript. 

This file was downloaded from Z-Library project 

_Your gateway to knowledge and culture. Accessible for everyone._ 

z-library.sk z-lib.gs z-lib.fm go-to-library.sk 

Ofcial Telegram channel 

- Z Access 

- https://wikipedia.org/wiki/Z Library 

