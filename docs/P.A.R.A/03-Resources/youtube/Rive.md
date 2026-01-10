
Search in video
Hello and welcome to this Rive quick start tutorial. Today we're going to be making an interactive resizable menu
that can be used in real time in your apps, websites, or games. In the first
stage of this tutorial, we're going to create the entire design using layouts. We're then going to move on to
animation, data binding, and then we'll implement the state machine logic. and
at the end you'll hopefully have a fully functioning menu. Let's begin. This is
the Rive editor. And of course, I want to create an artboard. I'm just going to
use the default 500 pixels x 500 pixels. Over here on the left, you'll see the
artboards hierarchy, which is currently empty apart from the artboard itself. We
also have the assets panel, which is empty. And we have the data panel which
has something called view model one inside. On the right hand side of the editor you'll see the inspector. This is
where we can see all of the properties of the selected layer. In this case we've selected the artboard. And so this
is all of the artboards properties. At the top you'll see that it is bound to view model one. So what is view model
one? Well, view models are part of our data binding feature that we're going to cover a little bit later. But in
essence, a view model is a place to create and control various properties
that we can then use as part of our designs and as conditions in our state
machine. So for now, I'm going to return to the hierarchy and I'm going to rename this artboard menu.
You can also rename artboards over here as well. Let's explore a few of the
menus settings. For instance, we can change its size.
We can change its background color. But for now, I'm actually going to
delete this background so that we start with a blank slate.
Open the data panel. And I'm going to rename this view model menu. View model.
Awesome. To design this menu, we're first going to make a bunch of different
components. And it's in this menu artboard that we're going to nest all of
those components in a layout. The first component that I'm going to create, I'm
just going to put up here. Now, a component is actually a type of artboard. And the shortcut to create a
new artboard is a. Then click and drag. Call this artboard item.
And just like the menu, I'm going to delete its background. And now to turn this artboard into a component, all we
have to do is click this symbol. All this means is that we can now nest this
component in a different artboard. But before we do that, let's design this
item. And I want my item to have a picture over here and a couple bits of
text. For the picture, I'm going to open my assets panel. And now I'm going to import some pictures
into Rive. Those images have successfully imported
into Rive. So I can close this folder. And now I can show you what these images are. We have a picture of a black helmet
which is 250 pixels x 250 pixels. Its size is as small as I could make it and
it's been used zero times. The next one is a blue helmet. It's the same size.
green helmet and a white helmet. I'm just going to drag the black helmet onto the item component. This automatically
zooms into your component, but we can zoom out by pinching. I can change the size of the image.
And I can change its position by clicking and dragging. I'm just going to leave it over on the left hand side.
Now, I'm going to create a couple bits of text. Shortcut T.
This first bit of text will be the item name. I'm going to change its font size to 30 and I'll change its style to bold.
Then I'll create another bit of text and this will be the item class. I'll change
the font size to 20. And finally, I'm actually going to create a third bit of
text that will be a long description
that will live underneath the other elements of this design.
Awesome. We have our four different elements and you can see them in the hierarchy.
Now, I want to arrange these using layouts. But what is layouts? Well, in
short, layouts is a design system in RIY that lets you arrange elements in either
rows or columns. And you can put columns inside rows, you can put rows inside of columns, rows inside of rows, columns
inside of columns. You can basically arrange your designs in any way that you want. create designs that can resize and
refflow depending on the size of your component or the artboard
or even the size of the device that your RI file is playing on. I usually start
by arranging the smallest pieces of my design into layouts and then work my way
out. For instance, these two bits of text should be arranged in a column.
Then this column and this image should be arranged into a row. And then this
row and this text description should be arranged into another column. Let me
show you how. So I'll just highlight these two bits of text and tap shift L.
As you can see in the hierarchy, this has been arranged into a column. This is because the two layers were more on top
of each other than next to each other. And so Rive calculated that they should be arranged in a column instead of a
row. I'm going to call this column text column. And we can see the two bits of
text, the item name and the item class have themselves been wrapped in their
own individual layouts. The text column is the parent of these
two text layouts. And therefore it is from the text column that we can control
the vertical gap in between its children. So over here in its properties
this is where we can control the vertical gap. I'm just going to set it to be zero.
Next I'm going to highlight my text column and my image and then tap shift
L. And as you can see that has arranged them in a row. So we now have our image
that's been wrapped in a layout and we have our text column. I'm going to call this row image and text row. And it is
here in the parent of these two layouts that we can change the horizontal gap
between its children. So we can go over to the image and text
row properties and change this horizontal gap. I'll change it to 10
pixels. And finally, I'm going to highlight the image and text row and the
text description underneath. Tap shift L. And as you can see, that has arranged
them in a column. And I'm going to call this column item column. And if we open
up the item column, you can see the image and text row and the text description underneath. And because the
item column is the parent of these two layouts, it is from here in the item
column that we can control the vertical gap between its children.
So if we go over to the item column settings, we can change the vertical gap and I'll
set it to 10. Now we have a bunch of stuff that we need to edit. The first
thing I'm going to do is change the size of the artboard. so that we can fit the text description
underneath. Next, I'm going to highlight my item column and I'm going to change its positioning to be zero on the left
and zero on the top. Now, what I want to happen is the item column fits perfectly
within the size of this component. That way, when we change the size of the component, it will change the size of
our design. So, let's look at its fit settings up here. It's set to hug the
width and hug the height of its child layouts. I'm actually going to change it
to a fixed width and a fixed height. Now, I know what you're thinking. A
fixed width and a fixed height is not being controlled by the size of the
component. However, right now it's set to be a
fixed pixel width and a fixed pixel height. But we can actually change this.
If we click on the pixel icon, we can change it to percent.
And if I change them both to 100%. That means that no matter what size our
item component, it will change the size of our item column layout. I'm now going
to highlight my item column and set some padding around its children. So, I just
go down here and set the padding on the left and right to 10 and the padding on
the top and bottom to 10. I'm also going to give it a background color.
And I now want to give this text description its own background color.
And to do this, I need to select it and wrap it in another layout. So, shift L.
And I'll call this text description. I'm going to change its fit to fill the
width of its parent layout and fill the height of its parent layout. I'm going
to add some padding on the left and right and the top and bottom. And then
I'll add a background color. Awesome.
We have designed our first component. Now, let's design another A. And I'll
call this artboard stats. Delete its background color and set it
to be a component. The first thing I'm going to create in the stats component is a rectangle. So,
go up to your create tools and select rectangle. Then click and drag. I'm going to change
the color of this rectangle to white. Select it. Duplicate it with command D.
Move that over to the right. And change this rectangle's color to black.
We can now turn these two rectangles into a bar that represents a number. So
if I highlight both of them, tap shift L to put them into a row layout. And I'm
going to do a few things. First of all, I'll turn off absolute positioning. I'm going to change the width to fill the
parent layout. And I'm going to change the horizontal gap between its children to zero.
Next, I'm going to go into the row and change the fit of the white bar
to be a fixed width in percent. And I'm going to change the fit of the black bar
to fill the remaining width of its parent layout. So now when we come to
data binding, all we need to do is control this pixel amount and it will control this bar.
Next up, I'm going to create two bits of text. Duplicate that text layer. Move it over
to the right. and change this one to be a number. Highlight these two bits of
text. Tap shift L to put them into a row. And then I'm going to highlight both of these rows and tap shift L to
put them inside a column. If we go over to the column in the hierarchy,
we can change their order just by clicking and dragging one below the other. So now the text is above the bar.
I want to get rid of this vertical gap between the two rows. So, I go into their parent layout
and then change the vertical gap to zero. Next, I want to spread out these
two bits of text. So, I'll select their row and change its width to fill the
width of its parent. I'll get rid of the horizontal gap between the two bits of text. And then I'm going to click here
twice. One time to center it and then another time to spread them out. Next,
I'm going to create a title for the component.
And then put it and this row in a column. And then of course the title
should go at the top. Select the column and duplicate it three
times. 1 2 3. And I've just realized that these four columns have a fixed
width instead of filling the width of their parent. So, let's change that now. And as you can see, that doesn't really
look how we expected. Why are they overrunning the edge of the component? Well, it's because if we look at their
parent, its width is set to hug. If we just change that to fill, then
everything looks great. Right now, the gap between all of these layers is exactly the same size. However, I want
the gaps between these stats to be a little bit smaller than this gap. To do
this, I'll just highlight all of these columns and wrap them in their own column. Shift L. We can now change the
horizontal gap between its children. And once again, we need to change its
width fit to be fill. This way, when I change the size of the
component, everything resizes
correctly. Next, I want to put some padding around all of these elements.
So, I'll go to the column layout and make sure that it is filling the height
of its parent as well. And then down here, we can add some padding.
Then, we can add a background. I'm going to make it black with 20%
opacity. And now, just to make the design look good, I'm going to make all of these titles different. So, I'll just
go into their text runs. And to select a layer that's deep in the hierarchy, hold
down command. And if you double click on a text layer, then you can change the text run.
I'll just set it to be a random number.
And later on when we come to data binding, we'll be able to control all of these numbers. And when we do, that will
be reflected in the size of all the bars. Next, I'm going to make a start
button. This one's pretty simple. Just uh tap T, create some text.
Tap shift L to put this into a text layout and then shift L again to put it into a
row. I'll turn off absolute positioning. I'll change the fit to fill the width
and fill the height of its parent. And I will change the alignment of its children to be centered. And I'll change
the artboard's background color to be black.
And I'll rename this artboard start. and change it to be a component.
I'm going to move up here and zoom out a little bit. Go into my assets panel and
I'll import the four images of the bikes. We're
going to use these four images as the background of our menu. So, we
have the black bike, the blue bike, green, and white. If we highlight them
all and drag them onto the stage, that will create a brand new artboard with
all four of them layered on top of each other,
which is exactly what we want. And when we're using these four images, we only want to see one at a time. So, if you
highlight them all and then right click and wrap in a solo,
a solo is a kind of group where you can toggle the visibility
of all the layers so that only one is visible at any given time. I'm going to
rename this artboard background. And I'll go over here and I'll change it to a component.
Let's see how our project's looking now. Just going to quickly zoom in and make
another very small component just to show how to use the create tools. Zoom
in and go up here. We can use the pen tool. And I can now draw some lines
to create a kind of arrow symbol. If I highlight this layer, you'll see over here we have two different layers. One
is the shape layer. This is where you can control the color
and the transform properties of the shape layer itself. But within the shape
layer, we have a path. And as you can see, it still has its own transform
tools, but we can also edit the vertices.
This allows us to change our vertices positions, change the vertex type,
and all that good stuff. However, I'm just going to leave my design looking how it did, and I can say done editing,
or I can just tap enter. Next, I'm going to duplicate this path and move this one
across. And I'll duplicate that one and move it across. Now I want this artboard
to contain the entire design. So I'll just change the size of the artboard so we
don't have any extra space around our design. Then I'm going to rename this artboard arrows and change it to a
component. As you can see, the artboard's probably going to need to be a little bit bigger
to fit all of these components in it. So, I'll just move it over here and change its size like that. Now, we can
start populating the menu with our various components. The first component I'm going to include is the background.
So, with menu selected, tap N to nest a component and click. And then you have a
drop-down of all of your components. I'm going to select background. So, here it
is. Our background component over here is now being nested in the menu
artboard. And I know what you're thinking. This is quite messy. It's uh going over the edge of the menu
artboard. Well, if we just go up here, we can clip. Now, I want this background
to cover the entire space of the menu artboard, no matter what size the menu
artboard is. So, you know, I could shrink it like that. And then, you know, the background would have to scale down
to stay covering the background. And uh if I uh you know, lengthened it out like
that, it would have to scale up. How do we do this? Well, just highlight your background component and then go over
here and change its mode from node to leaf. As you can see, its fit is
currently set to fill. So, it looks a little bit squashed down. And this will be more evident if I change the position
to 0 by 0. You can see that it is filling the artboard no matter what
size. So it stretches and does all of that. We don't want that. So instead of filling
the artboard, we want it to cover the artboard. Which means that if we change
the size of the artboard,
it scales up and down to always cover the background. Before we populate the
menu artboard, I'm first going to change a couple of things about the item component. First of all, I'm going to
hide this text description at the bottom. Then I'm going to change the
size of the component to be a little bit smaller. I've done this because this is what it will look like in its initial
state. The last thing I'll do is highlight the item column and change its background color to be 20% opacity.
Okay, we're now ready to populate the menu artboard. Tap N to nest a
component. First off, we have the arrows. And I'll just pop them in the top left corner. Shrink them down a
little bit. And I'll add some text. I'll set the text to say select your moto.
And then change its color to be black. Now I'm going to add some more text. Say
class. Change that to be black. And now I'm going to nest four different item
components. One, two,
3, 4. Don't worry if this looks bad. We're going to be changing it as we go. Over
here, I will nest the stats. And in the bottom right corner, I will nest the
start button. Okay. Before we start putting these elements into layouts, you'll notice that when my mouse is
hovering over this artboard, it highlights the background. Now, we've already set up the background exactly
how we want it. So, we don't need to select it anymore. So, I can just go over here and lock the layer. This just
means that if we were to click here, we wouldn't be selecting the background. Okay. So, just like we did before in
other components, we're going to start with the smallest elements first. Uh,
that will be these two elements. I'll tap shift L. And it looks like they've
been put into a column when I wanted them to be put into a row. That's fine. We can just change that over here.
We can change the vertical gap that we don't need anymore since they're not a column. We can add a horizontal gap. And
as you can see up here, it seems like the text is being pushed towards the top of the row. And that's because we're
currently aligning the children to the top left. And we can change that to be the center left. It is now more
vertically aligned. Next up, I'm going to put these four items in their own
column. So just highlight them all in your hierarchy and tap shift L to put
them into a column. Next, I'm going to put these two elements in their own
column. Then, I'll put these two columns in a row.
And finally, I'll put these three elements into a column.
Awesome. Everything is set up using layouts. However, it's not set up
properly. Uh if we were to change the size of the artboard, you'll see that the only thing that changes correctly is
the background. So let's change the various fitting and alignment settings. The first thing I'm
going to do is highlight the outermost column. Turn off absolute positioning and then
change it from hug to fill the width and fill the height of its parent, which is
the artboard itself. Then I'll add some padding around its children. Let's say
50 and 50. Then I'll select this row of
these two elements and I'll set that to be filling the width and filling the
height. But as you can see, this column is currently not touching the right edge
even though its parent is filling the width. This is because its position is
currently being determined by the horizontal gap between it and its sibling.
So let's get rid of this horizontal gap. You can see that the two elements are currently being aligned to the top left,
but we can spread them out by clicking here again. Now I want the start button
to be touching the bottom and aligned to the bottom right. So, let's go into this
row, select that column, and change it to fill its parent. Get rid of the
vertical gap. Align it to the right, but then click this again to spread out the
children. And finally, I want to reduce the gap in between these items. So, I'll
select this column, go over to its vertical gap, and change that. Even though this doesn't really matter
because we're going to be replacing this element soon with an actual list. And
now if we select the artboard and change its size,
the different elements move accordingly. Okay, now that we have everything
arranged using layouts, we can now start using data binding. Once again, data
binding is a way of creating and controlling various properties that you can use to control your designs and also
as conditions in the state machine. But the interesting thing about these properties called view model properties
is that you can actually control them in code. So if we had data binding in this
file controlling these numbers, these view model properties would be exposed
to the developer who's working on your project. And that doesn't matter whether or not it's in an app, a game, or on a
website. Rive has a whole bunch of free open- source runtimes that let
developers access and control these view model properties. So, with that being said, let's create our first view model
property. So, let's select our menu artboard. And over here, you can see the view model that we renamed earlier. And
if we go over to our data panel, we can see it here. I'm going to create a
number property and I'll call it index num. And now over here you can see that
index num has a default value of zero. And we can change this to be whatever we want. But I'm going to leave it as zero.
And now that we have this property, we can now use it as a condition in our state machine. But which state machine?
Since each artboard and component actually have their own state machine.
Well, I'm going to use it in our backgrounds state machine. So,
with background selected, we're going to go from design mode into animate mode.
And down here, we have our state machine. Now, for some reason, we have two state machines. That's actually
incorrect. So, I'm just going to delete that one. And we'll work with state machine 2. In this case, we have a
timeline. And inside our timeline, there's no key frames. So, nothing is
happening. I'm going to go back to our state machine and if I press play on the state machine, you'll see that timeline
one plays all the way through once. Now, what I'm going to do is delete this transition, drag entry over here, and
move timeline one up here. And I'm going to go over here and create three more
timelines. Move State Machine to the top just to
keep things tidy. And now in timeline one, I'm going to animate the solo that
we have in our hierarchy. So if you highlight the solo over here, we can set
a key frame for whichever bike we want to be visible. So in timeline one, I'm
going to set a key frame for the black bike. Timeline two,
blue. Three, green.
and four white. Excellent. We now have four
different timelines, each with their own unique key frames. We can go into our
state machine and drag the other three timelines onto the state machine stage.
And we can create transitions from the any state to each of our timelines. Now,
an any state basically lets you transition from any state to any other
state. And I'm going to highlight all four of these transitions and go down here and create a condition for all four
transitions. And this is where we can use our view model property
index num as a condition in the state machine. So for our first transition we
can say if index num is equal to zero then we transition to timeline one. If
index num is equal to 1 then timeline 2
two timeline 3 and three timeline 4. Now if I was to
press play on this state machine and then go into our data panel, you can see
that we don't have index num available to us to change. This is because index
num is contained in the view model for the menu. And so right now if we wanted to control index num, we need to be
playing the state machine for the menu. So let's highlight our menu artboard
and press play on its state machine. And you can see index num up here. And we
can change it to one, two, or three. Awesome. That is the simplest use of
data binding that we're going to have in this project. Now, what I want to implement is that whenever we change the
value of index num, we activate an animation happening in the background.
And that animation will just be animating the scale and opacity of the background. So, if we're going to
animate this background, we should animate it in its component. So, open its hierarchy and select the
solo. And the simplest way to do this would be to animate the scale and opacity in timeline 1 2 3 and four. But
if we're trying to minimize the number of key frames that we're using, what I'm going to do is give this state machine
another layer so that we can just play the same timeline
when index num changes. And I'm going to call this timeline scale and opacity.
And I'm going to animate the solos, scale key frames, and opacity key
frames. So, go into your timeline, highlight solo, tap U to see all existing key frames. And I'm going to
set the opacity to zero and the scale to 102.
And then we're going to go forward to frame 30 and set the opacity back to 100. And set the scale back to 100 as
well. Next, highlight the scale key frames and we'll change their interpolation
to start off fast and slow down. And this is what that animation looks like.
I'm actually going to make the opacity change a little bit quicker.
Okay, we can now open our state machine and drag scale and opacity onto the
state machine. Connect it to entry and then drag another scale and opacity onto
the state machine and connect that to the other one in both directions.
And we can now activate these transitions using index num. So if I
highlight both of them, create condition and we can say if index
num is not equal to itself, then we
transition. And this means that if we go back into the menu
and press play, the animation plays. If it is no longer equal to itself, then
we play that scale and opacity animation.
It's pretty cool. State machine layers are extremely useful to know.
Now let's use data binding to control these numbers and therefore the size of
these bars and let's also control this title. To do
this we need to go into our stats component and we need to give it its own
view model. So just click plus to create a new view model. This will be called view model one. Then go over into your
data panel and we can rename this stats view model and we're going to give this
view model a string property and four number properties.
I'll call the string property title. This one power.
this one speed, acceleration,
and handling. And we're going to be using these numbers to control strings,
which means that we need to create a converter, which converts our numbers to strings.
In the converter settings over here in the inspector, we can click round decimals on and remove trailing zeros.
Now go into your hierarchy and to select a layer just hold down command and then
you'll find it in your hierarchy. Let's open its text run. Right click data bind
and we'll take in the title view model property. Now as you can see the string has not
updated. It only updates if I press play on the state machine. It says initial
value because that is the initial value of the view model property. However, if
you want to see bound values without having to press play on your state machine, just go up here and toggle on
preview bound values or the shortcut commandB. I'm going to change this title to level
one. And then we'll continue binding these properties. So hold down command to find it in the hierarchy in the text
run data bind and we'll take in power and then because power is a number we
need to add a converter and that would be the convert to string converter that we made earlier. Let's do the same with
this number
speed. Add the converter
and finally
handling. In the data panel, you can see that we
change these numbers and it updates our design.
Now, back to the hierarchy shortcut command 1 and we can locate these rectangles and we're going to bind the
width of their layouts. So, data bind and bind it to power. Do the same with
this bar. Find its layout. and then bind its layout width to speed.
Same with acceleration layout bind its layouts width to
acceleration and handling layout
width bind handling. Now open your data panel command three.
And when you change these numbers, not only does it change the string, but
it also changes the size of the bar. And once again, these numbers and that
title string can be controlled in real time by your developer. Now, let's go to
our menu artboard. And you'll see that the view model properties are not
updating even if we select the artboard and press play on the state machine.
This is because the menu artboard is bound to the menu view model which
currently only has one view model property. This is the only property we
have access to from here. So how do we get access to these view model
properties? Well, what we can do is give the menu view model a property of the
stats view model. This will give the menu view model access to all of the
properties contained within the stats view model. So just highlight your menu
view model, click plus, go down to view models, and give it stats view model as
a property. All we need to do now is highlight that component in the hierarchy and bind this
component to that specific property of the stats view model.
You can see that those properties have now updated. And if we press play on the state machine and open the data panel,
you'll see that we can control them in real time from the menu artboard.
Pretty cool. Now, as you know, we have four different bikes, and each of them is going to need
their own unique stats. So, when index num is set to zero, I want to see the
black bike, its stats. And then when index num is one, I want to see that
specific bike's stats. How do we do this? Well, we do this using instances.
Instances basically allow you to make multiple different versions of view model properties and therefore multiple
different versions of components. If we highlight the property of stats view
model, you'll see that it is being controlled by something called instance.
Now this instance is the only instance of the stats view model that exists.
However, we can create more instances of the stats view model like this
and each of them can have their own unique property values.
So these are the property values of instance zero. These are the property values
of instance one. I'll just make them random
and so on. Awesome.
We now have four different instances of the stats view model that we can now
apply to four different copies of this stats component. So, first we need to go
over to our menu view model and create three more properties of the stats view
model. Each one is going to be controlled by a
different instance. This one I'll call stats view model
instance one. This one instance two,
instance three, and instance four. So for the first one,
we'll leave it as this first instance. This one we'll change it to the second
instance. Third
and the final one. Now we need to highlight this stats component, open our
hierarchy, and we need to duplicate this instance three times. 1 2 3. Now, as you
can see, that goes off of the artboard, but that's fine because we're only going to show one at a time. But for now, I'm
going to apply the correct property to each of our nested components. So for
this first one, I'm going to bind it to the property stats view model instance
one. And you can see that reflected in the property values here. The next one
down here, I'll bind it to the second one. You can see that
the third one and the fourth one is already bound to
the fourth. I'm now going to hide these three layouts just by clicking up here.
And we're now going to animate this property of each instance layout.
So in your menus state machine, we're going to have four different timelines.
Drag the state machine to the top. I'll call this timeline stats instance one.
This one 2
3 and four. Now in one just going to
highlight all four of these and set key frames for all four of them.
Right now only the first one is visible and this is exactly what we want for the
first timeline. Now in the second timeline
we're going to change this and only show the second one. Do the
same for three
and do the same for four.
And now in the state machine we can get rid of this transition. Move entry over here. Put stats instance 4 over there.
Drag one, two, and three onto the state machine stage
and connect them to the any state.
And now just like we did with the background state machine, we are going to set conditions for these four
transitions. And we're going to say if the index num
is zero, then go to the first instance. If it's one, go to the second.
Two, third, and three, the fourth. So
now when we press play, we're seeing the first bike and its stats. And if we go
to the data panel and change index num, we'll see a different bike and different
stats.
And now, just like we did in the background, I'm going to add some animation to the stats component. So
let's move to the stats component and I want to animate the Y position of
each of these different elements so that when the instance changes we get a nice
little animation. Now if you remember earlier the way that we set up each of
these columns was to fill the width of their parent and to hug their children.
However, fill does not let you use absolute positioning, and we're going to
need to use absolute positioning in order to animate the position. So, let's see what happens when we go from fill to
absolute position. Rive has given us a y position property
that measures the distance from this element to the top of its parent layout
up here. As you can see, it still says that we are filling the width of its parent
layout. However, that's not actually true. This has just not been updated. And you'll see that if I change the size
of the component, that element is not filling the width.
So, what we need to do instead is change it from fill to fixed and change it from
a fixed pixel amount by clicking here to a fixed percentage amount. And now
when we change the size of the component, it resizes as if it is
filling the width. But we are now able to animate its
position. So now let's do the same for these four other elements.
Turn on absolute positioning and change the fit from fill to a fixed percent.
Make sure it's 100. And then finally this text layout as well. Except for this text layout, I'm not actually going
to turn on absolute positioning. All I'm going to do is animate the position of the text layer within. So now we can
open up our timeline and I'll set a key frame for the Y position of the text layer
and then highlight all four columns and set a Y position key frame for all of
them as well. And finally, I'm going to animate the visibility of all of those layers.
So, if I lift this up and highlight them all and then tap U to
show all existing key frames, I'm going to go forward to frame 30 and set more
position key frames and then move back to the beginning again and increase all of these values
by the same amount. So hold down shift to change the pixel amount by 10. 1 2 3
4 5 1 2 3 4 5 1 2 3 4 5 1 2 3 4 5 and 1
2 3 4 5 I'm now going to set all four of those columns to hide
and move forward one frame by tapping the period key. And now I'll change them
back to show.
Now we just need to highlight all of the first positional key frames
and go over to the interpolation graph and change it to start off fast and slow
down. And this is what that looks like. So they're all moving at the same time.
So, uh, what we can do now is highlight these and offset them. So, hold down alt
or option and then tap period. Uh, I'll do five. 1 2 3 4 5.
And do the same for the rest. 1 2 3 4 5.
So now the animation looks like this. And finally, we need to animate the
background color. So, highlight your column and go over to the right and where the background has a fill, we need
to go back into design mode. So, tap tab. Here it is down here. And we need
to add a feather. Now, we're not actually going to be using the feather effect. So, we can turn the
amount down to zero. The thing that we are going to be using is the Y position.
So, we can now go back into our timeline, highlight the component, go down to the bottom and into its
settings, and we can now animate the Y offset. Set a key frame there, 30 frames
forward. Another one. Back to the beginning, and I'll set its value at the
beginning to plus 50, just like we did with the others. And then change the interpolation.
And then we can move over to the menu artboard. And when we press play,
it's all animating nicely. If we open our data panel, command 3, we can change
index num. And every time we change it, the animation plays.
Awesome. Okay, we're now going to be using the list feature in Rive to set up
these four different items. Now the first thing we need to do is go into our
item component and data bind its various elements to view model properties. So
I'm now going to show the text description. Then I'm going to give the item component its own
view model. Go into our data panel and I'll call this item view model. Now I'm going to
give it four view model properties. an image view model property and three
strings. So image I'll call this helmet
and one two three strings name
class and description. If you select your view model, you can
see all four of your view model properties over here. And I'm now going to create three more instances. 1 2 3.
And just like before, each of these instances can have their own unique view model property values. For the first
one, I'll select the helmet black. For the second one, I'll select helmet
blue. Third one, helmet green. And for the
fourth one, helmet white. For now, I'm going to keep the names simple. So, I'll
set the first one to black class one. And I'll set the description
to something that I just get from GPT
blue class 2. and the description.
Awesome. We have four different instances, each of them with their own unique view
model property values. Now let's bind each of these layers to their respective
view model properties. So go into your hierarchy and we'll start with the image. Now with your image selected, you
can go over here to image, rightclick data bind and then select the property
and that will be the helmet image view model property. Next, select this text.
Open its text run. Right click data bind and take in the
name. Now the item class text run
databind class. And finally description.
Well, it looks like my description might be a little bit too long. So, I'll just reduce the font size a little bit. I'm
once again going to select the description and hide it and then resize the
component. And we're going to get this set up as a list. So what we need to do is go to our
menu again data panel the menu view model and give
it a list property to work with. And I'll call this list property items.
Over in the inspector we can add list items. I'm going to add four. Go into
the first one. You can see that it's actually already taking the correct instance from the item view model. Now
in the second one, let's take instance two,
instance three and instance 4. That list is all set up
now. And all we have to do is create an artboard list to replace this column. So
go into your hierarchy and I'm going to locate this column in the hierarchy. Here it is. And I'm going to delete all
of its children
so that we now have an empty layout. And then go over to the right to its inspector to where it says layout
children and click plus. There you will find the artboard list.
And you can now see it in the hierarchy. And we now need to select the list property that this artboard list is
going to use. And that list property was called items. And you can see that here.
Now the artboard list has a parent layout. And this is where we're able to
change the vertical gap in between its children. So why are we using a list
instead of just having four individual components each bound to a different
instance just like we did with the stats component? Well, lists are interesting.
Let's say if I change the logic of this item to get bigger when I click it and
it gets bigger vertically. That would actually push down all of the other elements in the list. So let's implement
that logic in our item. Now for the item component, I want to have two
interactions. I want a hover and unhover interaction and I want a click
interaction. When we hover, I want the whole component to move to the right and will animate its opacity. Then when I
unhover, I want the component to move back and the opacity to return to normal. When I click, I want the size of
the component itself to get much bigger and for us to show the text description.
And when I click on a different instance of this item, I want the text description to disappear and the size to
return to normal. So to do this, we're going to need three timelines.
Call the first one unhover, the second one hover, and the third one click. In
unhover, we're first going to set the size of the component itself.
Then highlight item column and we're going to set a key frame for the left hand side. We're also going to set a key
frame for the background color. And finally, we are going to set a key frame
for the text description. We're going to keep it hidden. Next, go
into your hover state and we're going to set key frames for the exact same properties, but for some of them, we're
going to give slightly different values. So, for instance, the size of the component is going to stay the same.
Then select item column and we're going to change this key frame value. And also
we're going to change the opacity of the background to 10. And we're going to
keep the text description hidden. Then in your click state, we will change the
size of the component so it's wider and taller. Then the item column, just set a
key frame for the left, but keep it zero. Set a key frame for the background color. And then the text description,
we're going to show it. Awesome. We have three different states. So now we can
open the state machine and we can transition between them.
So I'm going to set it up so that we enter to unhover
and that we can transition back and forth between unhover and hover. And before I link these states to click, let
me show you how to implement this logic. Now the first thing we need is a view model property to control the
conditions. So go into your data panel and give item view model a boolean
and I'll call it hover. I've selected a boolean because a boolean only has false
or true. And when you're going back and forth between two different states, a boolean is all you really need. So
highlight both of your transitions and go down here to create a condition and we can say if
hover is true then we go from unhover to hover
and if it's false then we go from hover to unhover. So now if I press play we can see over here that hover is false
but if I change it to true then we transition and activate that state and we can go back and forth. I can even
check it on and off over here in this specific instance. But I don't want to have to check a box off and on. I want
to be able to hover and unhover to activate that boolean. How do we do that? Well, we need to listen for mouse
movements. So, if you create two listeners, I'll call one enter and one exit. In
enter we're going to select a target in our hierarchy to listen to. So command
one and click. And we can select the item column as our target. And we're
going to say if the pointer enters the item column, then set
hover to true. And in the case of exit,
we'll select the target item column and we'll say if the pointer exits item
column, then set hover to false. So now
when we press play, hover unhover.
And if we go into our assets panel, we can drag in our three sounds.
And once they're loaded, we can go up here to create an event.
And I'll call this event hover sound. And over in the events settings, we can
change its type to audio. And we can change its asset to be the hover sound
that we just imported. And now we can open up the hover state. And we can set a key frame to play that
audio. So, if we go back to our state machine and press play
and if we go over to our menu.
Awesome. Now, let's set up the click logic. If you remember, we're basically controlling this entire design using one
number, and that is the index num. When we press play, we can change the value
of index num and it changes the bike that is visible and the stats. So, how
do we control index num by clicking on these various item selectors? Well, it's
very simple really. But before we do that, we first need to change index num to minus1. And I'll explain why later.
What we need to do next is to go to our item view model that is the view model
bound to this and give it a list attribute and that would be a list
index. A list index tells us what position each of these items holds in
the list. So for instance this would be list index zero 1 2 and three. And what
we can now do is say if we click on this item which is list index zero then we
need to change index num to zero and if we click on this item change index num
to one and two and three. So let me show you how to do this. Uh we'll do it from
the item component and we do it with a listener and I'll call this listener
click. I'll open the hierarchy and I'll set the click listeners target to be the
item column. So we say if the pointer clicks the item column then we need to
set index num to the list index
of whatever instance of this component we just clicked.
So, if this was done correctly and I press play, we can hover and we can click, but
nothing happens. Now, for some reason, Rive needs you to turn off previewbound
values for this to work. So, just switch that off and the list will disappear because when the state machine is not
running, you need previewbound values on to be able to see a list. But in order
for a list to function correctly when the state machine is playing, we actually need preview bound values to be
off. So now when we press play, we can hover.
And when we click, that changes index num to whatever the list index of the
instance that we just clicked is.
So now that we're controlling index num with the list index, we can go to our
item component and use that as logic in its state machine to activate the click
state. We can set a transition to go into click and a transition away from
click. And we can set both of these to have the same condition. and that's
whether or not index num is equal to the list index. If you'll remember, when we
click on a specific instance, that then sets index num to the same value as the
list index of the instance that we just clicked. So that we know when we click
that index num is equal to the list index. However, if we were to click on
something else, then for this specific instance, index num is now no longer
equal to the list index, which basically means
that when we click on one item, that activates the click state. And if we
click on a different item, then our original item's click state is deactivated. In short, only one item can
have an active click state at any given moment. Real quick, I'm going to add a click
sound uh by going up here and adding an event, and I'll call it click sound. And
I'll change the event type to be audio. And I'll use the asset select sound.
Then we'll go into our click timeline and play the audio at the beginning. So
now whenever the click animation plays,
now that we have our stats animating in with all of the elements animating with an offset, I want to animate the list
items animating in with an offset as well. But how do you animate a single
component with different timings? Well, let me show you. Let's go to our item
component and then we're going to create two timelines.
One we'll call load and one we'll call empty. We're going to be animating in
load and then using empty to offset the animation in the state machine for the various instances. So, drag state
machine one to the top. And the first thing we'll do is animate load. We need to animate the visibility of the item
column and this top key frame. That's it. So if we go down here and tap U to
show all existing key frames, I'm going to change the top position to be + 50
and then move ahead one frame and change the visibility from hide to show. and then move forward to frame 30 and set
another key frame at zero. Then highlight the first key frame. Change
its interpolation to start off fast and slow down. Let's see what that looks
like. Now let's go into the state machine and I'm going to delete this transition from
entry to unhover. I'm going to make a little bit more space between entry and unhover. And bring in empty
and load. And I'll move empty up here. Now connect entry to empty, empty to
load, and load to unhover. The first thing we're going to do is highlight this transition and set it to have an
exit time of 100%. This just means that load has to play
100% of the way through. and then we will automatically transition to unhover. So when we press play, load
plays and we transition. Now if I was to open up the menu artboard, you'd see
that all four instances have the exact same load timing. So we're now going to
offset them using the list index as a condition in the items state machine. So
for this transition between empty and load, I can say
if the list index of the specific instance that this state machine is
controlling is equal to zero, then we transition with an exit time of 100
milliseconds. And now we can create another transition in the same direction.
and say if the list index is equal to 1
then the exit time of this transition should be 200 milliseconds. And we'll
create another one
300 milliseconds. And the final one
400 milliseconds. So now depending on which instance we see it will have a
different exit time depending on its list index.
So let's see how that looks in the menu artboard. Press play.
Oh, the problem is that in their design the
item components are initially visible just in the design itself and we then
have to go through empty and get to load where a key frame is set at the
beginning to hide the item column for one frame and then show it again and
move it up. So what we need to do is go to empty and set a key frame for the
item column to just be hidden. So now when we go to the menu artboard,
they come in one at a time. Okay, let's finalize this intro
animation by animating each of these remaining elements coming in in the same
way. So in your menu artboard, create a new state machine layer and I'll call
this intro. Then I'll create a new timeline
and I'll call this intro as well. Next, I'll select this component and set a key
frame for its Y position and I'll set its opacity to be zero. And I'll do the
same for this text. Animate its Y position and set its opacity to zero.
Okay. Now, highlight all of these in the timeline. Tap U to see all existing key frames. Go forward one frame and change
all of the opacities back to 100. Set all of the starting positional key
frames to be 50 and go forward to frame 30 and set them
all to zero. Then highlight the first positional key
frames and once again change the interpolation.
We'll offset the animation.
So it looks like this. And now let's see how it looks in the
state machine. Awesome. So, we have the intro
animation. We can select our different elements. We can click on them
and that changes which element is visible. Now, I want to be able to click on the start button and have all of the
elements disappear. To do this, I'm going to create a trigger in the menu artboards view
model. And I'll call this start. Now, a trigger
is a lot like a boolean because it can either be false or true. The main difference is that triggers are always
false unless you fire them, at which point they become true for one frame and
then immediately go back to false. For this reason, we typically use triggers instead of booleans when you don't want
to go back and forth between two states. You just simply want to activate a transition from one state to another.
And we can control this trigger using a listener.
And I'll set this listener's target to be the start buttons layout.
So instead of using the start button itself, we're going to select the layout. Then we can say if the pointer
clicks on the start buttons layout then set the start trigger to fire. And we
can now use that trigger in our various other components to activate animations
where they animate out. So in this artboard we have an intro animation.
Let's create an outro animation and transition to outro when the trigger
is fired. I'll set the condition
that if the start trigger is fired, then we go from intro to outro. If I press
play, you'll see that we are stuck in intro until I fire the trigger. And now
we're in outro. So, let's give outro some key frames.
And what I'm going to do is animate the same properties that I animated in intro. So just position and opacity of
these different layers. So this one Y and the opacity.
Now select all the layers in the timeline. Tap U. Move forward a few frames.
and change their position to something like minus 50
and then set opacity key frames at the end of zero.
Now I know what you're thinking. Interpolating between opacity uh is gradual and that does not look good. So
all we need to do is highlight the first opacity key frames and go over here and set them to be hold
key frames. This way they'll stay at this value until they hit the next key frame and
then immediately switch to that key frames value of zero. Next, highlight
all of the first positional key frames and we'll change the interpolation to
start off slow and then speed up. And this is what that looks like.
And now we can offset
back to the state machine. So, if we press play, we have our intro. And if we
press the start button, we have an outro. But, of course, we still need to animate stats and the list animating
out. For animating the outro of the stats component, I'm just going to keep things really simple and animate the
column that all of the different instances live in. So I'll open outro
and at the beginning I'll set a key frame for the margin. Now I just want to
animate the top margin. So to split margin into four unique properties, we
just need to click here. I can now set a key frame for the top margin. And you can see that in the timeline here.
And I can move forward a few frames and make it minus 50 and change its
interpolation. And I don't want to control the opacity of the column itself since the column
holds the start button inside. So instead, what I'm going to do is just
control the opacity of all of these four stats layouts. So I'll set a key frame
of zero. Go to the beginning. Set a key frame for 100.
And then set these first opacity key frames to be hold key frames. So now the
outro looks like this. The more I look at this outro, the less
I like the arrow and select your moto disappearing separately. I think we should make them disappear together
since they're on one line. And then I will move key frames for class disappearing a little bit forward.
So in the state machine that looks like. Awesome. Now let's animate the outro for
the items in the list. And we have to do that in the item component itself.
So let's create a timeline. I'll call it outro.
And in outro, I'm going to animate the item columns top position and the item columns
opacity. Go into the timeline and then move forward a few frames and
I'll set the position to be minus 50 and the opacity to be zero.
Set the opacity key frames to be hold and change the first positional key
frame to be cubic but start off slow and get
faster. So looks like this. Then go into your state machine and drag outro onto
the state machine stage. And again, just like we did with the transition from entry, we need to use an empty state
because we want to transition using an exit time. An entry doesn't give you an
exit time and neither does the any state.
So we need to drag another empty onto the state machine stage.
Connect the any state to empty and then create four transitions from empty to
outro. Now the reason that we would go into empty at all is because
the start trigger would have been fired. And for each of these transitions, I
want to add a condition that if the list index
is zero, then we transition with an exit time of 100 milliseconds.
If the list index is one, then we exit with 200 milliseconds.
two, we exit with 300 milliseconds
and 400 milliseconds.
So now if the start button is pushed, we will go from any state into empty and
then we'll stay in empty for a specific number of milliseconds depending on what
instance of the item component we're animating. So let's see how this looks in menu.
Now it looks like all of the items are disappearing at once. I wonder why this
is. Well, if we go into the item component, if I remember correctly, we
put a key frame in the empty state. And that key frame
hides the item column. Now, I don't want to change this because we have an empty
state up here. So, what do we do about this empty state? Well, we can just create a new timeline.
I'll just call it empty two. And I'll leave it actually empty. And to replace
this empty state with empty two, all we do is drag empty2 onto the state machine
stage and simply drop it on top of empty. That replaces empty with empty
two. So now
And one final touch, I'll create an event. I'll call it select sound. I'll
change it to an audio event. And I'll use the asset load sound. So I probably
should have called this load sound instead. And now in the outro timeline,
right at the beginning, I will play that audio.
So now in the state machine press play
and then if we click
