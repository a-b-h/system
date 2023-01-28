Continuous Integration (CI) is a DevOps software development practice that enables the developers to merge their code changes in the central repository to run automated builds and tests. It refers to the process of automating the integration of code changes coming from several sources.
Features of Continuous Integration
Following are some of the main features or practices for Continuous Integration.
1. Maintain a single source repository - Al source code is maintained in a single repository. This avoids having source code being scattered across multiple locations. Tools such as Subversion and Git are the most popular tools for maintaining source
code.
2. Automate the build - The build of the software should be carried out in such a
way that it can be automated. If there are multiple steps that need to be carried out, then the build tool needs to be capable of doing this. For .Net, MSBuild is the default
build tool and for Java based applications you have tools such as Maven and Grunt.
3. Make your build self-testing - The build should be testable. Directly after the
build occurs, test cases should be run to ensure that testing can be carried out for the various functionality of the software.
4. Every commit should build o n a n integration machine - The integration machine is the build server and it should be ensured that the build runs on this machine. This means that all dependent components should exist on the Continuous Integration server.
5. Keep the build fast - The build should happen in minutes. The build should not
take hours to happen, because this would mean the build steps are not properly configured.
6. Everyone can see what is happening - The entire process of build and testing and deployment should be visible to all.
7. Automate deployment - Continuous Integration leads to Continuous deployment. It is absolutely necessary to ensure that the build should be easy to deploy onto the production environment.

What Does Build Mean?
The term build may refer to the process by which source code is converted into a stand- alone form that can be run on a computer or to the form itself. One of the most important
steps of a software build is the compilation process, where source code files are converted into executable code. The process of building software is usually managed by a build tool. Builds are created when a certain point in development has been reached or the code has
been deemed ready for implementation, either for testing or outright release. A build is also known as a software build or code build.
Build automation is the process of automating the retrieval of source code, compiling it into binary code, executing automated tests, and publishing it into a shared, centralized repository.

1. Reduces Risk
The frequent testing and deployment of code reduce the project's risk level, as now
the code defects and bugs can be detected earlier. This states that these bugs and errors can be easily fixed and take less time, making the overall process cheaper. The general working speeds up the feedback mechanism that makes the communication smoother and effective.
2. Better Communication
The Continuous Integration process collaborates with the Continuous Delivery workflow
that makes code sharing easy and regularized. This makes the process more transparent and collaborative among team members. In the long term, this makes the communication speed more efficient and makes sure that everyone in the organization is on the same page.
3. Higher Product Quality
Continuous Integration provides features like Code review and Code quality detection, making the identification of errors easy. If the code does not match the standard level or a mistake, ti will be alerted with emails or SMS messages. Code review helps the developers to improve their programming skills continually.
4. Reduced Waiting Time
The time between the application development, integration, testing, and deployment
is considerably reduced. When this time is reduced, it, in turn, reduces the waiting time that may occur in the middle. CI makes sure that all these processes continue to happen no matter what.
What is Jenkins
Jenkins is an open-source automation tool written in Java with plugins built for Continuous Integration purposes and used to build and test software projects continuously making it easier for developers to integrate changes to the project, and making it easier for users to obtain a fresh build. It also allows to continuously deliver software by integrating with a large number of testing and deployment technologies.

