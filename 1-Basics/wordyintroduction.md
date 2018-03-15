# A Wordy Introduction

If you're doing ACI administration through the GUI, you're doing it wrong, in my opinion.  You know how much it sucks, but you feel you have no other choice, right?  Chances are, you know about Postman and a little bit about REST calls.  If so, this collection is for you, and I hope you find it useful.  Well, okay, to tell the truth, it's really for me.

When we were building our first deployment of ACI, I spent a lot of time manually configuring things in the GUI, it was slow and error prone.  I knew enough to find the API inspector, and had been briefly introduced to Postman, so tried deploying a couple of ePG's this way.  From then on, I was hooked.  API calls to ACI are faster, you get the output all at one time, and if you're configuring multiple ePG's, ports, tenants, well, anything, the API calls are almost always the better option.

Of course, there are a smattering of documented API calls here and there, but you usually find the same ones over and over.  I'm talking to you "Build a Tenant API," but really, how often are you building tenants, versus other tasks.  In our use case, tenant builds are rare; tenant changes are frequent, but that's nowhere near as documented, or at least, I haven't been able to find it all in one place.

That's the idea here.  At this point, I almost always only go into the GUI to figure out what the API calls are to do a particular task, and when I do, I plan to share that task here, for all to use.

Thanks,  
Chip McHuron