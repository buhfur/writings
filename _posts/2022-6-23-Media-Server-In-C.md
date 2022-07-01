---
layout: post
title: Media server in C 
---

Introduction
---
So recently with home media servers becoming more prevalent and accessible to non technical folks. Some have begun 
to capitalize on un-knowledgeable market. Me being one of them, I have grown tired of the annoyance of servers like Plex and Emby
requiring accounts for a pseudo netflix with local media storage & organization. 

What I want is simplicity, and going BEYOND accessibility with this new project.

Today I would like to dedicate this post to a new project I will create in order to provide users with a simple media server written
in a low level language.

I have always wanted an excuse to move away from higher level languages and really delve into computer networking and hopefully provide 
a somewhat workable product for the high price of 0$.

To avoid confusion , I will use this document ( for now ) for notes, and little tips I find along the way and make improvements 
as the project comes to a close.

Anywho, let's get all our W's ( who, what , when , where , why )


Who
---

This project is meant for any developers that feel like this code could be of use to them in a future project.
Feel free to fork and make improvements. I do ask however, that you kindly keep me in the loop , I would like to get 
some dopamine points to know that my code helped at least *someone*.

What
---
Okay now let's transition into the technical nitty gritty computer networking definition. *What* are we making and *What* do we need to know?

Starting off simple, our project is based off a Client/Server model. I'm not gonna waste time explaining what that is, just felt like I needed to say that.

So now *what* data is the client sending to the server? *what* protocols are involved? This is all new to me obviously. Will report back
with results.

For example , what protocols are we using to transmit the data.

Progress
---

First things first, checking for which protocols I want to use in this application.

Like reading the original RFC's about the protocols I wish to use

![RTSP RFC] (https://datatracker.ietf.org/doc/html/rfc2326)



I will admit I discriminate against projects that don't use my preferred language which is a 
flaw of mine. However I believe I will have to go outside my little C echo chamber and look at other
projects that might include better techniques on how to go about creating a server which hosts files 
and a client that can read and play them at the same time.

