title: “Hello World” - Wireless


This tutorial presents a simple example, which shows you all the basic
steps to quickly develop, run, and access the result of an experiment
with OMF. Subsequent tutorials will build on this one to show you how to
use other OMF features.

If you are a new OMF users, you may want to read
[the short OMF System Overview](http://mytestbed.net/projects/omf/wiki/An_Introduction_to_OMF) and/or the
[Experiment Life-cycle Overview](http://mytestbed.net/projects/omf/wiki/UsageOverview)


## Experiment Scenario:

Figure 1 shows the simple experiment scenario, which we will use as the
example for this basic tutorial.

![](http://omf.mytestbed.net/attachments/download/359)    
__Figure 1__. Simple experiment scenario

This experiment involves two wireless PC-based nodes, i.e. Node 1 and Node 2

* Node 1 is running a simple UDP traffic generator application (OTG2)
* Node 2 is running a simple traffic receiver application (OTR2)
* Node 1 is the “Sender” and will generate and send traffic to the “Receiver” node 2, over a wireless 802.11g channel.

Note: At NICTA and WINLAB, these 2 applications (OTG2 & OTR2) are
already pre-installed on the default baseline disk image for the
wireless nodes. If you are using another OMF testbeds, you can find and
install these applications from [the OML Application
pages](http://mytestbed.net/projects/show/omlapp).

Accessing and Reserving Resources 
----------------------------------

This tutorial assumes that you are using either one of the NICTA
testbeds or one of the WINLAB ORBIT testbeds.

-   **Using a testbed at NICTA?** Please refer to the [OMF
    at NICTA Getting Starting page](http://omf.mytestbed.net/projects/omf/wiki/OMFatNICTA)
-   **Using a testbed at WINLAB?** Please refer to the [OMF
    at WINLAB Getting Starting page](http://omf.mytestbed.net/projects/omf/wiki/OMFatWINLAB)
-   Using another OMF-enabled testbed? Please refer to
    [the Getting Started page](http://omf.mytestbed.net/projects/omf/wiki/GettingStarted) or contact the operator
    of your testbed
-   Using your own freshly installed testbed with OMF? Just replace host
    and username below with your specific details.

The OMF Experiment Controller (EC) is the software that will interpret
your Experiment Description (ED) and execute it accordingly. You can
either:

-   Use the already installed EC, which is present on the consoles of
    any of the NICTA or WINLAB testbeds
-   [Download, install, and configure](http://omf.mytestbed.net/projects/omf/wiki/Installation_Guide_54) the EC
    on your own machine (Supported OS: Ubuntu/Debian, Fedora, Mac OSX)

This tutorial assumes the former, i.e. you will be using the EC
installed on your NICTA/WINLAB testbed’s console:

-   make a reservation for some resources on a testbed (see
    [OMF at NICTA](http://omf.mytestbed.net/projects/omf/wiki/OMFatNICTA) or 
    [OMF at WINLAB](http://omf.mytestbed.net/projects/omf/wiki/OMFatWINLAB))
-   log on to the *console* machine corresponding to this testbed,
    during your reserved time slot:

<!-- -->

    Example at NICTA:
       ssh myUsername@norbit.npc.nicta.com.au
       password:

    Example at WINLAB:
       ssh myUsername@console.sb1.orbit-lab.org
       password:

-   If you cannot login, contact a testbed administrator [at
    NICTA](http://mytestbed.net/tab/show/omf) or [at
    WINLAB](http://www.orbit-lab.org/wiki/about/WhoToContact).
-   Install a *baseline* disk image on the 2 resources, which you have
    reserved and which we will use in this tutorial. Here we assume that
    these two nodes are: **`omf.nicta.node2`** and **`omf.nicta.node3`**
    (if you are using other nodes, replace these names accordingly).

<!-- -->
    omf-<version> load -t omf.nicta.node2,omf.nicta.node3 -i baseline.ndz

-   You should see something similar [to this output
    example](http://omf.mytestbed.net/projects/omf/wiki/OutputLoad) on your screen.
-   You may also want to view [the manual pages for the
    “omf” command](http://omf.mytestbed.net/projects/omf/wiki/ToolManPages),
    or read the [“How to load
    a disk image” tutorial](http://omf.mytestbed.net/projects/omf/wiki/BasicTutorialStage7-5-3)

Developing the “Hello World” Experiment Description
------------------------------------------------------

To run an experiment with OMF, you need first to describe it into an
Experiment Description (ED) file. An Experiment Description (ED) is a
script that is supplied as an input to the OMF Experiment Controller
(EC). It contains detailed descriptions of the resources involved in an
experiment and the sets of actions to perform in order to realize that
experiment. An ED is written using the
[[The\_Experiment\_Controller\_API|OMF Experiment Description Language
(OEDL)]].

The ED describing this simple “Hello World” experiment is:

    defGroup('Sender', "omf.nicta.node2") do |node|
      node.addApplication("test:app:otg2") do |app|
        app.setProperty('udp:local_host', '192.168.0.2')
        app.setProperty('udp:dst_host', '192.168.0.3')
        app.setProperty('udp:dst_port', 3000)
        app.measure('udp_out', :interval => 3)
      end
      node.net.w0.mode = "adhoc"
      node.net.w0.type = 'g'
      node.net.w0.channel = "6"
      node.net.w0.essid = "helloworld"
      node.net.w0.ip = "192.168.0.2"
    end

    defGroup('Receiver', "omf.nicta.node3") do |node|
      node.addApplication("test:app:otr2") do |app|
        app.setProperty('udp:local_host', '192.168.0.3')
        app.setProperty('udp:local_port', 3000)
        app.measure('udp_in', :interval => 3)
      end
      node.net.w0.mode = "adhoc"
      node.net.w0.type = 'g'
      node.net.w0.channel = "6"
      node.net.w0.essid = "helloworld"
      node.net.w0.ip = "192.168.0.3"
    end

    onEvent(:ALL_UP_AND_INSTALLED) do |event|
      info "This is my first OMF experiment"
      wait 10
      allGroups.startApplications
      info "All my Applications are started now..."
      wait 30
      allGroups.stopApplications
      info "All my Applications are stopped now."
      Experiment.done
    end
{:ruby}

### Resource Description and Configuration (Line 1 to 26)

-   **Line 1**: we define a new group of resources, called `Sender`.
    This group includes a unique node, which is identified by a unique
    id: `omf.nicta.node2`.

-   **Line 2-7**: we associate an existing application called
    `test:app:otg2` to this group. This application will be installed
    and run on each node of this group (here, only `omf.nicta.node2`).
    In this tutorial, this application is already installed on the
    baseline disk image, which you previously loaded on the node. This
    application is a simple traffic generator, which by default
    generates fixed-sized UDP packets at a constant bitrate.
    -   More precisely:
        -   Line 3: we set the parameter `udp:local_host` of the
            application to the IP address that we give to the
            experimental interface of `omf.nicta.node2` (i.e the sender)
        -   Line 4: we set the parameter `udp:dst_host` of the
            application to the IP address that we give to the
            experimental interface of `omf.nicta.node3` (i.e. the
            receiver)
        -   Line 5: we set the parameter `udp:dst_port` of the
            application to the port that node `omf.nicta.node3` will
            listen on
        -   Line 6: we request the collection of the measurements from
            the `udp_out` Measurement Point provided by the application,
            at a regular interval of 3 sec

-   **Line 8-12**: we configure some properties for this group, i.e. all
    the nodes in this group will share these properties (here, only node
    `omf.nicta.node2`)
    -   More precisely:
        -   Line 8: the first wireless interface (named `w0`) of the
            node is placed in `ad-hoc` mode
        -   Line 9: this same interface is configured to operate in
            802.11g type
        -   Line 10: this same interface is configured to operate on
            channel `6`
        -   Line 11: the Extended Service Set ID (ESSID) of this
            interface is set to `helloworld`
        -   Line 12: finally, the IP address of this interface is set to
            `192.168.0.2`

-   **Line 15-26**: we define a similar group, called `Receiver`, which
    will only include node `omf.nicta.node3` running the existing
    application `test:app:otr2`. This application is a simple traffic
    sink, which should also be installed on the baseline disk image.
    Similar to the previous OTG2 applications, we further set properties
    for OTR2, and request the data from the `udp_in` Measurement Points
    to be captured. We also configure the interface of the nodes in this
    group in a similar manner as for the `Sender` group.

-   **Note**:
    -   More details about how to define groups and topologies, or
        configure resources can be found on the [[other tutorial
        pages]].
    -   More details about all the available options of the above
        `defGroup`, `addApplication`, etc… commands can be found on the
        [[The\_Experiment\_Controller\_API|OEDL reference pages]].

### 3.2 Event-based Action Descriptions (Line 28 to 37)

OMF uses an event-based approach to describe the different actions
required to perform during an experiment. Basically, you can define
events and the sets of actions to execute when they are triggered.
Events can be characterise by many different conditions. For example, an
event can be “when nodes in group X are all powered ON”, or “when
measured data Z reaches a threshold X”, or “when interface of node Y is
configured”, …

In this simple experiment, we are only interested in 1 event, which is
`:ALL_UP_AND_INSTALLED` = “when all the nodes are ON, and all the
required applications are installed on them”.

OMF comes with a set of default events, which have already been defined
for you, and `:ALL_UP_AND_INSTALLED` is one of them. All we have to do
here is specify the tasks that we would like to do when that event
occurs, which is the call to `onEvent(...)` on line 26.

-   **Line 28-37**: here we declare what to do when the event
    `:ALL_UP_AND_INSTALLED` happens:
    -   line 29, 32, 35: print some messages on the standard output when
        our experiment is running
    -   Line 30: instruct the controller to pause for 10 sec
    -   Line 31: tell all the Groups of this experiment to start all the
        applications associated to them. In this tutorial, this command
        will tell all the nodes in the groups “Sender” and “Receiver” to
        start their associated applications.
    -   Line 33: wait for 30 sec. Basically, here we are giving time for
        UDP traffic to be exchanged from “Sender” to “Receiver”. This is
        in fact the experiment.
    -   Line 34: tell all the Groups to stop all the applications
        running on all the nodes associated to them.
    -   Line 36: declare the end of the Experiment. This will trigger
        some “cleaning” actions on the nodes (e.g. turn off the network
        interfaces, stop receiving commands for this experiment, etc…)

-   **Note**:
    -   More details about how to define other states or actions to
        perform within them can be found on the [[other tutorial
        pages]].
    -   More details about all the available options of the above
        commands can be found on the
        [[The\_Experiment\_Controller\_API|OEDL reference pages]].

4. Running the “Hello World” Experiment
---------------------------------------

### 4.1. How do you run it?

Please refer to the above Section 2 to find out how to access an
OMF-enabled testbed and how to reserve resources on it, if necessary.
The rest of this section assumes that you are using an NICTA or WINLAB
testbeds, and that you have installed a baseline image on your resources
(i.e. NICTA’s and WINLAB’s baseline image have the applications OTG2 and
OTR2 pre-installed).

The command line `omf exec` invokes the Experiment Controller (EC)
application, which will be orchestrating the experiment execution on
your behalf. As explained on the [[An\_Introduction\_to\_OMF|OMF
Introduction page]], the EC will interprets your ED and send commands to
the various Resource Controllers (RCs) and Aggregate Manager (AM)
related to the resources in your experiment. These commands will
configure the resources and instruct them to perform actions.

-   First you need to create an file, which will hold your experiment
    description:
    -   use your favorite editor to create a new file in your home
        directory on the console of the testbed (e.g. `hello-world.rb`)
    -   cut-and-paste the above “Hello World” ED into this file and save
        it.

-   Now invoke the EC to run your experiment

<!-- -->

    omf-<version> exec hello-world.rb

-   You can use the command `omf-<version> help exec` to get a full list
    of options for the `omf-<version> exec` command.

### 4.2. What you should see on the console:

When running the EC with the above command, you should see an output
similar to this (note that in this particular instance, we are using
node28 and node29):

    <code class="text">
     INFO NodeHandler: OMF Experiment Controller 5.4
     INFO NodeHandler: Slice ID: testing_slice (default)
     INFO NodeHandler: Experiment ID: testing_slice-2010-09-03t09.41.43+10.00
     INFO NodeHandler: Message authentication is disabled

     INFO Experiment: load system:exp:stdlib
     INFO property.resetDelay: value = 210 (Fixnum)
     INFO property.resetTries: value = 1 (Fixnum)
     INFO Experiment: load system:exp:eventlib
     INFO Experiment: load hello-world.rb
     INFO Topology: Loading topology 'omf.nicta.node28'.
     INFO Topology: Loading topology 'omf.nicta.node29'.
     INFO ALL_UP_AND_INSTALLED: Event triggered. Starting the associated tasks.
     INFO exp: This is my first OMF experiment
     INFO exp: Request from Experiment Script: Wait for 10s....
     INFO omf.nicta.node29: Device 'net/w0' reported 02:0B:6B:57:BA:04
     INFO omf.nicta.node28: Device 'net/w0' reported 02:0B:6B:57:BA:04
     INFO exp: All my Applications are started now...
     INFO exp: Request from Experiment Script: Wait for 30s....
     INFO exp: All my Applications are stopped now.
     INFO EXPERIMENT_DONE: Event triggered. Starting the associated tasks.
     INFO NodeHandler: 
     INFO NodeHandler: Shutting down experiment, please wait...
     INFO NodeHandler: 
     INFO run: Experiment testing_slice-2010-09-03t09.41.43+10.00 finished after 1:36

    </code>

-   Line 1-5: some information about the EC and your experiment:
    -   line 1: the EC’s version & revision number
    -   line 2: the name of your slice, here: `testing_slice`
    -   line 3: the ID of your experiment, here:
        `testing_slice-2010-09-03t09.41.43+10.00`
    -   line 4: the EC says that it is running without message
        authentication

-   Line 6-12: some information about the properties of your experiment

-   Line 13: indicates that the `:ALL_UP_AND_INSTALLED` event has been
    triggered, thus the EC will now execute the commands declared in the
    associated `onEvent` block, which we described in the above ED
-   Line 15: indicates that your experiment is waiting for 10sec as you
    requested in the ED
-   Line 16-17: some information coming directly from the nodes in your
    experiment, here the nodes say that their wireless interface `w0`
    joined the BSSID identified by the address `02:0B:6B:57:BA:04`
-   Line 18-20: some information about the execution of your experiment
-   Line 21: indicates that your experiment has reached the
    Experiment.Done statement in the ED, i.e. the event
    `:EXPERIMENT_DONE` has been triggered

-   **Note**:
    -   your experiment will generate a log file, which will be located
        at: `/tmp/Your_Experiment_ID.log`
    -   the EC in your experiment will also keep a XML tree describing
        the state of your experiment, which will be located at
        `/tmp/Your_Experiment_ID-state.xml`

5. Accessing the Results from the Experiment
--------------------------------------------

In the above ED, we requested the collection of measurements from two
Measurement Points (MP):\
\* the `udp_out` MP provided by the OTG2 application \
\* the `udp_in` MP provided by the OTR2 application

Thus, while the experiment was running, these applications were
forwarding measurements to the OML framework (refer to the
[[An\_Introduction\_to\_OMF\#OMLIntro|OMF Introduction page]] for more
details). The OML server stored these measurements in a SQL database.

### 5.1 How do you access the measurement database after the experiment stops?

Currently the collected measurements are stored in a SQLite database,
which is located on the server that runs the OML Measurement Collection
Server. For each new experiment execution, an measurement database is
created with the same name as the Experiment ID. In this example, the
experiment database has the name
`testing_slice-2010-09-03t09.41.43+10.00`.

Every OMF installation has one or more Aggregate Manager(s) providing a
range of services to manage the testbed resources. One of these services
is called *result*, and as its name implies, it provides an easy access
to experiment results. One of the possible ways to access your result
database, is to request a database dump of it from the *result* AM
service.

-   First, find out the hostname and port of the *result* AM service on
    your OMF-enalbed testbed
    -   For NICTA, this service is running on the console of your
        testbed. Its host & port are: “localhost:50<version_compact>”
    -   For WINLAB, this services is running on the server at the host &
        port: “oml:50<version_compact>”

-   To request a dump of your result database from the console:

<!-- -->

    ## At NICTA
    wget "http://localhost:50<version_compact>/result/dumpDatabase?expID=testing_slice-2010-09-03t09.41.43%2B10.00" -O myDatabase

    ## At WINLAB
    wget "http://oml:50<version_compact>/result/dumpDatabase?expID=testing_slice-2010-09-03t09.41.43%2B10.00" -O myDatabase

-   Note that as we are using an HTTP interface in this example and our
    experiment ID has a “+” in this example, we need to escape it with
    is ascii code “%2B”

-   You should now have a file named “myDatabase” which is a SQLite dump
    of your result database.

-   You can open this database, an run queries on it (refer to the
    [SQLITE3](http://www.sqlite.org) website for more information on how
    to do this)

<!-- -->

    sqlite3 -init myDatabase myDatabase.sq3

-   Alternatively, you may want to install the “SQLite manager”
    extension for the Firefox browser from
    [here](https://addons.mozilla.org/en-US/firefox/addon/5817/) . It
    allows you to open the SQLite binary database file or the dump file
    directly and gives you various options for viewing your results and
    exporting them into other formats such as comma-separated or XML.

-   Note: the *result* AM service provides more functions than just
    “dump a database”, a list of its other functions is available on
    [[AM\_Services\_Result|the Result AM page]].

-   Also please refer to the [[oml:|OML Documentation pages]] to learn
    more about the different tables and fields in any OML generated
    measurement database

Another way to access experiment result is to use the omf-web-basic
program from the omf\_web gem to launch a web interface where you can
browse data and view line graph visualisation. The interface looks like
this:

![](/attachments/609/2012-02-08-132036_686x744_scrot.png)

Please go to this page for more detailed instructions: [[Experiment
Visualisation]].

6. What is Next?
----------------

Now that you know how to develop and run a simple experiment, you may
want to read the following basic OMF tutorials. Each one of them is
introducing an OMF feature, using this simple “Hello World” experiment
as a base. You do not need to follow them in the order suggested below.

-   [[BasicTutorialStage1-5-4|How to pass parameters to your experiment,
    and change them at run-time]]

-   [[BasicTutorialStage2-5-3|How to configure or address all resources
    within a defined group, and use simple substitutions]]

-   [[BasicTutorialStage3-5-3|How to use your own or a 3rd party
    application with OMF]]

-   [[BasicTutorialStage4-5-3|How to use Measurement Filters to
    customise your Measurement]]

-   [[BasicTutorialStage5-5-3|How to use Prototypes to specify
    particular Applications]]

-   [[BasicTutorialStage6-5-3|How to save a disk image]]

-   [[BasicTutorialStage7-5-3|How to load a disk image]]

And finally, a “Conference Room” scenario which combines all of the
above features:

-   [[BasicTutorialStage8-5-3|The Conference Room tutorial]]

* * * * *