Jenkins Features
Jenkins offers many attractive features for developers:
1. Easy Installation
Jenkins is a platform-agnostic, self-contained Java-based program, ready to run with
packages for Windows, Mac OS, and Unix-like operating systems.
2. Easy Configuration
Jenkins is easily set up and configured using its web interface, featuring error checks
and a built-in help function.
3. Available Plugins
There are hundreds of plugins available in the Update Center, integrating with every tool in the CI and CD toolchain.
4. Extensible
Jenkins can be extended by means of its plugin architecture, providing nearly endless possibilities for what it can do.
5. Easy Distribution
Jenkins can easily distribute work across multiple machines for faster builds, tests, and deployments across multiple platforms.
6. Free Open Source
Jenkins is an open-source resource backed by heavy community support.
whyweuseit?
The image below depicts that Jenkins is integrating various DevOps stages:
Advantages of Jenkins
1. Open Source and Free: Developers don't need to take tension about the money; it is free of cost. It is platform-independent.
2. Plug-ins and Integration: It is one of the most important features that make it most widely used. It has its type of plug-in, which helps the developer a lot in executing the jobs. Jenkins plug-ins can be developed by anyone and for anyone. Dashboard view plug-in, test analysis plug-in, build pipeline plug-in, and many more like this makes the developer familiar with the Jenkins tool.
3. Hosting Option: It is yet another important feature of the Jenkins, which can be installed on any operating system like Windows, MacOS, Linux, etc. You can also run Jenkins on the cloud by downloading and deploying it on a VM. You can also use a Docker container in it.
4. Community Support: Jenkins has great support from the developer community. You can assume its popularity and community support that it has more than 1000000 users all over the world, while it was officially published in 2011.
5. Integration with other CI/CD platforms: Jenkins supports many CI/CD platforms, not only the pipeline. It can make interaction with other tools also. Several plug-ins are available in it, which allows users to make connections with other CI/CD platforms.
6. Keep your t e a m in sync: Jenkins focuses on a centralized way of working. Al the members of the team move in sync.
7. Easy to debug: It is very easy to find out the errors in the Jenkins. The developer can easily check the bug and resolve it.
8. Less time to deliver the project: It happens because of its continuous integration feature.
9. Flexible in creating the jobs: It is very flexible in creating the jobs. It can create jobs both in freestyle and in the pipeline process very easily.
10.Source Code Management (SCM): Jenkins supports different types of source code repositories like SVN, Git, etc. The developer can set different trigger after making changes in the codes. He can do it every time.
DisadvantagesofJenkins
• Its interface is out dated and not user friendly compared to current user interface trends.
•
•
Not easy to maintain it because it runs on a server and requires some skills as server administrator to monitor its activity.
CI regularly breaks due to some small setting changes. CI will be paused and therefore requires some developer's team attention.
All plug-ins are not compatible with the declarative pipeline syntax.
> Jenkins has many plug-ins in its library, but ti seems like they are not maintained by the developer team from time to time. This is when ti becomes very important that whatever plug-ins you are going to use; are getting a regular update or not.
Lots of plug-ins have a problem with the updating process.

Jenkins Architecture
Standalone Jenkins instances can be an intensive disk and CPU Resource-Consuming process. To avoid this Jenkins follows Master-Slave architecture to manage distributed builds by implementing slave nodes which essentially would help to offload a part of the master node's responsibilities.

Jenkins Master
Master & Slave Architecture
WindowsSlave N o d e
A p p l eOSXSlave Node
LinuxSlaveN o d e
JenkinsMaster(UI)
TCP Connection
The master is the base installation of the Jenkins tool and does the basic operations and serves the user interface while the slaves do the actual work.
The main server of Jenkins is the Jenkins Master. It is a web dashboard which is nothing but powered from a war file. By default, ti runs on 8080 port. With the help of Dashboard, we can configure the jobs/projects but the build takes place in Nodes/Slave. By default, one node (slave) is configured and running in Jenkins server. We can add more nodes using IP address, user name and password using the ssh, jnlp or webstart methods.
The server's job or master's job is to handle:
Scheduling build jobs.
• Dispatching builds to the nodes/slaves for the actual execution.
Monitor the nodes/slaves (possibly taking them online and offline as required).
• Recording and presenting the build results.
AMaster/Server instance of Jenkins can also execute build jobs directly.

Jenkins Slave
A slave is just a device that is configured to act as an executor on behalf of the master.A Slave is a Java executable that runs on a remote machine. Following are the characteristics of Jenkins Slaves:
• • •
It hears requests from the Jenkins Master instance. Slaves can run on a variety of operating systems.
The job of a Slave is to do as they are told to, which involves executing build jobs dispatched by the Master.
• You can configure a project to always run on a particular Slave machine, or a particular type of Slave machine, or simply let Jenkins pick the next available Slave.

Jenkins Pipeline
In Jenkins, a pipeline is a collection of events or jobs which are interlinked with one another in a sequence. It is a combination of plugins that support the integration and implementation of continuous delivery pipelines using Jenkins.
In other words, a Jenkins Pipeline is a collection of jobs or events that brings the software from version control into the hands of the end users by using automation tools. It is used to incorporate continuous delivery in our software development workflow.
A pipeline has an extensible automation server for creating simple or even complex delivery pipelines "as code", via DSL (Domain-specific language).
