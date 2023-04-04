## how the  C++ LInker work

hey little guys my name is Deshawn oh and today we're going to talk about Linker.
so what is Linker? 
what does the cpp Linker actually do. 
Linker is a process（过程) that we go through when we go from our source  cpp  files to our actual executable binary.
So the first stage(阶段) is actually compiling our source files and I actually made an entire video on that so go check that out link in the description below
Once(一旦) we've compiled our files we need to go through(通过) a process called  linking .
now the primary focus of linking is to find where each symbol and function is, and link them together.
Remember each file is compiled into a separate(单独) object file as a translation unit and they have no relation to each other those files can't actually interact so if we decide to split our program across multiple C++ files which is of course very common we need a way to actually link those files together into one program and that is the primary purpose of what the linker does even if you don't have functions in external files like for example you've

00:55

written your entire program in one file the application still needs to know where the entry point is so in other words where the main function is so that when you actually run your application the C runtime library can say hey here's the main function I'm going to jump there and start executing code from there and that is effectively what starts with your application so it still needs to link the main function and everything like that even if you don't have all the files the best way to explain this is by showing some examples

01:18

so let's jump over and take a look so here in Visual Studio we've got a very simple project that just contains one source file master tbp and inside there we have two functions log and multiply the multiply function actually calls the log function prints out the word multiply to the console and then returns a times B pretty simple stuff however this isn't an actual application since of course it doesn't contain a main function the first thing that you have to realize is that there are those two

01:42

stages of compilation right there's compiling and there's linking and there's actually a way that you can differentiate between the two individual studio if you press ctrl f7 or if you press the compile button only compilation will happen no linking will ever happen however if you build your project or if you hit f5 to run your project it will actually compile and then link so if I just hit ctrl f7 you'll see that I actually get no errors everything's fine because the compilation was successful

02:09

it generated that math dot obj file the object file and everything's great however if I right-click on my project and hit build you'll see that I actually get a linking error entry-point must be defined and again that's because I'm missing my entry point my main function so because our compilation is divided into those two stages compiling and linking we actually get different types of error messages associated with each stage if I make a syntax error for example which of course is something the

02:35

compiler has to deal with if I compile my code you'll see that it tells me that I actually get an error which is called c2 143 and then it says syntax error of course so this is the error code for this type of error and you'll notice that it actually starts with the letter C this tells us that it's an error that occurred in the compiling stage if I fix that and then build my entire project you'll see the error code listed here begins with the letters Ln K which of course stamps a link and it even tells

03:02

us over here that this happened during the link stage it's really important that you know what kind of error you get whether it's a compiling error or a linking error because of course you need to know that so that you can fix it properly so in this case we get an error which tells us the entry point must be defined again that is because we are compiling this as an application if we go to our properties and we take a look at what configuration type we have set here you'll see it is data application

03:27

or exe and every exe file has to have some kind of entry point if we go over here into the linker settings and into advanced you'll actually see that we can specify a custom entry point the entry point doesn't have to be the main function there just has to be an entry point now normally it is the main function and for pretty much anything you do it probably will be the main function but just so you know entry point doesn't necessarily have to be a function called main it can be really anything so if we back out of here and

03:56

actually write that main function I'll just write int main and then I'll build my project again you'll see that we no longer get that linking error and that we were successfully able to generate that exe file all right so now that we've established that let's go ahead and print out the value of that multiply function so we'll multiply 5 and 8 together so what we should see is this message being logged and then the value 40 being printed let's also add a CNCs so that our console doesn't close immediately

04:30

then I'll just click on this local windows debugger button to run this and you can see we get multiplied and 40 so our application seems to be running correctly great now suppose I had these in multiple files for example this log doesn't really need to be in this mass file because of course this just logs the message so why don't I have a separate file that actually contains all of my logging related functions I'm going to right click on source files and add a new C++ file called lock they'll

04:57

typically and then I'll click Add I'm going to grab that log function from here and move it into my log Delta VP file if I go back to master CBP and try and compile this code I'll get an error and you'll know that this is a compile error because the error code begins with let us see telling me the log is not found because this file has no knowledge that a function called log exists at all so we'll go ahead and grab this first line of the log function which is the signature and we'll add this so that we

05:23

have a declaration of the log function in this map dot CPP file no ctrl f7 and you can see it as compiling worked now let's go ahead and build our entire project we get several errors here compile errors telling us the CR is not found because we need to actually include iostream once we've done that let's build our entire project alright great it seemed to work successfully now let's take a look at one type of linking error that we might get this one called unresolved external symbol and this is what happens when the

05:52

linker can't find something that it needs so we'll go back over here and in the log file I'm going to change this to say something else for example I'm just going to add an R here so that we say logger if I go back to master CPP I still left my declaration as log so it still does expect the function to be called log so this file will still compile of course because this does no linking so all it's doing is checking to make sure everything here compiled correctly it believes that there is a

06:20

log function somewhere but it's going to be the job of the linking stage to actually find that log function so if I build my entire project now you'll see we actually get an error this is a linking error because if you can see that it begins with the LNK letters and the RS as unresolved external symbol now he tells us exactly what symbol is missing it's that log function it even tells us where we reference it that we're referencing it in a function called multiply so here it is in multiply we're calling log and

06:46

it cannot actually find which function to link it to so of course it has to give up an error because when we land on that code at runtime what is it supposed to do when it tries to call the log function it doesn't know where the log function is now if I go over here and I comment out this log function so that we actually never call it if I try and build this we get no errors the reason this happens because I never call the log function so the linker doesn't have to link this function call to actually call the log

07:12

function because we never call the log function another interesting note is that if I do call the log function here and multiply however I comment this line out so that I never call multiply which in turn never calls log if I build my project now you'll see that I still get a linking error and you might be like what but why is that happening I'm not calling multiply anywhere why is it complaining about a linking error Trinette have just removed a function entirely since this potentially dead code that's never used

07:40

wrong because whilst we're not using the multiply function in this file we actually could technically use it in another file and so the linker does actually need to link that if we could somehow tell the compiler that hey this function multiplied I'm only ever going to use it inside this file then of course we could remove that linking necessity since this multiplies never called it never needs to call log oh wait there is a way we could do that if we come over here and write the word static in front of multiply that

08:08

basically means that this multiply function is only declared for this translation unit which is this math dot CPP file in our case and since multiply is never called inside this file if I build we won't get any linking errors if I bring back my comment though and then I build of course we will get a linking error in this case we actually ended up modifying the name of the function however it's not just the name of the function that matters if I bring back to function I'll call it log again I'll

08:34

build my project we won't get any errors but then I for example change the return type to be int and then I'll just return 0 or something like if I build my project now you'll see that we get an error because in master CBP we specify that this log function was a void function and so because of that is going to look for a function called log that returns void and also takes in this one parameter if I go back to log and I might change this back to avoid get rid of this return zero and build it everything works fine but then

09:07

I might add another parameter for example the level if I now build this we'll get a linking error once again because the log function that it expects does not have another parameter you'll see if we go down here into the linking error message it actually expects a function which returns void which has this calling convention it's called log and it has to have just one parameter which is a constant that's it if they cannot find exactly that then you're going to get a linking error let's go

09:35

back over here to our log file and just remove this level so that our program works again and if I build it of course we shouldn't get any linking errors great okay so the other type of linking error that's pretty common is when we have to look at symbols so in other words we have functions or variables which have the same name and the same signature so two identically named functions which have the same return value and the same parameters if that happens we're in trouble the reason we're in trouble is because

10:01

the linker doesn't know which one to link to it's ambiguous so back in our code if I was for example to write another version of dysfunction so I'll just literally copy and paste this function and try and build my code you'll know that we actually get a compile error because this already has a body and the compiler can kind of tell us that yeah okay since I'm compiling this file I can obviously see that you've made a mistake this code just isn't valid so this is an example of having to look at symbols where the

10:28

compiler can actually save us because this all happens in one file and no linking actually needs to happen to see that we've got an error however if I was to move this into a different file for example I'll move it back into our math file right over here so we still have our declaration I can leave that there that's fine that's just a declaration where they have one definition of log in this file so it's not going to give us a compiling error if I had control f7 just to compile this you can see it's totally

10:54

fine but now if I build we get a linking error and you can see that the one we get it tells us that we have this log function already defined in log obj one or more multiply defined symbols found so in this case link it doesn't know which log function to link to does the link to the one in map specifically or does link to the one in log dot CBP it doesn't know now you might think that this type of arrow is not something that would happen often and that you're smarter than that however this can creep up on you so I'll

11:20

show you a few ways as to how that can happen all right firstly let's just remove this extra log definition we have here so that our project builds successfully now let's create a header file I'm going to right click on the header file select add new item going to be a header file I'm going to call this file log H and click Add now inside here I'm going to grab this log function and make sure that I'm declaring it inside this header file if I go back to log CPP I'll write some kind of other function for example

11:46

in its log that's just going to call the log function and say that it's initialized the log of course if we try and compile now we're going to get an error because we need that log function so I'll include log back over here in master zbp instead of having this declaration here I'm also going to include log so great we're calling a log function from both the multiply function inside the master zerah key file as well as the net log inside the log of CBP file it doesn't really matter that I'm

12:17

not calling this function so don't worry about that I'm just going to build my project okay check this out I get an error telling me the log is already defined in local obj so we get a one or more multiply divine symbol sound so we're getting a duplicate symbols error message however you can see that I've really only got one definition of log it's inside this log dot H file why is it complaining about multiple symbols now this comes back to how the include statement works remember when we include

12:41

a header file we're just taking the contents of that header file and putting it where our include statement is so what's actually happened is it's taking this log function popped it over here like so into logged up CBP and then also over here and now you can see that we of course do have to log functions so how do we fix this well we've got a few options here if we undo all of this so that we are including log again we could mark this log function static that means that the linking that should happen to this log function

13:11

should only be internal which means that this log function when it gets included into log dog therapy and master therapy is going to be just internal to this file kind of like what we did with multiply so basically log and math will have their own versions of this function called log and it won't be visible to any other object files so if we just compile this now you'll see that we won't get any linking errors another thing that we could do to this is make it inline of course in line just means that it's going to take our actual

13:37

function body and replace the call with it so in this case this log initialized log would just become that it saw we were to do something like that and build you'll see that we get no errors either now there's one other way that we could fix this and that's probably what I would do in this situation and that is just move the definition of this into one translation unit because right now what's happening is this log function is being included in two translation units love does EBP and maps are therapy

14:05

that's what's causing the error in the first place so we could move it into a third translation unit or we could put this log definition into one of these existing translation units since this function is called log and it's related to logging I'm actually going to put it into log dot CBP so I'll grab this function I'll copy it into logical sweetie I'll get rid of the in line and then I'll come back to my log door age and just leave the Declaration here again without the in line of course so

14:29
 
now this header file just has the declaration for log the actual function to link to is included inside logo CBP once in one translation unit in our project and then main we'll call that so if I build this we get no linking errors and our project was able to be linked successfully so that's it that's pretty much a quick crash course on linking and how linking works remember at the end of the day the linker needs to take all of our objects files that were generated during compilation and link them all

14:56

together it will also pull in any other libraries that we may be using for example the C runtime library the sippers law standard library our platform api is necessary and a whole lot of other stuff it's very common to be linking from many different places there's also different types of linking we have static linking and we have dynamic linking but I'll save that for another video anyway thanks for watching I hope you enjoyed this video if you have any other questions just leave them in the comments

15:20

and below and I'll try my best to answer them be sure to follow me on Twitter and Instagram and if you really like this video you can support me on patreon that'll help me make more of these videos and by doing so you'll also get access to early draft videos and be involved in the planning process but as always I'll see you guys next time goodbye fool
